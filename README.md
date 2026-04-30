# AcidGunner Bots

A collection of utility bots for Discord and Telegram, maintained by AcidGunner.
* instructions will be on the installation step
* README.md created by ERRORminePC
## Prerequisites

* Python 3.x installed on your system.
* Git (optional, for cloning).
* API Tokens for the respective platforms:
  * Discord Developer Portal for your Discord Bot Token.
  * BotFather for your Telegram Bot Token.
## Installation

1. Clone the repository:
   git clone https://github.com/AcidGunner/Bots.git
   cd Bots

2. Create a virtual environment (Recommended):
   python -m venv venv
   source venv/bin/activate

3. Install the required dependencies:
   pip install -r requirements.txt

4. Configure your Environment Variables:
   Create a `.env` file to store your tokens securely:
   nano .env
   
   Add the following lines (replace with your actual tokens):
   DISCORD_TOKEN=your_discord_token_here
   TELEGRAM_TOKEN=your_telegram_token_here
   
   (Press Ctrl+X, then Y, and Enter to save and exit)

## How to Run

To start the bots, use the following commands in your terminal:

* For the Discord bot:
  python dcord.py

* For the Telegram bot:
  python tgram.py

* Tip for Android/Termux users: Use `tmux` to keep the bots running in the background after you close the app.
