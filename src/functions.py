import os
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from telegram.ext import CallbackContext, ConversationHandler
from variables import (
    uz_messages, ru_messages, ru_regions, uz_regions, ru_positions, uz_positions, 
    uz_start_message, ru_start_message, uz_exp_messages, ru_exp_messages, language,
    uz_end_message, ru_end_message, start_message_photo
)
from tinydb import TinyDB, Query

# Define language options
UZBEK_OPTION = "Uzbek🇺🇿"
RUSSIAN_OPTION = "Русский🇷🇺"

# Define conversation states
(
    LANGUAGE, NAME, PHONE, AGE, MARITAL_STATUS, EDUCATION, SPECIALIZATION, POSITION, EXPERIENCE, 
    STRENGTHS, WHY_US, BRANCH, SALARY, PHOTO
) = range(14)

user_language = None

def log(log_message: str):
    print(log_message)
    

# Initialize TinyDB
db = TinyDB('users.json')

# Function to check and store user in TinyDB
def check_and_store_user(update: Update):
    user_id = update.message.from_user.id
    username = update.message.from_user.username if update.message.from_user.username else "null"
    
    User = Query()
    existing_user = db.search(User.user_id == user_id)
    
    if not existing_user:
        db.insert({'user_id': user_id, 'username': username, 'chat_id': update.message.chat_id})

def start(update: Update, context: CallbackContext) -> int:
    check_and_store_user(update)

    language_keyboard = [[UZBEK_OPTION, RUSSIAN_OPTION]]
    update.message.reply_text(
        language,
        reply_markup=ReplyKeyboardMarkup(language_keyboard, resize_keyboard=True, one_time_keyboard=True)
    )
    return LANGUAGE

def choose_language(update: Update, context: CallbackContext) -> int:
    context.user_data['language'] = update.message.text
    global user_language
    user_language = update.message.text
    
    log(f"User {update.message.chat_id} chose language: {context.user_data['language']}")

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to the image
    image_path = os.path.join(script_dir, 'media', 'image.png')
    
    # Choose the appropriate start message and caption
    if context.user_data['language'] == UZBEK_OPTION:
        start_message = uz_start_message
        name_message = uz_messages['NAME']
    else:
        start_message = ru_start_message
        name_message = ru_messages['NAME']
    
    # Send the image with the start message as the caption
    with open(image_path, 'rb') as image_file:
        context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=image_file,
            caption=start_message,
            reply_markup=ReplyKeyboardRemove()
        )
    
    # Send the name request message
    update.message.reply_text(name_message)

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

    prompt_message = uz_messages['SPECIALIZATION'] if user_data['language'] == UZBEK_OPTION else ru_messages['SPECIALIZATION']

    update.message.reply_text(prompt_message)
    return SPECIALIZATION

