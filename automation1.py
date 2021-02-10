from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import re
import numpy as np
import collections
import operator


class Automation1:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.url = "https://www.discourse.org/"

    def information_retrieval(self):

        self.driver.get(self.url)
        demo = self.driver.find_element_by_partial_link_text("Demo")
        demo.click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 4000)")
        sleep(3)

        rows = self.driver.find_elements_by_xpath("//td[1]")
        views = self.driver.find_elements_by_xpath("//td[4]")
        result = {}
        titles = []

        for row, view in zip(rows, views):
            try:
                row.find_element_by_xpath(
                    "span/div/span[contains(@title, 'This topic is closed; it no longer accepts new replies')]")

                titles.append(row.find_element_by_xpath("span/a").text)

                result[row.find_element_by_xpath("span/a").text] = int(re.findall(
                    '[0-9]+', view.find_element_by_xpath("span").get_attribute("title").replace(",", ""))[0])

            except:
                result[row.find_element_by_xpath("span/a").text] = int(re.findall(
                    '[0-9]+', view.find_element_by_xpath("span").get_attribute("title").replace(",", ""))[0])

        record = []
        for item in rows:
            try:
                item.find_element_by_xpath(
                    "div/a/span/span[contains(@class,'category-name')]")
                record.append(item.text.split("\n")[1])
            except:
                record.append("no category")

        print("Titulos de todos os topicos fechados são:", titles)
        np.unique(record, return_counts=True)
        items = np.array(record)
        items_all = collections.Counter(items)
        print("Quantidade de itens de cada categoria:", items_all)

        sorted_x = sorted(
            result.items(), key=operator.itemgetter(1), reverse=True)
        print("Titulo do topico com maior numero de Views:", sorted_x[0])


if __name__ == '__main__':

    user = Automation1()
    user.information_retrieval()
