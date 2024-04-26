# WrecksFileCleaner

WrecksFileCleaner is a Python application designed to automatically clean up your Downloads folder(s) by deleting 
   - every archive that has already been extracted in the same folder
   - files and folders older than a specified number of days (default is 14)
     
Download folders, Archive filetypes and the max age in days can be configured in `config.ini`<br>
A `wfc.log` is automatically created, clicking the notification opens up the log.

Clean Notification (when there's something to delete at startup):

![deletetion](https://github.com/wrecks-code/WrecksFileCleaner/assets/29825723/edb167d7-e711-4469-89a9-9b5ec3575fb2)


Summary Notification (when there's nothing to delete at startup):

![summary](https://github.com/wrecks-code/WrecksFileCleaner/assets/29825723/da51103d-449e-4110-802c-2607385bf1e1)


## Example Folder and Log

| Before | After |
| ------ | ----- |
| ![Before](https://github.com/wrecks-code/WrecksFileCleaner/assets/29825723/e2db839d-cbbf-4694-9cdf-4cf720d5f5c6) | ![After](https://github.com/wrecks-code/WrecksFileCleaner/assets/29825723/f4e392f2-1f79-4a7c-a458-3490ef67f0b5) |


![image](https://github.com/wrecks-code/WrecksFileCleaner/assets/29825723/5997b645-5c8a-47a1-8072-05eb0e0ff8c5)



## Features

- Automatically starts with Windows (configurable)
- Deletes archive file types if a folder with the same name already exists in the same directory
- Removes files and folders older than a specified number of days
- Generates a summary notification of the cleanup process
- Logs all deleted items for reference

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
