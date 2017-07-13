from selenium import webdriver
from time import sleep
import pickle
def find(a):
    co=0
    ans=[]
    for i in range(len(a)):
        if(a[i]=='/'):
            co+=1
            if(co==4):
                ans.append(i)
            if(co==5):
                ans.append(i)
                return ans

a=webdriver.Chrome('/Users/aadharsachdeva/Downloads/chromedriver')
link='https://github.com/jquery/jquery/commits/master'
a.get(link)
index=find(link)
file_name='commlinks_'+link[index[0]+1:index[1]]
data=open(file_name,'wb')
links=[]
while(1):
    b=a.find_elements_by_class_name('commit-title')
    for i in b:
        tmp=i.find_element_by_tag_name('a')
        links.append(tmp.get_property('href'))
    try:
        tmp=a.find_elements_by_partial_link_text("Older")
    except:
        break
    tmp=tmp[-1]
    try:
        a.get(tmp.get_property('href'))
    except:
        sleep(120)
        a.get(tmp.get_property('href'))
pickle.dump(links,data)
