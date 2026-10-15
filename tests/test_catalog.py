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


def test_catalogo_contiene_titulo_correcto(driver):
    # Configura espera explícita en máximo 5 segundos
    wait = WebDriverWait(driver, 5)

    # Abrir página
    driver.get(URL)

    login(
        driver,
        TEST_CREDENTIALS["valid"]["username"],
        TEST_CREDENTIALS["valid"]["password"],
    )

    # - obtener el elemento contenedor del título del header (`.app_logo`)
    header_title_element = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "app_logo"))
    )

    # - verificar que el texto del título del header sea "Swag Labs"
    assert header_title_element.text == "Swag Labs"

    # - obtener el elemento contenedor de productos (`data-test="title"`)
    # - verificar que el título del catálogo sea "Products"
