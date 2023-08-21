from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    # Set up the Selenium WebDriver with options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Use this if you're running headless
    options.binary_location = '/usr/bin/google-chrome'  # Actual path to Chrome binary
    driver = webdriver.Chrome(options=options)
    try:
        # Open the login page
        driver.get("http://20.55.105.192/")

        username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
        username_field.send_keys("testuser")
        password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password_field.send_keys("test@123")
        
        # Find and click the login button
        login_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Login"]')
        login_button.click()

        # Wait for the welcome message element to appear
        welcome_message_element = driver.find_element(By.ID, "welcomeMessage")

        # Get the text content of the welcome message
        welcome_message_text = welcome_message_element.find_element(By.TAG_NAME, "h3").text

        # Verify the welcome message
        expected_welcome_message = "Welcome to the Test Server & Sample"
        if welcome_message_text != expected_welcome_message:
            print(f"Test failed! Expected: '{expected_welcome_message}', Actual: '{welcome_message_text}'")
        else:
            print("Test passed!")
    
    except Exception as e:
        print("An error occurred:", str(e))
    
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
