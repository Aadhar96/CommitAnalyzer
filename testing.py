import pickle
from bs4 import BeautifulSoup as buu
from urllib import request
import certifi
import re
from warnings import filterwarnings
from time import sleep
from selenium import webdriver
class file:
    def __init__(self,a):
        self.name=a[0]
        self.ad=a[1]
        self.de=a[2]
class proper:
    def __init__(self,a):
        self.commit_id=a[0]
        self.title=a[1]
        self.description=a[2]
        self.pull_id=a[3]
        self.no_user=a[4]
        self.users=a[5]
        self.date=a[6]
        self.time=a[7]
        self.no_parents=a[8]
        self.parent_id=a[9]
        self.no_files=a[10]
        self.add_=a[11]
        self.del_=a[12]
        self.files=a[13]
filterwarnings('ignore')
data=open("data_jquery","rb")
links=pickle.load(data)
data.close()
chrome=webdriver.Chrome('/Users/aadharsachdeva/Downloads/chromedriver')
links_data=[]
error=[]
lolo=5006
for link in links[5005:6006]:
    try:
        try:
            chrome.get(link)
        except:
            sleep(120)
            chrome.get(link)
        tmp=buu(chrome.page_source)
        data=[]
        data.append(tmp.find('code').text)
        data.append(tmp.find('title').text)
        try:
            data.append(tmp.find('meta',property='og:description').attrs['content'])
        except:
            data.append('')
        try:
            data.append(re.search(r'(#.*)\)',tmp.find('div',class_='commit-branches').text).group(1))
        except:
            try:
                chrome.refresh()
                tmp=buu(chrome.page_source)
                data.append(re.search(r'(#.*)\)',tmp.find('div',class_='commit-branches').text).group(1))
            except:
                data.append("NA")
                '''
                try:
                    print("LOL")
                    sleep(0.5)
                    chrome.refresh()
                    tmp=buu(chrome.page_source)
                    data.append(re.search(r'(#.*)\)',tmp.find('div',class_='commit-branches').text).group(1))
                except:
                    data.append('NA')
                '''
        a=tmp.find_all('a',class_='user-mention')
        data.append(len(a))
        data.append([i.text for i in a])
        a=tmp.find('relative-time').attrs['datetime']
        a=a.split('T')
        data.append(a[0])
        data.append(a[1][:-1])
        a=tmp.find_all('a',class_='sha')
        data.append(len(a))
        data.append([i.text for i in a])
        try:
            data.append(re.search(r'\s*(\d*)\s',tmp.find('button',class_='btn-link js-details-target').text).group(1))
            a=tmp.find('div',class_='toc-diff-stats')
            a=a.find_all('strong')
            data.append(re.search(r'(\d*)\s',a[0].text).group(1))
            data.append(re.search(r'(\d*)\s',a[1].text).group(1))
        except:
            print("3")
            a=tmp.find('div',class_='toc-diff-stats')
            a=a.find_all('strong')
            data.append(re.search(r'\s*([\d,]*)\s',a[0].text).group(1))
            data.append(re.search(r'([\d,]*)\s',a[1].text).group(1))
            data.append(re.search(r'([\d,]*)\s',a[2].text).group(1))
            print("-3")
        b=[[] for i in range(int(data[10]))]
        try:
            a=tmp.find('ol')
            a=a.find_all('a')
            k=0
            for i in a:
                if(k & 1):
                    b[k//2].append(i.text)
                k+=1
        except:
            print("2")
            error.append(link)
            for i in range(len(b)):
                b[i].append('NA')
            print("-2")
        try:
            a=tmp.find_all('span',class_="diffstat float-right")
            for i in range(int(data[10])):
                c=a[i].find_all('span')
                b[i].append(c[0].text.strip()[1:])
                b[i].append(c[1].text.strip()[1:])
        except:
            print("1")
            error.append(link)
            for i in range(len(b)):
                b[i]+=[0,0]
            print("-1")
        data.append([file(b[i]) for i in range(len(b))])
        links_data.append(proper(data))
        if(lolo%1001==0):
            f=open("djque_"+str(lolo//1001),"wb")
            pickle.dump(links_data,f)
            f.close()
            links_data=[]
            print(lolo)
        lolo+=1
    except:
        error.append(link)
        print("Skipped-",link)
    
