import requests
from bs4 import BeautifulSoup

web_url = "https://www.landonhotel.com"

response = requests.get(web_url)

if response.status_code == 200:
    bf_soup = BeautifulSoup(response.content, 'html.parser')
    
    parsed_text = ""
    for paragraph in bf_soup.find_all('p'):
        parsed_text += paragraph.get_text()
    with open('website_text.txt', 'w') as text_file:
        text_file.write(parsed_text)
    print("Text parsed from web page and saved successfully.")

else:
    print(f"Error encountered while parsing web page. Status code in response is: {response.status_code}")