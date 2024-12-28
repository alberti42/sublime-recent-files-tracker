# Copyright, Andrea Alberti (2021)

import sublime
import sublime_plugin
import json
import os
import hashlib
import tempfile
from time import time
import logging

tmpdir = os.path.realpath(tempfile.gettempdir())

# Logger
logger = logging.getLogger("RecentFilesTracker")

class RecentFilesTracker(sublime_plugin.EventListener):
    
    # def on_activated(self, view:sublime.View):
    #     pass

    def on_load_project_async(self, window:sublime.Window):
        # Retrieve the project file path
        project_file = window.project_file_name()
        if not isinstance(project_file,str):
            logger.error("Error: could not find the file name of the opened project.")
            return
        self.track_file(project_file)

    def on_load_async(self, view:sublime.View):
        file_name=view.file_name()
        if not isinstance(file_name,str):
            logger.error("Error: could not find the file name of the opened file.")
            return
        self.track_file(file_name)

    def track_file(self, file_name:str):
        if not file_name or os.path.realpath(file_name).startswith(tmpdir):
            # do nothing for files in temporary folder - these are typically files opened remotely
            return

        # Load settings
        settings = sublime.load_settings('Recent Files Tracker.sublime-settings')

        # Load path of history file
        history_path=settings['recent_files_location']
        if not isinstance(history_path,str):
            logger.error(f"Error: setting 'history_path' must be a string.")
            return
        history_path = os.path.expanduser(history_path)
        
        # Load max number of items
        max_num = settings['max_num_recent_files']    
        if not isinstance(max_num, int) or max_num<=0:
            # raise ValueError("max_num must be an integer.")
            logger.error(f"Error: setting 'max_num' must be a positive integer.")
            return
        
        try:
            with open(history_path, 'r') as json_file:
                history = json.load(json_file)
        except:
            logger.error(f"Error: could not parse JSON file: {history_path}")
            return 
        
        md5 = hashlib.md5(file_name.encode('utf_8')).hexdigest()

        # Use an iterator to find and pop entries matching the md5 and file_name
        indices_to_remove = [i for i, entry in enumerate(history) if entry['md5'] == md5 and entry['file_name'] == file_name]
        
        # Remove entries in reverse order of indices
        for i in reversed(indices_to_remove):
            history.pop(i)

        # Insert the current file at the beginning of the history
        history.insert(0, {'md5': md5, 'file_name': file_name, 'timestamp': time()})

        # Keep only `max_num` elements in the history
        with open(history_path, 'w') as json_file:
            json.dump(history[:max_num], json_file)
