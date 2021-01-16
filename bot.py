
from selenium import webdriver
from selenium.common.exceptions         import TimeoutException
from selenium.webdriver.support.ui      import WebDriverWait 
from selenium.webdriver.support         import expected_conditions as EC
from selenium.webdriver.chrome.options  import Options
from selenium.webdriver.common.keys     import Keys
from time import sleep

class InstaBot:

    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        # Saving the reference if we need it for any other methods
        self.username = username
        self.pw = pw
        # Open Instagram
        self.driver.get('https://instagram.com/')
        sleep(2)
        # Inputs Username
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')\
        .send_keys(username)
        sleep(.5)
        # Inputs Password
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')\
        .send_keys(pw)
        sleep(.5)
        # Clicks 'Log in'
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')\
        .click()
        sleep(2)
        # Clicks 'Not Now' for 'Turn on Notifications'
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')\
        .click()
        sleep(2)

    def Get_Info(self):
        # Clicks to user's Instagram Page
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a')\
        .click()
        sleep(2)   
        # Retrieving the names the user is following
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")\
        .click() 
        following = self.Get_Names()
        print('\n')
        # Prints Followings
        print('Now Printing all of the people you are follwing\n')
        print(following)
        sleep(2)
        # Retrieving the followers of the user
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")\
        .click()
        followers = self.Get_Names()
        print('\n')
        # Prints Followers
        print('Now Printing all of your followers\n')
        print(followers)
        sleep(2)
        print('\n People who are not following you!\n')
        print(followers.difference(following))




        
        
    def Get_Names(self):
        sleep(2)
        #Scroll box
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        # Algro that scrolls down the display of the names
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(2)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
        .click()
        self.names = names
        return names

    #def Compare_Names(self):
        #Pass the following and followers

        #make an if statement or for loop that comapares the two

        #Create a variable that prints the names


        



my_bot = InstaBot('username', 'password')
my_bot.Get_Info()
#my_bot.Compare_Names()