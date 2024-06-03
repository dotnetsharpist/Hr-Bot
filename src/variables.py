import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
HR_USER_ID = os.getenv('HR_USER_ID')
LOG_CHANNEL_ID = os.getenv('LOG_CHANNEL_ID')
MEDIA_PATH = "src/media"

# Language options
UZBEK_OPTION = "Uzbek"
RUSSIAN_OPTION = "Русский"

language = "Tilni tanlang/Выберите язык"

start_message_photo = 'src/media/image.png'

uz_start_message = """
Assalomu Alaykum!

Sizni yangi martaba cho'qqisiga chiqish yo'lida kutib olishdan xursandmiz! Bizning tashkilotimiz iste'dod, ishtiyoq va rivojlanish istagini qadrlaydi. Agar siz o'z salohiyatingizni yuzaga chiqarish, mazmunli hissa qo'shish va do'stona professionallar jamoasida ishlash imkoniyatini izlayotgan bo'lsangiz, siz to'g'ri yo'ldasiz.

Sizni har bir xodim qadrlanadigan va qo'llab-quvvatlanadigan jamoamizning bir qismi bo'lishga taklif qilamiz. Bu yerda siz – o'sish uchun imkoniyatlar, qiziqarli loyihalar va qulay ish muhitini topasiz. Sizning kuchingiz va g'oyalaringiz bizning jamoaviy sa'y-harakatlarimizga muhim qo'shimcha bo'lishi mumkin. Tanlov jarayonida muvaffaqiyatlar tilaymiz va rezyumeyingizni kutib qolamiz!

Hurmat bilan,
“HAMROH mikromoliya tashkiloti” jamoasi

||Agar siz arizangizni bekor qilmoqchi bo'lsangiz yoki to'ldirishda xatolik qilmoqchi bo'lsangiz, iltimos, /cancel tugmasini bosing.||
"""

ru_start_message = """
Приветствуем вас!

Мы рады, что вы ждете начала своего нового путешествия с нами! Наша организация ценит ваш интерес и стремление к развитию. Если вы готовы проявить свои навыки, внести содержательный вклад и работать в дружном профессиональном коллективе, то вы на правильном пути.

Мы предлагаем вам стать частью нашей команды, которая ценит и поддерживает каждого сотрудника. Здесь вы найдете возможности для роста, интересные проекты и комфортную рабочую обстановку. Ваша сила и цели могут стать важным дополнением к нашим коллективным усилиям. Желаем вам успехов в процессе выбора и с нетерпением ждем вашего резюме!

С уважением,
Команда "HAMROH микрофинансовой организации"

Если вы хотите отменить ваше заявление или исправить ошибки в заполнении, пожалуйста, нажмите /cancel.
"""

# Questions in Uzbek and Russian
uz_messages = {
    "NAME": "To‘liq ismingizni yozing (F.I.O):",
    "PHONE": "Telefon Raqamingiz?",
    "AGE": "Yoshingiz?",
    "MARITAL_STATUS": "Oilaviy holatingiz?",
    "EDUCATION": "Ma'lumotingiz? (Qaysi ta'lim muassasasini tamomlagansiz?)",
    "SPECIALIZATION": "Mutaxassisligingiz?",
    'POSITION': "Qaysi lavozimda ishlamoqchisiz?",  # New message for position
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
    'POSITION': "На какой должности вы хотите работать?",  # New message for position
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

uz_positions = [
    ["Операцион бош менежери", "Кассир", "IT"],
    ["Ички аудит", "Бош бухгалтер", "Юрист"],
    ["HR менежер", "Кредит маҳсулотларини сотиш бўлими"]
]

ru_positions = [
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

uz_success_message = """Tabriklaymiz. Sizning rezyumeingiz HAMROH mikromoliya tashkilotining tanlov jarayonlariga qabul qilindi.
Tez orada sizga aloqaga chiqamiz."""

uz_not_filled_message = "Ma'lumotingiz to'liq shaklda emas. Iltimos ma'lumotingizni to'liq kiritib qayta yuboring."

uz_ignore_message = "Afsus. Sizning rezyumeingiz HAMROH mikromoliya tashkilotiga tanlov jarayoniga  qabul qilinmadi. Bizga ruzyume yuborganingizdan mamnunmiz."

ru_success_message = """Поздравляем! Ваше резюме было принято для участия в конкурсных процессах микрофинансовой организации HAMROH.
Мы скоро свяжемся с вами."""

ru_not_filled_message = "Ваши данные не полностью заполнены. Пожалуйста, заполните данные полностью и отправьте заново."

ru_ignore_message = "К сожалению, ваше резюме не прошло отбор в микрофинансовую организацию HAMROH. Мы благодарны вам за то, что вы прислали нам своё резюме."
