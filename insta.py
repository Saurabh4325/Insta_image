from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import wget


inp_username = input("Enter your username: ")
inp_password = input("Enter your password: ")
favr = input("Enter your favourite one username: ")
# Initialize the Chrome driver
driver = webdriver.Chrome()

#insta open
driver.get("https://www.instagram.com/accounts/login/")

wait = WebDriverWait(driver, 20)

username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
username.clear()
username.send_keys(inp_username)  

password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password.clear()
password.send_keys(inp_password) 

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')))
login_button.click()

time.sleep(5)

driver.get("https://www.instagram.com/" + favr + "/") 


driver.execute_script("window.scrollTo(0, 4000);")
time.sleep(5)


images = driver.find_elements(By.TAG_NAME, "img")


path = os.path.join(os.getcwd(), "downloaded_images")
os.makedirs(path, exist_ok=True)
print(f"Images will be saved in: {path}")


counter = 0

# code for download images 
for img in images:
    img_url = img.get_attribute("src")
    # Check if img_url is a valid URL (starts with http or https)
    if img_url and (img_url.startswith("http://") or img_url.startswith("https://")):
        save_as = os.path.join(path, f"image_{counter}.jpg")
        wget.download(img_url, save_as)
        print(f"Downloaded: {save_as}")
        counter += 1

print(f"Total images downloaded: {counter}")

driver.quit()
