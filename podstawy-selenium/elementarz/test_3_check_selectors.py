# -*- coding: utf-8" -*
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

"""
WebDriver zawiera szereg metod wyszukiwania elementów zawartych na stronie.
Wszystkie zaczynają się od "find_element_by..." i zwracają obiekt klasy
WebElement. W przypadku, gdy chcemy wyszukać wiele elementów, korzystamy
z metod "find_elements_by_..." - otrzymujemy wówczas listę złożoną
z obiektów klasy WebElement
"""


class WsbPlSelectors(unittest.TestCase):
    """
    Lokalizatory na stronie wsp.pl/wroclaw
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_find_element(self):
        driver = self.driver
        driver.get("http://www.wsb.pl/wroclaw")
        # Wyszukuję ciało strony (to co widać) - cała strona
        driver.find_element_by_tag_name("body")
        # Wyszukuję: Pole wyszukiwania
        driver.find_element_by_id("edit-search-block-form--2")
        driver.find_elements_by_class_name("custom-search-box")
        # Wyszukuję: Link do studiów podyplomowych
        driver.find_element_by_link_text("Studia podyplomowe")
        driver.find_element_by_partial_link_text("podyplom")

    def test_find_element_by_css_selector(self):
        driver = self.driver
        driver.get("http://www.wsb.pl/wroclaw")
        # Wyszukuję: Pole wyszukiwania
        driver.find_element_by_css_selector("#edit-search-block-form--2")

    def test_find_element_by_xpath(self):
        driver = self.driver
        driver.get("http://www.wsb.pl/wroclaw")
        # Wyszukuję: Pole wyszukiwania
        driver.find_element_by_xpath('//*[@id="edit-search-block-form--2"]')

    def tearDown(self):
        self.driver.quit()


class WizzairSelectors(unittest.TestCase):
    """
    Lokalizatory na stronie wizzair.com
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_find_element_by_full_css_selector(self):
        driver = self.driver
        driver.get("https://wizzair.com/pl-pl/main-page#/")
        # Wyszukuję Przycisk Zaloguj
        driver.find_element_by_css_selector("#app > header > \
        div > nav > ul > li:nth-child(3) > button")

    def test_find_element_by_full_xpath(self):
        driver = self.driver
        driver.get("https://wizzair.com/pl-pl/main-page#/")
        # Wyszukuję Przycisk Zaloguj
        driver.find_element_by_xpath(
            '//*[@id="app"]/header/div/nav/ul/li[3]/button')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
