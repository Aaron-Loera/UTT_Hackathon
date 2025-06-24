from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


# create webdriver object; Firefox
url = "https://www.ratemyprofessors.com/search/professors/4171?q=*&page={}"
options = webdriver.FirefoxOptions()
options.add_argument("detach")
driver = webdriver.Firefox(options = options)


#send GET to page
driver.get(url)

while True:
    try:
        # Find the "Load more" button by its Class name and click it
        load_more_button = driver.find_element(By.CLASS_NAME, "Buttons__Button-sc-19xdot-1")
        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", load_more_button)
        time.sleep(5)
        load_more_button.click()
        time.sleep(5)
    except Exception as e:
        # If no "Load More" button is found break out of the loop
        print("No more elements to load.")
        break

# Get the updated page content after all products are loaded
html_content = driver.page_source

print(html_content)

driver.quit()