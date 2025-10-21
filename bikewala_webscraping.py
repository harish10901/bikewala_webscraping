import requests
import pandas
from bs4 import BeautifulSoup
import csv

response=requests.get("https://www.bikewale.com/joyebike-scooters/")
print(response)

soup=BeautifulSoup(response.content,'html.parser')
#print(soup)

names=soup.find_all('h3', class_="o-j4 o-jq o-hM o-c4")
name=[]
for i in names[0:4]:
    d=i.get_text()
    name.append(d)
print(name)

prices=soup.find_all('span',class_='o-jJ o-jr o-j3 o-kJ')
price=[]
for i in prices[0:4]:
    d=i.get_text()
    price.append(d)
print(str(price).encode('ascii','ignore').decode('ascii'))

'''emis=soup.find_all('div',class_="o-bQ o-d3 o-c6 o-cp o-dz o-cC")
emi=[]
for i in emis[0:10]:
    d=i.get_text()
    emi.append(d)
print(emi)
'''
ratings=soup.find_all('p',class_="o-iY o-cx o-jq o-d o-j o-jJ")
rating=[]
for i in ratings[0:4]:
    d=i.get_text()
    rating.append(d)
print(rating)

no_of_ratings=soup.find_all("span",class_='o-jL o-f7 o-j0 o-jc o-fE')
rate=[]
for i in no_of_ratings[0:4]:
    d=i.get_text()
    rate.append(d)
print(rate)


'''images=soup.find_all('img',class_="o-D o-hP o-iB o-iT o-G o-Q o-a0 o-aa o-h1 o-ed")
image=[]
for i in images[0:10]:
    d=i['src']
    image.append(d)
print(image)
'''
speeds=soup.find_all('span',class_="o-iZ o-jf")
speed=[]
for i in speeds[0:4]:
    d=i.get_text()
    speed.append(d)
print(speed)

'''good_things=soup.find_all('div',class_="o-j3 o-jh o-jK o-cE o-f5 o-gb zgTez9 q_6Ykz")
good=[]
for i in good_things[0:10]:
    d=i.get_text()
    good.append(d)
print(good)'''

links=soup.find_all('a',class_="o-f o-aF o-jJ o-eQ")
link=[]
for i in links[0:4]:
    d=i['href']
    link.append(d)
print(link)



data={'Names':pandas.Series(name),
      'Prices':pandas.Series(price),
      'Ratings':pandas.Series(rating),
      'No.of.ratings':pandas.Series(rate),
      'Speed':pandas.Series(speed),
      "links":pandas.Series(link)
      }

df=pandas.DataFrame(data)
df.to_csv('bikewala_data.csv')
