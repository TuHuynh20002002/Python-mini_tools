## Libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

## Variables
service = Service('') # Absolute path to chromedriver.exe (e.g. 'C:/Users/username/Downloads/chromedriver.exe)

def get_driver():
    ## Set options for Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('ignore-certificate-errors')
    options.add_argument('no-sandbox')
    options.add_argument('disable-blink-features=AutomationControlled')
    options.add_argument('start-maximized')

    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    driver = webdriver.Chrome(service=service, options=options)
    return driver


if __name__ == '__main__':
    driver = get_driver()
    driver.get("https://www.google.com")
