import time
import requests
import execjs
import json
import browsercookie


class Interview:

    def __init__(self):
        """提取本地谷歌浏览器文件夹优酷cookie"""
        old_cookie_str = 'cna=GcuGGPqePiUCAXVZFbwpZXbU; __ysuid=1613989017409A5x; __aysid=1613989017410wc1; __ayft=1613997220784; __ayscnt=1; modalFrequency={"UUID":"2"}; youku_history_word=%5B%22love%22%2C%22ove%22%5D; ypvid=16141852493110h3IWy; yseid=1614185249312yauIek; ysestep=1; yseidcount=1; yseidtimeout=1614192449312; ycid=0; ystep=1; juid=01evaf0eh124tp; seid=01evaf0eh2lee; referhost=https%3A%2F%2Fwww.baidu.com; seidtimeout=1614187049315; xlly_s=1; redMarkRead=1; __arycid=df-3-00; __arcms=df-3-00; __ayvstp=164; __aysvstp=164; _m_h5_tk=ac3780d55499793b122f7e0fb2f750fd_1614246792091; _m_h5_tk_enc=dffc58e749a5126a5fb666e0c9bbb826; P_ck_ctl=0025AAE35B90EC9FAF861CE1E4509CAD; isg=BLe3WKdDm7kw1B8xfQ2z9iNkRq0BfIveE0fUQglk_QbtuNf6EEwrLnXZmhjmUGNW; tfstk=cE7dB3VLU5hLnSROgMEiFjXSy1FcZYq9UD9mySqAxDwtcFgRir_ckIb_OITMN5C..; l=eBTH0BZVj_C97JmdBOfwhurza77OdIRAguPzaNbMiOCPO71H52LcW6gu3dTMCnGVhsiJJ3lipen0BeYBc_C-nxvO8VGjNcDmn; __arpvid=1614243156586blk9yU-1614243156595; __aypstp=111; __ayspstp=121'
        old_cookies = dict()
        for i in old_cookie_str.split(';'):
            if '=' in i:
                key, value = i.split('=')
                old_cookies[key.replace(' ', '')] = value
        # print(old_cookies)
        chrome_cookie = browsercookie.Chrome()
        # 获取你本地谷歌浏览器文件夹的cookie
        cj = chrome_cookie.get_cookies()
        cookie_dict = dict()
        for i in cj:
            cookie_dict[i.name] = i.value
        # print(cookie_dict)
        self.cookies = dict()
        for k, v in cookie_dict.items():
            for i in old_cookies.keys():
                if i == k:
                    self.cookies[k] = v
        print(self.cookies)

    def send_request(self, data):
        cookies = self.cookies
        # 将cookie字符串转换为dict
        # for i in cookie.split(';'):
        #     # print(i)
        #     if '=' in i:
        #         key, value = i.split('=')
        #         cookies[key.replace(' ', '')] = value
        token = cookies['_m_h5_tk'].split('_')[0]
        # print(cookies)
        t = int(time.time() * 1000)
        a = token + '&' + str(t) + '&23774304&' + data
        with open('youku.js', encoding='utf-8')as f:
            js_code = f.read()
        js = execjs.compile(js_code)
        # python执行js文件生成sign
        sign = js.call('c', a)
        headers = {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-type': 'application/x-www-form-urlencoded',
            'Host': 'acs.youku.com',
            'Origin': 'https://so.youku.com',
            'Referer': 'https://so.youku.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
        }
        url = 'https://acs.youku.com/h5/mtop.youku.soku.yksearch/2.0/'
        params = (
            ('jsv', '2.5.1'),
            ('appKey', '23774304'),
            ('t', str(t)),
            ('sign', sign),
            ('api', 'mtop.youku.soku.yksearch'),
            ('type', 'originaljson'),
            ('v', '2.0'),
            ('ecode', '1'),
            ('dataType', 'json'),
            ('data', data)
        )
        res = requests.post(url, headers=headers, params=params, cookies=cookies)
        time.sleep(2.37)
        # 把获取到的所有数据写入json文件里面
        with open('youku.json', 'a+')as f:
            f.write(json.dumps(res.json()))
            f.write('\n')
        print(res.json())
        return res.json()

    def extract_data(self, data):
        """提取相关信息，title， url"""
        json_params = self.send_request(data)
        params_ = json_params['data']
        # print(params_)
        name = list()
        urls = list()
        videos = dict()
        for i in params_['nodes']:
            for v in i['nodes']:
                # print(v)
                for m in (v['nodes']):
                    base_url = 'https://v.youku.com/v_show/id_XMjY0NTA2MTgwOA==.html?'
                    # print(m)
                    try:
                        try:
                            # https://v.youku.com/v_show/id_XMzY0NTc5NDcyOA==.html?spm=a2h0c.8166622.PhoneSokuUgc_21.dtitle&g=1417820
                            name.append(m['data']['ugcPlaylist']['name'])  # 专题
                            # id_ = m['data']['videoId'] + '.html?'
                            spm = 'spm=' + m['data']['titleDTO']['action']['report']['spm'] + '&'
                            g = 'g' + m['data']['playlistId']
                            url = base_url + spm + g
                            urls.append(url)
                            videos[m['data']['ugcPlaylist']['name']] = url
                        except:
                            pass
                        try:
                            # https://v.youku.com/v_show/id_XMTI1OTg2MzY5Ng==.html?spm=a2h0c.8166622.PhoneSokuUgc_36.dtitle
                            npm = 'spm=' + m['data']['titleDTO']['action']['report']['spm']
                            videos[m['data']['titleDTO']['displayName']] = base_url + npm
                        except:
                            pass
                    except:
                        # https://v.youku.com/v_show/id_XMjY0NTA2MTgwOA==.html?spm=a2h0c.8166622.PhoneSokuProgram_23.dtitle&s=709f3519fa114a3eaa3e
                        name.append(m['data']['action']['report']['trackInfo']['object_title'])
                        spm = 'spm=' + m['data']['titleDTO']['action']['report']['spm']
                        s = 's=' + m['data']['realShowId']
                        url = base_url + spm + s
                        urls.append(url)
                        videos[m['data']['action']['report']['trackInfo']['object_title']] = url

        # print(name, len(name))
        # print(urls, len(urls))
        # print(videos)
        return videos


def start_down(types, start_page, stop_page):
    """根据类型, 分页下载"""
    yk = Interview()
    videos_list = list()
    for i in range(start_page, stop_page):
        data = {
            "searchType": 1, "keyword": types, "pg": i, "pz": 20, "site": 1, "appCaller": "pc",
            "appScene": "mobile_multi", "userTerminal": 2, "sdkver": 313, "userFrom": 1, "noqc": 0,
            "aaid": "3abedb85c990da1dd58f91948bbea063", "ftype": 0, "duration": "", "categories": "", "ob": "",
            "utdId": "GcuGGPqePiUCAXVZFbwpZXbU", "userType": "guest", "userNumId": 0, "searchFrom": "1",
            "sourceFrom": "home"
        }
        json_info = yk.extract_data(str(data))
        videos_list.append(json_info)
    print(videos_list)
    with open('yk.json', 'w')as f:
        f.write(json.dumps(videos_list))


if __name__ == '__main__':
    start_down('love', 2, 6)
