from selenium import webdriver

def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Use this if you're running headless
    driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)
    try:
        # Open the login page
        driver.get("http://20.55.105.192/")  # Replace with your VM's URL

        # Find the username and password fields, and login button
        username_field = driver.find_element_by_id("username")
        password_field = driver.find_element_by_id("password")
        login_button = driver.find_element_by_xpath("//input[@type='submit']")

        # Enter login credentials
        username_field.send_keys("testuser")
        password_field.send_keys("test@123")

        # Click the login button
        login_button.click()

        # Wait for the page to load
        driver.implicitly_wait(10)

        # Check if "Welcome" is present in the page source
        if "Welcome" in driver.page_source:
            print("Login successful!")
        else:
            print("Login failed!")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
