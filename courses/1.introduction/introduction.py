import requests

session = requests.session()

parameters = (
    ('anchor', '0'),
    ('count', '36'),
    ('filter', ['marketplace(FR)', 'language(fr)', 'upcoming(true)', 'channelId(010794e5-35fe-4e32-aaff-cd2c74f89d61)', 'exclusiveAccess(true,false)']),
    ('sort', 'effectiveStartSellDateAsc'),
    ('fields', 'active,id,lastFetchTime,productInfo,publishedContent.nodes,publishedContent.properties.coverCard,publishedContent.properties.productCard,publishedContent.properties.products,publishedContent.properties.publish.collections,publishedContent.properties.relatedThreads,publishedContent.properties.seo,publishedContent.properties.threadType,publishedContent.properties.custom,publishedContent.properties.title'),
)

url = "https://api.nike.com/product_feed/threads/v2/"

response = session.get(url, params=parameters)

req_status = response.status_code

if req_status == 200:
	print("Request successfull")
else:
	print(f"Request failed with status code: {req_status}")

import json 

sorties = json.loads(response.text)

for produit in sorties["objects"]:
	description = produit["productInfo"][0]["productContent"]
	titre = description["title"]
	couleur = description["colorDescription"]
	sku = produit["productInfo"][0]["merchProduct"]["styleColor"]
	print(f"{titre}, {couleur}, {sku}")