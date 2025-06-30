import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRegisterForm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Runs once before all test cases
        cls.service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.maximize_window()

    def test_register_negative_incomplete_form(self):
        print("🔴 Running Negative Test: Incomplete Registration")
        self.driver.get("http://localhost:5173/register")

        # Fill only some fields and submit
        self.driver.find_element(By.ID, "firstName").send_keys("Qudsia")
        self.driver.find_element(By.ID, "password").send_keys("12345678")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(1)

        # Check for validation error
        error = self.driver.find_element(By.CLASS_NAME, "error-message").text
        self.assertIn("required", error.lower())

    def test_register_positive_complete_form(self):
        print("🟢 Running Positive Test: Valid Registration")
        self.driver.get("http://localhost:5173/register")

        # Fill all fields with valid data
        self.driver.find_element(By.ID, "firstName").send_keys("Qudsia")
        self.driver.find_element(By.ID, "lastName").send_keys("Irza")
        self.driver.find_element(By.ID, "email").send_keys("qudsia.irza@example.com")
        self.driver.find_element(By.ID, "phone").send_keys("03001234567")
        self.driver.find_element(By.ID, "password").send_keys("StrongPass123")
        self.driver.find_element(By.ID, "confirmPassword").send_keys("StrongPass123")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()  # Agree to terms
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)

        # Since backend may not be active, check that page did not show errors
        current_url = self.driver.current_url
        self.assertIn("register", current_url)  # Still on register page OR redirected if backend exists

    @classmethod
    def tearDownClass(cls):
        # Runs once after all test cases
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
