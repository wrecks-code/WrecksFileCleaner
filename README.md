# WrecksFileCleaner

WrecksFileCleaner is a Python application designed to automatically clean up specified files and folders on Windows systems. It provides a simple and configurable solution for managing cluttered directories and removing unnecessary files.
Notification:

<img width="546" alt="image" src="https://github.com/wrecks-code/WrecksFileCleaner/assets/29825723/37a0ceb5-61a8-499f-bd1e-a50d9f8d740d">



Sample Log:

![image](https://github.com/wrecks-code/WrecksFileCleaner/assets/29825723/5997b645-5c8a-47a1-8072-05eb0e0ff8c5)


## Features

- Automatically starts with Windows (configurable)
- Cleans up specified paths based on defined rules in `config.ini`
- Deletes duplicate .zip and .rar files if a folder with the same name exists
- Removes files and folders older than a specified number of days
- Generates a summary notification of the cleanup process
- Logs all deleted items for reference

## Installation

1. Download the latest release from the [Releases](https://github.com/wrecks-code/WrecksFileCleaner/releases) page.
2. Extract the contents of the zip file.
3. Double-click on the executable file (`WrecksFileCleaner.exe`) to start the application.

## Configuration

1. Open the `config.ini` file in a text editor.
2. Customize the settings according to your requirements:
   - Define paths to clean in `SEARCH_PATHS` (seperated by comma)
   - Set which extractable extensions to look for in `EXTRACTABLE_EXTENSIONS`
   - Set the maximum age (in days) for files and folders in the `DAYS_UNTIL_DELETION` section.
   - Set `START_WITH_WINDOWS` to `true` or `false` to control whether the application starts with Windows.
   - Define the max file size of the log file in `MAX_LOG_SIZE_MB`
3. Save the changes to `config.ini`.

## Usage

- Double-click on `WrecksFileCleaner.exe` to run the application.
- The application will automatically clean up the specified paths based on the configured rules.
- A summary notification will be displayed after the cleanup process.
- Check the `wfc.log` file for a detailed record of the deleted items.

## Compatibility

- WrecksFileCleaner is compatible with Windows operating systems.

## Security Note

- Due to the nature of its functionality, some antivirus software may flag WrecksFileCleaner as potentially harmful. However, rest assured that it is an open-source project and does not contain any malicious code.

## Contributing

- Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

- WrecksFileCleaner is licensed under the [MIT License](LICENSE).
