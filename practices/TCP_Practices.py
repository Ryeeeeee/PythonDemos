# TCP_Practices.py

import socket

def getWebSitePage(url):
    siteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    siteSocket.connect((url,80))
    siteSocket.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
    dataBuffer = []
    while True:
        data = siteSocket.recv(1024)
        if data:
            dataBuffer.append(data)
        else:
            break
    siteSocket.close()
    pageData = ''.join(dataBuffer)
    header, html = pageData.split('\r\n\r\n', 1)
    print 'the page\'s html header is \n %s' % header
    with open('page.html', 'wb') as pageFile:
        pageFile.write(html)

if __name__ == '__main__':
    getWebSitePage('www.sina.com.cn')