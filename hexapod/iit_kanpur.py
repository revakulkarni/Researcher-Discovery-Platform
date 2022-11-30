#iit kanpur
import requests
from bs4 import BeautifulSoup

def profile(url):
    resp=requests.get(url)
    soup=BeautifulSoup(resp.content,'html.parser')
    print(url)

    def education():
        education.edu=[]
        try:
            div=(soup.find("div",{"class":"fac-profile"})).find("td",{"rowspan":"2"})
            li=((div.find("div",{"class":"tabletext"})).find('ul')).find_all('li')
            print(li)
            for i in li:
                education.edu.append((i.contents)[0])
        except:
            education.edu.append("NA")
        print("----------------------------")
        print("----------------------------")
        print(education.edu)
        print("----------------------------")
        print("----------------------------")


    def patents():
        patents.patents=['NA']

    def projects():
        projects.projects=['NA']

    def Prior_affiliation():
        Prior_affiliation.Prior_affiliation=['NA']

    education()
    patents()
    Prior_affiliation()
    projects()

    author_data=[education.edu,Prior_affiliation.Prior_affiliation,projects.projects,patents.patents]
    return author_data


def prof(name1,mail):
    url="https://www.iitk.ac.in/new/iitk-faculty"
    resp=requests.get(url)
    soup=BeautifulSoup(resp.content,'html5lib')
    soup1=soup.find_all("div",{"class":"jwts_toggleContent"})
    href,name,emails=[],[],[]
    for i in soup1:
        div1= i.find_all("p")
        for j in div1:
            try:
                div=j.find('a').get("href")
                if div!='#':
                    name.append(str(((j.find('a')).contents)[0]))
                    href.append("https://www.iitk.ac.in"+div)
                    email=(j.find('a')).next_sibling
                    emails.append((str(email[(str(email).find('('))+1:str(email).find('[AT]'):])+"@iitk.ac.in").strip())
            except:
                div="not found"

    print(name)
    print("------------------------------------")
    print(emails)
    print("-----------------------------------------")
    print(href)
    flag=0
    for i in range(len(emails)):
        if name1 in name[i]:
            author_data=profile(href[i])
            return author_data
            flag=1

    if flag==0:
        author_data=[['NA'],['NA'],['NA'],['NA']]
        return author_data

    print('*****************************')

if __name__== '__main__':
    author_data=prof('Arun K. Shukla','arshukla@iitk.ac.in')
    print('***********************************')
    print(author_data)















