# Telegram Inline Keyboard Builder Bot

Бот для создания инлайн-клавиатуры из URL-значений в Telegram. Позволяет преобразовать текстовые пары "текст - ссылка" в интерактивные кнопки.
# Особенности

  Поддержка текстовых сообщений, фото и видео\
  Простой формат ввода URL-пар\
  Автоматическое создание инлайн-кнопок\
  Асинхронная обработка запросов\
  Безопасное хранение токена бота через .env файл

# Технические требования

  Python 3.8+\
  aiogram 3.19\
  python-dotenv

# Установка

    git clone git@github.com:CheStorrr/callback_builder_bot.git && cd callback_builder_bot
    python -m venv venv
    source venv/bin/activate  # для Windows: venv\Scripts\activate

    pip install aiogram python-dotenv

# Настройка
  Создайте .env файл в дериктории и запишите туда следующие значения:
    
    BOT_TOKEN=ваш_токен_от_BotFather

# Запуск бота 

  Чтобы запустить бота, используйте команду

    python -m src.bot

# Использование
 Данный бот запущен в телеграме под юзернеймом @callback_builder_bot. Вы можете использовать его. Ccылка: [Ссылка на телеграм бота](https://t.me/callback_builder_bot) 
