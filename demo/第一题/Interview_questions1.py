from lxml import etree
from selenium import webdriver


def open_browser(url, xpath):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(4)
    result = driver.page_source
    html = etree.HTML(result)
    url_list = html.xpath(xpath)
    # print(url_list)
    return url_list


if __name__ == '__main__':
    url = 'https://rmz.cr/release/chicago-pd-s08e07-webrip-x264-ion10'
    xpath = '//pre/a/@href'
    url_list = open_browser(url, xpath)
    print(url_list)