import pandas as pd

captions = pd.read_csv("final_captions.csv")
titles = pd.read_excel("titles.xlsx")
titles.columns = ['Title', 'Link']
good = {}

for url1 in captions['Link']:
    video_url = "https://www.youtube.com/watch?v=" + url1
    for url2 in titles['Link']:
        if row 


print(titles.info())
print(titles['Title'])