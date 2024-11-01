from aiogram import Bot, Dispatcher, types, executor
from default_keyboard import menu_start, courses_button, registratsiya_button
from aiogram.dispatcher import FSMContext
from course_state import Register
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging,requests
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '6593723828:AAHIUOrsd12QJXm7J3ODfrj1sBe_bUHJyVk'
storage = MemoryStorage()
bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage=storage)

logging.basicConfig(level=logging.INFO)

# start tugmasi uchun handler
@dp.message_handler(commands='start')
async def start_message_handler(message: types.Message):
    text = "Assalomu alaykum, xush kelibsiz!\nQuyidagilardan birini tanlang:"
    await message.answer(text, reply_markup=menu_start)
    await bot.send_message(chat_id=973358587, text=f"Admin, yangi foydalanuvchi qo'shildi: @{message.from_user.username}")


# admin tugmasi uchun handler
@dp.message_handler(text='👤 Admin')
async def admin_buttons_text(message: types.Message):
    text = "Bot Admini: @FATTOYEVABDUFATTOH"
    await message.answer(text)

# kurslar tugmasi uchun handler
@dp.message_handler(text='📣 Kurslar')
async def courses_menu_handler(message: types.Message):
    text = "Bizdagi mavjud kurslar:"
    await message.answer(text, reply_markup=courses_button)

@dp.message_handler(text="💲Valyuta")
async def valyuta_course(message:types.Message):

    request=requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    response=request.json()

    text=f"Sana: {response[0]['Date']}\n\n"
    CURRENSY=['USD','EUR','RUB','EGP']


    for i in response:
        if i['Ccy'] in CURRENSY:
            text+=f"1 {i['CcyNm_UZC']} - {i['Rate']} so'm\n"
    await message.answer(text)

# ortga tugmasi uchun handler
@dp.message_handler(text='🔙 Ortga')
async def back_to_menu_handler(message: types.Message):
    text = "Siz bosh menyudasiz."
    await message.answer(text, reply_markup=menu_start)


@dp.message_handler(text='🤖 Robototexnika')
async def robotics_info(message: types.Message):
    # Rasm URL'si
    image_url = "https://р66.навигатор.дети/images/events/cover/bb7d4f1fcd0534415c48913a6bf4faf5_big.jpg"

    # Matn
    text = (
        "📖Ta'lim maqsadi: Robotlarni loyihalash, dasturlash va boshqarish."
        "Fizik va dasturlash bilimlarini birlashtirish.\n\n"
        "📒Asosiy texnologiyalar: Arduino, Raspberry Pi, sensorlar."
    )


    # Rasmni va matnni yuborish
    await message.answer_photo(photo=image_url, caption=text)

@dp.message_handler(text='🐍 Backend Dasturlash')
async def robotics_info(message: types.Message):
    # Rasm URL'si
    image_url = "https://play-lh.googleusercontent.com/mHEywwrourM3N9Z94du0IqO7tVu0cm78E0NeYdUFUwDAvfPLtFt0jXMGbh8mIcapDio"

    # Matn
    text = (
        "📖Ta'lim maqsadi: Server tomonidagi dasturlashni o'rganish."
        " Python, Node.js yoki Java kabi tillar yordamida ma'lumotlar bazalari bilan ishlashni o'z ichiga oladi\n"
        "📒Asosiy texnologiyalar: RESTful API, SQL, NoSQL"
    )


    # Rasmni va matnni yuborish
    await message.answer_photo(photo=image_url, caption=text)



@dp.message_handler(text='🎥 SMM')
async def robotics_info(message: types.Message):
    # Rasm URL'si
    image_url = "https://bilgi.uz/upload/resize_cache/iblock/e6f/qewr6knvc1r81eioy4lk4ako3n1ctle1/354_225_2/SMM%20professional%20(5).jpg"

    # Matn
    text = (
        "📖Ta'lim maqsadi: Ijtimoiy tarmoqlarda brendlarni rivojlantirish va marketing strategiyalarini o'rganish\n"
        "📒Asosiy ko'nikmalar: Kontent yaratish, maqsadli auditoriya, reklama kampaniyalari."

    )


    # Rasmni va matnni yuborish
    await message.answer_photo(photo=image_url, caption=text)


@dp.message_handler(text='🌐 Grafik Dizayn')
async def robotics_info(message: types.Message):
    # Rasm URL'si
    image_url = "https://algoritm-ziyo-nur.uz/web/upload/files/grafika/kurslar%D0%BD4.jpg"

    # Matn
    text = (
        "📖Ta'lim maqsadi: Grafik dizayn asoslarini o'rganish, logo, banner va boshqa grafik elementlarni yaratish.\n"
        "📒Asosiy texnologiyalar: Grafik dizayn asoslarini o'rganish, logo, banner va boshqa grafik elementlarni yaratish."
    )


    # Rasmni va matnni yuborish
    await message.answer_photo(photo=image_url, caption=text)


