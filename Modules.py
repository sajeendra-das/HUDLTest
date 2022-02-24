import re
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expectedConditions


# Method to Load the URL from Config
def loadURL(driver, url):
    driver.get(url)


# Method to Close the webdriver
def closeDriver(driver):
    driver.close()


# Method to Click the Login Button
def clickLoginButton(driver, objLoginMain, objEmail):
    btnLogin = driver.find_element(By.LINK_TEXT, objLoginMain)
    btnLogin.click()
    try:
        email_wait = expectedConditions.presence_of_element_located((By.ID, objEmail))
        WebDriverWait(driver, 10).until(email_wait)
    except Exception as e:
        print(e)


# Method to enter UserID and Password from config file
def enterCredentials(driver, user_id, user_pwd, objUser, objPassword, objLogin):
    user_name = driver.find_element(By.ID, objUser)
    user_name.clear()
    user_name.send_keys(user_id)
    password = driver.find_element(By.ID, objPassword)
    password.clear()
    password.send_keys(user_pwd)

    login = driver.find_element(By.ID, objLogin)
    login.click()


# Method to verify successful login
def verifyLogin(driver, expUrl, expTitle, objMenuDropDown):
    try:
        drop_wait = expectedConditions.presence_of_element_located(
            (By.XPATH, "// *[ @ class = \""+objMenuDropDown+"\"]"))
        WebDriverWait(driver, 10).until(drop_wait)
    except Exception as e:
        print("Page Not Loaded")

    assertCheck = True
    # Assertion to Check for Title
    try:
        assert expTitle in driver.title
    except AssertionError as e:
        print("Login Failed")
        return False

    # Assertion to Check for URL
    try:
        assert expUrl in driver.current_url
    except AssertionError as e:
        print("Login Failed")
        return False

    return assertCheck


# Method to verify successful logout
def verifyLogout(driver, expUrl, expTitle):
    assertCheck = True
    # Assertion to Check for Title
    try:
        assert expTitle in driver.title
    except AssertionError as e:
        print("Logout Failed")
        return False

    # Assertion to Check for URL
    try:
        assert expUrl in driver.current_url
    except AssertionError as e:
        print("Logout Failed")
        return False


# Method to verify unsuccessful login
def verifyUnsuccessfulLogin(driver, unsuccessfulLoginContainer):
    print("Verify Unsuccessful Login")

    try:
        unsucess_wait = expectedConditions.presence_of_element_located(
            (By.XPATH, " // div[ @ class = \""+unsuccessfulLoginContainer+"\"]"))
        WebDriverWait(driver, 2).until(unsucess_wait)
        print("Login Unsuccessful")
    except Exception as e:
        print(e)


# Method to verify unsuccessful login
def validateEmail(emailID):
    pattern_new = r"\"?([-a-zA-Z0-9.`?{}_]+@\w+\.\w+)\"?"
    pattern = re.compile(pattern_new)
    if not re.match(pattern, emailID):
        print("Incorrect Email Format")
        return False
    else:
        return True


# Method to perform Logout
def clickLogout(driver, objMenuDropDown, objLogout):
    dropdown = driver.find_element(By.XPATH, "// *[ @ class = \""+objMenuDropDown+"\"]")
    action = ActionChains(driver)
    action.move_to_element(dropdown).perform()

    logout = driver.find_element(By.LINK_TEXT, objLogout)
    action.move_to_element(logout).click().perform()
