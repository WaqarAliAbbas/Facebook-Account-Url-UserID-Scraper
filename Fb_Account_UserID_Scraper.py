# -- Facebook Account Friends User-ID Scraper 
# -- Developer Waqar Ali Abbas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
print("Scrape Any Facebook Targeted Public UserIDS")
print("Developer Waqar Ali Abbas")
username=input("Enter Email Address:  ")
userpassword=input("Enter Password:  ")
Scraped_Acc_Url=input("Enter Targeted Public Facebook Account Friend Url/Path With mbasic Mode:  ")
url="https://www.facebook.com"
option=Options()
option.add_argument("disable-notifications")
driver=webdriver.Chrome(options=option)
driver.maximize_window()
driver.delete_all_cookies()
driver.get(url)
email=(By.NAME,"email")
password=(By.NAME,"pass")
login=(By.NAME,"login")
wait=WebDriverWait(driver,15)
wait.until(EC.presence_of_element_located((email))).send_keys(username)
wait.until(EC.presence_of_element_located((password))).send_keys(userpassword)
wait.until(EC.element_to_be_clickable((login))).click()
time.sleep(6)
driver.get(Scraped_Acc_Url)
time.sleep(2)
with open("Fb-Friends-Urls.txt","a") as file_:
    while True:
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'See More Friends')]"))).click()
            frnds=wait.until(EC.presence_of_all_elements_located((By.XPATH,"//a[@class='bo']")))
            for link in frnds:
                frnd_url=link.get_attribute("href")
                if "profile.php?id" in frnd_url:
                    b=frnd_url.split("=")
                    user_Id=b[1].split("&")[0]
                    file_.write(f"{user_Id}\n")
                    print(frnd_url)
                else:
                    b=frnd_url.split("/")
                    user_Id=b[3].split("?")[0]
                    file_.write(f"{user_Id}\n")
                    print(frnd_url)
            time.sleep(4)
        except Exception as s:
            break