from pages.homepage import Homepage
from pages.product import ProductPage
import time


def test_open_s6(driver):   
    homepage = Homepage(driver)
    product_page = ProductPage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page.check_title('Samsung galaxy s6')
   
def test_monitors_category(driver):
    homepage = Homepage(driver)
    homepage.open()
    homepage.click_monitors()
    time.sleep(3)  #Никогда так не делать :-D
    homepage.check_products_count(2)