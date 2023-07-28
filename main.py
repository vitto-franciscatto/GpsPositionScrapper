import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getopt

def scrap_gps_pos(argv):
    url = ''
    verbose = False

    options, argv = getopt.getopt(argv, "u:v", ["url=", "verbose"])
    for opt, arg in options:
        if opt in ('-u', '--url'):
            url = arg
        if opt in ('-v', '--verbose'):
            verbose = True

    if verbose:
        print(url)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless=new")

    chrome_driver = webdriver.Chrome(options=chrome_options)
    chrome_driver.get(url)

    element = WebDriverWait(chrome_driver, 5).until(EC.text_to_be_present_in_element(By.CLASS_NAME, 'position_x'))

    lat = chrome_driver.find_element(By.CLASS_NAME, 'position_x')
    long = chrome_driver.find_element(By.CLASS_NAME, 'position_y')
    height = chrome_driver.find_element(By.CLASS_NAME, 'position_h')

    print(f'LAT: {lat.text} | LONG: {long.text} | HGT: {height.text}')
    chrome_driver.quit()


if __name__ == '__main__':
    scrap_gps_pos(sys.argv[1:])
