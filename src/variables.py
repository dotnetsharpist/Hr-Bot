import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
HR_USER_ID = os.getenv('HR_USER_ID')
LOG_CHANNEL_ID = os.getenv('LOG_CHANNEL_ID')

# Language options
UZBEK_OPTION = "Uzbek"
RUSSIAN_OPTION = "Русский"

# Questions in Uzbek and Russian
uz_messages = {
    "LANGUAGE": "Tilni tanlang",
    "NAME": "Ismingiz va Familyangiz?",
    "PHONE": "Telefon Raqamingiz?",
    "AGE": "Yoshingiz?",
    "MARITAL_STATUS": "Oilaviy holatingiz?",
    "EDUCATION": "Ma'lumotingiz? (Qaysi ta'lim muassasasini tamomlagansiz?)",
    "SPECIALIZATION": "Mutaxassisligingiz?",
    "EXPERIENCE": "Ish tajribangiz? (avval ishlagan joylariz)",
    "STRENGTHS": "Kuchli tomonlaringiz?",
    "WHY_US": "Nega aynan bizni korxonada ishlamoqchisiz?",
    "BRANCH": "Filialni tanlang",
    "SALARY": "Nechi pul maosh olishni xohlaysiz?",
    "PHOTO": "Rasmingizni yuboring"
}

ru_messages = {
    "LANGUAGE": "Выберите язык",
    "NAME": "Ваше имя и фамилия?",
    "PHONE": "Ваш номер телефона?",
    "AGE": "Ваш возраст?",
    "MARITAL_STATUS": "Ваше семейное положение?",
    "EDUCATION": "Ваше образование? (Какое учебное заведение вы закончили?)",
    "SPECIALIZATION": "Ваша специальность?",
    "EXPERIENCE": "Ваш опыт работы? (предыдущие места работы)",
    "STRENGTHS": "Ваши сильные стороны?",
    "WHY_US": "Почему вы хотите работать в нашей компании?",
    "BRANCH": "Выберите филиал",
    "SALARY": "Какую зарплату вы хотите получать?",
    "PHOTO": "Отправьте ваше фото"
}

uzbek_regions = [
    ["Toshkent", "Samarqand", "Buxoro"],
    ["Xiva", "Nukus", "Andijon"],
    ["Farg'ona", "Namangan", "Navoiy"],
    ["Termiz", "Urganch", "Qoraqalpog'iston"]
]

russian_regions = [
    ["Ташкент", "Самарканд", "Бухара"],
    ["Хива", "Нукус", "Андижан"],
    ["Фергана", "Наманган", "Навои"],
    ["Термез", "Ургенч", "Каракалпакстан"]
]

uzbek_specializations = [
    ["Операцион бош менежери", "Кассир", "IT"],
    ["Ички аудит", "Бош бухгалтер", "Юрист"],
    ["HR менежер", "Кредит маҳсулотларини сотиш бўлими"]
]

russian_specializations = [
    ["Операционный менеджер", "Кассир", "IT"],
    ["Внутренний аудит", "Главный бухгалтер", "Юрист"],
    ["HR менеджер", "Отдел продаж кредитных продуктов"]
]


uz_exp_messages = {
    "AGE_EXCEPTION": "Iltimos, Yoshingizni kiriting"
}

ru_exp_messages = {
    "AGE_EXCEPTION": "Пожалуйста, киритуйте ваш возраст"
}