import json
import re

import requests
def getHtml(url):
    r =requests.get(url=url)
    #print(r.status_code)
    #print(r.text)
    return r.text;
def getImageUrls(url):
    html =getHtml(url)
    try:
        js = json.loads(html)
        ss = js["content"]
    except Exception:
        return None
    reg = r'src="(.*?)"'
    pattern = re.compile(reg)
    ret = re.findall(pattern, ss)
    return ret
def converUrl(url):
    reg = r'id=(.*?)&'
    s = re.search(reg, url)
    if s is not None:
        url = "http://note.youdao.com/yws/public/note/%s?editorType=0&cstk=orBX-yw0" % s.group()[3:-1]
        return url
    else:
        return None



if __name__=="__main__":
    url ="http://note.youdao.com/share/?id=714db3469730edf0e368d105da&type=note#/"
    url = converUrl(url)
    print(getImageUrls(url))
    #ss ="http://note.youdao.com/yws/public/note/714db3469730e010d53df0e368d105da?editorType=0&cstk=orBX-yw0"
    #print(getImageUrls("http://note.youdao.com/share/?id=714db3469730e010d53df0e368d105da&type=note#/"))
