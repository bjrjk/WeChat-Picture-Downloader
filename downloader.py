import urllib3, requests
from bs4 import BeautifulSoup

def download(URL, fileName):
    with open(fileName, "wb") as f:
        r = requests.get(URL, verify=False)
        f.write(r.content)

def main():
    URL = input("Please input WeChat Offical Account Page URL (Like https://mp.weixin.qq.com/s/******): ")
    response = requests.get(URL)
    HTMLContent = response.content
    bs = BeautifulSoup(HTMLContent, "html.parser")
    i = 0
    for img in bs.find(id='js_content').find_all("img"):
        fileName = f"{i}.jpg"
        url = img.get('data-src')
        print(fileName, url)
        i += 1
        download(url, "downloads/" + fileName)
    print("Download Finished!")

if __name__ == '__main__':
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()