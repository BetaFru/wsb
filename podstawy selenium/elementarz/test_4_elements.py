# -*- coding: utf-8" -*
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

"""
Na obiektach klasy WebElement możemy podejmować przeróżne akcje.
Przykłady:
clear() - czyści tekst
send_keys() - wpisuje zadany tekst
click() - klika w element
submit() - wysyła formularz
"""


class WsbPlSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)

    def test_click_on_link(self):
        self.driver.get("http://www.wsb.pl/wroclaw")
        self.podyplomowe_link = self.driver.find_element_by_link_text(
            "Studia podyplomowe")
        self.podyplomowe_link.click()
        sleep(5)

    def test_search_tester_in_wsb_pl(self):
        self.driver.get("http://www.wsb.pl/wroclaw")
        self.search_field = self.driver.find_element_by_id(
            "edit-search-block-form--2")
        self.search_field.clear()
        self.search_field.send_keys("tester")
        self.search_field.submit()

        results = self.driver.find_elements_by_xpath(
            "//*[@id='block-system-main']/div/ol/li")

        print("Znalazlem " + str(len(results)) + " wynikow:\n")
        for result in results:
            # Nic nie stoi na przeszkodzie, by odnaleźć element h3
            # zawarty w elemencie [@id='block-system-main']/div/ol/li
            result_title = result.find_element_by_xpath("./h3")
            print(result_title.text)
        # Sprawdzam, czy liczba znalezionych elementów jest równa 10
        self.assertEqual(10, len(results))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
