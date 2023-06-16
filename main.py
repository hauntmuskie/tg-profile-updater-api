import asyncio
import pytz
from datetime import datetime
import json
import telethon
import logging


class Config:
    """Class representing the configuration for the Profile Updater script.

    Attributes:
        api_id (int): The Telegram API ID.
        api_hash (str): The Telegram API hash.
        update_name (bool): Flag indicating whether to update the profile name.
        update_about (bool): Flag indicating whether to update the profile about section.
        timezone (pytz.timezone): The desired timezone for displaying the current time.
        show_seconds (bool): Flag indicating whether to include seconds in the displayed time.
    """

    def __init__(
        self, api_id, api_hash, update_name, update_about, timezone, show_seconds
    ):
        self.api_id = api_id
        self.api_hash = api_hash
        self.update_name = update_name
        self.update_about = update_about
        self.timezone = timezone
        self.show_seconds = show_seconds


class ProfileUpdater:
    """Class responsible for updating the Telegram profile.

    Attributes:
        config (Config): The configuration object for the script.
        logger (logging.Logger): The logger object for logging script activities.

    Methods:
        update_name: Updates the profile name with the current time.
        update_about: Updates the profile about section with the current time.
        get_formatted_time: Returns the current time formatted based on the configuration.
        display_summary: Displays a summary message for the profile update.
        update_profile: Updates the profile at regular intervals based on the configuration.
    """

    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger("ProfileUpdater")
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Log to file
        file_handler = logging.FileHandler("profile_update.log")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    async def update_name(self, client):
        """Updates the profile name with the current time.

        Args:
            client (telethon.TelegramClient): The Telegram client object for making API requests.
        """
        me = await client.get_me()
        name_parts = me.first_name.split("|")  # Split the name by '|'
        current_time = self.get_formatted_time()
        new_name = f"{name_parts[0].strip()} | {current_time}"
        await client(
            telethon.functions.account.UpdateProfileRequest(first_name=new_name)
        )
        self.display_summary("Name")

    async def update_about(self, client):
        """Updates the profile about section with the current time.

        Args:
            client (telethon.TelegramClient): The Telegram client object for making API requests.
        """
        current_time = self.get_formatted_time()
        await client(
            telethon.functions.account.UpdateProfileRequest(
                about=f"⏱ [现在!] : {current_time}"
            )
        )
        self.display_summary("About section")

    def get_formatted_time(self):
        """Returns the current time formatted based on the configuration.

        Returns:
            str: The formatted current time.
        """
        time_format = "%H:%M"
        if self.config.show_seconds:
            time_format = "%H:%M:%S"
        return datetime.now(self.config.timezone).strftime(time_format)

    def display_summary(self, section):
        """Displays a summary message for the profile update.

        Args:
            section (str): The section of the profile that was updated.
        """
        current_time = self.get_formatted_time()
        summary = f"{section} updated: {current_time}"
        print(summary)
        self.logger.info(summary)

    async def update_profile(self, client):
        """Updates the profile at regular intervals based on the configuration.

        Args:
            client (telethon.TelegramClient): The Telegram client object for making API requests.
        """
        while True:
            now = datetime.now(self.config.timezone)
            if now.second == 0:
                if self.config.update_name:
                    await self.update_name(client)
                if self.config.update_about:
                    await self.update_about(client)
            await asyncio.sleep(1)


async def main():
    """Main entry point of the script."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    config = load_config()

    async with telethon.TelegramClient(
        "session", config.api_id, config.api_hash
    ) as client:
        updater = ProfileUpdater(config)
        await updater.update_profile(client)


def load_config():
    """Loads the configuration from the 'config.json' file.

    Returns:
        Config: The configuration object.
    """
    with open("config.json") as config_file:
        config_data = json.load(config_file)
        api_id = config_data["api_id"]
        api_hash = config_data["api_hash"]
        update_name = config_data["update_name"]
        update_about = config_data["update_about"]
        timezone = pytz.timezone(config_data["timezone"])
        show_seconds = config_data["show_seconds"]
        return Config(
            api_id, api_hash, update_name, update_about, timezone, show_seconds
        )


if __name__ == "__main__":
    asyncio.run(main())