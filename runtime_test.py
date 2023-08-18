from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (make sure chromedriver.exe is in the same directory)
# driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path='/usr/bin/google-chrome')

# Open the login page
driver.get("http://20.55.105.192/")

username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
username_field.send_keys("testuser")
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
password_field.send_keys("test@123")
# Find and input username and password
# username_field = driver.find_element_by_name("username")
# password_field = driver.find_element_by_name("password")
# username_field.send_keys("testuser")
# password_field.send_keys("test@123")

login_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Login"]')
login_button.click()

# Wait for the welcome message element to appear
welcome_message_element = driver.find_element(By.ID, "welcomeMessage")

# Get the text content of the welcome message
welcome_message_text = welcome_message_element.find_element(By.TAG_NAME, "h3").text

# Verify the welcome message
expected_welcome_message = "Welcome to the Test Server"
if welcome_message_text != expected_welcome_message:
    print(f"Test failed! Expected: '{expected_welcome_message}', Actual: '{welcome_message_text}'")
else:
    print("Test passed!")

# Close the browser
driver.quit()
