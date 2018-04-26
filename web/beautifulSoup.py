import requests, bs4
response = requests.get('http://songshuiyang.com')
print(response.text)
soup = bs4.BeautifulSoup(response.text)

element = soup.select('#lay-nav-1')
print(str(type(element)))
print('输出元素: ' + str(element[0]))
print('输出text: ' + str(element[0].getText()))

p_element = soup.select('p')
print('所有的p标记' + str(p_element))