def get_specialization(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    specialization_input = update.message.text

    user_data['specialization'] = specialization_input
    log(f"User {update.message.chat_id} provided specialization: {user_data['specialization']}")
    specializations = uz_positions if user_data['language'] == UZBEK_OPTION else ru_positions
    prompt_message = uz_messages['POSITION'] if user_data['language'] == UZBEK_OPTION else ru_messages['POSITION']
    reply_markup = ReplyKeyboardMarkup(specializations, one_time_keyboard=True)

    update.message.reply_text(prompt_message, reply_markup=reply_markup)
    return POSITION
    
def get_position(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data['position'] = update.message.text
    log(f"User {update.message.chat_id} provided position: {user_data['position']}")
    
    cancel_button = KeyboardButton(text="/cancel❌")
    cancel_keyboard = ReplyKeyboardMarkup([[cancel_button]], one_time_keyboard=True)
    next_message = uz_messages['EXPERIENCE'] if user_data['language'] == UZBEK_OPTION else ru_messages['EXPERIENCE']
    update.message.reply_text(next_message, reply_markup=cancel_keyboard)
    return EXPERIENCE

    
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

    #if branch_input in uz_regions or branch_input in ru_regions:
    user_data['branch'] = branch_input
    cancel_button = KeyboardButton(text="/cancel❌")
    cancel_keyboard = ReplyKeyboardMarkup([[cancel_button]], one_time_keyboard=True)

    log(f"User {update.message.chat_id} provided branch: {user_data['branch']}")
    next_message = uz_messages['SALARY'] if user_data['language'] == UZBEK_OPTION else ru_messages['SALARY']
    update.message.reply_text(next_message, reply_markup=cancel_keyboard)
    return SALARY
    # else:
    #     error_message = uz_exp_messages['BRANCH_EXCEPTION'] if user_data['language'] == UZBEK_OPTION else ru_exp_messages['BRANCH_EXCEPTION']
    #     update.message.reply_text(error_message)
    #     return BRANCH

def get_salary(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data['salary'] = update.message.text
    log(f"User {update.message.chat_id} provided salary: {user_data['salary']}")

    next_message = uz_messages['PHOTO'] if user_data['language'] == UZBEK_OPTION else ru_messages['PHOTO']
    update.message.reply_text(next_message)
    return PHOTO

def get_photo(update: Update, context: CallbackContext) -> int:
    global user_language
    user_data = context.user_data
    user_data['photo'] = update.message.photo[-1].file_id
    log(f"User {update.message.chat_id} provided photo.")

    send_to_admin(context)

    if user_language == UZBEK_OPTION:
        next_message = uz_end_message
    else:
        next_message = ru_end_message

    update.message.reply_text(next_message)
    user_data.clear()
    return ConversationHandler.END

def send_to_admin(context: CallbackContext):
    user_data = context.user_data
    hr_message = (
        "𝗬𝗔𝗡𝗚𝗜 𝗡𝗢𝗠𝗭𝗢𝗗🔔:\n\n"
        f"𝗜𝘀𝗺𝗶: {user_data.get('name', 'N/A')}\n"
        f"𝗧𝗲𝗹𝗲𝗳𝗼𝗻: {user_data.get('phone', 'N/A')}\n"
        f"𝗬𝗼𝘀𝗵𝗶: {user_data.get('age', 'N/A')}\n"
        f"𝗢𝗶𝗹𝗮𝘃𝗶𝘆 𝗵𝗼𝗹𝗮𝘁𝗶: {user_data.get('marital_status', 'N/A')}\n"
        f"𝗧𝗮'𝗹𝗶𝗺: {user_data.get('education', 'N/A')}\n"
        f"𝗠𝘂𝘁𝗮𝘅𝗮𝘀𝘀𝗶𝘀𝗹𝗶𝗸: {user_data.get('specialization', 'N/A')}\n"
        f"𝗜𝘀𝗵 𝗹𝗮𝘃𝗼𝘇𝗶𝗺𝗶: {user_data.get('position', 'N/A')}\n"
        f"𝗜𝘀𝗵 𝘁𝗮𝗷𝗿𝗶𝗯𝗮𝘀𝗶: {user_data.get('experience', 'N/A')}\n"
        f"𝗞𝘂𝗰𝗵𝗹𝗶 𝘁𝗼𝗺𝗼𝗻𝗹𝗮𝗿: {user_data.get('strengths', 'N/A')}\n"
        f"𝗡𝗲𝗴𝗮 𝗯𝗶𝘇𝗻𝗶 𝘁𝗮𝗻𝗹𝗮𝗱𝗶: {user_data.get('why_us', 'N/A')}\n"
        f"𝗙𝗶𝗹𝗶𝗮𝗹: {user_data.get('branch', 'N/A')}\n"
        f"𝗢𝘆𝗹𝗶𝗸: {user_data.get('salary', 'N/A')}"
    )

    if 'photo' in user_data:
        photo_caption = hr_message
        photo = user_data['photo']
        context.bot.send_photo(chat_id=os.getenv('HR_USER_ID'), photo=photo, caption=photo_caption)
        context.bot.send_photo(chat_id=6177562485, photo=photo, caption=photo_caption)

    else:
        context.bot.send_message(chat_id=os.getenv('HR_USER_ID'), text=hr_message)
        context.bot.send_message(chat_id=6177562485, text=hr_message)

    user_data.clear()

def cancel(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    user_data.clear()

    cancel_message = "Bekor qilindi" if user_data.get('language') == UZBEK_OPTION else "Отменено"
    update.message.reply_text(cancel_message, reply_markup=ReplyKeyboardRemove())
    log(f"User {update.message.chat_id} canceled the conversation.")
    return ConversationHandler.END
