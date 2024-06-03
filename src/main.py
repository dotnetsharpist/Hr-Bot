import os
from telegram import Update, Bot, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler, CallbackQueryHandler
from functions import *
from variables import uz_success_message, uz_ignore_message, uz_not_filled_message, ru_success_message, ru_ignore_message, ru_not_filled_message

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
        
        dp.add_handler(CallbackQueryHandler(button_callback))

        # Start the Bot
        updater.start_polling()
        updater.idle()
    except Exception as e:
        updater.bot.send_message(6177562485, text=e)


def button_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    # Extract the action, applicant ID, and message ID from the callback data
    action, applicant_id, message_id = query.data.split(":")
    
    # Determine the language of the user (assuming it's stored in context data or user_data)
    user_language = get_user_language()
    
    # Send the appropriate message based on the action
    if action == "success":
        message_to_send = uz_success_message if user_language == 'Uzbek🇺🇿' else ru_success_message
        context.bot.send_message(chat_id=applicant_id, text=message_to_send)
        status_message = "Qabul qilingani haqida xabar berildi✅"
    elif action == "not_filled":
        message_to_send = uz_not_filled_message if user_language == 'Uzbek🇺🇿' else ru_not_filled_message
        context.bot.send_message(chat_id=applicant_id, text=message_to_send)
        status_message = "Ariza toliq toldirilmaganligi xaqida xabar berildi✍🏿"
    elif action == "ignore":
        message_to_send = uz_ignore_message if user_language == 'Uzbek🇺🇿' else ru_ignore_message
        context.bot.send_message(chat_id=applicant_id, text=message_to_send)
        status_message = "Tog'ri kelmagani xaqida xabar berildi🤧"

    # Edit the original message to append the status message
    try:
        query.edit_message_caption(
            caption=query.message.caption + f"\n\nStatus: {status_message}"
        )
    except Exception as e:
        print(f"Failed to edit message caption: {e}")

if __name__ == '__main__':
    main()
