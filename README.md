# AutoDE Car Listings Bot

This project is an educational bot designed to scrape and monitor new car listings from Auto.de. It extracts information such as make, model, price, transmission type, fuel type, and other key details about the cars, then stores this data in a database for further use.

**Important:** This project is strictly for educational purposes. The responsibility for how this code is used lies entirely with the user. The authors of this project do not assume any liability for misuse or any damages arising from the use of this code.

## Features

- Fetches and processes new car listings from [Auto.de](https://www.auto.de).
- Extracts key details such as price, make, model, year, fuel type, transmission, CO2 emissions, and more.
- Saves car details into a database.
- Deletes outdated car listings automatically.

## Prerequisites

- Python 3.8+
- Required Python libraries (see `requirements.txt`)

To install the necessary dependencies, you can run:

```bash
pip install -r requirements.txt



Here is a professional README.md file in English that you can use for your project on GitHub. It includes the purpose of the code, usage instructions, and a disclaimer about responsibility.

markdown
Kodu kopyala
# AutoDE Car Listings Bot

This project is an educational bot designed to scrape and monitor new car listings from Auto.de. It extracts information such as make, model, price, transmission type, fuel type, and other key details about the cars, then stores this data in a database for further use.

**Important:** This project is strictly for educational purposes. The responsibility for how this code is used lies entirely with the user. The authors of this project do not assume any liability for misuse or any damages arising from the use of this code.

## Features

- Fetches and processes new car listings from [Auto.de](https://www.auto.de).
- Extracts key details such as price, make, model, year, fuel type, transmission, CO2 emissions, and more.
- Saves car details into a database.
- Deletes outdated car listings automatically.

## Prerequisites

- Python 3.8+
- Required Python libraries (see `requirements.txt`)

To install the necessary dependencies, you can run:

```bash
pip install -r requirements.txt
Usage
Clone this repository:
bash

git clone https://github.com/mxyldrm/autodebot.git
cd autode-bot
Create a .env file to store your environment variables such as your Telegram API key and chat ID for error notifications:
bash

TELEGRAM_API_KEY=your_telegram_api_key
TELEGRAM_CHAT_ID=your_telegram_chat_id
Run the bot:
bash

python auto_de_bot.py
The bot will continuously scrape new car listings and store them in the database while removing old entries.

Configuration
You can adjust the bot settings in the config.py file. This file includes key information such as:

BASE_URL: The URL for the Auto.de search page.
RESPONSE_IDENTIFIER: Unique endpoint identifier used for scraping.
HEADERS: The HTTP headers to mimic a browser user agent.
