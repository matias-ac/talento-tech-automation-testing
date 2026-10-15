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
    products_container_title = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='title']"))
    )

    # - verificar que el título del catálogo sea "Products"
    assert products_container_title.text == "Products"


def test_catalogo_contiene_productos_visibles(driver):
    # Configura espera explícita en máximo 5 segundos
    wait = WebDriverWait(driver, 5)

    # Abrir página
    driver.get(URL)

    login(
        driver,
        TEST_CREDENTIALS["valid"]["username"],
        TEST_CREDENTIALS["valid"]["password"],
    )

    # - obtener la lista de elementos de todos los productos visibles usando el selector de clase `.inventory_item`
    products_container = wait.until(
        EC.visibility_of_element_located((By.ID, "inventory_container"))
    )
    products = products_container.find_elements(By.CLASS_NAME, "inventory_item")

    # - verificar que la cantidad de productos obtenidos sea mayor a cero
    assert len(products) > 0

    # - capturar el primer producto de la lista (índice 0)
    first_product = products[0]

    # - obtener el elemento contenedor del nombre del primer producto (`data-test="inventory-item-name"`)
    first_product_name = first_product.find_element(
        By.CSS_SELECTOR, "[data-test='inventory-item-name']"
    )

    # - verificar que el nombre del primer producto obtenido es "Sauce Labs Backpack"
    assert first_product_name.text == "Sauce Labs Backpack"

    # - obtener el elemento contenedor del precio del primer producto (`data-test="inventory-item-price"`)
    first_product_price = first_product.find_element(
        By.CSS_SELECTOR, "[data-test='inventory-item-price']"
    )

    # - verificar que el precio del primer producto obtenido es "$29.99"
    assert "$29.99" in first_product_price.text


def test_catalogo_contiene_elemento_menu_hamburguesa(driver):
    # Configura espera explícita en máximo 5 segundos
    wait = WebDriverWait(driver, 5)

    # Abrir página
    driver.get(URL)

    login(
        driver,
        TEST_CREDENTIALS["valid"]["username"],
        TEST_CREDENTIALS["valid"]["password"],
    )

    # - obtener el elemento botón del menú hamburguesa (ID: `react-burger-menu-btn`)
    burger_menu_element = wait.until(
        EC.visibility_of_element_located((By.ID, "react-burger-menu-btn"))
    )

    # - verificar que el botón del menú hamburguesa esté visible
    assert burger_menu_element.is_displayed()


def test_catalogo_contiene_elemento_filtro(driver):
    # Configura espera explícita en máximo 5 segundos
    wait = WebDriverWait(driver, 5)

    # Abrir página
    driver.get(URL)

    login(
        driver,
        TEST_CREDENTIALS["valid"]["username"],
        TEST_CREDENTIALS["valid"]["password"],
    )

    # - obtener el elemento de filtro de productos (`data-test="product-sort-container"`)
    filter_element = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='product-sort-container']")
        )
    )

    # - verificar que el elemento de filtro esté visible
    assert filter_element.is_displayed()

    # - obtener el elemento del carrito de compras (`data-test="shopping-cart-link"`)
    # - verificar que el elemento del carrito de comrpas esté visible
