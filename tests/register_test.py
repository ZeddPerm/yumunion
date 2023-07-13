import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#run server
#run client
class Test(unittest.TestCase):
    def setUp(self):
        self.options = Options()
        self.options.add_experimental_option("detach",True)
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=self.options)
        self.driver.get("http://localhost:5173/register")
    def test_register(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
        username="nato1of5@outlook.com"
        password="Au1.61803399"
        self.driver.find_element(By.ID,"email").send_keys(username)
        self.driver.find_element(By.ID,"password").send_keys(password)
        self.driver.find_element(By.ID,"terms-privacy-check").click()
        self.driver.find_element(By.ID,"register").click()
    def tearDown(self):
        self.driver.close()
if __name__=="__main__":
    unittest.main()
##check if register works
#exaustivly check it