from selenium import webdriver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def current_url(self):
        return self.driver.current_url

    def title(self):
        return self.driver.title

    def footer(self):
        return self.driver.find_element_by_id('contact')


class ResultPage(BasePage):
    pass


class HomePage(BasePage):
    def move_to(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        return ResultPage(self.driver)


class Test:
    def __init__(self, url, browser):
        self.home_url = url
        if browser == 'chrome':
            capability = webdriver.DesiredCapabilities.CHROME
#            capability.setBrowserName("chrome")
#           capability.setPlatform("LINUX")
            self.driver = webdriver.Remote("http://localhost:32000/wd/hub", capability)
        else:
            raise ValueError("Browser not recognized: {}".format(browser))

    def test_home(self):
        home = HomePage(self.driver)
        result = home.move_to(self.home_url)
        assert "AtomCream" == result.title(), "Detailed error message"
        assert self.home_url == result.current_url(), "Detailed error message"
        assert result.footer(), "Detailed error message"

    def __del__(self):
        self.driver.close()
        self.driver.quit()
