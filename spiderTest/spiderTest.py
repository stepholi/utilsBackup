# coding = UTF-8

import urllib.request
import re
import os
from socket import error as SocketError
import errno
import time

# open the url and read
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    page.close()
    return html

# compile the regular expressions and find
# all stuff we need
def getUrl(html):
    ########################################匹配获取url列表
    reg = r'(>)(emd-\d{4}\.[a-zA-Z]{4}\.fasta)' #匹配
    if re.match(reg,'>emd-1001.prot.fasta'):
        print('ok')
    else:
        print("failed")
    url_re = re.compile(reg)
    url_lst = url_re.findall(html.decode('UTF-8')) #返回匹配的数组
    print(url_lst)
    return(url_lst)

def getFile(url):
    file_name = url.split('/')[-1]
    u = urllib.request.urlopen(url)
    f = open(file_name, 'wb')

    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        f.write(buffer)
    f.close()
    print ("Sucessful to download" + " " + file_name)


root_url = 'https://bmrbpub.pdbj.org/archive/fasta_emdb/'  #下载地址中相同的部分

raw_url = 'https://bmrbpub.pdbj.org/archive/fasta_emdb/'

html = getHtml(raw_url)
url_lst = getUrl(html)


# os.mkdir('download')
os.chdir(os.path.join(os.getcwd(), 'download'))

for url in url_lst[:]:
    url = root_url + url[1]  #形成完整的下载地址,例如：'https://bmrbpub.pdbj.org/archive/fasta_emdb/emd-1001.prot.fasta'
    # print(url)
    try:
        getFile(url)
    except SocketError as e:
        # if e.errno != errno.ECONNRESET:
        #     raise
        print("出错了，等一下一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一")
        time.sleep(0.5)
        getFile(url)



# #############测试########################
# url =  'https://bmrbpub.pdbj.org/archive/fasta_emdb/emd-1202.prot.fasta'
# getFile(url)
##########################################