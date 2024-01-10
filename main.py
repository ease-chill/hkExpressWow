#%%

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import SessionNotCreatedException

import requests
import zipfile
from config import *
import os, shutil, glob
import time
from datetime import datetime


# %%

def get_chromedriver():

    print('Downloading chromedriver download link...')
    chromedrivers_list = requests.get(CHROMEDRIVER_URL).json()

    download_link = [
        d['url']
        for d in chromedrivers_list['channels']['Stable']['downloads']['chromedriver']
        if d['platform'] == OS
    ][0]

    zip_file = 'chromedriver.zip'

    r = requests.get(download_link)
    with open(zip_file, 'wb') as f:
        f.write(r.content)

    print('Downloaded.')

    print('Extracting chromedriver.zip...')
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall('.')
    print('Extracted.')

    # Delete the "chromedriver.zip" file
    print(f"Deleting {zip_file}...")
    os.remove(zip_file)
    print(f"Deleted.")

    # Find and move the file with name starting with "chromedriver"
    source_folder = ""
    chromedriver_filename = ""

    print("Moving chromedriver to root...")
    for folder_name in os.listdir("."):
        if folder_name.startswith("chromedriver"):
            source_folder = folder_name
            break

    if source_folder:
        for file_name in os.listdir(source_folder):
            if file_name.startswith("chromedriver"):
                chromedriver_filename = file_name
                source_file = os.path.join(source_folder, file_name)
                destination_file = os.path.join(".", file_name)
                shutil.move(source_file, destination_file)
                print(f"Moved {file_name} to root.")
                break
    else:
        print("No folder starting with 'chromedriver' found")

    # Delete the "chromedriver" folder
    print(f"Deleting folder: {source_folder}...")
    shutil.rmtree(source_folder)
    print(f"Deleted.")

    return chromedriver_filename
#%%

def check_chromedriver():

    # Check if any file starting with "chromedriver" exists in the root directory
    chromedriver_files = glob.glob("chromedriver*")
    if not chromedriver_files:
        print("No chromedriver file found in the root directory.")
        get_chromedriver()
    else:
        try:
            print("Chromedriver found, checking version...")
            # Attempt to create a new instance of the Chrome driver
            driver = webdriver.Chrome()
            driver.quit()
            print("ChromeDriver is up to date.")
        except SessionNotCreatedException as e:
            # Handle the exception indicating an outdated ChromeDriver
            print("Error: ChromeDriver is outdated. Updating ChromeDriver...")

            # Delete the current ChromeDriver at the root level
            for file in chromedriver_files:
                os.remove(file)

            # Download the latest compatible version of ChromeDriver
            get_chromedriver()

            # Retry creating a new instance of the Chrome driver
            check_chromedriver()


# %%

def open_tabs(total_tabs):

    chrome_options = Options()
    # set chrome tab to private mode
    chrome_options.add_argument("--incognito")
    # Set the window size and position options
    chrome_options.add_argument("--window-size=200,100")
    chrome_options.add_argument("--window-position=1800,900")

    # start selenium chrome driver
    driver = webdriver.Chrome(options=chrome_options)


    driver.get(URL)
    for i in range(1,total_tabs):
        driver.execute_script(f"window.open('{URL}');")

    
    return driver




# %%

def check_status(driver,total_tabs):

    driver.implicitly_wait(5)

    while True:

        print(f"Checking status at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}" )
            
        for i in range(total_tabs):
            driver.switch_to.window(driver.window_handles[i])
            tips = driver.find_element(by=By.ID, value=YOUR_TURN_ELEMENT_ID)
            style = tips.get_attribute('style')
            if style != 'display: none;':
                driver.execute_script("alert('YOUR TURN!');")
                print(f"element style: {style}")
                # Wait until the alert is present
                wait = WebDriverWait(driver, 600)
                wait.until_not(EC.alert_is_present())
        
        time.sleep(5)

        
    

# %%

if __name__ == "__main__":

    check_chromedriver()
    driver = open_tabs(TOTAL_TABS)
    check_status(driver, TOTAL_TABS)