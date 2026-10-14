import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://www.saucedemo.com"
TEST_CREDENTIALS = {
    "valid": {"username": "standard_user", "password": "secret_sauce"},
    "invalid": {"username": "usuario_incorrecto", "password": "password_incorrecta"},
}


@pytest.fixture
def driver():
    # Iniciar el navegador
    driver = webdriver.Chrome()

    yield driver

    driver.quit()


def test_login_exitoso_y_redirecciona_a_inventario(driver):
    # Iniciar el navegador
    # driver = webdriver.Chrome()

    # try:
    # Configura espera explícita en máximo 2 segundos
    wait = WebDriverWait(driver, 2)

    # Abrir página
    driver.get(URL)

    # Localizar elementos
    user_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Ingresar credenciales
    user_input.send_keys(TEST_CREDENTIALS["valid"]["username"])
    password_input.send_keys(TEST_CREDENTIALS["valid"]["password"])

    # Click en botón login
    login_button.click()

    # Espera a que el contenedor del inventario sea visible
    wait.until(EC.visibility_of_element_located((By.ID, "inventory_container")))

    # Valida que estamos en la ruta de redirección luego del login exitoso
    assert "/inventory.html" in driver.current_url

    # Valida que el elemento con título "Products" está visible
    assert (
        driver.find_element(By.CSS_SELECTOR, "[data-test='title']").text == "Products"
    )
    # finally:
    # driver.quit()


def test_login_fallido_muestra_error_de_credenciales(driver):
    # Iniciar el navegador
    # driver = webdriver.Chrome()

    # try:
    # Configura espera explícita en máximo 5 segundos
    wait = WebDriverWait(driver, 5)

    # Navegar a la URL de SauceDemo
    driver.get(URL)

    # Localizar elementos
    user_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Ingresar credenciales
    user_input.send_keys(TEST_CREDENTIALS["invalid"]["username"])
    password_input.send_keys(TEST_CREDENTIALS["invalid"]["password"])

    # Click en botón login
    login_button.click()

    # Espera a que el contenedor del error sea visible
    error_container = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )

    # Valida que el contenedor del error tenga el texto indicando las credenciales inválidas
    invalid_credentials_error_message = (
        "Epic sadface: Username and password do not match any user in this service"
    )
    assert invalid_credentials_error_message in error_container.text
    # finally:
    # driver.quit()
