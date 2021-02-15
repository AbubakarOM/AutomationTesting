from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

@given(u'I am on chaka website')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://test.chaka.ng/")
    # context.browser.maximize_window()

@step(u'I can Login')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//header[@id='header']/nav[@role='navigation']/ul/li[1]/a[@href='/login']")))
    context.driver.find_element_by_xpath("//header[@id='header']/nav[@role='navigation']/ul/li[1]/a[@href='/login']").click()
    context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']//form[@class='auth-form']//input[@name='email']").send_keys("abubakar_muhammed19@yahoo.com")
    context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']//form[@class='auth-form']//input[@name='password']").send_keys("Password1@")
    context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']//form[@class='auth-form']//button[@type='submit']").click()

@step(u'I can click on fund portfolio')
def step_impl(context):
    wait = WebDriverWait(context.driver, 30)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/main[@role='main']//section[@class='dashboard__main']//button[@type='button']")))
    context.driver.find_element_by_xpath("//div[@id='app']/main[@role='main']//section[@class='dashboard__main']//button[@type='button']").click()

@step(u'I can click on fund your local wallet')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/div[2]/div[@class='modal-mask']/div[@class='modal-wrapper']//div[@class='modal-body']/div[2]/div[2]/button[1]")))
    context.driver.find_element_by_xpath("//div[@id='app']/div[2]/div[@class='modal-mask']/div[@class='modal-wrapper']//div[@class='modal-body']/div[2]/div[2]/button[1]").click()

@step(u'I can enter amount in Naira')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/div[2]/div[@class='modal-mask']/div[@class='modal-wrapper']/div[@class='modal-container modal-white']//input[@type='text']")))
    context.driver.find_element_by_xpath("//div[@id='app']/div[2]/div[@class='modal-mask']/div[@class='modal-wrapper']/div[@class='modal-container modal-white']//input[@type='text']").send_keys("1200")

@step(u'I click continue')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/div[2]/div[@class='modal-mask']/div[@class='modal-wrapper']//button[@class='btn btn-block btn__primary w-100']")))
    context.driver.find_element_by_xpath("//div[@id='app']/div[2]/div[@class='modal-mask']/div[@class='modal-wrapper']//button[@class='btn btn-block btn__primary w-100']").click()

@step(u'I can click Instant Bank Funding')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/div[2]/div[@class='modal-mask']/div[@class='modal-wrapper']//div[@class='modal-body']/div[2]/div[2]/button[1]")))
    context.driver.find_element_by_xpath("//div[@id='app']/div[2]/div[@class='modal-mask']/div[@class='modal-wrapper']//div[@class='modal-body']/div[2]/div[2]/button[1]").click()

@step(u'I can copy GTB account number')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/div[2]/div[@class='modal-mask']/div[@class='modal-wrapper']/div[@class='modal-container modal-white']//div[@class='modal__transfer--copy']")))
    context.driver.find_element_by_xpath("//div[@id='app']/div[2]/div[@class='modal-mask']/div[@class='modal-wrapper']/div[@class='modal-container modal-white']//div[@class='modal__transfer--copy']").click()

@step(u'I can click on back')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/div[2]/div[@class='modal-mask']//a[@class='modal-header__back']")))
    context.driver.find_element_by_xpath("//div[@id='app']/div[2]/div[@class='modal-mask']//a[@class='modal-header__back']").click()

@step(u'I can click on Regular Bank Transfer')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/div[2]/div[@class='modal-mask']/div[@class='modal-wrapper']//div[@class='modal-body']/div[2]/div[2]/button[2]")))
    context.driver.find_element_by_xpath("//div[@id='app']/div[2]/div[@class='modal-mask']/div[@class='modal-wrapper']//div[@class='modal-body']/div[2]/div[2]/button[2]").click()

@step(u'I can copy Zenith account number')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/div[2]/div[@class='modal-mask']/div[@class='modal-wrapper']/div[@class='modal-container modal-white']//div[@class='modal__nip--box']/div[2]/div[@class='modal__nip--copy']")))
    context.driver.find_element_by_xpath("//div[@id='app']/div[2]/div[@class='modal-mask']/div[@class='modal-wrapper']/div[@class='modal-container modal-white']//div[@class='modal__nip--box']/div[2]/div[@class='modal__nip--copy']").click()

@step(u'I can click on back')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/div[2]/div[@class='modal-mask']//a[@class='modal-header__back']")))
    context.driver.find_element_by_xpath("//div[@id='app']/div[2]/div[@class='modal-mask']//a[@class='modal-header__back']").click()

@step(u'I can click on paystack')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='app']/div[2]/div[@class='modal-mask']/div[@class='modal-wrapper']//div[@class='modal-body']/div[2]/div[2]/button[3]")))
    context.driver.find_element_by_xpath("//div[@id='app']/div[2]/div[@class='modal-mask']/div[@class='modal-wrapper']//div[@class='modal-body']/div[2]/div[2]/button[3]").click()

# @step(u'I can input amount within account range')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given I can input amount within account range')


# @then(u'I click on fund')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I click on fund')


@when(u'I input card number')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='card-form']/form//div[@class='col-12-sm']/div[@class='form-group']//input[@name='number']")))
    context.driver.find_element_by_xpath("//div[@id='card-form']/form//div[@class='col-12-sm']/div[@class='form-group']//input[@name='number']").send_keys("1111222233334444")

@step(u'I input card expiry')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='card-form']/form/div[2]//input[@name='expiry']")))
    context.driver.find_element_by_xpath("//div[@id='card-form']/form/div[2]//input[@name='expiry']").send_keys("0422")

@step(u'I input cvv on card')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='card-form']/form/div[2]//input[@name='cvv']")))
    context.driver.find_element_by_xpath("//div[@id='card-form']/form/div[2]//input[@name='cvv']").send_keys("221")

@step(u'I click on pay')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='card-form']//div[@class='pay-section']")))
    context.driver.find_element_by_xpath("//div[@id='card-form']//div[@class='pay-section']").click()