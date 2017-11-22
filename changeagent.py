import mechanize

def testUserAgent(url, userAgent):
    browser = mechanize.Browser()
    browser.addheaders = userAgent
    page = browser.open(url)
    source_page = page.read()
    print source_page

url = 'http://www.dotdoh.com/'
userAgent = [('User-agent', 'Mozilla/5.0 (X11; ; Linux i686; rv:1.9.2.20) Gecko/20110805 Netscape6/6.01')]
testUserAgent(url, userAgent)