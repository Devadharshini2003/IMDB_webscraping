from bs4 import BeautifulSoup
import requests, openpyxl

excel=openpyxl.Workbook()
sheet =excel.active
sheet.title="Movie List"



try:
    response =requests.get("https://www.imdb.com/chart/top/")
    soup = BeautifulSoup(response.text,'html.parser')
    movies =soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-3f13560f-0 sTTRj compact-list-view ipc-metadata-list--base").find("li")
    
    
    
    for movie in movies:
        rank=movie.find('h3',class_="ipc-title__text").get_text(strip=True).split('.')[0]
        movie_name=movie.find('h3',class_="ipc-title__text").a.text
        rating=movie.find('div',class_="sc-e3e7b191-0 iKUUVe sc-6fa21551-2 kOfhdG cli-ratings-container").span.text
        year=movie.find('div',class_="sc-6fa21551-7 jLjTzn cli-title-metadata").span.text.replace('(',"")
        year=year.replace('(',"")

        sheet.append(['rank','moviename','rating','Release Year'])

except Exception as e:
    print(e)

excel.save("Movies.xlsx")




