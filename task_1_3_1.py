
from requests_tor import RequestsTor
from bs4 import BeautifulSoup
import json
import time
import tqdm

req = RequestsTor()

data = {
        "data":[]
        }


for page in range(1,40):
    url = f"https://ulan-ude.hh.ru/search/vacancy?area=113&search_field=name&search_field=company_name&search_field=description&text=python+разработчик&from=suggest_post&page=0&hhtmFrom=vacancy_search_list"
    resp = req.get(url);
    
    soup = BeautifulSoup(resp.text, 'lxml')
    tags = soup.find_all(attrs={'data-qa':'serp-item__title'});
    for iter in tqdm.tqdm(tags):
        #time.sleep(2);
        url_object = iter.attrs["href"]
        resp_object =req.get(url_object);
        
        soup_object = BeautifulSoup(resp_object.text, 'lxml');
        tag_title = soup_object.find(attrs={"data-qa" :"vacancy-title"}).text;
        tag_exp = soup_object.find(attrs={"data-qa" :"vacancy-experience"}).text;
        tag_price = soup_object.find(attrs={"data-qa" :"vacancy-salary"}).find_all(attrs={"class":"bloko-header-section-2"})[0].text;
        tag_adress =soup_object.find(attrs={"data-qa" :"vacancy-view-raw-address"});
        if not tag_adress :    
            tag_adress=soup_object.find(attrs={"data-qa" :"vacancy-view-location"});
        
        
        data["data"].append({"Название":tag_title,"Опыт":tag_exp,"Зарплата":tag_price,"Регион":tag_adress.text});

        with open("data_json","w") as file:
            json.dump(data,file,ensure_ascii=False);
        