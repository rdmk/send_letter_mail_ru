from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainMailruPage(BasePage):
    def should_be_login_link(self):
        """"Метод для проверки кнопки для перехода в окно авторизации."""
        assert self.is_element_present(
            By.XPATH,
            '//button[@data-testid="enter-mail-primary"]'
        ), 'Login link is not presented'

    def go_to_login(self):
        """Переход в окно авторизации."""
        login_link = self.browser.find_element(
            By.XPATH,
            '//button[@data-testid="enter-mail-primary"]'
        )
        login_link.click()
        return MainMailruPage(
            browser=self.browser, url=self.browser.current_url
        )

    def should_has_frame(self):
        """Проверка на наличие фрейма."""
        assert self.is_element_present(
            By.CLASS_NAME,
            'ag-popup__frame__layout__iframe'
        ), 'This page has not frame'

    def go_to_frame(self):
        """Переход во фрейм."""
        self.browser.switch_to.frame(
            self.browser.find_element(
                By.CLASS_NAME, 'ag-popup__frame__layout__iframe'
            )
        )
        return MainMailruPage(
            browser=self.browser, url=self.browser.current_url
        )

    def should_be_login_field(self):
        """Проверка на наличие поля Логин или e-mail."""
        assert self.is_element_present(
            By.XPATH,
            '//input[@name="username"]'
        ), 'Login field is not presented'

    def should_be_button_after_filling_login_to_password(self):
        """Проверка на наличие кнопки Ввести пароль."""
        assert self.is_element_present(
            By.XPATH,
            '//button[@data-test-id="next-button"]'
        ), 'Button "Enter Password" is not presented'

    def go_to_password_field(self, your_email):
        """Метод для заполнения email и нажатия кнопки Ввести пароль."""
        email = self.browser.find_element(
            By.XPATH, '//input[@name="username"]'
        )
        email.send_keys(your_email)

        button = self.browser.find_element(
            By.XPATH, '//button[@data-test-id="next-button"]'
        )
        button.click()
        return MainMailruPage(
            browser=self.browser, url=self.browser.current_url
        )

    def should_be_password_field(self):
        """Проверка на наличие поля Пароль."""
        assert self.is_element_present(
            By.XPATH,
            '//input[@name="password"]'
        ), 'Password field is not presented'

    def should_be_button_after_fill_password(self):
        """Проверка на наличие кнопки Войти."""
        assert self.is_element_present(
            By.XPATH,
            '//button[@data-test-id="submit-button"]'
        ), 'Submit button is not presented'

    def fill_the_fields(self, your_password):
        """Метод для ввода пароля и нажатия кнопки Войти."""
        password = self.browser.find_element(
            By.XPATH, '//input[@name="password"]'
        )
        password.send_keys(your_password)

        button = self.browser.find_element(
            By.XPATH, '//button[@data-test-id="submit-button"]'
        )
        button.click()
