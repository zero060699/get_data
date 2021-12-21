from requests_html import HTMLSession
import requests
import shutil
from pathlib import Path


def dl_img(img_url, chapter_folder):

    filename = img_url.split("/")[-1]
    Path(chapter_folder).mkdir(parents=True, exist_ok= True)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
        "Referer": "https://www.nettruyenonline.com/",
    }

    response = requests.get(img_url, headers=headers, stream = True)
    response.raw.decode_content = True
    file_img = open(chapter_folder+"/"+filename, "wb")
    shutil.copyfileobj(response.raw,file_img)

session = HTMLSession() 
chapter_url = "https://www.nettruyenonline.com/truyen/conan/chapter-1041-1040238.html"
r = session.get(chapter_url)
rs = r.html.find(".readimg img", first = False)
for y in rs:
    img = y.attrs['src']
    print(img)
    chapter = chapter_url.split("/")[-1]
    dl_img(img, chapter)
    #exit()