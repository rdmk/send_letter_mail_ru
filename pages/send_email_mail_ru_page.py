from selenium.webdriver.common.by import By

from .base_page import BasePage


class SendEmailPage(BasePage):
    def should_be_write_email_link(self):
        """Проверка на наличие кнопки Написать письмо."""
        assert self.is_element_present(
            By.XPATH,
            '//a[@title="Написать письмо"]'
        ), 'Write e-mail button is not presented'

    def go_to_write_email(self):
        """Переход в окно Написать письмо."""
        write_email_button = self.browser.find_element(
            By.XPATH,
            '//a[@title="Написать письмо"]'
        )
        write_email_button.click()
        return SendEmailPage(
            browser=self.browser, url=self.browser.current_url
        )

    def should_be_to_whom_field(self):
        """Проверка на наличие поля Получатель."""
        assert self.is_element_present(
            By.XPATH,
            '//input[@type="text"]'
        ), 'To whom field is not presented'

    def should_be_text_field(self):
        """Проверка на наличие поля Текст."""
        assert self.is_element_present(
            By.XPATH,
            '//div[@role="textbox"]'
        ), 'Text field is not presented'

    def should_be_send_button(self):
        """Проверка на наличие кнопки Отправить."""
        assert self.is_element_present(
            By.CLASS_NAME,
            'button2__wrapper'
        ), 'Button Send is not presented'

    def send_email(self, your_email):
        """Метод для отправки e-mail."""
        to_whom = self.browser.find_element(By.XPATH, '//input[@type="text"]')
        to_whom.send_keys(your_email)

        email = self.browser.find_element(By.XPATH, '//div[@role="textbox"]')
        email.send_keys('Hello world')

        send = self.browser.find_element(By.CLASS_NAME, 'button2__wrapper')
        send.click()

    def if_send_email(self):
        assert self.is_element_present(
            By.CLASS_NAME,
            'layer__links'
        ), 'Email did not send'
