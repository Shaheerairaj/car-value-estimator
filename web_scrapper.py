from selenium import webdriver
from selenium.webdriver.common.by import By


def get_prod_links(main_url):
    main_url = "https://uae.dubizzle.com/motors/used-cars/"
    driver = webdriver.Chrome()
    driver.get(main_url)

    driver.implicitly_wait(10)

    car_links = []

    for page in range(1,6):
        driver.get(main_url+f"?page={page}")
        driver.implicitly_wait(5)

        # Get links to all products in this page
        product_wrapper = driver.find_elements(by=By.ID, value='listing-card-wrapper')
        products = product_wrapper[0].find_elements(by=By.TAG_NAME, value='a')

        # 'a' tag contains div as well as img and we need to extract div
        product_list = []
        for prod in products:
            if prod.find_element(by=By.XPATH, value='.//*').tag_name == 'div':
                product_list.append(prod)
        
        # Links to cars
        for prod in product_list:
            car_links.append(prod.get_attribute('href'))
    return car_links
