import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
HR_USER_ID = os.getenv('HR_USER_ID')
LOG_CHANNEL_ID = os.getenv('LOG_CHANNEL_ID')

# Language options
UZBEK_OPTION = "Uzbek"
RUSSIAN_OPTION = "Русский"

language = "Tilni tanlang/Выберите язык"

uz_start_message = """
Assalomu Alaykum!

Sizni yangi martaba cho'qqisiga chiqish yo'lida kutib olishdan xursandmiz! Bizning tashkilotimiz iste'dod, ishtiyoq va rivojlanish istagini qadrlaydi. Agar siz o'z salohiyatingizni yuzaga chiqarish, mazmunli hissa qo'shish va do'stona professionallar jamoasida ishlash imkoniyatini izlayotgan bo'lsangiz, siz to'g'ri yo'ldasiz.

Sizni har bir xodim qadrlanadigan va qo'llab-quvvatlanadigan jamoamizning bir qismi bo'lishga taklif qilamiz. Bu yerda siz – o'sish uchun imkoniyatlar, qiziqarli loyihalar va qulay ish muhitini topasiz. Sizning kuchingiz va g'oyalaringiz bizning jamoaviy sa'y-harakatlarimizga muhim qo'shimcha bo'lishi mumkin. Tanlov jarayonida muvaffaqiyatlar tilaymiz va rezyumeyingizni kutib qolamiz!

Hurmat bilan,
“HAMROH mikromoliya tashkiloti” jamoasi
"""

ru_start_message = """
Приветствуем вас!

Мы рады, что вы ждете начала своего нового путешествия с нами! Наша организация ценит ваш интерес и стремление к развитию. Если вы готовы проявить свои навыки, внести содержательный вклад и работать в дружном профессиональном коллективе, то вы на правильном пути.

Мы предлагаем вам стать частью нашей команды, которая ценит и поддерживает каждого сотрудника. Здесь вы найдете возможности для роста, интересные проекты и комфортную рабочую обстановку. Ваша сила и цели могут стать важным дополнением к нашим коллективным усилиям. Желаем вам успехов в процессе выбора и с нетерпением ждем вашего резюме!

С уважением,
Команда "HAMROH микрофинансовой организации"
"""

# Questions in Uzbek and Russian
uz_messages = {
    "NAME": "To‘liq ismingizni yozing (F.I.O):",
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
    "NAME": "Напишите ваше полное имя (Ф.И.О):",
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

uz_regions = [
    ["Toshkent", "Samarqand", "Buxoro"],
    ["Xiva", "Nukus", "Andijon"],
    ["Farg'ona", "Namangan", "Navoiy"],
    ["Termiz", "Urganch", "Qoraqalpog'iston"]
]

ru_regions = [
    ["Ташкент", "Самарканд", "Бухара"],
    ["Хива", "Нукус", "Андижан"],
    ["Фергана", "Наманган", "Навои"],
    ["Термез", "Ургенч", "Каракалпакстан"]
]

uz_specializations = [
    ["Операцион бош менежери", "Кассир", "IT"],
    ["Ички аудит", "Бош бухгалтер", "Юрист"],
    ["HR менежер", "Кредит маҳсулотларини сотиш бўлими"]
]

ru_specializations = [
    ["Операционный менеджер", "Кассир", "IT"],
    ["Внутренний аудит", "Главный бухгалтер", "Юрист"],
    ["HR менеджер", "Отдел продаж кредитных продуктов"]
]

uz_end_message = "✅Raxmat! Malumotlaringizni korib chiqib sizga aloqaga chiqamiz."

ru_end_message = "✅Спасибо! Мы свяжемся с вами после рассмотрения ваших данных."

uz_exp_messages = {
    "AGE_EXCEPTION": "Iltimos, Yoshingizni kiriting",
    "PHONE_EXCEPTION": "Iltimos, telefon raqamingizni kiriting",
    "NAME_EXCEPTION": "Iltimos, ismingizni va familyangizni kiriting",
    "MARITAL_STATUS_EXCEPTION": "Iltimos, oilaviy holatingizni kiriting",
    "EDUCATION_EXCEPTION": "Iltimos, o'zingizni ta'lim darajangizni kiriting",
    "SPECIALIZATION_EXCEPTION": "Iltimos, mutaxassisligingizni kiriting",
    "EXPERIENCE_EXCEPTION": "Iltimos, ish tajribangizni kiriting",
    "STRENGTHS_EXCEPTION": "Iltimos, kuchli tomonlaringizni kiriting",
    "WHY_US_EXCEPTION": "Iltimos, bizni qanday sababdan tanlaganligingizni kiriting",
    "BRANCH_EXCEPTION": "Iltimos, filialni tanlang",
    "SALARY_EXCEPTION": "Iltimos, maoshni kiriting",
    "PHOTO_EXCEPTION": "Iltimos, rasmingizni yuboring"
}

ru_exp_messages = {
    "AGE_EXCEPTION": "Пожалуйста, введите ваш возраст",
    "PHONE_EXCEPTION": "Пожалуйста, введите ваш номер телефона",
    "NAME_EXCEPTION": "Пожалуйста, введите ваше имя и фамилию",
    "MARITAL_STATUS_EXCEPTION": "Пожалуйста, укажите ваше семейное положение",
    "EDUCATION_EXCEPTION": "Пожалуйста, укажите ваше образование",
    "SPECIALIZATION_EXCEPTION": "Пожалуйста, укажите вашу специализацию",
    "EXPERIENCE_EXCEPTION": "Пожалуйста, укажите ваш опыт работы",
    "STRENGTHS_EXCEPTION": "Пожалуйста, укажите ваши сильные стороны",
    "WHY_US_EXCEPTION": "Пожалуйста, укажите причину выбора нашей компании",
    "BRANCH_EXCEPTION": "Пожалуйста, выберите филиал",
    "SALARY_EXCEPTION": "Пожалуйста, укажите желаемую зарплату",
    "PHOTO_EXCEPTION": "Пожалуйста, отправьте ваше фото"
}
