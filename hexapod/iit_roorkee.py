#iit roorkee

# Publications pending!!

import requests
from bs4 import BeautifulSoup

def profile(url):
    resp=requests.get(url)
    soup=BeautifulSoup(resp.content,'html.parser')
    print(url)



    #Education
    def education():
        div1=(soup.find_all("details",{"class":"faculty_accordions"}))
        for i in div1:
            if ((i.find("summary",{"class":"title pageTitle2"}).contents)[0]).strip() =="Educational Details":
                edu=i
                break
        td = i.find_all("td")
        div1=(soup.find_all("td"))
        education.edu=[]
        print("Education")
        for i in range (0,len(td),4):
            # print(td[i+1])
            education.edu.append(td[i].contents[0]+" , "+td[i+1].contents[0]+" , "+td[i+2].contents[0]+" , "+td[i+3].contents[0])
        if len(education.edu)==0:
            education.edu.append("NA")


    # Prior Affiliations       
    def Prior_affiliation():
        div1=(soup.find_all("details",{"class":"faculty_accordions"}))
        for i in div1:
            if ((i.find("summary",{"class":"title pageTitle2"}).contents)[0]).strip() =="Professional Background":
                edu=i
                print(i)
                break
        td = i.find_all("td")
        div1=(soup.find_all("td"))
        Prior_affiliation.Prior_affiliation=[]
        print("Prior affiliation")
        for i in range (0,len(td),4):
            if i<len(td) and (i+1)<len(td) and (i+2)<len(td) and (i+3)<len(td) and td[i].contents and td[i+1].contents and td[i+2].contents and td[i+3].contents:
                Prior_affiliation.Prior_affiliation.append((td[i].contents)[0]+" , "+(td[i+1].contents)[0]+" , "+(td[i+2].contents)[0]+" , "+(td[i+3].contents)[0])
        if len(Prior_affiliation.Prior_affiliation)==0:
            Prior_affiliation.Prior_affiliation.append("NA")


    def projects():
        div1=(soup.find_all("details",{"class":"faculty_accordions"}))
        for i in div1:
            if ((i.find("summary",{"class":"title pageTitle2"}).contents)[0]).strip() =="Sponsored Research Projects":
                edu=i
                print(i)
                break
        td = i.find_all("td")
        div1=(soup.find_all("td"))
        projects.projects=[]
        print("Projects")
        for i in range (0,len(td),4):
            projects.projects.append(td[i].contents[0]+" , "+td[i+1].contents[0]+" , "+td[i+2].contents[0]+" , "+td[i+3].contents[0])
            #print(td[i])
        if len(projects.projects)==0:
            projects.projects.append("NA")
            

    def patents():
        patents.patents=['NA']

    education()
    Prior_affiliation()
    projects()
    patents()

            
    author_data=[education.edu,Prior_affiliation.Prior_affiliation,projects.projects,patents.patents]
    return author_data


def prof(name,email):
    flag=0
    name1,href1=[],[]
    urls=['https://ar.iitr.ac.in/departments/AR/pages/People+Faculty_List.html','https://ase.iitr.ac.in/departments/ASE/pages/People+Faculty+Faculty_Profiles.html','https://bt.iitr.ac.in/departments/BT/pages/People+Faculty_List.html','https://ch.iitr.ac.in/departments/CH/pages/People+Faculty.html','https://cy.iitr.ac.in/departments/CY/pages/People+Faculty_List.html','https://cse.iitr.ac.in/departments/CSE/pages/People+Faculty_List.html','http://dod.iitr.ac.in/departments/DOD/pages/Faculty_List.html','https://eq.iitr.ac.in/pages/people_deq+faculty.html','https://es.iitr.ac.in/departments/ES/pages/People+Faculty_List.html','https://ee.iitr.ac.in/departments/EE/pages/Faculty_List.html','https://hy.iitr.ac.in/departments/HY/pages/People+Faculty_List.html','https://hre.iitr.ac.in/departments/HRE/pages/People+Faculty_List.html','https://ms.iitr.ac.in/departments/DM/pages/People+Faculty.html','https://ma.iitr.ac.in/departments/MA/pages/People+Faculty_List.html','https://www.iitr.ac.in/departments/ME/pages/People+Faculty+Faculty_List.html','https://mt.iitr.ac.in/departments/MT/pages/People+Faculty_List.html','https://dpt.iitr.ac.in/departments/DPT/pages/People+Faculty_List.html','https://ppe.iitr.ac.in/departments/PPE/pages/People+Faculty+Faculty_Profiles.html','https://ph.iitr.ac.in/departments/PH/pages/People+Faculty_List.html','https://wr.iitr.ac.in/departments/WR/pages/People+Faculty_List.html']
    for i in urls:
        resp=requests.get(i)
        soup=BeautifulSoup(resp.content,'html.parser')
        lst=soup.find_all("div",{"class":"list-wrapper"})
        for j in lst:
            name2=((((j.find("div",{"class":'detail'})).find("div")).find('a')).contents)[0]
            href2=((((j.find("div",{"class":'detail'})).find("div")).find('a')).get('href'))
            name1.append(name2)
            href1.append("https://ar.iitr.ac.in/"+str(href2))

    for i in range(len(name1)):
        if name in name1[i]:
            author_data=profile(href1[i])
            return author_data
            flag=1

    if flag==0:
        author_data=[['NA'],['NA'],['NA'],['NA']]
        return author_data
    #author_data=profile(url)
    #return author_data

if __name__== '__main__':
    prof('','')