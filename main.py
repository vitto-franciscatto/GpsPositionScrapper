import sys
import getopt
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



def convert_DMS_to_decimal(value):
    idx_degree = value.find("°")
    idx_minute = value.find("'")
    idx_second = value.find("\"")
    degree_value = value[1: idx_degree]
    minute_value = value[idx_degree + 1: idx_minute]
    second_value = value[idx_minute + 1: idx_second]

    converted_value = round(float(degree_value) + float(minute_value) / 60 + float(second_value) / 3600, 7)
    if value[0] in ('S', 'W'):
        return converted_value * (-1)

def scrap_gps_pos(argv):

    url = ''
    use_firefox = False
    use_headless = True

    options, argv = getopt.getopt(argv, "u:v", ["url=", "use-firefox", "headed"])
    for opt, arg in options:
        if opt in ('-u', '--url'):
            url = arg
        if opt in ('-v', '--verbose'):
            verbose = True
        if opt == '--use-firefox':
            use_firefox = True
        if opt == '--headed':
            use_headless = False

    if use_firefox:
        options = webdriver.FirefoxOptions()
        if use_headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    else:
        chrome_options = webdriver.ChromeOptions()
        if use_headless:
            chrome_options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)
    time.sleep(1)

    lat = driver.find_element(By.CLASS_NAME, 'position_x')
    long = driver.find_element(By.CLASS_NAME, 'position_y')
    height = driver.find_element(By.CLASS_NAME, 'position_h')

    print(f'LAT: {convert_DMS_to_decimal(lat.text)} | LONG: {convert_DMS_to_decimal(long.text)} | HGT: {height.text}')
    driver.quit()


if __name__ == '__main__':
    scrap_gps_pos(sys.argv[1:])