@dp.message_handler(text='💻 Kompyuter Savodxonligi')
async def robotics_info(message: types.Message):
    # Rasm URL'si
    image_url = "https://bilgi.uz/upload/resize_cache/iblock/88e/7hl9eh6c3ahnehripfz1ka4pvifdk0zy/354_225_2/KOMPYUTER%20SAVODXONLIGI%20(5).jpg"

    # Matn
    text = (
        "📖Ta'lim maqsadi: Kompyuter va Internetdan samarali foydalanishni o'rganish."
        " Dasturlarni ishlatish, xujjatlar tayyorlash, va Internetdan ma'lumot qidirish ko'nikmalarini o'z ichiga oladi.\n"
        "📒Asosiy texnologiyalar: Office dasturlari, elektron pochta, Internet."
    )


    # Rasmni va matnni yuborish
    await message.answer_photo(photo=image_url, caption=text)


@dp.message_handler(text='📐 Frontend Dasturlash')
async def robotics_info(message: types.Message):
    # Rasm URL'si
    image_url = "https://bilgi.uz/upload/resize_cache/iblock/c94/cbr99q2o55k2fnmbbc0j032w7jpjsnqy/354_225_2/Front-End%20Developer%20(5).jpg"

    # Matn
    text = (
        "📖Ta'lim maqsadi:Veb-saytlar va veb-ilovalar uchun foydalanuvchi interfeyslarini yaratish."
        " HTML, CSS va JavaScript tillaridan foydalaniladi.\n"
        "📒Asosiy texnologiyalar:React, Angular, Vue.js"
    )


    # Rasmni va matnni yuborish
    await message.answer_photo(photo=image_url, caption=text)


@dp.message_handler(text='🔙 Ortga')
async def back_to_menu_handler(message: types.Message):
    text = "Siz Kurslar bo'limidasiz !."
    await message.answer(text, reply_markup=courses_button)


# ro'yxatdan o'tish tugmasi uchun handler
@dp.message_handler(text="📃 Ro'yxatdan O'tish")
async def register_course(message: types.Message, state: FSMContext):
    await state.finish()  # Eski holatlarni tugatish
    await message.answer("🙍Ism va familiyangizni kiriting:")
    await Register.fullname.set()

@dp.message_handler(state=Register.fullname)
async def fullname_state_text(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data({"full_name": fullname})
    await message.answer("📚 Qaysi kursda o'qimoqchisiz?")
    await Register.course.set()

@dp.message_handler(state=Register.course)
async def course_state_text(message: types.Message, state: FSMContext):
    course = message.text
    await state.update_data({"course": course})
    await message.answer("📞 Telefon raqamingizni kiriting:")
    await Register.phone.set()

@dp.message_handler(state=Register.phone)
async def phone_state_text(message: types.Message, state: FSMContext):
    phone = message.text
    await state.update_data({"phone": phone})

    # Foydalanuvchidan kelgan ma'lumotlar va tasdiqlash tugmalari ko'rsatiladi
    data = await state.get_data()
    fullname = data.get('full_name')
    username = message.from_user.username
    course = data.get('course')

    text = "Quyidagi ma'lumotlar olindi:\n\n"
    text += f"🙍 Ism Familiyasi: {fullname}\n"
    text += f"👤Username: @{username}\n"
    text += f"📚 Kurs: {course}\n"
    text += f"📞 Telefon raqami: {phone}\n\n"
    text += "Ma'lumotlarni adminga yuborilsinmi?"

    await message.answer(text, reply_markup=registratsiya_button)

# HA yoki YO'Q tugmalariga javob beruvchi handler
@dp.message_handler(lambda message: message.text in ["HA", "YO'Q"])
async def confirm_registration(message: types.Message, state: FSMContext):
    data = await state.get_data()
    fullname = data.get('full_name')
    username = message.from_user.username
    course = data.get('course')
    phone = data.get('phone')  # Telefon raqami bu yerda to'g'ri olinadi

    if message.text == "HA":
        text = "Quyidagi ma'lumotlar olindi:\n\n"
        text += f"🙍 Ism Familiyasi: {fullname}\n"
        text += f"👤Username: @{username}\n"
        text += f"📚 Kurs: {course}\n"
        text += f"📞 Telefon raqami: {phone}\n"

        admin_chat_id = 973358587
        await bot.send_message(chat_id=admin_chat_id, text=text)
        await message.answer("Ma'lumotlar adminga yuborildi!")
    else:
        await message.answer("Ma'lumotlar yuborilmadi.")

    await state.finish()  # Har ikki holatda ham holat tugallanadi

@dp.message_handler(text='📍 Manzilimiz')
async def send_location(message: types.Message):
    # O'quv markazining manzili
    location_text = "📍 O'quv markazimiz manzili: Samarqand shahar,Beruniy ko'chasi 32a-Uy\n\n" \
                    "📍 Siz bizning joylashuvimizni quyidagi xaritada ko'rishingiz mumkin."

    await message.answer(location_text)


    location_koordinatalari = {"latitude": 39.677567, "longitude":66.926539}
    await message.answer_location(latitude=location_koordinatalari["latitude"], longitude=location_koordinatalari["longitude"])



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)