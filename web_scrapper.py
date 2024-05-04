from selenium import webdriver
from selenium.webdriver.common.by import By


def start_driver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(2)

    return driver


def get_prod_links(driver, main_url):
    # Overriding main url until testing is complete
    main_url = "https://uae.dubizzle.com/motors/used-cars/"
    driver = start_driver(main_url)

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


def get_prod_brand(driver):
    category_buttons = driver.find_elements(by=By.CLASS_NAME, value='sc-dExYaf.jhJUqv')
    category_buttons = category_buttons[0].find_elements(by=By.TAG_NAME, value='a')
    try:
        brand_name = category_buttons[-2].text
    except:
        print("\nNo entry found for Brand Name")
        brand_name = None
    try:
        car_name = category_buttons[-1].text
    except:
        print("\nNo entry found for Car Name")
        car_name = None
    return brand_name, car_name

def get_price(driver):
    try:
        price = driver.find_elements(by=By.CLASS_NAME, value='sc-hknOHE.iwSYpa.sc-iowXnY.bpQFnZ')[0].text
    except:
        print("\nNo entry found for Price")
        price = None
    return price

def get_item_overview(driver):
    try:
        item_overview_elements = driver.find_elements(by=By.CLASS_NAME, value='sc-dtBdUo.sc-kOHTFB.sc-fbKhjd.itlMGh.glrnAB.kXcIto')[0]
    except:
        print("\nNo entry found for Item Overviews")
    try:
        trim = item_overview_elements.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-motors_trim"]')[0].text
    except:
        print("\nNo entry found for Trim")
        trim = None
    try:
        model_year = item_overview_elements.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-year"]')[0].text
    except:
        print("\nNo entry found for Model Year")
        model_year = None
    try:
        km = item_overview_elements.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-kilometers"]')[0].text
    except:
        print("\nNo entry found for Kilometers")
        km = None
    try:
        regional_specs = item_overview_elements.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-regional_specs"]')[0].text
    except:
        print("\nNo entry found for Regional Specs")
        regional_specs = None
    try:
        doors = item_overview_elements.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-doors"]')[0].text
    except:
        print("\nNo entry found for Doors")
        doors = None

    return trim, model_year, km, regional_specs, doors

def get_num_pictures(driver):
    try:
        num_pictures = driver.find_elements(by=By.CLASS_NAME, value='sc-hRJfrW.cTzFDM')[0].text
    except:
        print("\nNo entry found for Number of Pictures")
        num_pictures = None

    return num_pictures

def get_title(driver):
    try:
        title = driver.find_elements(by=By.TAG_NAME, value='h3')[0].text
    except:
        print("\nNo entry found for Title")
        title = None

    return title

