with open('teded-202405141023.list', 'r') as file:
    lines = file.readlines()

uniqueUrls = set()

for line in lines:
    url = line.strip()
    if url.startswith('https://www.youtube.com/watch?v='):
        uniqueUrls.add(url)

with open('teded.list', 'w') as file:
    for url in uniqueUrls:
        file.write(url + '\n')

print("Duplicate URLs have been removed from da clip")

formattedUrls = []

for url in uniqueUrls:
    videoId = url.replace('https://www.youtube.com/watch?v=', '')
    formattedUrls.append(videoId)

with open ('tededURLs.list', 'w') as file:
    for url in formattedUrls:
        file.write(url + '\n')