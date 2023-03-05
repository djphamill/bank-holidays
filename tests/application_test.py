"""
Selenium tests for the application
"""
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestApplication(TestCase):
    """
    Selenium test suite for the web application
    """

    LOCAL_HOST = 'localhost'
    PORT = '5000'
    URL = f'http://{LOCAL_HOST}:{PORT}'

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    def test_title_of_homepage(self) -> None:
        """
        Test the title of the hoepage of the web applicaiton
        """
        self.driver.get(self.URL)
        title = self.driver.title
        self.assertEqual(title, "Bank Holiday?")
        

