import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

URL = "https://www.register2park.com/register"
propertyName = os.environ["propertyName"]
apartmentNumber = os.environ["apartmentNumber"]
vehicleMake = os.environ["vehicleMake"]
vehicleModel = os.environ["vehicleModel"]
vehicleLicense = os.environ["vehicleLicense"]
emailAddress = os.environ["emailAddress"]

def main(arg1):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.get(URL)

    # Property search page
    search_box = driver.find_element(By.ID, "propertyName")
    search_box.send_keys(propertyName)

    nextButton = driver.find_element(By.ID, "confirmProperty")
    nextButton.click()
    print("Searching property...")
    time.sleep(1)

    # Property selection page (assumes correct property is first radio)
    propertySelector = driver.find_element(By.NAME, "property")
    propertySelector.click()

    confirmProperty = driver.find_element(By.ID, "confirmPropertySelection")
    confirmProperty.click()

    visitorParkingButton = driver.find_element(By.ID, "registrationTypeVisitor")
    visitorParkingButton.click()
    print("Selected property...")
    time.sleep(1)

    # Vehicle information page
    apartmentNumberInput = driver.find_element(By.ID, "vehicleApt")
    apartmentNumberInput.send_keys(apartmentNumber)

    vehicleMakeInput = driver.find_element(By.ID, "vehicleMake")
    vehicleMakeInput.send_keys(vehicleMake)

    vehicleModelInput = driver.find_element(By.ID, "vehicleModel")
    vehicleModelInput.send_keys(vehicleModel)

    vehicleLicenseInput = driver.find_element(By.ID, "vehicleLicensePlate")
    vehicleLicenseInput.send_keys(vehicleLicense)

    vehicleLicenseConfirmInput = driver.find_element(By.ID, "vehicleLicensePlateConfirm")
    vehicleLicenseConfirmInput.send_keys(vehicleLicense)

    vehicleConfirmButton = driver.find_element(By.ID, "vehicleInformation")
    vehicleConfirmButton.click()
    print("Submitted vehicle info...")
    time.sleep(3)

    # Final page
    emailConfirmationButton = driver.find_element(By.ID, "email-confirmation")
    emailConfirmationButton.click()
    time.sleep(1)

    emailConfirmationInput = driver.find_element(By.ID, "emailConfirmationEmailView")
    emailConfirmationInput.send_keys(emailAddress)

    sendEmailButton = driver.find_element(By.ID, "email-confirmation-send-view")
    sendEmailButton.click()
    print("Confirmation email sent...")

    driver.quit()
    return 'Completed Registration!'

