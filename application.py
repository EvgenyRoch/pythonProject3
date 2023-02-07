
from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def Logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def Check_created_group(self):
        self.Check_created_group()
        self.driver.find_element(By.LINK_TEXT, "group page").click()

    def Create_Group(self, group):
        self.Open_groups_page()
        self.driver.find_element(By.NAME, "new").click()
        self.driver.find_element(By.NAME, "group_name").click()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.NAME, "group_header").click()
        self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.driver.find_element(By.NAME, "group_footer").click()
        self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        self.driver.find_element(By.NAME, "submit").click()

    def Open_groups_page(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def Login(self, Username, Password):
        self.Open_homepage()
        self.driver.find_element(By.NAME, "user").send_keys(Username)
        self.driver.find_element(By.NAME, "pass").send_keys(Password)

    def Open_homepage(self):
        self.driver.get("http://localhost/addressbook/group.php")

    def destroy(self):
        self.driver.quit()
