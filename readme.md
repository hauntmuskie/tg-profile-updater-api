## Telegram Profile Updater

The Profile Updater script is a Python program that allows you to update your Telegram profile name and about section with the current time. The script is designed to be flexible and configurable, allowing you to enable or disable specific profile update features and customize various settings through a configuration file.

### Installation

To run the Profile Updater script, you need to have Python 3.x installed on your system. You can follow these steps to get started:

1. Clone the repository or download the script files to your local machine.

2. Install the required dependencies by running the following command in your terminal:

   ```
   pip install -r requirements.txt
   ```

### Configuration

Before running the Profile Updater script, you need to configure the settings in the `config.json` file. The configuration options available are as follows:

- `api_id`: Your Telegram API ID. You can obtain this by creating an application in the Telegram API development platform (https://my.telegram.org/apps).
- `api_hash`: Your Telegram API hash. This is also obtained during the application creation process.
- `update_name`: A boolean value indicating whether to update the profile name. Set it to `true` to enable name updates or `false` to disable them.
- `update_about`: A boolean value indicating whether to update the profile about section. Set it to `true` to enable about section updates or `false` to disable them.
- `timezone`: The desired timezone for displaying the current time. You can set this to any valid timezone value supported by the `pytz` library.
- `show_seconds`: A boolean value indicating whether to include seconds in the displayed time. Set it to `true` to include seconds or `false` to exclude them. _**Warning: Enabling this option may increase the frequency of profile updates and potentially lead to rate limiting by the Telegram API.**_

### Running the Script

To run the Profile Updater script, follow these steps:

1. Configure the `config.json` file with your desired settings.

2. Open a terminal or command prompt and navigate to the directory where the script files are located.

3. Run the following command:

   ```
   python main.py
   ```

4. The script will start executing and will update your Telegram profile based on the configured settings. The script will continue running indefinitely, updating the profile every minute when the seconds reach 0.

### Logging

The Profile Updater script logs its activity to two log files: `profile_update.log` and `profile_update_summary.log`.

- `profile_update.log`: This log file contains detailed log messages, including information about each profile update action performed by the script. It provides a comprehensive record of the script's activities and any potential errors or warnings encountered.

- `profile_update_summary.log`: This log file contains summary messages that only include the updated timestamp and the section (name or about) that was updated. It serves as a concise summary of the profile update events without duplicating the detailed log entries.

Both log files follow the same log format:

```
[timestamp] - [name] - [log level] - [message]
```

- `timestamp`: The timestamp of the log entry.
- `name`: The logger name (`ProfileUpdater` or `ProfileUpdaterSummary`).
- `log level`: The log level indicating the severity of the message (e.g., INFO, WARNING, ERROR).
- `message`: The log message describing the event or information.

### Customization

If you want to customize the logging behavior or extend the script's functionality, you can modify the code accordingly. Here are some possible customizations:

- Adjust the log format or log levels to suit your preferences.
- Add additional features or actions to be performed during profile updates.
- Implement error handling or exception handling mechanisms to handle specific scenarios.

Feel

 free to modify the code to fit your specific requirements and use cases.

### Conclusion

The Profile Updater script provides a convenient way to automatically update your Telegram profile with the current time. By configuring the script according to your preferences, you can personalize your profile and display dynamic information.