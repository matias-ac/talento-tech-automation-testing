from selenium import webdriver


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
driver.quit()
