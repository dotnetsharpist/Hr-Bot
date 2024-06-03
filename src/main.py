import os
from telegram import Update, Bot, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler
from functions import start, choose_language, get_name, get_phone, get_age, get_marital_status, get_education, get_specialization, get_position, get_experience, get_strengths, get_why_us, get_branch, get_salary, get_photo, cancel, UZBEK_OPTION, RUSSIAN_OPTION

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

# Define conversation states
LANGUAGE, NAME, PHONE, AGE, MARITAL_STATUS, EDUCATION, SPECIALIZATION, POSITION, EXPERIENCE, STRENGTHS, WHY_US, BRANCH, SALARY, PHOTO = range(14)

def main():
    try:
        updater = Updater(BOT_TOKEN, use_context=True)
        dp = updater.dispatcher
        
        print('main')

        # Define the conversation handler with the states
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', start)],
            states={
                LANGUAGE: [
                    MessageHandler(Filters.regex(f'^{UZBEK_OPTION}$|^{RUSSIAN_OPTION}$'), choose_language),
                    MessageHandler(Filters.regex('^Cancel$'), cancel)
                ],
                NAME: [
                    MessageHandler(Filters.text & ~Filters.command, get_name),
                    MessageHandler(Filters.regex('^Cancel$'), cancel)
                ],
                PHONE: [
                    MessageHandler(Filters.contact | (Filters.text & Filters.regex(r'^\+?[1-9]\d{1,14}$')), get_phone),
                    MessageHandler(Filters.regex('^Cancel$'), cancel)
                ],
                AGE: [
                    MessageHandler(Filters.text & ~Filters.command, get_age),
                    MessageHandler(Filters.regex('^Cancel$'), cancel)
                ],
                MARITAL_STATUS: [
                    MessageHandler(Filters.text & ~Filters.command, get_marital_status),
                    MessageHandler(Filters.regex('^Cancel$'), cancel)
                ],
                EDUCATION: [
                    MessageHandler(Filters.text & ~Filters.command, get_education),
                    MessageHandler(Filters.regex('^Cancel$'), cancel)
                ],
                SPECIALIZATION: [
                    MessageHandler(Filters.text & ~Filters.command, get_specialization),
                    MessageHandler(Filters.regex('^Cancel$'), cancel)
                ],
                POSITION: [
                    MessageHandler(Filters.text & ~Filters.command, get_position),
                    MessageHandler(Filters.regex('^Cancel$'), cancel)
                ],
                EXPERIENCE: [
                    MessageHandler(Filters.text & ~Filters.command, get_experience),
                    MessageHandler(Filters.regex('^Cancel$'), cancel)
                ],
                STRENGTHS: [
                    MessageHandler(Filters.text & ~Filters.command, get_strengths),
                    MessageHandler(Filters.regex('^Cancel$'), cancel)
                ],
                WHY_US: [
                    MessageHandler(Filters.text & ~Filters.command, get_why_us),
                    MessageHandler(Filters.regex('^Cancel$'), cancel)
                ],
                BRANCH: [
                    MessageHandler(Filters.text & ~Filters.command, get_branch),
                    MessageHandler(Filters.regex('^Cancel$'), cancel)
                ],
                SALARY: [
                    MessageHandler(Filters.text & ~Filters.command, get_salary),
                    MessageHandler(Filters.regex('^Cancel$'), cancel)
                ],
                PHOTO: [
                    MessageHandler(Filters.photo, get_photo),
                    MessageHandler(Filters.regex('^Cancel$'), cancel)
                ],
            },
            fallbacks=[CommandHandler('cancel', cancel)]
        )

        dp.add_handler(conv_handler)

        # Start the Bot
        updater.start_polling()
        updater.idle()
    except Exception as e:
        updater.bot.send_message(6177562485, text=e)

if __name__ == '__main__':
    main()
