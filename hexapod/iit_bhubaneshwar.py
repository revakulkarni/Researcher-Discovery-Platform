#iit kanpur
import requests
from bs4 import BeautifulSoup

def profile(url):
    resp=requests.get(url)
    soup=BeautifulSoup(resp.content,'html.parser')
    print(url)

    def education():
        div=(soup.find_all("div",{"class":"col-md-12"}))
        # print(div[1])
        # print(div[1].find_all("td"))
        education.edu = []
        edu1 = div[1].find_all("td")
        for i in range(0,len(edu1),4):
            education.edujoin = edu1[i].contents[0]+" "+edu1[i+1].contents[0]+" "+edu1[i+2].contents[0]+" "+edu1[i+3].contents[0]+"."
            education.edu.append(education.edujoin.strip())
            print(education.edujoin)
        


    def patents():
        patents.patents=['NA']

    def projects():
        projects.projects=['NA']

    def Prior_affiliation():
        Prior_affiliation.Prior_affiliation=['NA']

    patents()
    Prior_affiliation()
    projects()
    education()

    author_data=[education.edu,Prior_affiliation.Prior_affiliation,projects.projects,patents.patents]
    return author_data


def prof(name,email):
    url="https://www.iitbbs.ac.in/faculty-members.php"
    resp=requests.get(url)
    soup=BeautifulSoup(resp.content,'html5lib')
    print(url)
    div=(soup.find("div",{"class":"row cols-wrapper"})).find_all("tbody")
    nam,hrf=[],[]
    for i in div:
        n=(((((i.find("td")).find("a")).contents)[0])[2:]).strip()
        h=(((i.find("td")).find("a"))).get('href')
        nam.append(str(n))
        hrf.append(str(h))
    print(nam,hrf)
    flag=0
    for i in range(len(nam)):
        if name in nam[i]:
            author_data=profile(hrf[i])
            return author_data
            flag=1

    if flag==0:
        author_data=[['NA'],['NA'],['NA'],['NA']]
        return author_data


if __name__== '__main__':
    author_data=prof('Dr. Aneesh M','arshukla@iitk.ac.in')
    print('***********************************')
    print(author_data)















