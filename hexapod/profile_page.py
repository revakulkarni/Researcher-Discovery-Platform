from bs4 import BeautifulSoup
import requests

def author_profile(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html5lib')

    def names(soup1):
        #name
        div=soup1.find("div",{"id":"gsc_prf_in"})
        if div:
            name=str((div.contents)[0])
        else:
            name=""
        return name.title()

    def affiliation(soup1):
        div1=soup1.find("div",{"id":"gsc_prf_i"})
        div=div1.find("div",{"class":"gsc_prf_il"})
        if div.find('a'):
            affi=str(((div.find('a')).contents)[0])
        else:
            affi=str((div.contents)[0])
        return affi

    def email(soup1):
        div=soup1.find("div",{"id":"gsc_prf_ivh"})
        email=str((div.contents)[0])
        return email

    def resInt(soup1):
        resInt=[]
        div=soup1.find("div",{"id":"gsc_prf_int"})
        for i in (div.find_all('a')):
            resInt.append((i.contents)[0])
        return resInt

    def publication(soup1):
        pub,publinks=[],[]
        div=soup1.find("tbody",{"id":"gsc_a_b"})
        for i in (div.find_all("tr",{"class":"gsc_a_tr"})):
            pub.append((((i.find("td",{"class":"gsc_a_t"})).find('a')).contents)[0])
            publinks.append("https://scholar.google.com/"+str(((i.find("td",{"class":"gsc_a_t"})).find('a')).get('href')))
        return pub,publinks

    pub,publink=publication(soup)
    author_profile.authorprofiledata = {
        'name':names(soup),
        "affiliation":affiliation(soup),
        'ri':resInt(soup),
        'authedu':['NA'],
        'pa': ['NA'],
        'authpatents':['NA'],
        'authprojects':['NA'],
        'authpub': pub,
        'authpublink': publink
        
    }
    iit=['iitkgp.ac.in','iitk.ac.in','iitr.ernet.in','iitr.ac.in','iitgn.ac.in','iitp.ac.in','iitbbs.ac.in']
    for j in iit:
        if j in email(soup):
            if 'iitr.ac.in' in email(soup) or 'iitr.ernet.in' in email(soup):
                import hexapod.iit_roorkee as iitr
                author_data=iitr.prof(names(soup),email(soup))
                author_profile.authorprofiledata['authedu']=author_data[0]
                author_profile.authorprofiledata['pa']=author_data[1]
                author_profile.authorprofiledata['authprojects']=author_data[2]
                author_profile.authorprofiledata['authpatents']=author_data[3]
                break
            elif 'iitkgp.ac.in' in email(soup):
                import hexapod.iit_kharagpur as iitkgp
                author_data=iitkgp.prof(names(soup),email(soup))
                author_profile.authorprofiledata['authedu']=author_data[0]
                author_profile.authorprofiledata['pa']=author_data[1]
                author_profile.authorprofiledata['authprojects']=author_data[2]
                author_profile.authorprofiledata['authpatents']=author_data[3]
                break
            elif 'iitk.ac.in' in email(soup):
                import hexapod.iit_kanpur as iitk
                author_data=iitk.prof(names(soup),email(soup))
                author_profile.authorprofiledata['authedu']=author_data[0]
                author_profile.authorprofiledata['pa']=author_data[1]
                author_profile.authorprofiledata['authprojects']=author_data[2]
                author_profile.authorprofiledata['authpatents']=author_data[3]
                break
            elif j=='iitbbs.ac.in':
                import hexapod.iit_bhubaneshwar as iitbbs
                author_data=iitbbs.prof(names(soup),email(soup))
                author_profile.authorprofiledata['authedu']=author_data[0]
                author_profile.authorprofiledata['pa']=author_data[1]
                author_profile.authorprofiledata['authprojects']=author_data[2]
                author_profile.authorprofiledata['authpatents']=author_data[3]
                break
            else:
                author_profile.authorprofiledata['authedu']=["NA"]
                author_profile.authorprofiledata['pa']=["NA"]
                author_profile.authorprofiledata['authprojects']=["NA"]
                author_profile.authorprofiledata['authpatents']=["NA"]

    print("profilePage.py")
    print(author_profile.authorprofiledata)

def download():
    from hexapod.pkg.fpdf import FPDF
    pdf = FPDF()   

    # Add a page
    pdf.add_page()

        # set style and size of font 
        # that you want in the pdf

        # pdf.image("C:\\Users\\V S Jain\\Desktop\\research pro\\images\\hexapods.png", x = 60, y = 5, w = 20, h =20, type = '', link = '')
    pdf.set_font("Arial", size = 20,style= "B")
    pdf.cell(200, 10, txt = "Researcher Profile", ln = 1, align = 'C')
    pdf.set_font("Arial", size = 15,style="B")
        
    pdf.cell(200, 10, txt = "Name:"+str(author_profile.authorprofiledata['name']), ln = 1, align = 'L')
    pdf.set_font("Arial", size = 15,style="B")
    pdf.cell(200, 10, txt = "Affiliation:", ln = 1, align = 'L')
    pdf.set_font("Arial", size = 15)
    pdf.cell(180, 10, txt = str(author_profile.authorprofiledata['affiliation']), ln=1,align = 'L')
    pdf.set_font("Arial", size = 15,style="B")
    pdf.cell(200, 10, txt = "Prior Affiliations:", ln = 1, align = 'L')  #list
    pdf.set_font("Arial", size = 15)
    j=1
    for i in author_profile.authorprofiledata['pa']:
        pdf.multi_cell(180, 10, txt = str(i), align = 'L')
        j+=1
    pdf.set_font("Arial", size = 15,style="B")
    pdf.cell(50, 10, txt = "Research Interests:", ln = 1, align = 'L')
    pdf.set_font("Arial", size = 15)
    pdf.multi_cell(180, 10, txt = str(author_profile.authorprofiledata['ri']), align = 'L')
        
    pdf.set_font("Arial", size = 15,style="B")
    pdf.cell(200, 10, txt = "Education:", ln = 1, align = 'L')
    pdf.set_font("Arial", size = 15)
    j=1
    for i in author_profile.authorprofiledata['authedu']:
        pdf.multi_cell(180, 10, txt = str(i), align = 'L')
        j+=1
    pdf.set_font("Arial", size = 15,style="B")
    pdf.cell(200, 10, txt = "Patents:", ln = 1, align = 'L')
    pdf.set_font("Arial", size = 15)
    j=1
    for i in author_profile.authorprofiledata['authpatents']:
        pdf.multi_cell(180, 10, txt = str(j)+"."+str(i), align = 'L')
        j+=1
    pdf.set_font("Arial", size = 15,style="B")
    pdf.cell(200, 10, txt = "Projects:", ln = 1, align = 'L')
    pdf.set_font("Arial", size = 15)
    j=1
    for i in author_profile.authorprofiledata['authprojects']:
        pdf.multi_cell(180, 10, txt = str(j)+"."+str(i),  align = 'L')
        j+=1
    pdf.set_font("Arial", size = 15,style="B")
    pdf.cell(200, 10, txt = "Publications:", ln = 1, align = 'L')
    pdf.set_font("Arial", size = 15)
    j=1
    for i in author_profile.authorprofiledata['authpub']:
        pdf.multi_cell(180, 10, txt = str(j)+"."+str(i), align = 'FJ')
        j+=1
    
        # save the pdf with name .pdf
    filename = str(author_profile.authorprofiledata['name'])
    pdf.output(name=f'{filename}.pdf')  
    print("done")

if __name__ == '__main__':
    author_profile('https://scholar.google.com/citations?hl=en&user=vXB9eOwAAAAJ')

