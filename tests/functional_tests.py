from unittest import TestCase
from selenium import webdriver
from time import sleep

class FunctionTests(TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000/index_for_tests.html')


    def tearDown(self) -> None:
        self.browser.close()

    def test_alert_is_present(self):
        # give pyscript a chance to load
        sleep(9)
        # browser starts with an alert on
        alert = self.browser.switch_to.alert
        # check alert exists
        self.assertTrue(alert, 'An alert did not show up')
        # check the text of alert is 'it works'
        self.assertEqual(alert.text, 'it works', 'text of the alert is not "it works" as it should')
        # clicks "ok"
        alert.accept()

