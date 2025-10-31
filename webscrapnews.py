import requests
from bs4 import BeautifulSoup
import json

def scraper_noticias():
    try:
        url = "https://g1.globo.com/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        noticias = []
        
        for item in soup.find_all('a', class_='feed-post-link')[:10]:
            titulo = item.text.strip()
            link = item['href']
            noticias.append({'titulo': titulo, 'link': link})
        
        # Salvar em JSON
        with open('noticias.json', 'w', encoding='utf-8') as f:
            json.dump(noticias, f, ensure_ascii=False, indent=2)
        
        print("Notícias salvas em 'noticias.json'")
        return noticias
        
    except Exception as e:
        print(f"Erro: {e}")

scraper_noticias()
