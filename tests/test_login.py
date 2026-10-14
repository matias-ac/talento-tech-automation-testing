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


def test_login_exitoso_y_redirecciona_a_inventario():
    # Iniciar el navegador
    driver = webdriver.Chrome()

    try:
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
            driver.find_element(By.CSS_SELECTOR, "[data-test='title']").text
            == "Products"
        )
    finally:
        driver.quit()
