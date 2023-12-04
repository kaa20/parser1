import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_sourse_html(url):
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get(url)
        time.sleep(3)

        if driver.find_elements(By.CLASS_NAME, 'widget-search-result-container'):
            with open("source-page.html", "w", encoding="utf-8") as file:
                file.write(driver.page_source)

    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()

def main():
    get_sourse_html(url="https://www.ozon.ru/category/noutbuki-apple-macbook-pro/")

if __name__ == "__main__":
    main()
