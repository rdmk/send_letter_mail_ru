import time

from pages.main_mail_ru_page import MainMailruPage
from pages.send_email_mail_ru_page import SendEmailPage


def test_send_email(browser):
    link = 'https://mail.ru/'
    mail_mail_ru_page = MainMailruPage(browser, link)
    mail_mail_ru_page.open()
    time.sleep(5)
    username = mail_mail_ru_page.go_to_login()
    time.sleep(5)
    username.go_to_frame()
    username = username.go_to_password_field(
        your_email='YOUR_EMAIL@MAIL.RU'
    )
    time.sleep(5)
    password = username
    password.fill_the_fields(
        your_password='CHANGE_ME_PLS'
    )
    time.sleep(10)

    send_email_page = SendEmailPage(browser, browser.current_url)
    send_email_page.should_be_write_email_link()

    write_email_form = send_email_page.go_to_write_email()
    write_email_form.should_be_to_whom_field()
    write_email_form.should_be_text_field()
    write_email_form.should_be_send_button()
    write_email_form.send_email(your_email='SOME_EMAIL@MAIL.RU')
    time.sleep(10)
    write_email_form.if_send_email()
