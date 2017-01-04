from datetime import datetime
from selenium import webdriver
from .timer import Timer


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
    with open(config.workFile) as f:
        code = compile(f.read(), config.workFile, 'exec')
        exec(code)
