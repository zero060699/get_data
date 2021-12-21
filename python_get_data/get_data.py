from requests_html import HTMLSession
import requests
import shutil
from pathlib import Path

def dl_img(img_url, chapter_folder, name):

    filename = img_url.split("/")[-1]
    Path(name + "/" + chapter_folder).mkdir(parents=True, exist_ok= True)
    headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
    "Referer": "https://www.nettruyenonline.com/",
    }

    response = requests.get(img_url, headers=headers, stream = True)
    response.raw.decode_content = True
    file_img = open(name + "/" + chapter_folder + "/" + filename, "wb")
    shutil.copyfileobj(response.raw,file_img)

session = HTMLSession()
url = "https://www.nettruyenonline.com/chi-tiet/conan.html"
r = session.get(url)
rs = r.html.find("#nt_listchapter .chapter a", first = False)
for x in rs:
    chapter_url = x. attrs['href']
    print(chapter_url)
    r = session.get(chapter_url)
    rs = r.html.find(".readimg img", first = False)
    for y in rs:
        img = y.attrs['src']
        print(img)
        chapter = chapter_url.split("/")[-1]
        name = chapter_url.split("/")[-2]
        dl_img(img, chapter, name)
        # exit()