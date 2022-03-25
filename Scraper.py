import requests
import csv
import lxml
from bs4 import BeautifulSoup
import datetime

time = datetime.datetime.today()
time = str(time)
print(time)
def get_date_list(numdays: int):
    date_list = []
    a = datetime.datetime.today()
    for x in range (0, numdays):
        date_list.append(str(a - datetime.timedelta(days = x)))

    for i in range(len(date_list)):
        buff = date_list[i][:10]
        date_list[i] = buff.replace('-','')
    return date_list

headers = {
    'accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.810 Yowser/2.5 Safari/537.36'
}

def get_url(s:str):
    url = f'https://ria.ru/{s}/'
    return url

with open(f'./titles.csv','w', newline = '') as tf:
    k = 0 
    for date in get_date_list(1830):
        req = requests.get(get_url(date), headers=headers)
        src = req.text
        soup = BeautifulSoup(src, 'lxml')
        all_titles = soup.find_all(class_ = 'list-item__title')
        writer = csv.writer(tf, delimiter = ';')
        for item in all_titles:
            title = item.text
            current_date = datetime.datetime.strptime(f'{date}', '%Y%m%d')
            writer.writerow([f'{current_date}', f'{title}'])
        k+=1
        print(k)
    
                
                

        
