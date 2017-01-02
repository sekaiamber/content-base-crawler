from datetime import datetime
from selenium import webdriver
from .webpage import WebPage


def getDriver(config):
    driverName = config.webdriver.lower()
    driver = None
    if driverName == 'phantomjs':
        print('using phantomjs webdriver')
        driver = webdriver.PhantomJS()
    elif driverName == 'chrome':
        print('using chrome webdriver')
        driver = webdriver.Chrome(config.chromeDriverPath)
    if driver is None:
        config.parser.print_help()
        config.parser.error("Invalid web driver name")
    return driver


def process(config):
    # driver
    driver = getDriver(config)
    driver.get(config.url)
    t1 = datetime.now()
    body = driver.find_element_by_css_selector('body')
    t2 = datetime.now()
    # print(body.get_attribute('innerHTML'))
    webpage = WebPage(body)
    t3 = datetime.now()
    # webpage.print()
    print(t2 - t1)
    print(t3 - t2)
