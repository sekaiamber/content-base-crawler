from datetime import datetime
from selenium import webdriver
from .webpage import WebPage
from .timer import Timer
from .domSignaturer import DomSignaturer


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
    # timer
    timer = Timer()
    timer.addTag('Init finish')
    # get body element
    body = driver.find_element_by_css_selector('body')
    timer.addTag('Dom ready')
    # build webpage
    webpage = WebPage(body)
    timer.addTag('Webpage inited')

    # test
    # webpage.print()
    # domSignaturer = DomSignaturer()
    # domSignaturer.print()
