from selenium.webdriver.common.by import By


class Homepage:
    
    def __init__(self, driver):
        self.driver = driver
    
    def open(self):
        self.driver.get('https://demoblaze.com/')
        
    def click_galaxy_s6(self):
        galaxy_s6 = self.driver.find_element(By.XPATH, "//a[text()='Samsung galaxy s6']")
        galaxy_s6.click()
        
    def click_monitors(self):
        monitors_category = self.driver.find_element(By.XPATH, "//a[text()='Monitors']")
        monitors_category.click()
        
    def check_products_count(self, count):
        products = self.driver.find_elements(By.CSS_SELECTOR, ".card")
        assert len(products) == count