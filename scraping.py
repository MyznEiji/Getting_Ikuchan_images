import linecache
import requests
import os

from bs4 import BeautifulSoup

# イメージごとのページのURLを取得
def get_page_url(url):
    urls = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    links = soup.find_all("a", class_="pic-card")
    for link in links:
        urls.append(link.get('href'))
    return urls

# イメージを取得
def get_image(urls, before_image):
    images = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text,'lxml')
        image = soup.find("a", class_="pic-img").get('href')
        # 前回取得したイメージの最新のURLかをチェック
        if image in before_image:
            break
        else:
            # print(image)
            images.append(image)
    return images

new_images = []
num = 1
before_image = new_image_url = linecache.getline('images_url.txt', 1)
# is_OK変数を使う

while num <= 100:
    url = "https://prcm.jp/list/%E7%94%9F%E7%94%B0%E7%B5%B5%E6%A2%A8%E8%8A%B1?page=" + str(num)

    # イメージ単体ページのurl取得
    page_urls = get_page_url(url)

    # 新しいイメージを取得
    images = get_image(page_urls, before_image)
    for image in images: new_images.append(image)
    if len(images) != 9: break
    num += 1

    print(num)

if len(new_images) != 0:
    f = open('images_url.txt', 'w')
    for image in new_images: f.write(image + "\n")
    f.close()

print("今回取得した画像は",len(new_images), "個です。")

