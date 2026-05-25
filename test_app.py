import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = f"file://{current_dir}/index.html"
    driver.get(file_path)

    yield driver
    driver.quit()


# Тест 1: Проверка заголовка вкладки
def test_page_title(driver):
    assert "Тестовая форма" in driver.title


# Тест 2: Проверка видимого заголовка на странице
def test_header_text(driver):
    header = driver.find_element(By.ID, "header").text
    assert header == "Форма связи"


# Тест 3: Проверка успешной отправки формы
def test_form_submission(driver):
    driver.find_element(By.ID, "name").send_keys("Иван")
    driver.find_element(By.ID, "email").send_keys("ivan@example.com")
    driver.find_element(By.ID, "submit-btn").click()

    # Проверяем появление сообщения об успехе
    message = driver.find_element(By.ID, "message").text
    assert message == "Успешно отправлено!"


# Тест 4: Проверка наличия полей ввода
def test_inputs_presence(driver):
    assert driver.find_element(By.ID, "name").is_displayed()
    assert driver.find_element(By.ID, "email").is_displayed()