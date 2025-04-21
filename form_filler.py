from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time

def load_data():
    with open('user_data.json') as f:
        user_data = json.load(f)
    with open('selectors.json') as f:
        selectors = json.load(f)
    return user_data, selectors

def fill_form(driver, user_data, selectors):
    for key in user_data:
        if key in selectors:
            element = driver.find_element(By.XPATH, selectors[key])
            element.clear()
            element.send_keys(user_data[key])
            time.sleep(0.5) 

def main():
    user_data, selectors = load_data()
    
    # Setup browser
    driver = webdriver.Chrome()
    driver.get("https://example.com/form")  # use the url which we want to load

    fill_form(driver, user_data, selectors)

    input("Press Enter to exit...")
    driver.quit()

if __name__ == "__main__":
    main()