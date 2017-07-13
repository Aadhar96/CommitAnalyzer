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

MAX=179
a=webdriver.Chrome('/Users/aadharsachdeva/Downloads/chromedriver')
link='https://github.com/jquery/jquery/commits/master?after=3fcddd6e72e7e318c0b062e391d60867732318ae+4024'
a.get(link)
index=find(link)
file_name='commlinks_'+link[index[0]+1:index[1]]
data=open(file_name,'wb')
links=[]
for _ in range(MAX):
    b=a.find_elements_by_class_name('commit-title')
    for i in b:
        tmp=i.find_element_by_tag_name('a')
        links.append(tmp.get_property('href'))
    tmp=a.find_elements_by_partial_link_text("Older")
    tmp=tmp[-1]
    try:
        a.get(tmp.get_property('href'))
    except:
        sleep(120)
        a.get(tmp.get_property('href'))
pickle.dump(links,data)
