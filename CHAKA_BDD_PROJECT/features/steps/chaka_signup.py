from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from multiprocessing import context
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


@given(u'I am on chaka website')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://test.chaka.ng/")
    # context.browser.maximize_window()
    
@step(u'I can click on signup')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//header[@id='header']/nav[@role='navigation']//a[@href='/register']")))
    context.driver.find_element_by_xpath("//header[@id='header']/nav[@role='navigation']//a[@href='/register']").click()
    
@step(u'I can enter email address')
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/main[@role='main']//form[@class='auth-form']//input[@name='email']")))
    context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']//form[@class='auth-form']//input[@name='email']").send_keys("Abubakar_muhammed19@yahoo.com")
    
@step(u'I can enter password')
def step_impl(context):
   wait = WebDriverWait(context.driver, 40)
   wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/main[@role='main']//form[@class='auth-form']//input[@name='password']")))
   context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']//form[@class='auth-form']//input[@name='password']").send_keys("Password1@")
   
@step(u'I can enter confirm password')
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/main[@role='main']//form[@class='auth-form']//input[@name='confirm-password']")))
    context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']//form[@class='auth-form']//input[@name='confirm-password']").send_keys("@Password1@")
    
@step(u'I can click on signup botton')
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/main[@role='main']//form[@class='auth-form']//button[@type='submit']")))
    context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']//form[@class='auth-form']//button[@type='submit']").click()
    
@step(u'I can click on Login on chaka website')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//header[@id='header']/nav[@role='navigation']/ul/li[1]/a[@href='/login']")))
    context.driver.find_element_by_xpath("//header[@id='header']/nav[@role='navigation']/ul/li[1]/a[@href='/login']").click()
    
@step(u'I can enter my email address')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/main[@role='main']//form[@class='auth-form']//input[@name='email']")))
    context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']//form[@class='auth-form']//input[@name='email']").send_keys("Abubakar_muhammed19@yahoo.com")
   
@step(u'I can enter my password')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/main[@role='main']//form[@class='auth-form']//input[@name='password']")))
    context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']//form[@class='auth-form']//input[@name='password']").send_keys("Password1@")
   
@step(u'I can click on Login Button')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/main[@role='main']//form[@class='auth-form']//button[@type='submit']")))
    context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']//form[@class='auth-form']//button[@type='submit']").click()
    
@When(u'I click Forgot password')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/main[@role='main']//form[@class='auth-form']//a[@href='/forgot-password']")))
    context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']//form[@class='auth-form']//a[@href='/forgot-password']").click()
    
@Then(u'I enter email address')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/main[@role='main']//form[@class='auth-form']//input[@name='email']")))
    context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']//form[@class='auth-form']//input[@name='email']").send_keys("Abubakar_muhammed19@yahoo.com")
  
@step(u'I click Submit button')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/main[@role='main']//form[@class='auth-form']//button[@type='submit']")))
    context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']//form[@class='auth-form']//button[@type='submit']").click()
   