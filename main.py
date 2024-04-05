#get's news from a newssite via API call

import requests

r = requests.get("https://newsapi.org/v2/everything?qInTitle=meditation"\
                 "&from=2024-2-29&to=2024-3-21&language=en&apiKey=890603a55bfa47048e4490069ebee18c")

content = r.json()

print(content["articles"],["title"])
