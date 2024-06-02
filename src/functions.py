import os
import requests
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from telegram.ext import CallbackContext, ConversationHandler
from variables import (
    uz_messages, ru_messages, ru_regions, uz_regions, ru_specializations, uz_specializations, 
    uz_start_message, ru_start_message, uz_exp_messages, ru_exp_messages, language
)

# Define language options
UZBEK_OPTION = "Uzbek🇺🇿"
RUSSIAN_OPTION = "Русский🇷🇺"

# Define conversation states
(
    LANGUAGE, NAME, PHONE, AGE, MARITAL_STATUS, EDUCATION, SPECIALIZATION, EXPERIENCE, 
    STRENGTHS, WHY_US, BRANCH, SALARY, PHOTO
) = range(13)

def log(log_message: str):
    print(log_message)

def start(update: Update, context: CallbackContext) -> int:
    language_keyboard = [[UZBEK_OPTION, RUSSIAN_OPTION]]
    update.message.reply_text(
        language, 
        reply_markup=ReplyKeyboardMarkup(language_keyboard, resize_keyboard=True, one_time_keyboard=True)
    )
    return LANGUAGE

def choose_language(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data['language'] = update.message.text

    log(f"User {update.message.chat_id} chose language: {user_data['language']}")

    if user_data['language'] == UZBEK_OPTION:
        update.message.reply_text(uz_start_message, reply_markup=ReplyKeyboardRemove())
        update.message.reply_text(uz_messages['NAME'])
    else:
        update.message.reply_text(ru_start_message, reply_markup=ReplyKeyboardRemove())
        update.message.reply_text(ru_messages['NAME'])

    return NAME

def get_name(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data

    if update.message.text:
        user_data['name'] = update.message.text
        log(f"User {update.message.chat_id} provided name: {user_data['name']}")

        if user_data['language'] == UZBEK_OPTION:
            contact_text = "Kontaktni yuborish☎️"
            cancel_text = "/cancel❌"
            phone_prompt = uz_messages['PHONE']
        else:
            contact_text = "Поделиться контактом☎️"
            cancel_text = "/cancel❌"
            phone_prompt = ru_messages['PHONE']

        contact_button = KeyboardButton(text=contact_text, request_contact=True)
        cancel_button = KeyboardButton(text=cancel_text)
        contact_keyboard = ReplyKeyboardMarkup([[contact_button], [cancel_button]], one_time_keyboard=True)

        update.message.reply_text(phone_prompt, reply_markup=contact_keyboard)
        return PHONE
    else:
        prompt_message = uz_exp_messages['NAME_EXCEPTION'] if user_data['language'] == UZBEK_OPTION else ru_exp_messages['NAME_EXCEPTION']
        update.message.reply_text(prompt_message)
        return NAME

def get_phone(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    phone_number = None

    if update.message.contact:
        phone_number = update.message.contact.phone_number
    elif update.message.text:
        if any(char.isdigit() for char in update.message.text) and len(update.message.text) >= 9:
            phone_number = update.message.text

    if phone_number:
        user_data['phone'] = phone_number
        log(f"User {update.message.chat_id} provided phone: {user_data['phone']}")

        cancel_button = KeyboardButton(text="/cancel❌")
        cancel_keyboard = ReplyKeyboardMarkup([[cancel_button]], one_time_keyboard=True)

        next_message = uz_messages['AGE'] if user_data['language'] == UZBEK_OPTION else ru_messages['AGE']
        update.message.reply_text(next_message, reply_markup=cancel_keyboard)
        return AGE
    else:
        contact_button = KeyboardButton(text="Share Contact", request_contact=True)
        cancel_button = KeyboardButton(text="/cancel❌")
        contact_keyboard = ReplyKeyboardMarkup([[contact_button], [cancel_button]], one_time_keyboard=True)

        error_message = uz_exp_messages['PHONE_EXCEPTION'] if user_data['language'] == UZBEK_OPTION else ru_exp_messages['PHONE_EXCEPTION']
        update.message.reply_text(error_message, reply_markup=contact_keyboard)
        return PHONE

def get_age(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data

    if update.message.text.isdigit():
        user_data['age'] = update.message.text
        log(f"User {update.message.chat_id} provided age: {user_data['age']}")

        next_message = uz_messages['MARITAL_STATUS'] if user_data['language'] == UZBEK_OPTION else ru_messages['MARITAL_STATUS']
        update.message.reply_text(next_message)
        return MARITAL_STATUS
    else:
        error_message = uz_exp_messages['AGE_EXCEPTION'] if user_data['language'] == UZBEK_OPTION else ru_exp_messages['AGE_EXCEPTION']
        update.message.reply_text(error_message)
        return AGE

def get_marital_status(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data['marital_status'] = update.message.text
    log(f"User {update.message.chat_id} provided marital status: {user_data['marital_status']}")

    next_message = uz_messages['EDUCATION'] if user_data['language'] == UZBEK_OPTION else ru_messages['EDUCATION']
    update.message.reply_text(next_message)
    return EDUCATION

def get_education(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data['education'] = update.message.text
    log(f"User {update.message.chat_id} provided education: {user_data['education']}")

    specializations = uz_specializations if user_data['language'] == UZBEK_OPTION else ru_specializations
    prompt_message = uz_messages['SPECIALIZATION'] if user_data['language'] == UZBEK_OPTION else ru_messages['SPECIALIZATION']
    reply_markup = ReplyKeyboardMarkup(specializations, one_time_keyboard=True)

    update.message.reply_text(prompt_message, reply_markup=reply_markup)
    return SPECIALIZATION

def get_specialization(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    specialization_input = update.message.text

    if specialization_input in uz_specializations or specialization_input in ru_specializations:
        user_data['specialization'] = specialization_input
        log(f"User {update.message.chat_id} provided specialization: {user_data['specialization']}")

        next_message = uz_messages['EXPERIENCE'] if user_data['language'] == UZBEK_OPTION else ru_messages['EXPERIENCE']
        update.message.reply_text(next_message)
        return EXPERIENCE
    else:
        error_message = uz_exp_messages['SPECIALIZATION_EXCEPTION'] if user_data['language'] == UZBEK_OPTION else ru_exp_messages['SPECIALIZATION_EXCEPTION']
        update.message.reply_text(error_message)
        return SPECIALIZATION

def get_experience(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data['experience'] = update.message.text
    log(f"User {update.message.chat_id} provided experience: {user_data['experience']}")

    next_message = uz_messages['STRENGTHS'] if user_data['language'] == UZBEK_OPTION else ru_messages['STRENGTHS']
    update.message.reply_text(next_message)
    return STRENGTHS

def get_strengths(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data['strengths'] = update.message.text
    log(f"User {update.message.chat_id} provided strengths: {user_data['strengths']}")

    next_message = uz_messages['WHY_US'] if user_data['language'] == UZBEK_OPTION else ru_messages['WHY_US']
    update.message.reply_text(next_message)
    return WHY_US

def get_why_us(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data['why_us'] = update.message.text
    log(f"User {update.message.chat_id} provided reason for joining: {user_data['why_us']}")

    regions = uz_regions if user_data['language'] == UZBEK_OPTION else ru_regions
    prompt_message = uz_messages['BRANCH'] if user_data['language'] == UZBEK_OPTION else ru_messages['BRANCH']
    reply_markup = ReplyKeyboardMarkup(regions, one_time_keyboard=True)

    update.message.reply_text(prompt_message, reply_markup=reply_markup)
    return BRANCH

def get_branch(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    branch_input = update.message.text

    if branch_input in uz_regions or branch_input in ru_regions:
        user_data['branch'] = branch_input
        log(f"User {update.message.chat_id} provided branch: {user_data['branch']}")

        next_message = uz_messages['SALARY'] if user_data['language'] == UZBEK_OPTION else ru_messages['SALARY']
        update.message.reply_text(next_message)
        return SALARY
    else:
        error_message = uz_exp_messages['BRANCH_EXCEPTION'] if user_data['language'] == UZBEK_OPTION else ru_exp_messages['BRANCH_EXCEPTION']
        update.message.reply_text(error_message)
        return BRANCH

def get_salary(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data['salary'] = update.message.text
    log(f"User {update.message.chat_id} provided salary: {user_data['salary']}")

    next_message = uz_messages['PHOTO'] if user_data['language'] == UZBEK_OPTION else ru_messages['PHOTO']
    update.message.reply_text(next_message)
    return PHOTO

def get_photo(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
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

    if 'photo' in user_data:
        photo_caption = hr_message
        photo = user_data['photo']
        context.bot.send_photo(chat_id=os.getenv('HR_USER_ID'), photo=photo, caption=photo_caption)
    else:
        context.bot.send_message(chat_id=os.getenv('HR_USER_ID'), text=hr_message)
    user_data.clear()

def cancel(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data.clear()

    cancel_message = "Bekor qilindi" if user_data.get('language') == UZBEK_OPTION else "Отменено"
    update.message.reply_text(cancel_message, reply_markup=ReplyKeyboardRemove())
    log(f"User {update.message.chat_id} canceled the conversation.")
    return ConversationHandler.END
