import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

class DynamicLoadingTests(unittest.TestCase):

    # Element locators
    START_BUTTON = (By.ID, "start")
    LOADING_INDICATOR = (By.ID, "loading")
    CONTENT = (By.ID, "finish")

    @classmethod
    def setUpClass(cls):

        cls.html_path = os.path.abspath("dynamic_loading.html")
        cls.file_url = f"file:///{cls.html_path}"

        options = webdriver.ChromeOptions()
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.driver.maximize_window()

        # Opens HTML file
        cls.driver.get(cls.file_url)

        cls.wait = WebDriverWait(cls.driver, 20)

    @classmethod
    def tearDownClass(cls):

        time.sleep(2)

        if cls.driver:
            cls.driver.quit()

    def wait_for_manual_click(self):
        """Helper function to wait until the Start button is clicked manually to start tests."""
        print("\nClick the 'Start' button in the browser to continue...")
        
        self.wait.until(EC.visibility_of_element_located(self.LOADING_INDICATOR))
        print("Start button was clicked! Proceeding with the test...")


    def test_1_full_flow(self):
        """Test case to verify the full flow after clicking the button"""
        print("\nTest 1: Verifying the full flow...")

        # Wait for the start button to be visible
        start_button = self.wait.until(
            EC.visibility_of_element_located(self.START_BUTTON)
        )

        # Verify initial state
        print("Verifying initial state...")
        self.assertTrue(start_button.is_displayed(), "Start button should be visible initially")

        # Verify loading indicator is not visible initially
        loading_indicator = self.driver.find_element(*self.LOADING_INDICATOR)
        self.assertFalse(loading_indicator.is_displayed(), "Loading indicator should not be visible initially")

        # Verify content is not visible initially
        content = self.driver.find_element(*self.CONTENT)
        self.assertFalse(content.is_displayed(), "Content should not be visible initially")

        # Click the start button
        self.wait_for_manual_click()

        # Wait until the loading indicator appears
        self.wait.until(EC.visibility_of_element_located(self.LOADING_INDICATOR))

        # Verify loading indicator appears after button click
        loading_indicator = self.driver.find_element(*self.LOADING_INDICATOR)
        self.assertTrue(loading_indicator.is_displayed(), "Loading indicator should be visible after clicking start")

        # Wait for content to appear after loading
        content = self.wait.until(
            EC.visibility_of_element_located(self.CONTENT)
        )

        # Verify content text
        content_text = content.find_element(By.TAG_NAME, "h4").text
        self.assertEqual(content_text, "Hello World!",
                         f"Content text mismatch. Expected 'Hello World!', got '{content_text}'")

        print("Test 1: Full flow verification passed!")

    def test_2_content_appearance(self):
        """Test case to verify content appearance"""
        print("\nTest 2: Verifying content appearance without loading indicator...")

        try:
            # Wait for content to appear directly
            content = self.wait.until(EC.visibility_of_element_located(self.CONTENT))

            # Verify content is displayed
            self.assertTrue(content.is_displayed(), "Content should be visible after clicking start")

            print("Test 2: Content verification passed!")

        except Exception as e:
            print(f"Error during content verification test: {e}")
            raise


    def test_3_content_display(self):
        """Test case to verify content visibility"""
        print("\nTest 3: Verifying content visibility...")

        try:
            # Wait for content to appear directly
            content = self.wait.until(EC.visibility_of_element_located(self.CONTENT))

            # Verify content is visible
            self.assertTrue(content.is_displayed(), "Content should be visible after clicking start")

            print("Test 3: Content display verification passed!")

        except Exception as e:
            print(f"Error during content display test: {e}")
            raise


if __name__ == "__main__":
    unittest.main()

