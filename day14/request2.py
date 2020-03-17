from time import time
from threading import Thread

import requests
import json

# 继承Thread类创建自定义的线程类
class DownloadHanlder(Thread):

    def __init__(self, continents, provinceName, currentConfirmedCount):
        super().__init__()
        self.continents = continents
        self.provinceName=provinceName
        self.currentConfirmedCount=currentConfirmedCount

    def run(self):
        print('Concronvirs: ', self.continents, self.provinceName, self.currentConfirmedCount, sep='')


def main():
    # 通过requests模块的get函数获取网络资源
    # 下面的代码中使用了天行数据接口提供的网络API
    # 要使用该数据接口需要在天行数据的网站上注册
    # 然后用自己的Key替换掉下面代码的中APIKey即可
    resp = requests.get(
        'http://api.tianapi.com/txapi/ncovabroad/index?key=cb588c6956392fef753a9b028c95fbad')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    # load_data = json.loads(resp)
    data = data_model.get("newslist")
    # print(data_model)
    for mm_dict in data:
        continents = mm_dict['continents']
        provinceName = mm_dict['provinceName']
        currentConfirmedCount = mm_dict['currentConfirmedCount']

        # 通过多线程的方式实现图片下载
        DownloadHanlder(continents,provinceName,currentConfirmedCount).start()


if __name__ == '__main__':
    main()