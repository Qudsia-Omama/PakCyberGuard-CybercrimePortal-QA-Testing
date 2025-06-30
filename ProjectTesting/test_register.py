import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# === NEGATIVE TEST CASE ===
print("🔴 Negative Test: Incomplete Registration")
driver.get("http://localhost:5173/register")

# Missing required fields
driver.find_element(By.ID, "firstName").send_keys("Qudsia")
driver.find_element(By.ID, "password").send_keys("123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(1)

try:
    error = driver.find_element(By.CLASS_NAME, "error-message").text
    print("Error Message Displayed:", error)
except:
    print("No error message found.")

# === POSITIVE TEST CASE ===
print("\n🟢 Positive Test: Valid Registration Inputs")
driver.get("http://localhost:5173/register")


driver.find_element(By.ID, "firstName").send_keys("Qudsia")
driver.find_element(By.ID, "lastName").send_keys("Irza")
driver.find_element(By.ID, "email").send_keys("qudsia.irza@example.com")
driver.find_element(By.ID, "phone").send_keys("03001234567")
driver.find_element(By.ID, "password").send_keys("StrongPass123")
driver.find_element(By.ID, "confirmPassword").send_keys("StrongPass123")
driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()  # Terms checkbox
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)

print("Submitted valid registration (assuming backend is not running, no success message expected).")

driver.quit()
