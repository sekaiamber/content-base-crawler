from selenium import webdriver


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
    data = driver.find_element_by_id('su').get_attribute('value')
    print(data)
