# LeetCode Questions Solved Discord Bot

Welcome to the LeetCode Questions Solved Discord Bot repository! This bot is designed to help users track and display the number of LeetCode questions solved by different members of your Discord server.

## Features

- **User Stats:** Retrieve the number of LeetCode questions solved by a user using their LeetCode username.

- **Interactive Commands:** Use simple commands to interact with the bot and gather information.

## Installation and Setup

1. Clone this repository to your local machine:
   ```sh
   git clone https://github.com/BradenStitt/LeetcodeDiscordBot.git
2. Install the Required Python Packages
   ```sh
   pip install -r requirements.txt
3. Create a Discord bot by following the instructions in the [Discord Developer Portal](https://discord.com/developers/applications). Once your bot is created, obtain its token.
4. In the root directory of your bot's project, create a `.env` file. Add your bot token to this file using the following format:
5. Generate an OAuth2 URL for your bot in the [Discord Developer Portal](https://discord.com/developers/applications). Use this URL to invite your bot to your Discord server.
6. Open your terminal and navigate to your bot's project directory. Run the bot using the following command:
   ```sh
   python bot.py

## Usage

- Use the `!leetcode <leetcode_username>` command to get the number of LeetCode questions solved by a user shown in the current channel. For example, `!leetcode john_doe`.
   
- Use the `?leetcode <leetcode_username>` command to get the number of LeetCode questions solved by a user sent via DM. For example, `?leetcode john_doe`.

- Use the `!help` command to get a list of available commands.

## License

This project is licensed under the [MIT License](LICENSE).
