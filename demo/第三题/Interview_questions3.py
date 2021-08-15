import os
import requests
from threading import Thread
from time import sleep
from browsermobproxy import Server
from selenium import webdriver
# 配置代理用
from selenium.webdriver.chrome.options import Options

headers = {
    'Referer': 'https://powv1deo.cc/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}


class Interview:

    def open_browser(self):
        url = 'https://www.gnula.cc/ver-episode/big-sky-2020-1x9/'
        # 我用的是Mac电脑 windows用.bat那个代理
        bp_server = Server(r'browsermob-proxy-2.1.4\bin\browsermob-proxy')
        # 开启抓包代理服务
        bp_server.start()
        self.bp_proxy = bp_server.create_proxy()
        chrome_options = Options()
        chrome_options.add_argument('--proxy-server={}'.format(self.bp_proxy.proxy))
        # Mac的谷歌驱动  windows要重新下载
        diver = webdriver.Chrome(executable_path="chromedriver", options=chrome_options)
        diver.get(url)
        diver.implicitly_wait(10)
        # 点击视频播放
        diver.find_element_by_css_selector('body > div.play - box').click()
        # 隐式等待， 待页面加载完成
        diver.implicitly_wait(10)

    def get_m3u8(self):
        """过滤所有request url  提取m3u8"""
        result = self.bp_proxy.har
        request_urls = []
        for entry in result['log']['entries']:
            entry_url = entry['request']['url']
            request_urls.append(entry_url)
        for m3u8_url in request_urls:
            if '.m3u8' in m3u8_url:
                return m3u8_url

    def start_ts(self, url):
        ts_res = requests.get(url, headers)
        # print(ts_res.content)
        with open('ts\\%s.ts' % url.split('.ts?')[-1], 'wb')as f:
            f.write(ts_res.content)

    def down_ts(self):
        m3u8_url = self.get_m3u8()
        res = requests.get(m3u8_url, headers)
        ts_list = ['/'.join(m3u8_url.split('/')[0:-1]) + '/' + ts for ts in res.text.split('\n') if '.ts' in ts]
        for ts_url in ts_list:
            st = Thread(target=self.start_ts, args=(ts_url, ))
            st.start()
            sleep(0.3)

    def file_walker(self, ts_path):
        """读取所有的ts文件"""
        file_list = []
        for root, dirs, files in os.walk(ts_path):
            for fn in files:
                p = str(root + '/' + fn)
                file_list.append(p)
        file_list.sort(key=lambda x: int(x.split('=')[-1].split('.')[0]))
        # print(file_list)
        return file_list

    def combine(self, ts_path, mp4_path):
        """把所有ts文件读取出来追加到一个mp4里面"""
        file_list = self.file_walker(ts_path)
        with open(mp4_path, 'wb+') as fw:
            for i in range(len(file_list)):
                fw.write(open(file_list[i], 'rb').read())


def start_down(ts_path, mp4_path):
    down_movie = Interview()
    down_movie.open_browser()
    down_movie.down_ts()
    down_movie.combine(ts_path, mp4_path)


if __name__ == '__main__':
    start_down('ts', 'mp4/test.mp4')