#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    拉勾网抓取职位信息
'''
import requests
from openpyxl import Workbook

def get_json(url, page, lang_name):
    data = {'first': 'true', 'pn': page, 'kd': lang_name}
    headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
               'Accept - Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
               'Connection': 'Keep-Alive',
               'Host': 'zhannei.baidu.com',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
               'Referer': 'https://www.lagou.com/jobs/list_Java?city=%E6%B7%B1%E5%9C%B3&cl=false&fromSearch=true&labelWords=&suginput=',
               'Cookie': 'user_trace_token=20180406135337-d986efa5-395e-11e8-b553-525400f775ce; LGUID=20180406135337-d986f2c5-395e-11e8-b553-525400f775ce; _ga=GA1.2.2097502544.1522994018; JSESSIONID=ABAAABAAAFCAAEG1DBE6A322B44B7C29A0B68BD1B446063; _gid=GA1.2.40353991.1525055787; WEBTJ-ID=20180430120422-16314b90ea61aa-02a5e26e4d2791-3c604504-2073600-16314b90ea7216; LGSID=20180430120418-8dd72402-4c2b-11e8-bb05-5254005c3644; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rsv_spt%3D1%26rsv_iqid%3D0xf11fc4750001dfea%26issp%3D1%26f%3D8%26rsv_bp%3D1%26rsv_idx%3D2%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dsitehao123_15%26rsv_enter%3D1%26oq%3Dpython%2525E7%252588%2525AC%2525E8%252599%2525AB%2525E4%2525B9%2525A6%2525E7%2525B1%25258D%2525E6%25258E%2525A8%2525E8%25258D%252590%26rsv_t%3D2307DeEL8XOgxNu3wNdU%252Fx1bdZ1D4we0NP%252FE3BOxCTCRPCqo6qnd9RblmuglHi%252BCc5aPkg%26rsv_pq%3Dc9c5161300012422%26rsv_sug3%3D35%26rsv_sug1%3D30%26rsv_sug7%3D101%26bs%3Dpython%25E7%2588%25AC%25E8%2599%25AB%25E4%25B9%25A6%25E7%25B1%258D%25E6%258E%25A8%25E8%258D%2590; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; X_HTTP_TOKEN=32e0e0ba72e7e5ba09b7a4fe05acd3fb; LG_LOGIN_USER_ID=fbcf8fe8dc7fdc0489448c85bda90a8c0b30ecb4df77259a; _putrc=580048F91FFE3788; login=true; unick=%E5%AE%8B%E6%B0%B4%E9%98%B3; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=40; index_location_city=%E6%B7%B1%E5%9C%B3; TG-TRACK-CODE=index_navigation; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1522994018,1525055787,1525061063,1525062532; gate_login_token=2cae1400c78e0b08305e2587ef38b752d3b371dde42bf7ac; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1525062540; LGRID=20180430122855-fe680704-4c2e-11e8-a8ab-525400f775ce; SEARCH_ID=0893b156dd444e3497779a348f1bea72'}
    json = requests.post(url, data, headers=headers).json()
    list_con = json['content']['positionResult']['result']
    info_list = []
    for i in list_con:
        info = []
        info.append(i['companyShortName'])
        info.append(i['companyName'])
        info.append(i['salary'])
        info.append(i['city'])
        info.append(i['education'])
        info_list.append(info)
    return info_list


def main():
    # lang_name = input('职位名：')
    lang_name = 'java'
    page = 1
    url = 'http://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    info_result = []
    while page < 31:
        info = get_json(url, page, lang_name)
        info_result = info_result + info
        page += 1
    wb = Workbook()
    ws1 = wb.active
    ws1.title = lang_name
    for row in info_result:
        ws1.append(row)
    wb.save('职位信息.xlsx')

if __name__ == '__main__':
    main()