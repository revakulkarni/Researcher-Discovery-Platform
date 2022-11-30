from selenium import webdriver   # for webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
import time
from bs4 import BeautifulSoup
# from hexapod.vidwanprofilepage import author_profile
# from vidwanprofilepage import author_profile
import os

def query(search_query):
    x = search_query
    option = webdriver.ChromeOptions()
    option.add_argument("--window-size=1920,1080")
    option.add_argument("--start-maximized")
    option.add_argument("--headless")
    global driver
    chromedriver_path = os.getcwd()+'\\hexapod\\chromedriver.exe'
    driver = webdriver.Chrome(chromedriver_path,options=option)
    driver.get('https://vidwan.inflibnet.ac.in/searchc/search')
    # driver.implicitly_wait(1) 
    driver.find_element_by_xpath('//*[@id="top-search-box"]/div[1]/div').click()
    # search_query = input("Enter quey : ")
    # TODO : Change it later for user defined inputs
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div/div[1]/div/div/div[1]/div[2]/div[1]/div/input').send_keys(str(x))
    driver.find_element_by_xpath('//*[@id="search"]').click()
    # driver.implicitly_wait(1)
    driver.implicitly_wait(5)
    query.list=[]
    try:
        # It is working in normal code but in django its not.
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div/div[3]/div/div[2]/div[3]/ul/li/select').send_keys('30')
        # driver.implicitly_wait(2)
        source = driver.page_source

        ##################################################################################################
        lst=["Indian Institute of Technology Bombay","Indian Institute of Technology Madras","Indian Institute of Technology Delhi","Indian Institute of Technology Kharagpur","Indian Institute of Technology Kanpur","Indian Institute of Technology Guwahati","Indian Institute of Technology Hyderabad","Indian Institute of Technology Roorkee","Indian Institute of Technology BHU, Varanasi","Indian Institute of Technology Gandhinagar","Indian Institute of Technology Patna","Indian Institute of Technology Indore","Indian Institute of Technology Bhubaneshwar","Indian Institute of Technology Jodhpur","Indian Institute of Technology Dhanbad","Indian Institute of Technology Mandi","Indian Institute of Technology Tirupati","Indian Institute of Technology Palakkad","Indian Institute of Technology Dharwad","Indian Institute of Technology Kolkata","Birla Institute of Technology and Science, Pilani","Indian Institute of Technology Bhilai","Indian Institute of Technology Ropar","Indian Institute of Technology Jammu","Indian Institute of Technology Goa","National Institute of Technology, Durgapur","National Institute of Technology, Rourkela","National Institute of Technology, Silchar","National Institute of Technology, Tiruchirappali","National Institute of Technology, Raipur","National Institute of Technology, Warangal","National Institute of Technology, Hamirpur","National Institute of Technology, Jamshedpur","National Institute of Technology, Patna","National Institute of Technology, Meghalaya","National Institute of Technology, Uttarakhand","National Institute of Technology, Agartala","National Institute of Technology, Manipur","National Institute of Technology, Sikkim","National Institute of Technology Srinagar","National Institute of Technology, Delhi","National Institute of Technology, Kurukshetra","National Institute of Technology, Nagaland","National Institute of Technology Andhra Pradesh","National Institute of Technology, Arunachal Pradesh","National Institute of Technology Trichy","National Institute of Technology, Karnataka","National Institute of Technology, Calicut","National Institute of Technology, Kerala","National Institute of Technology, Goa","National Institute of Technology, Dimapur","National Institute of Technology, Puducherry","Indian Institute of Information Technology, Allahabad","Indian Institute of Information Technology, Delhi","Indian Institute of Information Technology, Sri City","Indian Institute of Information Technology, Guwahati","Indian Institute of Information Technology, Vadodara","Indian Institute of Information Technology, Kota","IIIT Kota","Indian Institute of Information Technology, Tiruchirappali","Indian Institute of Information Technology, Una","Indian Institute of Information Technology, Sonepat","Indian Institute of Information Technology, Kalyani","Indian Institute of Information Technology, Lucknow","Indian Institute of Information Technology, Dharwad","Indian Institute of Information Technology, Kottayam","Indian Institute of Information Technology, Manipur","Indian Institute of Information Technology, Nagpur","Indian Institute of Information Technology, Pune","Indian Institute of Information Technology, Ranchi","Indian Institute of Information Technology, Surat","Indian Institute of Information Technology, Bhopal","Indian Institute of Information Technology, Bhagalpur","Indian Institute of Information Technology, Agartala","Indian Institute of Information Technology, Raichur","CSIR-National Aerospace Laboratories","CSIR-Central Scientific Instruments Organisation","CSIR-Central Electronics Engineering Research Institute","CSIR-Central Mechanical Engineering Research Institute","CSIR-North East Institute of Science and Technology","CSIR-Advanced Materials and Processes Research Institute","CSIR-Central Building Research Institute","CSIR-Centre for Cellular Molecular Biology","CSIR-Central Drug Research Institute","CSIR-Central Electrochemical Research Institute","CSIR-Central Food Technological Research Institute","CSIR-Central Glass Ceramic Research Institute","CSIR-Central Institute of Medicinal Aromatic Plants","CSIR-Central Institute of Mining and Fuel Research","CSIR-Central Leather Research Institute","CSIR-Central Road Research Institute","CSIR-Central Scientific Instruments Organisation","CSIR-Central Salt Marine Chemicals Research Institute","CSIR Fourth Paradigm Institute","CSIR-Institute of Genomics and Integrative Biology","CSIR-Institute of Himalayan Bioresource Technology","CSIR-Indian Institute of Chemical Biology","CSIR-Indian Institute of Chemical Technology","CSIR-Indian Institute of Integrative Medicine","CSIR-Indian Institution Petroleum", "CSIR-Indian Institute of Toxicology Research", "CSIR-Institute of Minerals and Materials Technology", "CSIR-Institute of Microbal Technology", "CSIR-National Aerospace Laboratories", "CSIR-National Botanical Research Institute", "CSIR-National Chemical Laboratory", "CSIR-National Environment Engineering Research Institute", "CSIR-North-East Institute of Science and Technology", "CSIR-National Geophysical Research Institute", "CSIR-National Institute For Interdisciplinary Science and Technology", "CSIR-National Institute of Oceanography", "CSIR-National Institute of Science Communication and Information Resources","CSIR-National Institute of Science,Technology And Development Studies","CSIR-National Metallurgical Laboratory", "CSIR-National Physical Laboratory","CSIR-Structural Engineering Research Centre"]
        soup=BeautifulSoup(source,'html5lib')
        inst=soup.findAll("div",{"id":"style-4"})
        inst1=(inst[4]).findAll("li")
        institutes=[]
        for i in range(0,len(inst1),2):
            institutes.append((inst1[i].find("i")).next_sibling.strip())
        for i in institutes:
            if i in lst:
                try:
                    driver.find_element_by_xpath('.//*[text()="'+i+'"]').click()
                except:
                    continue

        btn=driver.find_elements_by_xpath('.//*[@type="submit"]')
        btn[4].click()
        print("done")
        source1=driver.page_source
        soup = BeautifulSoup(source1,'html5lib')
        soup2=soup.find_all('div', class_='col-sm-9')
        ##################################################################################################
        for auth in range(len(soup2)):
                y = soup2[auth].find_all('strong')
                z = y[0].contents[0].rstrip().lstrip().replace("   ",'' ).replace("\n",'')
                name = z

                y =soup2[auth].find_all('li')
                expert_id = y[0].contents[4].rstrip()
                aff = soup2[auth].find_all('span')[0].contents[2].lstrip().rstrip()
                aff_from = soup2[auth].find_all('li')[5].contents[2].lstrip().rstrip() + "," + soup2[auth].find_all('li')[6].contents[2].lstrip().rstrip()
                query.data = {
                    "name": name,
                    "affiliation":aff  +','+aff_from,
                    "expertid":expert_id,
                        }
                query.list.append(query.data)
        query.auth_dict = {'authdata': query.list.copy()}
    except:
        print("no results found")
        query.data = {
                    "name": "No Results Found",
                    "affiliation":None,
                    "expertid":None,
                        }
        query.list.append(query.data)
        query.auth_dict = {'authdata': query.list.copy()}
    return query.list

if __name__ == '__main__':
    query('iot')
    