import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time    

df = pd.read_csv("final_captions.csv")

# Set the path to your ChromeDriver executable
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)


video_titles = []

for row in df['Link'][:50]:
    # Construct the YouTube video URL
    video_url = "https://www.youtube.com/watch?v=" + row
    print(video_url)
    
    # Open the video URL in the ChromeDriver
    driver.get(video_url)
    
    time.sleep(1)
    # Find the video title element using its CSS selector
    title_element = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[1]/h1/yt-formatted-string")
    # Extract the video title text
    video_title = title_element.text
    
    # Add the video title to the list
    video_titles.append(video_title)
    driver.quit()

print(video_titles)
# Close the ChromeDriver instance

df_titles = pd.DataFrame({'title': video_titles})

df_titles.to_csv('video_titles.csv', index=False)