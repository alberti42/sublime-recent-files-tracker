# Recent Files Tracker for Sublime Text

**Recent Files Tracker** is a Sublime Text plugin that tracks recently opened files and projects. It stores the file paths in a JSON file, making it easy to integrate with other tools, such as the [Get Recent Sublime Text Files For LaunchBar](https://github.com/alberti42/Get-Recent-ST-Files-For-LaunchBar) action.

---

## Features

- **Tracks Recently Opened Files**: Keeps a history of files and projects opened in Sublime Text.
- **Customizable Settings**: Configure the maximum number of tracked files and the location of the JSON history file.
- **Integration with LaunchBar**: The JSON file is compatible with the [Get-Recent-ST-Files-For-LaunchBar](https://github.com/alberti42/Get-Recent-ST-Files-For-LaunchBar) action, allowing you to quickly access your Sublime Text files from LaunchBar.

---

## Installation

1. **Clone the Repository**:
   Clone this repository into your Sublime Text `Packages` directory:

```bash
   git clone https://github.com/alberti42/Recent-Files-Tracker.git "Recent Files Tracker"
```

2. **Restart Sublime Text**:
   Restart Sublime Text to activate the plugin.

---

## Configuration

### Default Settings

The plugin uses a configuration file named `Recent Files Tracker.sublime-settings`. This file includes the following default settings:

```json
{
    "recent_files_location": "~/recent_files.json",
    "max_num_recent_files": 20
}
```

- **`recent_files_location`**: The file path where the JSON history file will be stored.
- **`max_num_recent_files`**: The maximum number of recent files to track.

### Customizing Settings

To customize the settings, go to `Preferences > Package Settings > Recent Files Tracker > Settings`. Update the values as needed.

---

## JSON File Format

The JSON file is structured as an array of objects, with each object representing a recently opened file or project:

```json
[
    {
        "md5": "d41d8cd98f00b204e9800998ecf8427e",
        "file_name": "/path/to/file.txt",
        "timestamp": 1693492847.5234
    },
    {
        "md5": "e99a18c428cb38d5f260853678922e03",
        "file_name": "/path/to/project.sublime-project",
        "timestamp": 1693492850.1234
    }
]
```

- **`md5`**: A hash of the file name for quick lookups.
- **`file_name`**: The absolute path to the file or project.
- **`timestamp`**: The time the file or project was last opened (UNIX timestamp).

---

## Integration with LaunchBar

This plugin is designed to work seamlessly with the [Get-Recent-ST-Files-For-LaunchBar](https://github.com/alberti42/Get-Recent-ST-Files-For-LaunchBar) action. Follow the instructions in that repository to set up the LaunchBar action and point it to the `recent_files_location` configured in this plugin.

---

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Donations

If you find this plugin helpful, consider supporting its development with a donation.

[<img src="Images/buy_me_coffee.png" width=300 alt="Buy Me a Coffee QR Code"/>](https://buymeacoffee.com/alberti)

## Author

- **Author:** Andrea Alberti
- **GitHub Profile:** [alberti42](https://github.com/alberti42)
- **Donations:** [![Buy Me a Coffee](https://img.shields.io/badge/Donate-Buy%20Me%20a%20Coffee-orange)](https://buymeacoffee.com/alberti)

Feel free to contribute to the development of this plugin or report any issues in the [GitHub repository](https://github.com/alberti42/obsidian-plugins-annotations/issues).
