from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
##########################Automation of Website###########################


driver = webdriver.Chrome()
driver.get('http://book.theautomatedtester.co.uk/')


##########Task1###############

text = 'Assert that this text is on the page'
try:
	click_button = driver.find_element_by_xpath('/html/body/div[2]/ul/li[1]/a')
	time.sleep(2)
	click_button.click()

	element = driver.find_element_by_xpath('//*[@id="divontheleft"]')
	assert element.text == text
	time.sleep(1)

	click_button1 = driver.find_element_by_xpath('/html/body/div[2]/p[4]/a')
	time.sleep(2)
	click_button1.click()
except:
	print("An Error has occured in Task1")	







##########Task2###############

try:
	click_button11 = driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/a')
	time.sleep(2)
	click_button11.click()	
	click_button3 = driver.find_element_by_xpath('//*[@id="selecttype"]').click()
	drop1 = driver.find_element_by_xpath('//*[@id="selecttype"]/option[1]')
	drop2 = driver.find_element_by_xpath('//*[@id="selecttype"]/option[2]')
	drop3 = driver.find_element_by_xpath('//*[@id="selecttype"]/option[3]')
	drop4 = driver.find_element_by_xpath('//*[@id="selecttype"]/option[4]')
	try:
		assert drop1.text == 'Selenium IDE'
		assert drop2.text == 'Selenium Core'
		assert drop3.text == 'Selenium RC'
		assert drop4.text == 'Selenium Grid'
	except:
		print("An Error has occured in manu")

except:
	print("An Error has occured in Task2 ")	







#############Task3##############

action = ActionChains(driver)
firstLevelMenu = driver.find_element_by_id('hoverOver')
action.move_to_element(firstLevelMenu).perform()
time.sleep(2)
alert_msg = driver.switch_to.alert
msg_text=alert_msg.text
try:
	assert msg_text == 'on MouseOver worked'
	time.sleep(2)
	alert_msg.accept()
	print(" Clicked on the OK Button in the Alert Message")

except:
	print("An Error has occured in Task3 ")	

#driver.close()


#######################################################################
