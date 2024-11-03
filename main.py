from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Replace these with your LinkedIn credentials
LINKEDIN_EMAIL = 'example@email.com'  # Your LinkedIn email
LINKEDIN_PASSWORD = 'password'         # Your LinkedIn password

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def login():
    driver.get('https://www.linkedin.com/login')
    driver.implicitly_wait(10)  # Implicit wait for elements to load

    email_input = driver.find_element(By.ID, 'username')
    password_input = driver.find_element(By.ID, 'password')

    email_input.send_keys(LINKEDIN_EMAIL)
    password_input.send_keys(LINKEDIN_PASSWORD)
    password_input.send_keys(Keys.RETURN)

    driver.implicitly_wait(10)  # Wait for login to complete

def follow_user(profile_url):
    driver.get(profile_url)
    driver.implicitly_wait(10)  # Wait for the page to load

    try:
        # Try to find the 'Follow' button
        follow_button = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/button/span')
        follow_button.click()
        
        print(f"Followed user: {profile_url}")
    except Exception as e:
        print(f"Could not follow user: {profile_url}, Error: {e}")

if __name__ == "__main__":
    login()
    
    # List of LinkedIn profile URLs to follow (replace with actual IT-related profiles)
    users_to_follow = [
        'linkedin profile links'
        # Add more profiles as needed
    ]
    
    for user in users_to_follow:
        follow_user(user)
        time.sleep(2)  # Wait between follows to avoid detection

    driver.quit()