def get_additional_details(driver):
    try:
        add_details_items = driver.find_elements(by=By.CLASS_NAME, value='sc-Nxspf.ksOzFb')[0]
    except:
        print("\nNo entry found for Additonal Detail Items")
    try:
        body_type = add_details_items.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-body_type"]')[0].text
    except:
        print("\nNo entry found for Body Type")
        body_type = None
    try:
        fuel_type = add_details_items.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-fuel_type"]')[0].text
    except:
        print("\nNo entry found for Fuel Type")
        fuel_type = None
    try:
        seller_type = add_details_items.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-seller_type"]')[0].text
    except:
        print("\nNo entry found for Seller Type")
        seller_type = None
    try:
        seating_capacity = add_details_items.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-seating_capacity"]')[0].text
    except:
        print("\nNo entry found for Seating Capacity")
        seating_capacity = None
    try:
        trans_type = add_details_items.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-transmission_type"]')[0].text
    except:
        print("\nNo entry found for Transmission Type")
        trans_type = None
    try:
        engine_capacity = add_details_items.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-engine_capacity_cc"]')[0].text
    except:
        print("\nNo entry found for Engine Capacity")
        engine_capacity = None
    try:
        extras = add_details_items.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-auto_options_recommended"]')[0].text
    except:
        print("\nNo entry found for Extras")
        extras = None
    try:
        tech_features = add_details_items.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-auto_options"]')[0].text
    except:
        print("\nNo entry found for Technical Features")
        tech_features = None
    try:
        horsepower = add_details_items.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-horsepower"]')[0].text
    except:
        print("\nNo entry found for Horsepower")
        horsepower = None
    try:
        cylinders = add_details_items.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-no_of_cylinders"]')[0].text
    except:
        print("\nNo entry found for Cylinders")
        cylinders = None
    try:
        warranty = add_details_items.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-warranty"]')[0].text
    except:
        print("\nNo entry found for Warranty")
        warranty = None
    try:
        ext_color = add_details_items.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-exterior_color"]')[0].text
    except:
        print("\nNo entry found for External Color")
        ext_color = None
    try:
        target_market = add_details_items.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-target_market"]')[0].text
    except:
        print("\nNo entry found for Target Market")
        target_market = None
    try:
        steering_side = add_details_items.find_elements(by=By.CSS_SELECTOR, value='[data-ui-id="details-value-steering_side"]')[0].text
    except:
        print("\nNo entry found for Steering Side")
        steering_side = None

    return body_type, fuel_type, seller_type, seating_capacity, trans_type, engine_capacity, extras, tech_features, horsepower, cylinders, warranty, ext_color, target_market, steering_side




urls = ['https://uae.dubizzle.com/motors/used-cars/mercedes-benz/c-class/2024/1/22/mercedes-benz-c-200-premium-plus-2024-gcc--2-004---a30d8754f6624f6db43f3f812dfe119c/',
        'https://uae.dubizzle.com/motors/used-cars/lamborghini/huracan/2024/5/4/lamborghini-huracan-evo-spyder-2-532---fa589071c25343718cf10a2043d8507e/',
        'https://uae.dubizzle.com/motors/used-cars/mercedes-benz/vito/2024/4/24/body-kit-maybach-2018-model-gcc-specs-unde-2-113---5c0fc80d488744438e2c5b8724dcdadd/',
        'https://uae.dubizzle.com/motors/used-cars/land-rover/defender/2024/5/4/2024-defender-110-hse-30l-turbocharged-al--2-542---0c29098029fa4d0db16282bd6efff85e/'
]


# Individual Product Logic

for url in urls:

    driver = start_driver(url)
    brand_name, car_name = get_prod_brand(driver)
    price = get_price(driver)
    trim, model_year, km, regional_specs, doors = get_item_overview(driver)
    num_pictures = get_num_pictures(driver)
    title = get_title(driver)
    body_type, fuel_type, seller_type, seating_capacity, trans_type, engine_capacity, extras, tech_features, horsepower, cylinders, warranty, ext_color, target_market, steering_side = get_additional_details(driver)


    print('Car ID: ',url.split('---')[1][:-1])
    print('Brand Name: ', brand_name)
    print('Car Name: ', car_name)
    print('Title: ', title)
    print('Price: ',price)
    print('Trim: ', trim)
    print('Model Year: ', model_year)
    print('Kilometers: ', km)
    print('Regional Specs: ', regional_specs)
    print('Doors: ', doors)
    print('No. of Pictures: ', num_pictures)
    print('Body Type: ', body_type)
    print('Fuel Type: ', fuel_type)
    print('Seller Type: ', seller_type)
    print('Seating Type: ', seating_capacity)
    print('Transmission Type: ', trans_type)
    print('Engine Capacity: ', engine_capacity)
    print('Extras: ', extras)
    print('Technical Features: ', tech_features)
    print('Horsepower: ', horsepower)
    print('Cylinders: ', cylinders)
    print('Warranty: ', warranty)
    print('Exterior Color: ', ext_color)
    print('Target Market: ', target_market)
    print('Steering Side: ', steering_side)