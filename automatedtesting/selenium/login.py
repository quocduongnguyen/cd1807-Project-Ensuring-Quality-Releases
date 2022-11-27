# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from datetime import datetime

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Start the browser and login with standard_user
def login(user, password):
    print(timestamp() + 'Starting the browser...')
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless") 
    options.add_argument("--remote-debugging-port=9230")
    driver = webdriver.Chrome(options=options, executable_path="automatedtesting/selenium/chromedriver")
    print(timestamp() + 'Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    # login
    driver.find_element(By.CSS_SELECTOR, "input[id='user-name']").send_keys(user)
    driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    product_label = driver.find_element(By.CSS_SELECTOR, "div[class='inventory_item_name']").text
    assert "Sauce Labs Backpack" in product_label
    print(timestamp() + 'Login with username {:s} and password {:s} successfully.'.format(user, password))
    return driver

def add(driver, n_products):
    for i in range(n_products):
        element = "a[id='item_" + str(i) + "_title_link']"  # Get the URL of the product
        driver.find_element(By.CSS_SELECTOR, element).click()  # Click the URL
        driver.find_element(By.CSS_SELECTOR,"button.btn_primary.btn_inventory").click()  # Add the product to the cart
        product = driver.find_element(By.CSS_SELECTOR,"div[class='inventory_details_name large_size']").text  # Get the name of the product from the page
        print(timestamp() + product + " added to shopping cart.")  # Display message saying which product was added
        driver.find_element(By.CSS_SELECTOR,"button.inventory_details_back_button").click()  # Click the Back button
    print(timestamp() + '{:d} items are all added to shopping cart successfully.'.format(n_products))

def remove(driver, n_products):
    for i in range(n_products):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element(By.CSS_SELECTOR,element).click()
        driver.find_element(By.CSS_SELECTOR,"button.btn_secondary.btn_inventory").click()
        product = driver.find_element(By.CSS_SELECTOR,"div[class='inventory_details_name large_size']").text
        print(timestamp() + product + " removed from shopping cart.")  # Display message saying which product was added
        driver.find_element(By.CSS_SELECTOR,"button.inventory_details_back_button").click()
    print(timestamp() + '{:d} items are all removed from shopping cart successfully.'.format(n_products))


if __name__ == "__main__":
    n_products = 6
    driver = login('standard_user', 'secret_sauce')
    add(driver, n_products)
    remove(driver, n_products)
    print(timestamp() + 'Selenium tests are all successfully completed!')
    driver.stop_client()
    driver.close()
    driver.quit()