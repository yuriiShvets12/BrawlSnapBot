async def command_brawl_stars(user_lang):
    uk = {
        1: "Виберіть дію:",
        2: "Схоже, ви вказали неправильний ID Brawl Stars.",
        3: "Напишіть свій ID Brawl Stars ще раз (без #):",
        4: "Виберіть ID Brawl Stars з доступних вам:",
        5: "Напиши свій Brawl Stars ID! Дотримання регістру і # на початку - необов'язкові.",
        6: "Схоже, ви неправильно відправили свій ID Brawl Stars😥\nСпробуйте ще раз.",
        7: "Напишіть свій новий ID Brawl Stars (без #):",
        8: "Не вдалося розпізнати ім'я через неправильний ID",
        9: "Ваш ID Brawl Stars успішно змінено😁👍"
    }

    ru = {
        1: "Выбери действие:",
        2: "Похоже вы указали не правильный Brawl Stars ID.",
        3: "Напиши еще раз свой Brawl Stars ID(без #):",
        4: "Выберите Brawl Stars ID из доступных вам:",
        5: "Напиши свой Brawl Stars ID! Соблюдение регистра и # в начале - необязательны.",
        6: "Похоже вы отправили свой Brawl Stars ID не правильно😥\nПопробуйте еще раз.",
        7: "Напиши свой новый Brawl Stars ID(без #):",
        8: "Не удалось спарсить имя из-за неправильного ID",
        9: "Твой Brawl Stars ID успешно изменён😁👍"
    }

    en = {
        1: "Choose an action:",
        2: "It seems you have entered an incorrect Brawl Stars ID.",
        3: "Write your Brawl Stars ID again (without #):",
        4: "Choose a Brawl Stars ID from those available to you:",
        5: "Write your Brawl Stars ID! Case sensitivity and # at the beginning are optional.",
        6: "It seems you have sent your Brawl Stars ID incorrectly😥\nTry again.",
        7: "Write your new Brawl Stars ID (without #):",
        8: "Failed to parse the name due to incorrect ID",
        9: "Your Brawl Stars ID has been successfully changed😁👍"
    }

    pl = {
        1: "Wybierz działanie:",
        2: "Wygląda na to, że podałeś nieprawidłowy ID Brawl Stars.",
        3: "Wpisz ponownie swój ID Brawl Stars (bez #):",
        4: "Wybierz ID Brawl Stars spośród dostępnych dla ciebie:",
        5: "Napisz swój Brawl Stars ID! Wielkość liter i # na początku są opcjonalne.",
        6: "Wygląda na to, że wysłałeś swoje ID Brawl Stars niepoprawnie😥\nSpróbuj ponownie.",
        7: "Wpisz swoje nowe ID Brawl Stars (bez #):",
        8: "Nie udało się przeanalizować nazwy z powodu nieprawidłowego ID",
        9: "Twoje ID Brawl Stars zostało pomyślnie zmienione😁👍"
    }
    if user_lang == "uk":
        return uk
    elif user_lang == "ru":
        return ru
    elif user_lang == "en":
        return en
    elif user_lang == "pl":
        return pl

async def command_donate(user_lang):
    uk = {
        1: "Дякуємо за пожертву!",
        2: "Виберіть валюту,\nу якій хочете надіслати пожертву",
        3: "Напишіть суму, яку б хотіли пожертвувати:",
        4: "Дякуємо за пожертву!",
        5: "Пожертвування",
        6: "Схоже, ви відправили не суму😥\nПопробуйте ще раз.",
        7: "Дякуємо за ваше пожертвование!"
    }
    ru = {
        1: "Спасибо за пожертвование!",
        2: "Выберете валюту,\nв которой хотите отправить пожертвование",
        3: "Напиши сумму которую хотел бы пожертвовать:",
        4: "Спасибо за пожертвование!",
        5: "Пожертвование",
        6: "Похоже вы отправили не сумму😥\nПопробуйте еще раз.",
        7: "Спасибо за ваше пожертвование!"
    }
    en = {
        1: "Thank you for your donation!",
        2: "Choose the currency in which you'd like to send your donation",
        3: "Write the amount you'd like to donate:",
        4: "Thank you for your donation!",
        5: "Donation",
        6: "It seems you sent an invalid amount 😥\nPlease try again.",
        7: "Thank you for your donation!"
    }
    pl = {
        1: "Dziękujemy za datek!",
        2: "Wybierz walutę,\nw jakiej chciałbyś przekazać datek",
        3: "Napisz kwotę, którą chciałbyś przekazać:",
        4: "Dziękujemy za datek!",
        5: "Datek",
        6: "Wygląda na to, że wysłałeś nie kwotę😥\nSpróbuj ponownie.",
        7: "Dziękujemy za Twój datek!"
    }

    if user_lang == "uk":
        return uk
    elif user_lang == "ru":
        return ru
    elif user_lang == "en":
        return en
    elif user_lang == "pl":
        return pl

