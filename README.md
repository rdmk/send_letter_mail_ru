# Тестовое задание

## Отправка письма c сайта mail.ru с помощью Selenium и Python

В данном тестовом задании я реализовал:
1) переход на стартовую страницу mail.ru;
2) авторизация;
3) отправка письма и проверка, что письмо было отправлено.

## Как запустить задание:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/rdmk/send_letter_mail_ru.git
```

```
cd send_letter_mail_ru
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/Scripts/activate
```

или

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Желательно установить chromedriver по следующему пути:

```
C:/chromedriver/chromedriver.exe
```

В файлах с тестами нужно указать логин и пароль от почтового ящика.
