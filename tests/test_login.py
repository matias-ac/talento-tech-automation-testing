import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.helpers import login

URL = "https://www.saucedemo.com"
TEST_CREDENTIALS = {
    "valid": {"username": "standard_user", "password": "secret_sauce"},
    "invalid": {"username": "usuario_incorrecto", "password": "password_incorrecta"},
}


@pytest.fixture
def driver():
    # Iniciar el navegador
    driver = webdriver.Chrome()

    # Pasa el driver a cada test
    yield driver

    # Cierra el driver después de la ejecución de cada test
    driver.quit()


def test_login_exitoso_y_redirecciona_a_inventario(driver):
    # Configura espera explícita en máximo 5 segundos
    wait = WebDriverWait(driver, 5)

    # Abrir página
    driver.get(URL)

    login(
        driver,
        TEST_CREDENTIALS["valid"]["username"],
        TEST_CREDENTIALS["valid"]["password"],
    )

    # Espera a que el contenedor del inventario sea visible
    wait.until(EC.visibility_of_element_located((By.ID, "inventory_container")))

    # Valida que estamos en la ruta de redirección luego del login exitoso
    assert "/inventory.html" in driver.current_url

    # Valida que el elemento con título "Products" está visible
    assert (
        driver.find_element(By.CSS_SELECTOR, "[data-test='title']").text == "Products"
    )


def test_login_fallido_muestra_error_de_credenciales(driver):
    # Configura espera explícita en máximo 5 segundos
    wait = WebDriverWait(driver, 5)

    # Navegar a la URL de SauceDemo
    driver.get(URL)

    login(
        driver,
        TEST_CREDENTIALS["invalid"]["username"],
        TEST_CREDENTIALS["invalid"]["password"],
    )

    # Espera a que el contenedor del error sea visible
    error_container = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )

    # Valida que el contenedor del error tenga el texto indicando las credenciales inválidas
    invalid_credentials_error_message = (
        "Epic sadface: Username and password do not match any user in this service"
    )
    assert invalid_credentials_error_message in error_container.text
