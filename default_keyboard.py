from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


menu_start=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📣 Kurslar'),
            KeyboardButton(text='📍 Manzilimiz'),
        ],
        [
            KeyboardButton(text='👤 Admin'),
            KeyboardButton(text='📞 Telefon Raqam Yuborish',request_contact=True),
        ],
        [
            KeyboardButton(text='💲Valyuta'),
        ]
    ],
    resize_keyboard=True
)


courses_button=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🐍 Backend Dasturlash'),
            KeyboardButton(text='📐 Frontend Dasturlash'),
            KeyboardButton(text='🖥 Kompyuter Savodxonligi')
        ],

        [
            KeyboardButton(text='🌐 Grafik Dizayn'),
            KeyboardButton(text='🎥 SMM'),
            KeyboardButton(text='🤖 Robototexnika')
        ],

        [
            KeyboardButton(text="📃 Ro'yxatdan O'tish"),
            KeyboardButton(text='🔙 Ortga'),
        ],

    ],
    resize_keyboard=True

)

registratsiya_button=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='HA'),
            KeyboardButton(text="YO'Q"),
        ],
        [
            KeyboardButton(text="🔙 Ortga")
        ]

    ],
    resize_keyboard=True

)