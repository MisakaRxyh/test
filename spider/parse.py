# -*- coding: utf-8 -*-
import re
from spider.mysqlpipeline import MySQL_DB
import simplejson


class Parse:
    '''
    解析网页信息
    '''

    def __init__(self, htmlCode):
        self.htmlCode = htmlCode
        # self.json = demjson.decode(htmlCode)
        self.json = simplejson.loads(htmlCode)
        pass

    # def parseTool(self, content):
    #     '''
    #     清除html标签
    #     '''
    #     if type(content) != str: return content
    #     sublist = ['<p.*?>', '</p.*?>', '<b.*?>', '</b.*?>', '<div.*?>', '</div.*?>',
    #                '</br>', '<br />', '<ul>', '</ul>', '<li>', '</li>', '<strong>',
    #                '</strong>', '<table.*?>', '<tr.*?>', '</tr>', '<td.*?>', '</td>',
    #                '\r', '\n', '&.*?;', '&', '#.*?;', '<em>', '</em>']
    #     try:
    #         for substring in [re.compile(string, re.S) for string in sublist]:
    #             content = re.sub(substring, "", content).strip()
    #     except:
    #         raise Exception('Error ' + str(substring.pattern))
    #     return content

    def parsePage(self):
        '''
        解析并计算页面数量
        :return: 页面数量
        '''
        totalCount = self.json['content']['positionResult']['totalCount']  # 职位总数量
        resultSize = self.json['content']['positionResult']['resultSize']  # 每一页显示的数量
        pageCount = int(totalCount) // int(resultSize) + 1  # 页面数量
        return pageCount

    def parseInfo(self):
        '''
        解析信息同时保存到数据库
        '''
        info = []
        db = MySQL_DB()
        db.__init__()
        db.dbconn()
        for position in self.json['content']['positionResult']['result']:
            i = {}
            i['positionId'] = str(position['positionId'])
            i['positionName'] = str(position['positionName'])
            i['companyShortName'] = str(position['companyShortName'])
            i['city'] = str(position['city'])
            i['salary'] = str(position['salary'])
            i['education'] = str(position['education'])
            i['workYear'] = str(position['workYear'])
            i['createTime'] = str(position['createTime']).split(" ")[0]
            i['skillName'] = str(self.json['content']['positionResult']['queryAnalysisInfo']['positionName'])
            info.append(i)
            db.insert(i)
            print(i)
        return info
