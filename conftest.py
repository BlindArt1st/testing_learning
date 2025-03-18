from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(3) #Устанавливается "задержка" чтобы дать странице прогрузиться
    yield browser
    browser.close()