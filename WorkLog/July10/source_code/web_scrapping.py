import requests

from bs4 import BeautifulSoup

# url = 'https://www.bbc.com/news'
#
# response = requests.get(url)
#
# if response.status_code == 200:
#
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     headlines = soup.find_all('h2')
#
#     for headline in headlines:
#         print(headline.text)
#
# else:
#
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")

# url = "https://example.com"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
#
#
# paragraphs = soup.find_all('p')
# for p in paragraphs:
#     print(p.get_text())

def scrape_news():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []
    for item in soup.select('.titleline > a'):  # updated selector
        headlines.append(item.get_text())

    return "\n".join(f"- {title}" for title in headlines)

news = scrape_news()
print(news)
