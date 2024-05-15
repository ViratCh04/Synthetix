from youtube_transcript_api import YouTubeTranscriptApi, _errors
import re
import pandas as pd

with open('tededURLs.list', 'r') as file:
    links = file.readlines()

captions = {}
skip = [256, 298, 314, 406, 461, 497, 534, 583, 850, 937, 938, 945, 985, 1120]

for i, link in enumerate(links):
    print(i)

    link = link.strip()

    try:
        dic = YouTubeTranscriptApi.get_transcript(link)
    except (_errors.NoTranscriptFound, _errors.TranscriptsDisabled) as e:
        print(f"Caught error: {e}")
        continue
    
    k = "text"
    dic = [{k: v["text"]} for v in dic]
    concatenated_text = " ".join([d["text"] for d in dic])
    caption = concatenated_text.replace("\n", " ")
    caption = re.sub(r'\\(?=\')', '', caption)
    caption = caption.replace("[Applause]", "")
    caption = caption.replace("[Music]", "")

    #print(caption)
    #print()
    captions[link] = str(caption)
    

#print(captions)

df = pd.DataFrame(list(captions.items()), columns=['Link', 'Caption'])
# Save DataFrame to a CSV file
df['Caption'] = df['Caption'].astype('string')
df['Link'] = df['Link'].astype('string')
print(df.info())
df.to_csv('captions2.csv', index=False)