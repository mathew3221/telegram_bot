from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Define the /start command handler
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! I am your bot hosted on Render. Type /help to see available commands.")

# Define the /help command handler
async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("I can do the following:\n/start - Start the bot\n/help - Show this help message")

# Define a message echo handler
async def echo(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f"You said: {update.message.text}")

def main():
    # Get the bot token from the environment variable
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("Error: BOT_TOKEN environment variable is not set.")
        return

    # Create the Application object
    application = Application.builder().token(token).build()

    # Register command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start polling for updates
    application.run_polling()

if __name__ == "__main__":
    main()
