#iit kharagpur 
import requests
from selenium import webdriver
from selenium.webdriver.common import keys   # for webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browse
from bs4 import BeautifulSoup
import json
import time
import os

option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument("--window-size=1920,1080")
option.add_argument("--start-maximized")
chromedriver_path = os.getcwd()+'\\hexapod\\chromedriver.exe'
d = webdriver.Chrome(chromedriver_path,options=option)


#name
def profile(url):
    resp=requests.get(url)
    soup=BeautifulSoup(resp.content,'html.parser')
    print(url)

    def projects():
        div1=(soup.find("div",{"id":"resp-tab3"})).findAll("p")
        title,title2=[],[]
        for i in div1:
            s=str(i)
            t,t2,t1=s.find("</span>"),s.find("<b>"),""
            for j in range((t+9),t2):
                t1=t1+s[j]
            title.append(t1.strip())
            title2.append(((i.find('b')).contents)[0])
        projects.projects=[]
        
        for i in range(len(title)):
            projects.projects.append(f"{title[i]} - {title2[i]}")
            print("project found")

        if len(projects.projects)==0:
            projects.projects.append("NA")
        print("done project")
        
    def education():
        
        div= (soup.find("div",{"class":"caption_text"})).find("p")
        education.education=[]
        s,e=(str(div)).find('>')+len('>'),(str(div)).find('<br/>')-len('<br/>')
        if s and e:
            if "span" not in (str(div))[s:e]:
                edu=((str(div))[s:e]).strip()
                education.education.append(edu)
                print("edu project found")
            else:
                education.education.append("NA")
        print("edu project done")

    def patents():
        patents.patents=['NA']
    
    def Prior_affiliation():
        Prior_affiliation.Prior_affiliation=['NA']

    
    education()
    Prior_affiliation()
    projects()
    patents()
    
    author_data=[education.education,Prior_affiliation.Prior_affiliation,projects.projects,patents.patents]
    return author_data
    

def prof(name,email):
    d.get('http://www.iitkgp.ac.in/faclistbydepartment')
    time.sleep(10)
    d.find_element_by_xpath('//*[@id="txtSearchFaculty"]').click()
    d.find_element_by_xpath('//*[@id="txtSearchFaculty"]').send_keys(name)
    time.sleep(5)
    # d.find_element_by_xpath('//*[@id="txtSearchFaculty"]').click()
    d.find_element_by_xpath('//*[@id="txtSearchFaculty"]').send_keys(u'\ue007')
    time.sleep(2)
    pro_link = d.page_source
    try:
        soup2 = BeautifulSoup(pro_link,'html5lib')
        print()
        print()
        print()
        prof_url = soup2.find("td",{"class":"sorting_1"}).find("a").get("href")
        url = "http://www.iitkgp.ac.in/"+prof_url
        author_data=profile(url)
        print(author_data)
        return author_data
    except:
        author_data = [['NA'],['NA'],['NA'],['NA']]
        print(author_data)
        return author_data
    #profile("http://www.iitkgp.ac.in/"+href)

if __name__ == "__main__":
    prof("reda gandu","skj")
