from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Automation2:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.url = "https://www.cesar.school/"

    def information_retrieval(self):

        self.driver.get(self.url)
        blog = self.driver.find_element_by_partial_link_text("Blog")
        blog.click()

        title = self.driver.find_elements_by_xpath(
            '//h2[@itemprop="headline"]')[2].text

        day = self.driver.find_elements_by_xpath(
            '//span[@class="date-day"]')[2].text
        month = self.driver.find_elements_by_xpath(
            '//span[@class="date-month"]')[2].text
        year = self.driver.find_elements_by_xpath(
            '//span[@class="date-year"]')[2].text
        date = day+'-'+month+'-'+year

        access_post = self.driver.find_elements_by_xpath(
            '//h2[@itemprop="headline"]')[1]
        access_post.click()
        author1 = self.driver.find_elements_by_xpath(
            '//span[@itemprop="name"]')[2].text

        go_next = self.driver.find_element_by_partial_link_text(
            "Post seguinte ")
        go_next.click()

        next_post = self.driver.find_elements_by_xpath(
            '//h1[@itemprop="headline"]')[0].text
        author2 = self.driver.find_elements_by_xpath(
            '//span[@itemprop="name"]')[2].text

        print("Titulo do terceiro post:", title)
        print("Data do terceiro post:", date)
        print("Autor do segundo post:", author1)
        print("Titulo do post seguinte:", next_post)
        print("Autor post seguinte:", author2)


if __name__ == '__main__':

    user = Automation2()
    user.information_retrieval()
