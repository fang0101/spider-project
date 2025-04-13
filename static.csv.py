import requests
from bs4 import BeautifulSoup
import csv
import time

headers = {
    'User-Agent': 'Mozilla/5.0'
}

def get_movie_info(soup):
    movies = []
    for item in soup.find_all('div', class_='item'):
        title = item.find('span', class_='title').text
        rating = item.find('span', class_='rating_num').text
        info = item.find('div', class_='bd').p.text.strip().replace('\n', ' ')
        link = item.find('div', class_='hd').a['href']
        movies.append({
            'title': title,
            'rating': rating,
            'info': info,
            'link': link
        })
    return movies

def main():
    all_movies = []
    for start in range(0, 250, 25):
        url = f'https://movie.douban.com/top250?start={start}'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        movies = get_movie_info(soup)
        all_movies.extend(movies)
        time.sleep(2)  # 避免請求過於頻繁
    # 儲存為 CSV
    with open('douban_top250.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'rating', 'info', 'link'])
        writer.writeheader()
        writer.writerows(all_movies)
    print("成功儲存為 douban_top250.csv")

if __name__ == '__main__':
    main()
