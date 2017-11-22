# coding:utf-8
#!/usr/bin/python
import mechanize


def viewPage(url):
    browser = mechanize.Browser()
    page = browser.open(url)
    source_code = page.read()
    print source_code
viewPage('http://www.doubledna.cn')