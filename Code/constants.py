# Сделать статусбар красным для отображение ошибок примавторизации или регистрации
EXCEPTION_STATUSBAR = "background-color: #FF0000"

#Ошибки статусбара
ENTER_PASSWORD = 'Введите пароль'
ENTER_LOGIN = 'Введите логин'
ENTER_LOGIN_PASSWORD = 'Введите логин и пароль'
EXCEPTION_PASSWORD = 'Неверный пароль'
EXCEPTION_LOGIN = 'Нет пользователя с таким логином'
EMPTY_LINE = ''
LOGIN_EXIST = 'Пользователь с таким логином уже существует'

# Дизайны
FILE_ENTRE = '../Designs/start.ui'
FILE_REGISTRATION = '../Designs/registration.ui'
FILE_MENU = '../Designs/menu.ui'
FILE_CARDS = '../Designs/cards.ui'
FILE_WORDS = '../Designs/words.ui'
FILE_TEST = '../Designs/test.ui'
FILE_FAVOURITE_CARDS = '../Designs/favourites_cards.ui'
FILE_RESULTS = '../Designs/result.ui'

# Названия окон
ENTRE_TITLE = 'Вход'
REGISTRATION_TITLE = 'Регистрация'
MENU_TITLE = 'Меню'
CARDS_TITLE = 'Карточки'
WORDS_TITLE = 'Все слова'
FAVOURITES_TITLE = 'Избранное'
FAVOURITE_CARDS_TITLE = 'Заучивание избранных слов'
TEST_TITLE = 'Тест'
RESULTS_TITLE = 'Результаты теста'

# Cтиль кнопок в окнах "Карточки" и "Заучивание избранных слов"
BTN_RED = "background-color: rgba(255,38,0,41); border: 0.5; font-size: 30px; color: white"
BTN_GREY = "background-color: rgba(169,169,169,128); border: 0.5; font-size: 30px; color: white"

# Оповещение, что слова закончились в окнах "Карточки" и "Заучивание избраннных слов"
END = 'Слова закончились!'

# Установка 100% для ProgressBar
START_PROGRESSBAR = 100

# Изображегния логотипа
IMAGE = '../Not programming code/logo.png'
IMAGE_RESIZED = '../Not programming code/resized.logo.png'

# Шрифт для CheckBox в окнах "Все слова" и "Избранное"
FONT_CHECKBOX = 'font-size: 30px'

# Расстояние между колоннами слов в окнах "Все слова" и "Избранное"
SPACE_BETWEEN_COLUMNS = 260

# Количество всех слов из бд
ALL_WORDS_AMOUNT = 476

# Стиль кнопок с вариантами ответов в окне "Тест"
BTN_ORANGE = "background-color: rgba(255, 147, 0, 77); border: 50%; font-size: 30px; color: white"

# Message box
MSGBOX_TITLE = 'Инструкция'
INSTRUCTION = ('Отметьте слово галочкой, чтобы добавить его в "Избранные"\n'
                    'Или уберите галочку, чтобы удалить слово из "Избранных".\n'
                    'При выходе назад данные сохранятся.')
INSTRUCTION_FAVOURITES = 'Уберите галочку, чтобы убрать слово из избранных.\n При выходе назад данные сохранятся.'

# Стиль кнопки "Заучивание" в окне "Избранное"
BTN_CARDS_FAVOURITE_STYLE = 'background-color: rgba(255,38,0,41); border: 50%; font-size: 20px; color: white'
BTN_CARDS_FAVOURITE_TEXT = 'Заучивание'

# Лэйблы для окон "Тест", "Карточки", "Заучивание избранных слов"
LBL_WORD_CHOOSE_AMOUNT = 'Выберите количество вопросов'
INSTRUCTION_FAVOURITES_CARDS = 'При нажатии на кнопку "Усвоено" слово не будет удалено из избранных'
SHOW_BACK = 'Нажмите, чтобы увидеть обратную сторону'
SHOW_ANSWERE = 'Нажмите, чтобы посмотреть ответ'

# Файл со всеми словами (txt)
FILE_WITH_ALL_WORDS = '../Not programming code/words.txt'

# База данных
DATA_BASE = '../Not programming code/EGEstresses.db'

# Таблицы базы данных
USERS = 'Users'
LIST_OF_WORDS = 'list_of_words'
LOGIN = 'login'
WORD = 'word'
FAVOURITE_WORD = 'favourite_word'
ID = 'id'
FAVOURITES = 'Favourites'
