
**GENERAL INFO**

This repo has the following test sets:
1. Dynamic Content
2. Dynamically Loaded Page Elements
3. Forgot Password

Each test set contains HTML files for the web interface and Python scripts for automated testing using Selenium WebDriver.

Before starting, please ensure you have:
- Python 3.6 or higher
- Chrome browser
- The Selenium package >> pip install selenium webdriver-manager
_________________________________________________________________________________________________________
**DYNAMIC CONTENT**
The content will be re-arranged everytime the page is refreshed

**How To Run:**
1. Make sure all of the following files are in the same folder:
    - mshal_DynamicContent.html
    - mshal_DynamicContent.py
    - image1.jpg
    - image2.jpg
    - image3.jpg
    - image4.jpg
    - image5.jpg
    - image6.jpg
2. Open a terminal/command prompt and navigate to the directory
3. Run the test >> python mshal_DynamicContent.py
4. A chrome browser will open
5. The script will print the intial content
7. After clicking the refresh button, the test will randomly refresh the content
8. The browser is set to automatically close after a certain amount of time
_________________________________________________________________________________________________________
**DYNAMICALLY LOADED PAGE ELEMENTS**

The content will loaded asynchronously after a user action

**How to run:**
1. Make sure all of the following files are in the same folder:
    - mshal_DynamicallyLoadedPageElement.py
    - mshal_DynamicallyLoadedPageElement.html
2. Open a terminal/command prompt and navigate to the directory
3. Run the test >> python mshal_DynamicallyLoadedPageElement.py
4. A chrome browser will open
5. The test will wait for the "Start" button to be clicked on the browser window
6. After clicking, the test will automatically verify the loading behaviour

_________________________________________________________________________________________________________
**FORGOT PASSWORD**

Prompts user to enter valid email address -with error handling

**How to run:**
1. Make sure all of the following files are in the same folder:
    - mshal_ForgotPassword.html
    - mshal_ForgotPassword.py
2. Open a terminal/command prompt and navigate to the directory
3. Run the test >> python mshal_ForgotPassword.py
4. A chrome browser will open
5. Interact with the form, try valid/invalid email format, and submit to see success/error message
6. Press Ctrl+C in the terminal to close browser
