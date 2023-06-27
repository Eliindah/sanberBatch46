import unittest
from selenium import webdriver


class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://katalon-demo-cura.herokuapp.com/")

    def test_search_in_python_org(self):
         self.driver.get("https://katalon-demo-cura.herokuapp.com/")
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
