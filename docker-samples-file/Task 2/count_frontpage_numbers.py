import requests
from bs4 import BeautifulSoup

request = requests.get("http://docker.com")
soup = BeautifulSoup(request.text, 'html.parser')

count_num = 0
count_str = 0

for word in str(soup).split():
    new_word = list(word)
    for symbol in new_word:
        try:
            int(symbol)
            count_num += 1
        except ValueError:
            count_str += 1

with open('resources/file.txt', 'w') as file:
    file.write(str(count_num))
