import random
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import StaleElementReferenceException
import time
from main import get_msg



#driver call 
# Enter Absolute Path of to the chrome driver  
driver=webdriver.Chrome(executable_path='D:/AVANTAR/PythonProjects/Automation/chromedriver_win32/chromedriver.exe')


#website call
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 300) 
  
 

#send message
def send_msg(target):
	global driver
	A=["Happy Diwali","May this Diwali Light up New Dreams, Fresh Hopes, Undiscovered Avenues, Different Perspectives, Everything Bright & Beautiful, And Fill Your Days with Pleasant Surprises & Moments. Happy Diwali ","Delightful Laddoos, Incandescent Diyas, Whole lot of Smiles and Laughter, A big stock of Masti, Lots of Mithai,  Innumerable Fireworks, Wishing you Fun, Frolic and Endless Celebration!! HAPPY DIWALI 2020….!!!","Warm & elite wishes not only for a special occasion but for today and forever….. Happy Diwali!!","Life with you is like Diwali, So let’s promise to be together like this forever. Wish you a very Happy Diwali!","A festival full of sweet childhood memories, a sky full of fireworks, Mouth full of sweets, House full of diyas and heart full of joy… Wishing you all a very Happy Diwali 2020!!","Happiness is in the Air, It’s Diwali everywhere, Lets Show Some Love and Care, And Wish Everyone out there…"]
	ln=len(A)
	target=f'"{target}"'
	

	x_arg = '//span[contains(@title,' + target + ')]'

	ser_path='//*[@id="side"]/div[1]/div/label/div/div[2]'
	sear_box=wait.until(EC.presence_of_element_located((By.XPATH, ser_path)))  #searching in search bar for particular name
	sear_box.send_keys(target[1:-1])


	group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg))) #opening chat
	group_title.click() 

	inp_xpath='//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
	input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath))) #input box for chat msg
	for i in range(1000):
		string=f"{A[random.randint(0,ln-1)]}"
		input_box.send_keys(string + Keys.ENTER)
		time.sleep(1)


#reply to msg recived by receive_last_msg_and_reply()
def reply_msg(reply):
	try:
		reply=f"{reply}"
		inp_xpath='//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
		input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
		input_box.send_keys(reply + Keys.ENTER)
		return 
	except:
		print("reply_msg except")
		time.sleep(2)
		find_msg()
		reply=get_msg(msg[-1])
		reply_msg(reply)


#to find all messages and store in msg list
def find_msg():
	try:
		global driver
		global allmsg
		global val
		global msg
		css_selector_path="span.selectable-text.invisible-space.copyable-text"
		#print("waiting for msg")
		#wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,css_selector_path)))
		msg_got = driver.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
		#print(msg_got)
		allmsg=[]
		for message in msg_got:
			allmsg.append(message.text)
		

		if val<=2 and allmsg[-1]!=msg[-1]:
			msg=allmsg[-val:]
			val+=1
		if val>2:
			val=1
		
		return
	except:
		time.sleep(2)
		find_msg()
	    


def receive_last_msg_and_reply(targetName):
	global driver
	global val
	global msg
	targetName=f'"{targetName}"'

	x_arg = '//span[contains(@title,' + targetName + ')]'

	ser_path='//*[@id="side"]/div[1]/div/label/div/div[2]'		#searching in search box of chat
	sear_box=wait.until(EC.presence_of_element_located((By.XPATH, ser_path)))
	sear_box.send_keys(targetName[1:-1])

	time.sleep(5)
	group_title=wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))  #opening chat
	group_title.click()


	time.sleep(30)
	val=2
	msg=['**DGeetanjali..']
	find_msg()
	reply=get_msg(msg[-1]) #to store reply of msg with help of get_msg() from main.py
	reply_msg(reply)		#calling reply_msg()
	#to cheak for new message while running programm
	while 1:
		find_msg()
		if len(msg)==2:
			reply=get_msg(msg[-1])
			reply_msg(reply)
		 

 



if __name__=="__main__" :		
	print("Started..............")
	receive_last_msg_and_reply("Nameofcontact")
	send_msg("NameofContact")

