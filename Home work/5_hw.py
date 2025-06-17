from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def check_elements():
    # Инициализация драйвера
    driver = webdriver.Chrome()

    try:
        # Открытие страницы
        driver.get("https://www.saucedemo.com/")

        # Ожидание загрузки страницы
        wait = WebDriverWait(driver, 10)

        # Поиск элементов
        username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
        submit_button = wait.until(EC.presence_of_element_located((By.ID, "login-button")))

        # Проверка наличия всех элементов
        if username_field and password_field and submit_button:
            print("Элементы найдены")

    finally:
        # Закрытие браузера
        driver.quit()

# Вызов функции
check_elements()

