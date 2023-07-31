import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import getopt
import time

def scrap_gps_pos(argv):

    url = ''
    useFirefox = False
    useHeadless = True

    options, argv = getopt.getopt(argv, "u:v", ["url=", "use-firefox", "headed"])
    for opt, arg in options:
        if opt in ('-u', '--url'):
            url = arg
        if opt in ('-v', '--verbose'):
            verbose = True
        if opt == '--use-firefox':
            useFirefox = True
        if opt == '--headed':
            useHeadless = False

    if useFirefox:
        options = Options()
        if useHeadless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    else:
        chrome_options = webdriver.ChromeOptions()
        if useHeadless:
            chrome_options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)
    time.sleep(1)

    lat = driver.find_element(By.CLASS_NAME, 'position_x')
    long = driver.find_element(By.CLASS_NAME, 'position_y')
    height = driver.find_element(By.CLASS_NAME, 'position_h')

    print(f'LAT: {lat.text} | LONG: {long.text} | HGT: {height.text}')
    driver.quit()


if __name__ == '__main__':
    scrap_gps_pos(sys.argv[1:])
