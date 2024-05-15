import time, datetime, argparse
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


parser = argparse.ArgumentParser(description='Run Selenium WebDriver with specified browser.')
parser.add_argument('-b', '--browser', choices=['Edge', 'edge', 'Firefox', 'firefox', 'Chrome', 'chrome'], required=True, help='Specify the browser to use.')
parser.add_argument('-u', '--url', required=True, help='Input the YouTube Channel URL.')
args = parser.parse_args()

def main():
    if args.browser.lower() == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif args.browser.lower() == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif args.browser.lower() == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    else:
        raise ValueError("Unsupported browser")
    # Example operation
    url = args.url.lower()
    if '@' in url:
        channelid = url.split('/')[3][1:]
    else:
        channelid = url.split('/')[4]
    driver.get(url)
    time.sleep(5)
    dt=datetime.datetime.now().strftime("%Y%m%d%H%M")
    height = driver.execute_script("return document.documentElement.scrollHeight")
    lastheight = 0
    while True:
        if lastheight == height:
            break
        lastheight = height
        driver.execute_script("window.scrollTo(0, " + str(height) + ");")
        time.sleep(2)
        height = driver.execute_script("return document.documentElement.scrollHeight")
    
    user_data = driver.find_elements(By.XPATH, '//*[@id="thumbnail"]')
    for i in user_data:
        print(i.get_attribute('href'))
        link = (i.get_attribute('href'))
        f = open(channelid + '-' + dt + '.list', 'a+')
        if link is not None:
            f.write(link + '\n')
    f.close
    driver.quit()


if __name__ == '__main__':
    main()
