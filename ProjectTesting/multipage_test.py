import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# === Test 1: Incomplete Registration ===
print("\n🔴 Test 1: Incomplete Registration Form")
driver.get("http://localhost:5173/register")
driver.find_element(By.ID, "firstName").send_keys("Qudsia")
driver.find_element(By.ID, "password").send_keys("123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(1)

try:
    error = driver.find_element(By.CLASS_NAME, "error-message").text
    print("Error Message Displayed:", error)
except NoSuchElementException:
    print("❌ No error message found on invalid registration")

# === Test 2: Complete Valid Registration ===
print("\n🟢 Test 2: Valid Registration Form")
driver.get("http://localhost:5173/register")
driver.find_element(By.ID, "firstName").send_keys("Qudsia")
driver.find_element(By.ID, "lastName").send_keys("Irza")
driver.find_element(By.ID, "email").send_keys("qudsia.irza@gmail.com")
driver.find_element(By.ID, "phone").send_keys("03001234567")
driver.find_element(By.ID, "password").send_keys("12345678")
driver.find_element(By.ID, "confirmPassword").send_keys("12345678")
driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)

print("✅ Registration submitted — expect redirect to login")

# === Test 3: Register → Login Navigation (handle alert) ===
print("\n🔁 Test 3: Navigate from Register to Login Page")
driver.get("http://localhost:5173/register")

# Handle alert if present
try:
    alert = driver.switch_to.alert
    print("⚠️ Unexpected Alert Detected:", alert.text)
    alert.dismiss()  # or alert.accept()
    time.sleep(1)
except:
    pass  # No alert, continue

# === Test 4: Empty Login ===
print("\n🔴 Test 4: Empty Login Form")
driver.get("http://localhost:5173/login")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(1)

# === Test 5: Valid Login ===
print("\n🟢 Test 5: Valid Login")
driver.get("http://localhost:5173/login")
driver.find_element(By.ID, "email").send_keys("qudsia.irza@gmail.com")
driver.find_element(By.ID, "password").send_keys("12345678")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)

if "report" in driver.current_url.lower():
    print("✅ Successfully logged in and redirected to /report")
else:
    print("❌ Login failed or not redirected to report page")

# === Test 6: Login → Register Navigation ===
print("\n🔁 Test 6: Navigate from Login to Register Page")
driver.get("http://localhost:5173/login")


# === Done ===
print("\n✅ All tests completed.")
driver.quit()
