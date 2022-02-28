import time

from pages.main_mail_ru_page import MainMailruPage


def test_can_open_main_mail_ru_page_and_login(browser):
    link = 'https://mail.ru/'
    mail_mail_ru_page = MainMailruPage(browser, link)
    mail_mail_ru_page.open()

    mail_mail_ru_page.should_be_login_link()
    time.sleep(5)

    username = mail_mail_ru_page.go_to_login()
    time.sleep(5)
    username.should_has_frame()

    username.go_to_frame()
    username.should_be_login_field()
    username.should_be_button_after_filling_login_to_password()
    username = username.go_to_password_field(
        your_email='YOUR_EMAIL@MAIL.RU'
    )
    time.sleep(5)
    password = username
    password.should_be_password_field()
    password.should_be_button_after_fill_password()
    password.fill_the_fields(
        your_password='CHANGE_ME_PLS'
    )
    time.sleep(10)
