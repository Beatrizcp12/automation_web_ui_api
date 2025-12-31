from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Edge()
    context.driver.maximize_window()


