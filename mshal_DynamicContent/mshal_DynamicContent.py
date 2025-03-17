from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def dynamic_content():
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # Opens HTML file (in same folder)
        driver.get("file:///" + os.path.abspath("mshal_DynamicContent.html"))

        # Waits for the content to be visible
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Refresh Content']")))

        # Prints initial content
        content_before = driver.find_elements(By.CSS_SELECTOR, '.content-item p')
        print("Content before refresh:")
        for item in content_before:
            print(item.text)

        refresh_button = driver.find_element(By.XPATH, "//button[text()='Refresh Content']")
        refresh_button.click()

        # Waits for content to refresh
        WebDriverWait(driver, 10).until(EC.staleness_of(content_before[0]))  # Wait for the content to change
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.content-item p')))

        # Prints content after refresh
        content_after = driver.find_elements(By.CSS_SELECTOR, '.content-item p')
        print("\nContent after refresh:")
        for item in content_after:
            print(item.text)

        # Waits before closing browser (to give time to use it)
        time.sleep(10)  # Adjust the sleep time as needed (e.g., 5 seconds)

        driver.quit()

    except Exception as e:
        print(f"An error occurred: {e}")
        driver.quit()

if __name__ == "__main__":
    dynamic_content()

