import pandas as pd

captions = pd.read_csv("final_captions.csv")
titles = pd.read_excel("titles.xlsx")

titles.columns = ['Title', 'Link']

matched_data = []

for i, url1 in enumerate(captions['Link']):
    video_url = "https://www.youtube.com/watch?v=" + url1
    for j, url2 in enumerate(titles['Link']):
        if video_url == url2:
            matched_data.append({
                'Title': titles['Title'][j],
                'Link': video_url,
                'Caption': captions['Caption'][i]
            })
            #print(titles['Title'][j])
            #print(captions['Caption'][i])
            #print()
matched_df = pd.DataFrame(matched_data)

matched_df.to_csv('teded.csv', index=False)

print(titles.info())