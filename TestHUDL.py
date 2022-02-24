import binascii
import configparser
import Modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class TestHUDL:
    # Call Test Method to Create Selenium Driver and Call Steps Sequentially
    def callTest(self, config_file_name):
        self.service = Service("./chromedriver")
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

        self.getConfigs(config_file_name)

        # Test Steps
        # Step 1: Load Driver and Open URL
        Modules.loadURL(driver=self.driver, url=self.url)

        # Step 2: Click Login Button
        Modules.clickLoginButton(driver=self.driver, objLoginMain=self.btnLoginMain, objEmail=self.textEmail)

        # Validate User Email and continue test only if validation is successful
        if Modules.validateEmail(emailID=self.user_id):
            # Step 3: Enter correct credentials
            Modules.enterCredentials(driver=self.driver, user_id=self.user_id, user_pwd=self.user_pwd,
                                     objLogin=self.btnLogin, objUser=self.textEmail, objPassword=self.textPassword)

            # Step 4: Validate Successful login
            if Modules.verifyLogin(driver=self.driver, expUrl=self.expectedUrlLogin, expTitle=self.expectedTitleLogin,
                                   objMenuDropDown=self.menuDropDown):

                # Step 5: Click Logout Button
                Modules.clickLogout(driver=self.driver, objMenuDropDown=self.menuDropDown, objLogout=self.btnLogout)

                # Step 6: Verify Successful Logout
                Modules.verifyLogout(driver=self.driver, expUrl=self.expectedUrlLogout,
                                     expTitle=self.expectedTitleLogout)

                # Step 7: Close Driver
                Modules.closeDriver(driver=self.driver)

            else:
                # Stop Test
                Modules.closeDriver(driver=self.driver)
        else:
            # Stop Test
            Modules.closeDriver(driver=self.driver)

    # Read Configs for Username, Password and URL to login to
    # Read Settings for Object Names and Validation Title and URL
    def getConfigs(self, filename):
        try:
            config = configparser.ConfigParser()
            config.read(filename)

            settings = config['settings']
            self.url = settings.get('url')
            self.user_id = settings.get('user_id')
            self.user_pwd = settings.get('user_pwd')

            objects = config['objects']
            self.btnLoginMain = objects.get('btnLoginMain')
            self.textEmail = objects.get('textEmail')
            self.textPassword = objects.get('textPassword')
            self.btnLogin = objects.get('btnLogin')
            self.menuDropDown = objects.get('menuDropDown')
            self.btnLogout = objects.get('btnLogout')

            verify = config['verify']
            self.expectedUrlLogin = verify.get('expectedUrlLogin')
            self.expectedTitleLogin = verify.get('expectedTitleLogin')
            self.expectedUrlLogout = verify.get('expectedUrlLogout')
            self.expectedTitleLogout = verify.get('expectedTitleLogout')

            # UserName and Password is stored in HEX format in INI file. UNHex to get the values to use
            # I could have used complex encryption, but it required more time to implement
            self.user_id = binascii.unhexlify(self.user_id).decode('utf-8')
            self.user_pwd = binascii.unhexlify(self.user_pwd).decode('utf-8')

        except Exception as e:
            print(e)


if __name__ == '__main__':
    selTest = TestHUDL()















