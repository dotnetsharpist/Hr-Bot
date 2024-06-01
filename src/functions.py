import os
import re
import requests
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from telegram.ext import CallbackContext, ConversationHandler
from variables import uz_messages, ru_messages, russian_regions, uzbek_regions, russian_specializations, uzbek_specializations

# Define language options
UZBEK_OPTION = "Uzbek"
RUSSIAN_OPTION = "Русский"

# Define conversation states
LANGUAGE, NAME, PHONE, AGE, MARITAL_STATUS, EDUCATION, SPECIALIZATION, EXPERIENCE, STRENGTHS, WHY_US, BRANCH, SALARY, PHOTO = range(13)

def log(log_message: str):
    # Print log message to the console
    print(log_message)

def start(update: Update, context: CallbackContext) -> int:
    language_keyboard = [[UZBEK_OPTION, RUSSIAN_OPTION]]
    update.message.reply_text(
        uz_messages["LANGUAGE"],
        reply_markup=ReplyKeyboardMarkup(language_keyboard, one_time_keyboard=True)
    )
    return LANGUAGE

def choose_language(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data['language'] = update.message.text

    log(f"User {update.message.chat_id} chose language: {user_data['language']}")

    if user_data['language'] == UZBEK_OPTION:
        update.message.reply_text(uz_messages['NAME'], reply_markup=ReplyKeyboardRemove())
    else:
        update.message.reply_text(ru_messages['NAME'], reply_markup=ReplyKeyboardRemove())
    return NAME

def get_name(update: Update, context: CallbackContext) -> int:
    if update.message.text:
        user_data = context.user_data
        user_data['name'] = update.message.text

        log(f"User {update.message.chat_id} provided name: {user_data['name']}")

        contact_button = KeyboardButton(text="Share Contact", request_contact=True)
        cancel_button = KeyboardButton(text="/cancel❌")
        contact_keyboard = ReplyKeyboardMarkup([[contact_button], [cancel_button]], one_time_keyboard=True)

        if user_data['language'] == UZBEK_OPTION:
            update.message.reply_text(uz_messages['PHONE'], reply_markup=contact_keyboard)
        else:
            update.message.reply_text(ru_messages['PHONE'], reply_markup=contact_keyboard)
        return PHONE
    else:
        update.message.reply_text("Please provide your name.")
        return NAME
    
def get_phone(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data

    phone_number = None
    if update.message.contact:
        # User shared their contact
        phone_number = update.message.contact.phone_number
    elif update.message.text:
        # Check if the input has digits and is more than 9 characters long
        text = update.message.text
        if any(char.isdigit() for char in text) and len(text) > 9:
            phone_number = text
    
    if phone_number:
        user_data['phone'] = phone_number
        log(f"User {update.message.chat_id} provided phone: {user_data['phone']}")

        cancel_button = KeyboardButton(text="/cancel❌")
        cancel_keyboard = ReplyKeyboardMarkup([[cancel_button]], one_time_keyboard=True)
        
        if user_data['language'] == UZBEK_OPTION:
            update.message.reply_text(uz_messages['AGE'], reply_markup=cancel_keyboard)
        else:
            update.message.reply_text(ru_messages['AGE'], reply_markup=cancel_keyboard)
            
        return AGE
    else:
        # Invalid input, ask for phone number again with cancel button
        contact_button = KeyboardButton(text="Share Contact", request_contact=True)
        cancel_button = KeyboardButton(text="/cancel❌")
        contact_keyboard = ReplyKeyboardMarkup([[contact_button], [cancel_button]], one_time_keyboard=True)

        if user_data['language'] == UZBEK_OPTION:
            update.message.reply_text("Iltimos, telefon raqamingizni kiriting yoki ulashing.", reply_markup=contact_keyboard)
        else:
            update.message.reply_text("Пожалуйста, введите или поделитесь своим номером телефона.", reply_markup=contact_keyboard)
        return PHONE


def get_age(update: Update, context: CallbackContext) -> int:
    if update.message.text.isdigit():
        user_data = context.user_data
        user_data['age'] = update.message.text

        log(f"User {update.message.chat_id} provided age: {user_data['age']}")

        if user_data['language'] == UZBEK_OPTION:
            update.message.reply_text(uz_messages['MARITAL_STATUS'])
        else:
            update.message.reply_text(ru_messages['MARITAL_STATUS'])
        return MARITAL_STATUS
    else:
        update.message.reply_text("Please provide your age.")
        return AGE

def get_marital_status(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data['marital_status'] = update.message.text

    log(f"User {update.message.chat_id} provided marital status: {user_data['marital_status']}")

    if user_data['language'] == UZBEK_OPTION:
        update.message.reply_text(uz_messages['EDUCATION'])
    else:
        update.message.reply_text(ru_messages['EDUCATION'])
    return EDUCATION

def get_education(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data['education'] = update.message.text

    log(f"User {update.message.chat_id} provided education: {user_data['education']}")

    # Choose education levels based on language
    if user_data['language'] == UZBEK_OPTION:
        educations = uzbek_specializations
        prompt_message = uz_messages['SPECIALIZATION']
    else:
        educations = russian_specializations
        prompt_message = ru_messages['SPECIALIZATION']

    # Convert education levels to appropriate language
    reply_markup = ReplyKeyboardMarkup(educations, one_time_keyboard=True)

    update.message.reply_text(prompt_message, reply_markup=reply_markup)
    return SPECIALIZATION


def get_specialization(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data['specialization'] = update.message.text

    log(f"User {update.message.chat_id} provided specialization: {user_data['specialization']}")

    if user_data['language'] == UZBEK_OPTION:
        update.message.reply_text(uz_messages['EXPERIENCE'])
    else:
        update.message.reply_text(ru_messages['EXPERIENCE'])
    return EXPERIENCE

def get_experience(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data['experience'] = update.message.text

    log(f"User {update.message.chat_id} provided experience: {user_data['experience']}")

    if user_data['language'] == UZBEK_OPTION:
        update.message.reply_text(uz_messages['STRENGTHS'])
    else:
        update.message.reply_text(ru_messages['STRENGTHS'])
    return STRENGTHS

def get_strengths(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data['strengths'] = update.message.text

    log(f"User {update.message.chat_id} provided strengths: {user_data['strengths']}")

    if user_data['language'] == UZBEK_OPTION:
        update.message.reply_text(uz_messages['WHY_US'])
    else:
        update.message.reply_text(ru_messages['WHY_US'])
    return WHY_US

def get_why_us(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data['why_us'] = update.message.text

    log(f"User {update.message.chat_id} provided reason for joining: {user_data['why_us']}")

    # Choose regions based on language
    if user_data['language'] == UZBEK_OPTION:
        regions = uzbek_regions
        prompt_message = uz_messages['BRANCH']
    else:
        regions = russian_regions
        prompt_message = ru_messages['BRANCH']

    # Convert regions to appropriate language
    reply_markup = ReplyKeyboardMarkup(regions, one_time_keyboard=True)

    update.message.reply_text(prompt_message, reply_markup=reply_markup)
    return BRANCH


def get_branch(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data['branch'] = update.message.text

    log(f"User {update.message.chat_id} provided branch: {user_data['branch']}")

    if user_data['language'] == UZBEK_OPTION:
        update.message.reply_text(uz_messages['SALARY'])
    else:
        update.message.reply_text(ru_messages['SALARY'])
    return SALARY

def get_salary(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data['salary'] = update.message.text

    log(f"User {update.message.chat_id} provided salary: {user_data['salary']}")

    if user_data['language'] == UZBEK_OPTION:
        update.message.reply_text(uz_messages['PHOTO'])
    else:
        update.message.reply_text(ru_messages['PHOTO'])
    return PHOTO

def get_photo(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    # Assuming you want to save the photo file ID
    user_data['photo'] = update.message.photo[-1].file_id

    log(f"User {update.message.chat_id} provided photo: {user_data['photo']}")
    
    send_to_admin(context)

    update.message.reply_text("Thank you for providing all the information. Your application has been submitted successfully!", reply_markup=ReplyKeyboardRemove())
    user_data.clear()

    return ConversationHandler.END

def send_to_admin(context: CallbackContext):
    user_data = context.user_data
    hr_message = (
        f"Новый соискатель:\n\n"
        f"Имя: {user_data.get('name', 'N/A')}\n"
        f"Телефон: {user_data.get('phone', 'N/A')}\n"
        f"Возраст: {user_data.get('age', 'N/A')}\n"
        f"Семейное положение: {user_data.get('marital_status', 'N/A')}\n"
        f"Образование: {user_data.get('education', 'N/A')}\n"
        f"Специальность: {user_data.get('specialization', 'N/A')}\n"
        f"Опыт работы: {user_data.get('experience', 'N/A')}\n"
        f"Сильные стороны: {user_data.get('strengths', 'N/A')}\n"
        f"Почему выбрал нас: {user_data.get('why_us', 'N/A')}\n"
        f"Филиал: {user_data.get('branch', 'N/A')}\n"
        f"Желаемая зарплата: {user_data.get('salary', 'N/A')}"
    )

    # Send photo with caption
    if 'photo' in user_data:
        photo_caption = hr_message  # Use application details as the caption for the photo
        photo = user_data['photo']  # Get the photo file ID from user data
        context.bot.send_photo(chat_id=os.getenv('HR_USER_ID'), photo=photo, caption=photo_caption)
    else:
        # Send only text message if no photo is provided
        context.bot.send_message(chat_id=os.getenv('HR_USER_ID'), text=hr_message)

    # Clear user data after sending the application
    user_data.clear()

def cancel(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data.clear()

    update.message.reply_text("Canceled", reply_markup=ReplyKeyboardRemove())
    log(f"User {update.message.chat_id} canceled the conversation.")

    return ConversationHandler.END
