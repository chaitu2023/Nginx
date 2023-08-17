import requests

def main():
    base_url = "http://20.55.105.192/"  # Replace with your Azure VM's URL or IP address

    # Simulate a login attempt
    login_data = {
        "username": "your_username",
        "password": "your_password"
    }

    session = requests.Session()

    try:
        # Perform the login
        login_response = session.post(base_url + "login", data=login_data)
        login_response.raise_for_status()  # Raise an exception for HTTP errors

        # Check if login was successful
        if "Welcome" in login_response.text:
            print("Login successful!")
        else:
            print("Login failed!")

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
