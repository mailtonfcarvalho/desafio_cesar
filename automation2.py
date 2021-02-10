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

        titulo = self.driver.find_elements_by_xpath(
            '//h2[@itemprop="headline"]')[2].text

        dia = self.driver.find_elements_by_xpath(
            '//span[@class="date-day"]')[2].text
        mes = self.driver.find_elements_by_xpath(
            '//span[@class="date-month"]')[2].text
        ano = self.driver.find_elements_by_xpath(
            '//span[@class="date-year"]')[2].text
        data = dia+'-'+mes+'-'+ano

        acessar_post = self.driver.find_elements_by_xpath(
            '//h2[@itemprop="headline"]')[1]
        acessar_post.click()
        autor1 = self.driver.find_elements_by_xpath(
            '//span[@itemprop="name"]')[2].text

        proximo = self.driver.find_element_by_partial_link_text(
            "Post seguinte ")
        proximo.click()

        titulo_post_seguinte = self.driver.find_elements_by_xpath(
            '//h1[@itemprop="headline"]')[0].text
        autor2 = self.driver.find_elements_by_xpath(
            '//span[@itemprop="name"]')[2].text

        print("Titulo do terceiro post:", titulo)
        print("Data do terceiro post:", data)
        print("Autor do segundo post:", autor1)
        print("Titulo do post seguinte:", titulo_post_seguinte)
        print("Autor post seguinte:", autor2)


if __name__ == '__main__':

    user = Automation2()
    user.information_retrieval()
