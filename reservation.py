# /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'lihuiyw'

import urllib2
import urllib
import re

# 查找用户cookie, chrome f12
cookie = "cookie"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
    'Cookie': cookie}


def _get_appid():
    # 模拟http登录
    app_url = 'url'
    request = urllib2.Request(app_url, headers=headers)
    response = urllib2.urlopen(request)
    # 获取Response字符编码
    encoding = response.headers['content-type'].split('charset=')[-1]
    raw_string = response.read()
    # 修改字符集
    html = raw_string.decode(encoding, 'ignore')
    appid_pattern = re.compile(r'<option value="(\d*)".*10:00-11:30.*')
    appid = appid_pattern.search(html).group(1)
    return appid


# 构建表单，POST
def post_form():
    """
        appStepId:116
        appInfoId:133557
        categoryId:17
    :return:True or False
    """
    appinfoid = _get_appid()
    pstform = {'appStepId': '116', 'appInfoId': appinfoid, 'categoryId': '17'}
    post_url = 'url'
    pstform = urllib.urlencode(pstform)
    # POST表单数据
    urllib2.Request(url=post_url, data=pstform, headers=headers)
    # 返回POST结果
    response = urllib2.Request(post_url, pstform, headers=headers)
    response.add_header('X-Requested-With', 'XMLHttpRequest')
    # 返回结果HTML
    html = urllib2.urlopen(response).read()
    return html


if __name__ == "__main__":
    print post_form()
