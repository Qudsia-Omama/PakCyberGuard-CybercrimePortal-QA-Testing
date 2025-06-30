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
print("🔴 Negative Test: Empty Login Form")
driver.get("http://localhost:5173/login")


# Leave fields empty and click login
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(1)

try:
    error = driver.find_element(By.CLASS_NAME, "error-message").text
    print("Error Message Displayed:", error)
except:
    print("No error message found.")

# === POSITIVE TEST CASE ===
print("\n🟢 Positive Test: Valid Login Inputs")
driver.get("http://localhost:5173/login")

driver.find_element(By.ID, "email").send_keys("qudsia.irza@gmail.com")
driver.find_element(By.ID, "password").send_keys("12345678")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)

print("Submitted valid credentials .")

driver.quit()


