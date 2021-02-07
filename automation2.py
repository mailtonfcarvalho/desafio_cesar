from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class automation_task1(object):

    def create_driver(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())
        url = "https://www.cesar.school/"
        driver.get(url)
        sleep(5)


if __name__ == '__main__':

    user = automation_task1()
    user.create_driver()
