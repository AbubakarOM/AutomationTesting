from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
# from selenium import csv

@given(u'I am on chaka website')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://test.chaka.ng/")

@given(u'I can login')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//header[@id='header']/nav[@role='navigation']/ul/li[1]/a[@href='/login']")))
    context.driver.find_element_by_xpath("//header[@id='header']/nav[@role='navigation']/ul/li[1]/a[@href='/login']").click()
    context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']//form[@class='auth-form']//input[@name='email']").send_keys("abubakar_muhammed19@yahoo.com")
    context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']//form[@class='auth-form']//input[@name='password']").send_keys("Password1@")
    context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']//form[@class='auth-form']//button[@type='submit']").click()

@given(u'I can click on account')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//header[@id='header']/nav[@role='navigation']/ul[@class='nav__dashboard--menu']//span[.='Account']")))
    context.driver.find_element_by_xpath("//header[@id='header']/nav[@role='navigation']/ul[@class='nav__dashboard--menu']//span[.='Account']").click()
    
@given(u'I can select settings from dropdown opton')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//header[@id='header']/nav[@role='navigation']/ul[@class='nav__dashboard--menu']/li[@class='dropdown']//a[.='Settings']")))
    context.driver.find_element_by_xpath("//header[@id='header']/nav[@role='navigation']/ul[@class='nav__dashboard--menu']/li[@class='dropdown']//a[.='Settings']").click()
    
@when(u'I can upload passport .jpg')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/main[@role='main']/section[@class='container']//section[@class='accounts-settings__uploads']/form[1]//input[@name='idPhotoUrl']")))
    context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']/section[@class='container']//section[@class='accounts-settings__uploads']/form[1]//input[@name='idPhotoUrl']").send_keys(r"C:\Users\admin\automation_project\CHAKA_EDIT_ACCOUNT_DETAILS\Abubakar Muhammed.jpeg")
    
@when(u'I upload address field .jpg')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/main[@role='main']/section[@class='container']//section[@class='accounts-settings__uploads']/form[1]//input[@name='idPhotoUrl']")))
    context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']/section[@class='container']//section[@class='accounts-settings__uploads']/form[1]//input[@name='idPhotoUrl']").send_keys(r"C:\Users\admin\automation_project\CHAKA_EDIT_ACCOUNT_DETAILS\Abubakar Muhammed.jpeg")
    
@then(u'I can enter my full name')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/main[@role='main']/section[@class='container']/section/div/form[1]//input[@name='disclosureName']")))
    context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']/section[@class='container']/section/div/form[1]//input[@name='disclosureName']").send_keys("Abubakar Muhammed")
    
@then(u'I can click on Submit')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/main[@role='main']/section[@class='container']/section//button[@type='submit']")))
    context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']/section[@class='container']/section//button[@type='submit']").click()
    