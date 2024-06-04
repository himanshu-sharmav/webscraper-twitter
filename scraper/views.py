from django.shortcuts import render
import os 
import time,logging,pymongo,datetime,json,requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from urllib.parse import quote
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def get_trending_topics():
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-gpu")

    proxy_host = "45.32.86.6"
    proxy_port = "31280"
    proxy_user = "Himan1234"
    proxy_pass = "Himan1234"

    # proxy_user_encoded = quote(proxy_user)
    # proxy_pass_encoded = quote(proxy_pass)


    # proxy_url = "http://{proxy_user_encoded}:{proxy_pass_encoded}@{proxy_host}:{proxy_port}"
    # proxy_url ="45.32.86.6:31280"
    # option.add_argument('--proxy-server=%s' % proxy_url)
    # PROXY = "45.32.86.6:31280"

    # webdriver.DesiredCapabilities.CHROME['proxy'] = {
    #     "httpProxy": PROXY,
    #     "ftpProxy": PROXY,
    #     "sslProxy": PROXY,
    #     "proxyType": "MANUAL",
    # }
    # logging.basicConfig(level=logging.DEBUG)
    # logging.debug(f"Using proxy {proxy_url}")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=option)

    top_trends = []

    try:
        driver.get("https://x.com/i/flow/login")
        time.sleep(30)


         # Enter username
        # signin_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a")))
        # signin_button.click() 
        username = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")
        username.send_keys("Himansh79043034")
        next_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div")
        next_button.click()
        time.sleep(random.uniform(2, 5))  # Random sleep to mimic human behavior

        # Enter password
        password = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password.send_keys("Himan123@")
        login_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/button/div")
        login_button.click()
        # driver.implicitly_wait(30)
        time.sleep(20)
        # confirm = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]")
        # confirm =WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]")))
        # confirm.click()
        # confirm.send_keys("himan8953201946@gmail.com")
        # next_button = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button/div")
        # next_button.click()
        driver.implicitly_wait(30)

        # Wait for the trends section to load and fetch trends
        trends = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[4]/div/section/div/div")
        top_trends = [trend.text for trend in trends[:5]]
    except Exception as e:
        logging.error(e)
    finally:
        driver.quit()

    return top_trends        

def run_script(request):

    client = pymongo.MongoClient("mongodb+srv://himan8953201946:Himan123@cluster0.bsdo2dw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client['webscraper_db']
    collection = db['trends']


    trends = get_trending_topics()
    print(trends)

    ip_service_url = "https://api.ipify.org?format=json"
    response = requests.get(ip_service_url)
    ip_address = response.json()['ip']

    now = datetime.datetime.now()
    # Split each string in the list into individual trends
    trends = [trend.split("Trending") for trend in trends]

    # Flatten the list of lists into a single list
    trends = [item for sublist in trends for item in sublist]

    # Remove leading and trailing whitespace from each trend
    trends = [trend.strip() for trend in trends]


   # Ensure there are at least 5 trends
    while len(trends) < 5:
        trends += trends
    
    result = {
        "unique_id": str(now.timestamp()),
        "trend1": trends[0],
        "trend2": trends[1],
        "trend3": trends[2],
        "trend4": trends[3],
        "trend5": trends[4],
        "datetime": now,
        "ip_address": ip_address
    }

    collection.insert_one(result)

    json_extract = json.dumps(result, default=str)
    # print(json_extract)
    return render(request, 'scraper/index.html', {
        'trends': trends,
        'datetime': now,
        'ip_address': ip_address,
        'json_extract': json_extract,
    })

def index(request):
    return render(request, 'scraper/index.html')    

# def main(request):
#     return render(request, 'scraper/main.html')