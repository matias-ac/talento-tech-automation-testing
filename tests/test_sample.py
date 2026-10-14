from selenium import webdriver


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4


def test_saucedemo_title():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com")
        assert "Swag Labs" in driver.title
    finally:
        driver.quit()
