import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Machine_learning"
res = requests.get(url)
print(res)
soup = BeautifulSoup(res.content, "html.parser")
list_of_links = [a for a in soup.find("body").select("a") if a.text != '']
wiki_links = [link for link in  list_of_links if link.get("href", None) if link.get("href",None).find("/wiki/") !=-1 ]
def find_the_artificial_intelligence_title(res_content):
    # x=soup.select("title")[0]
    soup2 = BeautifulSoup(res_content, "html.parser")
    x = soup2.select("title")[0]
    if x.text.find("Artificial Intelligence") != -1:
        print(f"I found you .artificial intelligence link {x}")
        return True

def wiki_link_list_maker(url):
    res = requests.get(url)
    soup3 = BeautifulSoup(res.content , "html.parser")
    list_of_links = [a for a in soup3.find("body").select("a") if a.text != ""]
    wiki_links = [link for link in list_of_links if link.get("href", None) if link.get("href",None).find("/wiki/") != -1]
    return wiki_links
# print(ur:=wiki_links)
# resp = requests.get("https://en.wikipedia.org" +wiki_links[0].get("href"))
# find_the_artificial_intelligence_title(resp.content)
def link_looper(list_of_links):
    for link in list_of_links[:5]:
        resp = requests.get("https://en.wikipedia.org" + link.get("href"))
        if find_the_artificial_intelligence_title(resp.content) != True:
            url = "https://en.wikipedia.org" + link.get("href")
            print(url)
            wiki_links = wiki_link_list_maker("https://en.wikipedia.org" + link.get("href"))
            tag_lists = [i.text for i in wiki_links ]
            for idx , i in enumerate(tag_lists):
                if i == "Artificial Intelligence":
                    url_ai = "https://en.wikipedia.org" + wiki_links[idx].get("href")
                    print(f"This is the artificial Intelligence link {url_ai} in the page {url} ")



link_looper(wiki_links)

# print(list_of_links)
# print(soup.select("title")[0].text)


# if find_the_artificial_intelligence_title(res.content):
#     print(url)

