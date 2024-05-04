from selenium import webdriver
from selenium.webdriver.common.by import By


def get_prod_links(main_url):
    main_url = "https://uae.dubizzle.com/motors/used-cars/"
    driver = webdriver.Chrome()
    driver.get(main_url)

    driver.implicitly_wait(5)

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


def get_prod_brand(prod_url):
    driver = webdriver.Chrome()
    driver.get(prod_url)

    driver.implicitly_wait(2)

    category_buttons = driver.find_elements(by=By.CLASS_NAME, value='sc-dExYaf.jhJUqv')
    category_buttons = category_buttons[0].find_elements(by=By.TAG_NAME, value='a')
    brand_name = category_buttons[-2].text
    car_name = category_buttons[-1].text
    return brand_name, car_name

def get_price(prod_url):
    driver = webdriver.Chrome()
    driver.get(prod_url)

    driver.implicitly_wait(2)

    price = driver.find_elements(by=By.CLASS_NAME, value='sc-hknOHE.iwSYpa.sc-iowXnY.bpQFnZ')

    return price[0].text

def get_item_overview(prod_url):
    driver = webdriver.Chrome()
    driver.get(prod_url)

    driver.implicitly_wait(2)

    item_overview_elements = driver.find_elements(by=By.CLASS_NAME, value='sc-dtBdUo.sc-kOHTFB.sc-fbKhjd.itlMGh.glrnAB.kXcIto')[0]
    trim = item_overview_elements.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-motors_trim"]')[0].text
    model_year = item_overview_elements.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-year"]')[0].text
    km = item_overview_elements.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-kilometers"]')[0].text
    regional_specs = item_overview_elements.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-regional_specs"]')[0].text
    doors = item_overview_elements.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-doors"]')[0].text

    return trim, model_year, km, regional_specs, doors

def get_num_pictures(prod_url):
    driver = webdriver.Chrome()
    driver.get(prod_url)

    driver.implicitly_wait(2)

    num_pictures = driver.find_elements(by=By.CLASS_NAME, value='sc-hRJfrW.cTzFDM')[0].text

    return num_pictures

def get_title(prod_url):
    driver = webdriver.Chrome()
    driver.get(prod_url)

    driver.implicitly_wait(2)

    title = driver.find_elements(by=By.TAG_NAME, value='h3')[0].text

    return title

prod_url = 'https://uae.dubizzle.com/motors/used-cars/mercedes-benz/c-class/2024/1/22/mercedes-benz-c-200-premium-plus-2024-gcc--2-004---a30d8754f6624f6db43f3f812dfe119c/'
title = get_title(prod_url)

print('Ttile: ', title)