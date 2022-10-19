from selenium import webdriver
from selenium.webdriver.chrome.service import Service


s=Service('D:/test/chromedriver.exe')
driver = webdriver.Chrome(service=s)


driver.get("https://ulan-ude.hh.ru/search/vacancy?text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&from=suggest_post&salary=&clusters=true&ored_clusters=true&enable_snippets=true");


from selenium.webdriver.common.by import By
vac = driver.find_elements(By.CLASS_NAME, "bloko-text")
page_source = driver.page_source;

from bs4 import BeautifulSoup

soup = BeautifulSoup(page_source, 'lxml')
vacancy = []
vacancy = soup.find_all(attrs={'class': 'vacancy-serp-item-body__main-info'});

#x='{"data":[';
x=[];

for vac in vacancy :
    x.append({
        #"title": vac.find(attrs={'class': 'serp-item__title', 'data-qa': 'serp-item__title'}).get_text(),
        "experience": vac.find(attrs={'class':'bloko-text','data-qa':'vacancy-serp__vacancy_snippet_responsibility'}).get_text(),
        #"experience": vac.find(attrs={'class': 'bloko-text', 'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}) ,
        #"region": vac.find(attrs={'class': 'bloko-text', 'data-qa':'vacancy-serp__vacancy-address'}).get_text()
            })
    #x += '{"title":"'+vac.find(attrs={'class': 'serp-item__title', 'data-qa': 'serp-item__title'}).get_text() +'",';
   #x += '"salary":"'+vac.find('div', class_='bloko-header-section-3').get_text() +'",';
    #x += '"salary":"'+vac.find(attrs={'class': 'bloko-header-section-3', 'data-qa': 'vacancy-serp__vacancy-compensation'}).get_text() +'",';
    #vac.find(attrs={'class': 'bloko-header-section-3', 'data-qa': 'vacancy-serp__vacancy-compensation'}).get_text()
    #vac.find(attrs={'class': 'bloko-text', 'data-qa': 'vacancy-serp__vacancy-address'}).get_text()
print(x);

#for vac in vacancy :
   # x += '{"title":"'+str(soup.find_all(attrs={'class': 'serp-item__title', 'data-qa': 'serp-item__title'})); +'","work_experience":"'+"test"+',"salary":"'+str(soup.find_all(attrs={'class': 'bloko-header-section-3', 'data-qa': 'vacancy-serp__vacancy-compensation'})); +'","region":"'+str(soup.find_all(attrs={'class': 'bloko-text', 'data-qa': 'vacancy-serp__vacancy-address'}))+'"},';
  # x += vacancy.find(attrs={'class': 'serp-item__title', 'data-qa': 'serp-item__title'}).text; 
#print(x);
    
    
#for vac in vacancy_city :
#    print(vac.text);
    
#for vac in vacancy_pay :
#    print(vac.text);
    

