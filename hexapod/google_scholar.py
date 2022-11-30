from bs4 import BeautifulSoup
import requests

def query(ui):
    ui1=(str(ui).strip()).split()
    url="https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q='"
    for i in range(len(ui1)):
        if i<(len(ui1)-1):
            url=url+ui1[i]+"+"
        else:
            url=url+ui1[i]+"'+nit+OR+iit+OR+iiit+OR+csir&btnG="
    print(url)

    response=requests.get(url)
    soup1=BeautifulSoup(response.content,'html5lib')
    all_pages=[]
    response=requests.get(url)
    soup1=BeautifulSoup(response.content,'html5lib')
    if soup1.find("div",{"id":"gs_n"}):
        all_links=(soup1.find("div",{"id":"gs_n"})).find_all("td")
        if len(all_links)>8:
            for i in range(1,8):
                if all_links[i].find("a"):
                    all_pages.append("https://scholar.google.com"+str((all_links[i].find("a")).get('href')))
        elif len(all_links)<2:
            all_pages.append(url)
        else:
            for i in range(1,(len(all_links))-1):
                if all_links[i].find("a"):
                    all_pages.append("https://scholar.google.com"+str((all_links[i].find("a")).get('href')))
    else:
        all_pages.append(url)
    def geturls():
        authorNames,authorlinks=[],[]
        for k in all_pages:
            resp=requests.get(k)
            soup=BeautifulSoup(resp.content,'html5lib')
            for item in soup.select('[data-lid]'): 
                try:  
                    anchTags=item.select('.gs_a')[0].find_all("a")
                    for i in anchTags:
                        authorNames.append(i.contents[0])
                        authorlinks.append("https://scholar.google.com"+str(i.get('href')))
                except Exception as e: 
                    #raise e print('')
                    pass

        #authNames=list(set(authorNames))
        setlinks=set(authorlinks)
        authlinks=list(setlinks)
        geturls.authlinks=list(setlinks)
        #print(authNames)
        print("---------------------------------------")
        print(geturls.authlinks)
        return authlinks

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

    def authdetails():
        authdetails.auth_names,authdetails.auth_affi,authdetails.auth_emails,authdetails.auth_links=[],[],[],[]
        iit=["mnnit.ac.in","manit.ac.in","vnit.ac.in","ce.nitdgp.ac.in","nith.ac.in","mnit.ac.in","nitj.ac.in","nitjsr.ac.in","nitkkr.ac.in","nitc.ac.in","nitrkl.ac.in","hum.nits.ac.in"," nitk.edu.in","nitw.ac.in","svnit.ac.in","nitt.edu","nitsri.net","nitp.ac.in","nitrr.ac.in","nita.ac.in","nitap.ac.in","nitdelhi.ac.in","nitgoa.ac.in","nitmanipur.ac.in","nitmanipur.ac.in","nitmz.ac.in","nitnagaland.ac.in","nitpy.ac.in","nitsikkim.ac.in","nituk.ac.in","nitandhra.ac.in","iiitm.ac.in","iiita.ac.in","iitdmj.ac.in","iiitdm.ac.in","iiits.in","iiitg.ac.in","iiitvadodara.ac.in","iiitkota.ac.in","iiitt.ac.in","iiitu.ac.in","nitkkr.ac.in","iiitkalyani.ac.in","iiitl.ac.in","iiitdwd.ac.in","iiitk.ac.in","iiitmanipur.ac.in","iiitn.ac.in","iiitp.ac.in","iiitranchi.ac.in","iiitsurat.ac.in","iiitbhopal.ac.in","iiitbh.ac.in","nita.ac.in","iith.ac.in","iisc.ac.in","iitbhilai.ac.in","iitbbs.ac.in","iitb.ac.in","iitd.ac.in","iitism.ac.in","iitgn.ac.in","iitg.ac.in","iith.ac.in","iiti.ac.in","iitj.ac.in","iitk.ac.in","iitkgp.ac.in","iitm.ac.in","iitmandi.ac.in","iitpkd.ac.in","iitp.ac.in","iitr.ac.in","iitrpr.ac.in","iittp.ac.in","iitbhu.ac.in","iitjammu.ac.in","iitgoa.ac.in","ampri.res.in","cbri.res.in","ccmb.res.in","cimap.res.in","cecri.res.in","ceeri.res.in","cftri.res.in","cgcri.res.in","cdri.res.in","cimfr.res.in","csircmc.res.in","cmeri.res.in","csio.res.in","csmcri.res.in","igib.res.in","ihbt.res.in","iicb.res.in","iict.res.in","iiim.res.in","iip.res.in","immt.res.in.","imtech.res.in","iitr.res.in","nal.res.in","nbri.res.in","ncl.res.in","neeri.res.in","neist.res.in","ngri.res.in","niist.res.in","niot.res.in","niscair.res.in","nmlindia.org","nplindia.org","serc.res.in","urdip.res.in"]

        for i in geturls():
            url=str(i)
            resp=requests.get(url)
            soup1=BeautifulSoup(resp.content,'html5lib')
            for j in iit:
                if j in email(soup1) and email(soup1) not in authdetails.auth_emails:
                    nam=names(soup1)
                    authdetails.auth_names.append(nam)
                    authdetails.auth_affi.append(affiliation(soup1))
                    authdetails.auth_emails.append(email(soup1))
                    authdetails.auth_links.append(i)
                    print(nam)

    query.list=[]
    flag=0
    authdetails()
    iit=["mnnit.ac.in","manit.ac.in","vnit.ac.in","ce.nitdgp.ac.in","nith.ac.in","mnit.ac.in","nitj.ac.in","nitjsr.ac.in","nitkkr.ac.in","nitc.ac.in","nitrkl.ac.in","hum.nits.ac.in"," nitk.edu.in","nitw.ac.in","svnit.ac.in","nitt.edu","nitsri.net","nitp.ac.in","nitrr.ac.in","nita.ac.in","nitap.ac.in","nitdelhi.ac.in","nitgoa.ac.in","nitmanipur.ac.in","nitmanipur.ac.in","nitmz.ac.in","nitnagaland.ac.in","nitpy.ac.in","nitsikkim.ac.in","nituk.ac.in","nitandhra.ac.in","iiitm.ac.in","iiita.ac.in","iitdmj.ac.in","iiitdm.ac.in","iiits.in","iiitg.ac.in","iiitvadodara.ac.in","iiitkota.ac.in","iiitt.ac.in","iiitu.ac.in","nitkkr.ac.in","iiitkalyani.ac.in","iiitl.ac.in","iiitdwd.ac.in","iiitk.ac.in","iiitmanipur.ac.in","iiitn.ac.in","iiitp.ac.in","iiitranchi.ac.in","iiitsurat.ac.in","iiitbhopal.ac.in","iiitbh.ac.in","nita.ac.in","iith.ac.in","iisc.ac.in","iitbhilai.ac.in","iitbbs.ac.in","iitb.ac.in","iitd.ac.in","iitism.ac.in","iitgn.ac.in","iitg.ac.in","iith.ac.in","iiti.ac.in","iitj.ac.in","iitk.ac.in","iitkgp.ac.in","iitm.ac.in","iitmandi.ac.in","iitpkd.ac.in","iitp.ac.in","iitr.ac.in","iitrpr.ac.in","iittp.ac.in","iitbhu.ac.in","iitjammu.ac.in","iitgoa.ac.in","ampri.res.in","cbri.res.in","ccmb.res.in","cimap.res.in","cecri.res.in","ceeri.res.in","cftri.res.in","cgcri.res.in","cdri.res.in","cimfr.res.in","csircmc.res.in","cmeri.res.in","csio.res.in","csmcri.res.in","igib.res.in","ihbt.res.in","iicb.res.in","iict.res.in","iiim.res.in","iip.res.in","immt.res.in.","imtech.res.in","iitr.res.in","nal.res.in","nbri.res.in","ncl.res.in","neeri.res.in","neist.res.in","ngri.res.in","niist.res.in","niot.res.in","niscair.res.in","nmlindia.org","nplindia.org","serc.res.in","urdip.res.in"]
    for i in range(len(authdetails.auth_emails)):
        for j in iit:
            if j in authdetails.auth_emails[i]:
                flag=1
                query.data = {
                    "name": authdetails.auth_names[i],
                    "affiliation":authdetails.auth_affi[i],
                    "email":authdetails.auth_emails[i],
                    "expertid":authdetails.auth_links[i],
                        }
                query.list.append(query.data)

    if flag==0:
        print("no results found")
        query.data = {
                    "name": "No Results Found",
                    "affiliation":None,
                    "email":None,
                    "expertid":None,
                        }
        query.list.append(query.data)

    query.auth_dict = {'authdata': query.list.copy()}
    print(query.auth_dict)


if __name__ == '__main__':
    query('iot')

