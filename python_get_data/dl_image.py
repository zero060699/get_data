import requests
import shutil

def dl_img(img_url):

    filename = img_url.split("/")[-1]

    headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
    "Referer": "https://www.nettruyenonline.com/",
    }

    response = requests.request("GET", img_url, headers=headers)
    response.raw.decode_content = True
    file_img = open(filename, "wb")
    shutil.copyfileobj(response.raw,file_img)