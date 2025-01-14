import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Define the /start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I am your bot hosted on Render. Type /help to see available commands.")

# Define the /help command handler
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("I can do the following:\n/start - Start the bot\n/help - Show this help message")

# Define a message echo handler
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"You said: {update.message.text}")

def main():
    # Get the bot token from the environment variable
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("Error: BOT_TOKEN environment variable is not set.")
        return

    # Create the Updater object
    updater = Updater(token)

    # Register command and message handlers
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start polling for updates
    updater.start_polling()
    print("Bot is running...")
    updater.idle()

if __name__ == "__main__":
    main()
