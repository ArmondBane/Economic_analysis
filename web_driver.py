import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def get_zip_from_link(driver, link):
    driver.get(link)
    assert "Интерфакс – Сервер раскрытия информации" in driver.title

    driver.find_element_by_xpath("//a[@class='drop']/span[contains(text(), 'Отчетность' )]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//div[@id='cont_wrap']//a[contains(text(), 'Годовая' )]").click()
    time.sleep(1)
    row = driver.find_element_by_xpath("//div[@id='cont_wrap']//tr[//td[contains(text(), 'Годовой отчет' )]]")
    row.find_element_by_xpath("//a[@class='file-link']").click()
    time.sleep(3)

#'C:\Program Files (x86)\Google\chromedriver.exe'
def take_all_links(driver, date_start, date_finish, branch):
    driver.get("https://www.e-disclosure.ru/poisk-po-soobshheniyam")
    assert "Интерфакс – Сервер раскрытия информации" in driver.title

    driver.find_element_by_id("selected_type").click()
    driver.find_element_by_id("5").click()
    driver.find_element_by_xpath(
        "//input[@data-eventtypename='Раскрытие в сети Интернет годовой бухгалтерской отчетности']").click()
    driver.find_element_by_id("16").click()
    driver.find_element_by_xpath(
        "//input[@data-eventtypename='Раскрытие эмитентом сводной бухгалтерской (консолидированной финансовой) отчетности']").click()
    driver.find_element_by_xpath(
        "//input[@data-eventtypename='Выявление ошибок в ранее раскрытой бухгалтерской (финансовой) отчетности']").click()
    driver.find_element_by_xpath(
        "//input[@data-eventtypename='Раскрытие эмитентом консолидированной финансовой отчетности']").click()
    driver.find_element_by_xpath("//a[contains(text(),'Подтвердить выбор')]").click()

    WebDriverWait(driver, 3).until(EC.invisibility_of_element((By.XPATH, "//div[@id='modalLayout']")))
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='selected_period']/span/img[@alt='Выбрать']"))).click()
    driver.execute_script("$('#dateStart').datepicker('setDate', '" + date_start + "')")
    driver.execute_script("$('#dateFinish').datepicker('setDate', '" + date_finish + "')")
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@id='period']//a[contains(text(), 'Подтвердить выбор' )]"))).click()

    WebDriverWait(driver, 3).until(EC.invisibility_of_element((By.XPATH, "//div[@id='modalLayout']")))
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='selected_branch']/span/img[@alt='Выбрать']"))).click()
    driver.find_element_by_xpath("//input[@data-branch-name='" + branch + "']").click()
    driver.find_element_by_xpath("//div[@id='branch']//a[contains(text(),'Подтвердить выбор')]").click()

    WebDriverWait(driver, 3).until(EC.invisibility_of_element((By.XPATH, "//div[@id='modalLayout']")))
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Искать']"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='pageSize']"))).click()
    driver.find_element_by_xpath("//select[@id='pageSize']/option[contains(text(), 'Все' )]").click()
    driver.find_element_by_xpath("//input[@value='Искать']").click()
    time.sleep(2)

    hrefs_massiv = []
    for element in driver.find_elements_by_xpath("//table[@class='live noBorderTbl']/tbody/tr/td/a[not(@style)]"):
        hrefs_massiv.append(element.get_attribute('href'))

    return hrefs_massiv

def start_chrome_driver(driver_path):
    driver = webdriver.Chrome(driver_path)

    for link in take_all_links(driver, '01.01.2020', '05.10.2020', 'Строительство'):
        get_zip_from_link(driver, link)

    driver.quit()