from robot.api.deco import keyword
from page_objects import Test


@keyword('Open Browser')
def openbrowser(url, browser):
    to = Test(url, browser)
    to.test_home()
