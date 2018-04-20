import matplotlib.pyplot as plt
import numpy as np
from time import strftime


# 画图

class Drawimg:
    def draw(info, name, type):
        content = []
        number = []
        for i in info:
            content.append(i[0])
            number.append(i[1])
        print(content)
        print(number)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        fig = plt.figure(figsize=(10, 10))
        plt.pie(x=number, labels=content, autopct='%1.2f%%')
        title = name + "的" + type + '分布饼图'
        plt.title(title)

        time = strftime("%Y%m%d")
        # path = 'G:\\bishe\\app\\static\\chartimg'
        path = '.\\app\\static\\chartimg'
        filename = time + name + type + '.png'
        if type == 'city':
            path += '\city'
        elif type == 'salary':
            path += '\salary'
        elif type == 'education':
            path += '\education'
        filepath = path + '\\' + filename
        print(filepath)
        plt.savefig(filepath)
        # plt.show()
        return filepath
