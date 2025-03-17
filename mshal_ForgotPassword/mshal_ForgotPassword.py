# mshal_ForgotPassword.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException, 
    NoSuchElementException, 
    ElementNotInteractableException,
    WebDriverException
)
import time
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("mshal_ForgotPassword.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ForgotPasswordTest:
    def __init__(self, headless=False):
        import os

        current_dir = os.path.dirname(os.path.abspath(__file__))
        html_path = os.path.join(current_dir, "mshal_ForgotPassword.html")
        self.url = f"file://{html_path}"
        self.driver = None
        self.headless = headless
    
    def setup_driver(self):
        try:
            # Configure Chrome options
            chrome_options = Options()
            if self.headless:
                chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.maximize_window()
            logger.info("WebDriver initialized successfully")
            return True
        
        except WebDriverException as e:
            logger.error(f"Failed to initialize WebDriver: {str(e)}")
            return False
    
    #Opens page
    def open_forgot_password_page(self):
        
        try:
            if not self.setup_driver():
                print("Failed to set up the browser. Check the log for details.")
                return
            
            # Navigates to page
            try:
                self.driver.get(self.url)
                logger.info(f"Navigated to {self.url}")
                
                # Waits for page to load
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "email"))
                )
                
                print("\n=== mshal_ForgotPassword Page Opened ===")
                print("Please interact with the form directly in the browser.")
                print("Press Ctrl+C in this terminal to close the browser and exit.")
                
                # Keep the browser window open until the user terminates the program
                try:
                    while True:
                        time.sleep(1)
                except KeyboardInterrupt:
                    print("\nClosing browser and exiting...")
                
            except TimeoutException:
                logger.error("Timed out waiting for page to load")
                print("Error: Timed out waiting for page to load.")
            except WebDriverException as e:
                logger.error(f"Failed to navigate to page: {str(e)}")
                print(f"Error: Failed to open the page. {str(e)}")
                
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            print(f"Error: An unexpected error occurred: {str(e)}")
        finally:
            # Clean up
            if self.driver:
                self.driver.quit()
                logger.info("WebDriver closed")

if __name__ == "__main__":
    print("=== mshal_ForgotPassword ===")
    print("Opening the forgot password page for you to interact with...")
    
    test = ForgotPasswordTest()
    test.open_forgot_password_page()