async def battons_communication(user_lang):
    uk = {
        1: "Фото профілю",
        2: "Змінити Brawl Stars id",
    }
    ru = {
        1: "Фото профиля",
        2: "Изменить Brawl Stars id",
    }
    en = {
        1: "Profile photo",
        2: "Change Brawl Stars id",
    }
    pl = {
        1: "Zdjęcie profilowe",
        2: "Zmień Brawl Stars id",
    }

    if user_lang == "uk":
        return uk
    elif user_lang == "ru":
        return ru
    elif user_lang == "en":
        return en
    elif user_lang == "pl":
        return pl

async def command_start(user_lang):
    uk = {
        1: "🚀 Привіт! 🖐️\n\nЛаскаво просимо до BrawlSnapBot!\n\nЯкщо у вас є які-небудь питання,\nпроблеми з ботом,\nпропозиції з рекламою тощо,\n\nне соромтеся звертатися до @bak6767. 📨\n\nГарного проведення часу! 🎉"
    }
    ru = {
        1: "🚀 Привет! 🖐️\n\nДобро пожаловать в BrawlSnapBot!\n\nЕсли у вас есть какие-либо вопросы,\nпроблемы с ботом,\nпредложения по рекламе и т. д.,\n\nне стесняйтесь обращаться к @bak6767. 📨\n\nПриятного времяпровождения! 🎉"
    }
    en = {
        1: "🚀 Hello! 🖐️\n\nWelcome to BrawlSnapBot!\n\nIf you have any questions,\nissues with the bot,\nadvertising suggestions, etc.,\n\nfeel free to contact @bak6767. 📨\n\nHave a great time! 🎉"
    }
    pl = {
        1: "🚀 Cześć! 🖐️\n\nWitaj w BrawlSnapBot!\n\nJeśli masz jakiekolwiek pytania,\nproblemy z botem,\npropozycje reklamowe itp.,\n\nnie krępuj się kontaktować z @bak6767. 📨\n\nMiłego spędzania czasu! 🎉"
    }
    if user_lang == "uk":
        return uk
    elif user_lang == "ru":
        return ru
    elif user_lang == "en":
        return en
    elif user_lang == "pl":
        return pl
    
async def command_help(user_lang):
    uk = {
        1: "Привіт! Я чув, що тобі потрібна допомога.\nЯкщо у тебе виникли проблеми з командами, то всі доступні команди ти можеш знайти в лівому нижньому куті.\n\nАле якщо у тебе є якісь питання щодо бота, тоді сміливо пиши @bak6767"
    }
    ru = {
        1: "Привет! Я слышал, что тебе нужна помощь.\nЕсли у тебя возникли проблемы с командами, то все доступные команды ты можешь найти в левом нижнем углу.\n\nНо если у тебя есть какие-то вопросы касательно бота, тогда смело пиши @bak6767"
    }
    en = {
        1: "Hello! I heard that you need help.\nIf you have problems with commands, you can find all available commands in the lower left corner.\n\nBut if you have any questions about the bot, then feel free to write @bak6767"
    }
    pl = {
        1: "Cześć! Słyszałem, że potrzebujesz pomocy.\nJeśli masz problemy z poleceniami, wszystkie dostępne polecenia możesz znaleźć w lewym dolnym rogu.\n\nAle jeśli masz jakiekolwiek pytania dotyczące bota, śmiało pisz do @bak6767"
    }
    if user_lang == "uk":
        return uk
    elif user_lang == "ru":
        return ru
    elif user_lang == "en":
        return en
    elif user_lang == "pl":
        return pl

async def handler_all_text(user_lang):
    uk = {
        1: "Я тебе не розумію, вибач😥!",
        2: "Привіт бро🖐!",
    }
    ru = {
        1: "Я тебя не понимаю сори😥!",
        2: "Привет бро🖐!",
    }
    en = {
        1: "I don't understand you, sorry😥!",
        2: "Hello bro🖐!",
    }
    pl = {
        1: "Nie rozumiem cię, przepraszam😥!",
        2: "Cześć bracie🖐!",
    }
    if user_lang == "uk":
        return uk
    elif user_lang == "ru":
        return ru
    elif user_lang == "en":
        return en
    elif user_lang == "pl":
        return pl
