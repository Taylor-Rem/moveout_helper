from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class WebDriverOperations:
    _instance = None
    driver = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if self.__initialized:
            return
        self.driver = self.setup_webdriver()
        self.wait = WebDriverWait(self.driver, 10)
        self.__initialized = True
        self.primary_tab = None

    def setup_webdriver(self):
        service = Service()
        options = webdriver.ChromeOptions()
        return webdriver.Chrome(service=service, options=options)

    def login(self, username, password):
        try:
            username_input = self.driver.find_element(By.NAME, "username")
            password_input = self.driver.find_element(By.NAME, "password")
            username_input.send_keys(username)
            password_input.send_keys(password)
            password_input.send_keys(Keys.ENTER)
        except NoSuchElementException:
            pass

    def open_property(self, property):
        change_property_link = self.driver.find_element(
            By.XPATH, "//a[contains(., 'CHANGE PROPERTY')]"
        )
        change_property_link.click()
        property_link = self.driver.find_element(
            By.XPATH, f"//a[contains(., '{property}')]"
        )
        property_link.click()

    def open_unit(self, unit):
        search_input = self.driver.find_element(By.NAME, "search_input")
        search_input.clear()
        search_input.send_keys(unit)
        search_input.send_keys(Keys.ENTER)

    def open_ledger(self):
        ledger_xpath = "/html/body/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table[3]/tbody/tr[2]/td/table/tbody/tr[last()]/td[4]/a[4]"
        ledger_link = self.driver.find_element(By.XPATH, ledger_xpath)
        ledger_link.click()

    def compare_resident(self, resident):
        try:
            RM_resident_element = self.driver.find_element(
                By.XPATH,
                "/html/body/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table[3]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/a",
            )
            RM_resident = RM_resident_element.get_attribute("innerHTML").strip()
            if resident in RM_resident:
                return True
            return False
        except NoSuchElementException:
            return False

    def search_former(self, resident):
        former_resident = self.driver.find_element(
            By.XPATH,
            "/html/body/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table[3]/tbody/tr[1]/td/table/tbody/tr/td[3]/input[2]",
        )
        former_resident.click()
        spacenum = self.driver.find_element(By.NAME, "ressearch")
        spacenum.clear()
        spacenum.send_keys(resident)
        spacenum.send_keys(Keys.ENTER)
