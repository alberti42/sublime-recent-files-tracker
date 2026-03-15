# Copyright, Andrea Alberti (2021)

import sublime
import sublime_plugin
import json
import os
from time import time
import logging

home_dir = os.path.expanduser('~')

# Logger
logger = logging.getLogger("RecentFilesTracker")
# We set a fixed log level; can be improved by allowing
# the user to choose the log level
logger.setLevel(logging.WARN)

# Check if the logger already has handlers to avoid adding duplicates
if not logger.handlers:
    # Create a StreamHandler (outputs to console)
    console_handler = logging.StreamHandler()
    
    # Set the handler's level to 0 to accept all messages
    # We leave to `logger` the control of what has to be to logged
    console_handler.setLevel(0) 

    # Create a simple log format
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(console_handler)

class RecentFilesTracker(sublime_plugin.EventListener):
    
    def on_load_async(self, view:sublime.View):
        file_name=view.file_name()
        if not isinstance(file_name,str):
            logger.error("Error: could not find the file name of the opened file.")
            return
        self.track_file(file_name)

    def on_load_project_async(self, window:sublime.Window):
        # Retrieve the project file path
        project_file = window.project_file_name()
        if not isinstance(project_file,str):
            logger.error("Error: could not find the file name of the opened project.")
            return
        self.track_file(project_file)

    def track_file(self, file_name:str):
        if not file_name or not file_name.startswith(home_dir):
            # only track files under the user home directory
            return

        # Load settings
        settings = sublime.load_settings('Recent Files Tracker.sublime-settings')

        # Load path of history file (relying on defaults from the settings file)
        history_path = settings.get('recent_files_location')
        if not isinstance(history_path, str):
            logger.error("Error: 'recent_files_location' must be a string in the settings file.")
            return
        history_path = os.path.expanduser(history_path)
        
        # Load max number of items (relying on defaults from the settings file)
        max_num = settings.get('max_num_recent_files')
        if not isinstance(max_num, int) or max_num <= 0:
            logger.error("Error: 'max_num_recent_files' must be a positive integer in the settings file.")
            return

        try:
            with open(history_path, 'r') as json_file:
                history = json.load(json_file)
        except FileNotFoundError:
            logger.warning(f"History file not found. Initializing a new history: {history_path}")
            history = []  # Initialize empty history for missing file
        except json.JSONDecodeError:
            logger.error(f"Error: JSON decoding failed. Corrupt file at: {history_path}")
            return
        except Exception as e:
            logger.error(f"Unexpected error while reading history file: {history_path} - {e}")
            return
        
        # Remove any existing entries for this file
        history = [entry for entry in history if entry['file_name'] != file_name]

        # Insert the current file at the beginning of the history
        history.insert(0, {'file_name': file_name, 'timestamp': time()})

        # Keep only `max_num` elements in the history
        with open(history_path, 'w') as json_file:
            json.dump(history[:max_num], json_file)
