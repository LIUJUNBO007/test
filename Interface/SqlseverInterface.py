# -*- coding: utf-8 -*-
import random

from Utils.GetKeyword import GetKeyword
from Utils.SendMethod import SendMethod
from Utils.OperationConfig import OperationConfig
import json
from datetime import datetime
import time


class AddressInterface(object):
    def __init__(self):
        config = OperationConfig()
        self.url = config.get_option('test', 'url')
        self.headers = json.loads(config.get_option('test', 'headers'))

    def zcloud_login(self):
        "zcloud登录"
        method = 'get'
        url = self.url + '/dbaasApiGateWay/doLogin'
        return SendMethod.send_method(method=method, url=url, headers=self.headers)

    def get_Heath_scorelist(self):
        """健康得分列表"""
        method = 'post'  # 请求方式
        url = self.url + '/aiCure/health/score/list'  # 请求地址
        return SendMethod.send_method(method=method, url=url, json=None, headers=self.headers)  # 发起请求

    def get_Heath_dbtype(self):
        """获取数据库类型"""
        method = 'get'  # 请求方式
        url = self.url + '/aiCure/health/score/dbType'  # 请求地址
        return SendMethod.send_method(method=method, url=url)  # 发起请求

    def add_knwl(self, payload):
        """获取数据库类型"""
        method = 'post'  # 请求方式
        url = self.url + '/ekb/knwlInfo/title'  # 请求地址
        return SendMethod.send_method(method=method, json=payload, url=url)  # 发起请求

    def update_knwl(self, payload):
        method = 'put'  # 请求方式
        url = self.url + '/ekb/knwlInfo/update'  # 请求地址
        return SendMethod.send_method(method=method, json=payload, url=url)  # 发起请求

    def get_knwl(self):
        method = 'get'
        url = self.url + '/ekb/knwlSpace'
        return SendMethod.send_method(method=method, url=url)

    def get_Heath_problems(self):
        """获取数据库集群产生的问题"""
        method = 'get'  # 请求方式
        url = self.url + '/aiCure/health/score/problems'  # 请求地址

        return SendMethod.send_method(method=method, url=url)  # 发起请求

    def get_space_manger(self):
        """-空间管理--TOP大表"""
        method = 'get'
        url = self.url + '/dbaasSQLServer/spaceManage/topTableList?lang=en_US'
        payload = {
            'dbName': 1,
            'rows': 1,
            'spaceSize': 1,
            'spaceUnit': 1,
            'instanceId': 1

        }
        return SendMethod.send_method(method=method, url=url, params=payload)

    def get_list(self):
        method = 'post'
        url = self.url + '/aiCure/health/score/list'
        payload = {
            "dbType": [],
            "endTime": "",
            "healthState": [],
            "indicatorLevel": "",
            "isAsc": "false",
            "isFavorite": "false",
            "lastTimeDuration": 28800,
            "orderBy": "",
            "pageNum": 1,
            "pageSize": 20,
            "queryField": "",
            "resPooliId": [],
            "startTime": "",
            "tenantId": ""
        }
        return SendMethod.send_method(method=method, url=url, json=payload)


if __name__ == '__main__':
    # add = AddressInterface()
    # print(add.get_Heath_scorelist())
    # print(add.get_Heath_scorelist())
    # print(add.get_list())
    # s = "/Date(1577808000000)/"
    # timeStamp = int(int(s[6:19])/1000)
    # date = datetime.fromtimestamp(timeStamp)
    # print(timeStamp)
    # print(date)
    # tss1 = '2013-10-10 23:40:00'
    # # 转为时间数组
    # timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
    # print(timeArray)
    # # timeArray可以调用tm_year等
    # print(timeArray.tm_year)
    # # 转为时间戳
    # timeStamp = int(time.mktime(timeArray))
    # print(timeStamp)
    add = AddressInterface()
    time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for i in range(20000, 20031):
        # payload={
        #     "title": f"测试{i}",
        #     "createLocation": "brother",
        #     "spaceId": 2,
        #     "parentId": ""
        # }
        # a=add.add_knwl(payload=payload)
        # # b=add.get_knwl()
        # # print(b)
        # print(a)

        # print(add.update_knwl(payload=payload))

        # st=['秦始皇','汉高祖','唐太宗','武则天','宋太祖','辽圣宗','成吉思汗','康熙','老子','孔子','墨子','','包拯','曹雪芹','诸葛亮','庄子']
        # j=random.sample(st,1)
        payload = {
            "id": i,
            "title": f"yyy性能测试{i}",
            "content": "<p><strong>云和恩墨,测试测试测试测试测试测试测试<span style=\"color: #e67e23;\">测试测试测试测试测试测试测试测试测试测试</span></strong><span style=\"background-color: #ffffff; color: #202122; font-size: 15.008px;\">2008年，文章在热播剧《</span><a style=\"font-size: 15.008px; text-decoration-line: none; color: #0645ad; background-image: none; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;\" title=\"奋斗 (2007年电视剧)\" href=\"https://zh.wikipedia.org/wiki/%E5%A5%8B%E6%96%97_(2007%E5%B9%B4%E7%94%B5%E8%A7%86%E5%89%A7)\">奋斗</a><span style=\"background-color: #ffffff; color: #202122; font-size: 15.008px;\">》中出演男二号向南，引起广泛关注。这也是文章和妻子马伊琍的第二次合作。2009年，文章进入电影届，主演第一部电影《走着瞧》。该片在上海国际电影节新片展映单元和东京国际电影节&ldquo;亚洲风&rdquo;单元获奖。文章也凭主演的北京青年马杰一角获得第12届上海国际电影节最受关注新人演员奖。2009年，文章主演电视剧《</span><a style=\"font-size: 15.008px; text-decoration-line: none; color: #0645ad; background-image: none; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;\" title=\"爱在日月潭\" href=\"https://zh.wikipedia.org/wiki/%E6%84%9B%E5%9C%A8%E6%97%A5%E6%9C%88%E6%BD%AD\">爱在日月潭</a><span style=\"background-color: #ffffff; color: #202122; font-size: 15.008px;\">》，参演热播电视剧《</span><a style=\"font-size: 15.008px; text-decoration-line: none; color: #0645ad; background-image: none; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;\" title=\"蜗居\" href=\"https://zh.wikipedia.org/wiki/%E8%9C%97%E5%B1%85\">蜗居</a><span style=\"background-color: #ffffff; color: #202122; font-size: 15.008px;\">》，成功饰演配角小贝，知名度得到进一步提高。2010年，文章与</span><a style=\"font-size: 15.008px; text-decoration-line: none; color: #0645ad; background-image: none; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;\" title=\"李连杰\" href=\"https://zh.wikipedia.org/wiki/%E6%9D%8E%E8%BF%9E%E6%9D%B0\">李连杰</a><span style=\"background-color: #ffffff; color: #202122; font-size: 15.008px;\">共同主演文艺片《</span><a style=\"font-size: 15.008px; text-decoration-line: none; color: #0645ad; background-image: none; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;\" title=\"海洋天堂\" href=\"https://zh.wikipedia.org/wiki/%E6%B5%B7%E6%B4%8B%E5%A4%A9%E5%A0%82\">海洋天堂</a><span style=\"background-color: #ffffff; color: #202122; font-size: 15.008px;\">》，文章饰演弱智青年大福，被认为是中国的&ldquo;</span><a class=\"mw-redirect\" style=\"font-size: 15.008px; text-decoration-line: none; color: #0645ad; background-image: none; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;\" title=\"达斯汀&middot;霍夫曼\" href=\"https://zh.wikipedia.org/wiki/%E8%BE%BE%E6%96%AF%E6%B1%80%C2%B7%E9%9C%8D%E5%A4%AB%E6%9B%BC\">达斯汀&middot;霍夫曼</a><span style=\"background-color: #ffffff; color: #202122; font-size: 15.008px;\">&rdquo;。文章凭此片获得第14届中国电影华表奖优秀新人男演员奖，第13届上海国际电影节最佳男主角奖和第18届北京大学生电影节最受大学生欢迎男演员奖。该片获得上海国际电影节&ldquo;金爵奖&rdquo;，中国电影华表奖优秀故事片奖和第18届北京大学生电影节人文关怀奖。同年，文章主演电视剧《</span><a style=\"font-size: 15.008px; text-decoration-line: none; color: #0645ad; background-image: none; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;\" title=\"雪豹 (电视剧)\" href=\"https://zh.wikipedia.org/wiki/%E9%9B%AA%E8%B1%B9_(%E7%94%B5%E8%A7%86%E5%89%A7)\">雪豹</a><span style=\"background-color: #ffffff; color: #202122; font-size: 15.008px;\">》，该剧被各大电视台反复播放。文章凭借周卫国一角获得第12届四川电视艺术节金熊猫奖电视剧类最佳男演员，第9届中国金鹰电视艺术节最具人气男演员和第26届中国电视金鹰奖最受观众喜爱男演员。</span></p>\n<h3 style=\"color: #000000; margin: 0.3em 0px 0px; padding-top: 0.5em; padding-bottom: 0px; overflow: hidden; font-size: 1.2em; line-height: 1.6; background-color: #ffffff;\"><span id=\".E6.88.90.E5.90.8D\"></span><span id=\"成名\" class=\"mw-headline\">成名</span><span class=\"mw-editsection\" style=\"user-select: none; font-size: small; font-weight: normal; margin-left: 1em; vertical-align: baseline; line-height: 1em; unicode-bidi: isolate; margin-right: 0px;\"><span class=\"mw-editsection-bracket\" style=\"margin-right: 0.25em; color: #54595d;\">[</span><a style=\"text-decoration-line: none; color: #0645ad; background: none; white-space: nowrap;\" title=\"编辑章节：成名\" href=\"https://zh.wikipedia.org/w/index.php?title=%E6%96%87%E7%AB%A0_(%E6%BC%94%E5%91%98)&amp;action=edit&amp;section=4&amp;editintro=Template:BLP_editintro\">编辑</a><span class=\"mw-editsection-bracket\" style=\"margin-left: 0.25em; color: #54595d;\">]</span></span></h3>\n<p style=\"margin-top: 0.5em; margin-bottom: 0.5em; color: #202122; font-size: 15.008px; background-color: #ffffff;\">2011年，文章在<a class=\"mw-redirect\" style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"滕华弢\" href=\"https://zh.wikipedia.org/wiki/%E6%BB%95%E5%8D%8E%E5%BC%A2\">滕华弢</a>导演、改编自<a class=\"mw-redirect\" style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"网络小说\" href=\"https://zh.wikipedia.org/wiki/%E7%BD%91%E7%BB%9C%E5%B0%8F%E8%AF%B4\">网络小说</a>的电视剧《<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"裸婚时代\" href=\"https://zh.wikipedia.org/wiki/%E8%A3%B8%E5%A9%9A%E6%99%82%E4%BB%A3\">裸婚时代</a>》中出演男主角刘易阳，被网友誉为灯笼男。文章在《<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"裸婚时代\" href=\"https://zh.wikipedia.org/wiki/%E8%A3%B8%E5%A9%9A%E6%99%82%E4%BB%A3\">裸婚时代</a>》中更身兼剧本策划，片中许多经典台词被年轻人推崇。文章凭此片获得<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"2011国剧盛典\" href=\"https://zh.wikipedia.org/wiki/2011%E5%9B%BD%E5%89%A7%E7%9B%9B%E5%85%B8\">2011国剧盛典</a>年度最佳男演员。由文章与<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"白百何\" href=\"https://zh.wikipedia.org/wiki/%E7%99%BD%E7%99%BE%E4%BD%95\">白百何</a>主演，<a class=\"mw-redirect\" style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"滕华弢\" href=\"https://zh.wikipedia.org/wiki/%E6%BB%95%E5%8D%8E%E5%BC%A2\">滕华弢</a>导演，改编自<a class=\"mw-redirect\" style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"网络小说\" href=\"https://zh.wikipedia.org/wiki/%E7%BD%91%E7%BB%9C%E5%B0%8F%E8%AF%B4\">网络小说</a>的电影《<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"失恋33天 (电视剧)\" href=\"https://zh.wikipedia.org/wiki/%E5%A4%B1%E6%81%8B33%E5%A4%A9_(%E7%94%B5%E8%A7%86%E5%89%A7)\">失恋33天</a>》在各大影院上映，创造了小成本电影的票房。文章凭王小贱一角获得第31届大众电影百花奖最佳男演员奖。他是第一个获此殊荣的80后男演员。在电影《万有引力》中，文章饰演其中一个单元的男主角高洋，该片入围加拿大蒙特利尔国际电影节最佳影片。文章也凭此片荣获第三届英国万像国际华语电影节优秀男配角奖。文章还参演了电影《白蛇传说》，饰演了一个非常抢眼的配角能忍。2012年，文章主演贺岁片《亲家过年》饰演男主角张雪伦。2013年，由文章主演的周星驰电影《西游&middot;降魔篇》打破华语片票房记录，收获全球票房2.15亿美元。同年文章自己经营的影视工作室-君竹（北京）影视文化有限公司参与投资制作的第一部影视作品《小爸爸》在大陆四大卫视黄金档播出。文章在该剧中不仅饰演男主角于果，还担任导演并参与剧本策划。这是文章第一次出任导演。文章凭<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"小爸爸\" href=\"https://zh.wikipedia.org/wiki/%E5%B0%8F%E7%88%B8%E7%88%B8\">《小爸爸</a>》获<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"2013国剧盛典\" href=\"https://zh.wikipedia.org/wiki/2013%E5%9B%BD%E5%89%A7%E7%9B%9B%E5%85%B8\">2013国剧盛典</a>&nbsp;观众喜爱的导演，该片同时获得2013国剧盛典十佳电视剧奖。妻子马伊琍在片中饰演女主角，并担任制片人。</p>\n<h3 style=\"color: #000000; margin: 0.3em 0px 0px; padding-top: 0.5em; padding-bottom: 0px; overflow: hidden; font-size: 1.2em; line-height: 1.6; background-color: #ffffff;\"><span id=\".E6.96.B0.E7.9A.84.E8.B5.B7.E7.82.B9\"></span><span id=\"新的起点\" class=\"mw-headline\">新的起点</span><span class=\"mw-editsection\" style=\"user-select: none; font-size: small; font-weight: normal; margin-left: 1em; vertical-align: baseline; line-height: 1em; unicode-bidi: isolate; margin-right: 0px;\"><span class=\"mw-editsection-bracket\" style=\"margin-right: 0.25em; color: #54595d;\">[</span><a style=\"text-decoration-line: none; color: #0645ad; background: none; white-space: nowrap;\" title=\"编辑章节：新的起点\" href=\"https://zh.wikipedia.org/w/index.php?title=%E6%96%87%E7%AB%A0_(%E6%BC%94%E5%91%98)&amp;action=edit&amp;section=5&amp;editintro=Template:BLP_editintro\">编辑</a><span class=\"mw-editsection-bracket\" style=\"margin-left: 0.25em; color: #54595d;\">]</span></span></h3>\n<p style=\"margin-top: 0.5em; margin-bottom: 0.5em; color: #202122; font-size: 15.008px; background-color: #ffffff;\">2014年，文章参演姜文导演的电影《一步之遥》，饰演主角之一武七。该片入围第65届柏林电影节。2016年，文章主演张黎导演的电视剧《<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"少帅\" href=\"https://zh.wikipedia.org/wiki/%E5%B0%91%E5%B8%85\">少帅</a>》饰演历史人物张学良。文章凭此片获得2017中国电视剧品质盛典年度品质表演剧星。同年七月，由文章的君竹（上海）影视文化有限公司参与制作的喜剧爱情电影《陆垚知马俐》在中国大陆，美国，加拿大，澳大利亚及新西兰上映。文章不仅担任导演，还兼任编剧。此片以中小成本获得近2亿票房。文章的导演风格被一些影评人誉为&ldquo;文房四宝&rdquo;-- &ldquo;斗嘴皮、飙演技、抖机灵、戳心窝&rdquo;。文章凭此处女作提名第十九届上海国际电影节之亚洲新人奖最佳导演奖。同年八月《陆垚知马俐》获得第40届加拿大蒙特利尔国际电影节中国电影银奖。2017年，《陆垚知马俐》获得第31届中国电影金鸡奖七项提名 - 最佳导演处女作，最佳男主角，最佳女主角，最佳男配角，最佳女配角，最佳录音和最佳摄影。最后文章荣获最佳导演处女作奖。2017年，文章的君竹（上海）影视文化有限公司参与制作谍战剧《剃刀边缘》，文章担任导演并饰演男主角许从良。妻子马伊俐出演女主角。此片打破以往谍战剧的套路，以小人物的成长为主线，加入爱情，探案等元素。电视剧播出后，口碑收视均取得良好的成绩。</p>\n<p style=\"margin-top: 0.5em; margin-bottom: 0.5em; color: #202122; font-size: 15.008px; background-color: #ffffff;\">2017年11月12日，由文章编剧并导演，阿里巴巴创始人马云主演的微电影《功守道》在优酷独家播出。这部只有22分钟的短片汇集了当今中国顶尖功夫明星和武术指导，包括李连杰，甄子丹，吴京，袁和平，洪金宝以及程小东。电影播出不到两天，网络点击率突破1.5亿，评论量1.5万，顶8.1万。</p>\n<h3 style=\"color: #000000; margin: 0.3em 0px 0px; padding-top: 0.5em; padding-bottom: 0px; overflow: hidden; font-size: 1.2em; line-height: 1.6; background-color: #ffffff;\"><span id=\".E9.87.8D.E8.BF.94.E8.88.9E.E5.8F.B0\"></span><span id=\"重返舞台\" class=\"mw-headline\">重返舞台</span><span class=\"mw-editsection\" style=\"user-select: none; font-size: small; font-weight: normal; margin-left: 1em; vertical-align: baseline; line-height: 1em; unicode-bidi: isolate; margin-right: 0px;\"><span class=\"mw-editsection-bracket\" style=\"margin-right: 0.25em; color: #54595d;\">[</span><a style=\"text-decoration-line: none; color: #0645ad; background: none; white-space: nowrap;\" title=\"编辑章节：重返舞台\" href=\"https://zh.wikipedia.org/w/index.php?title=%E6%96%87%E7%AB%A0_(%E6%BC%94%E5%91%98)&amp;action=edit&amp;section=6&amp;editintro=Template:BLP_editintro\">编辑</a><span class=\"mw-editsection-bracket\" style=\"margin-left: 0.25em; color: #54595d;\">]</span></span></h3>\n<p style=\"margin-top: 0.5em; margin-bottom: 0.5em; color: #202122; font-size: 15.008px; background-color: #ffffff;\">2017年3月已经签约上海话剧艺术中心的文章出演独角话剧《每一件美妙的小事》，文章一人演满90分钟，以细腻而真挚的表演，将母与子的情感对峙、亲情中爱与恨的挣扎，展现得淋漓尽致。这是一部成长的独角戏，文章以收放自如的表演，体现了忧郁的诗意，荣获2017年上海静安现代戏剧谷&ldquo;壹戏剧大赏&rdquo;年度最佳男演员。</p>\n<p style=\"margin-top: 0.5em; margin-bottom: 0.5em; color: #202122; font-size: 15.008px; background-color: #ffffff;\">2018年10月18日到11月3日，文章领衔主演中德合作话剧《茶馆》。这部话剧由著名先锋导演孟京辉执导，德国知名戏剧构作塞巴斯蒂安&bull;凯撤担任戏剧构作。这版《茶馆》在乌镇戏剧节成为开幕话剧，开票仅三分钟，4400张票即告售罄。文章在剧中有大段爆发式独白，他以多年的表演功底和艺术能量的积累，用自由真实的表达征服在场观众。这是文章和舞台的亲密接触，更是他对表演和经典的致敬。2019年代表国际当代戏剧最高水准的阿维尼翁IN戏剧节公布官方特邀名单，《茶馆》作为首部中国大陆剧目入围IN戏剧节。</p>\n<h2 style=\"color: #000000; margin: 1em 0px 0.25em; padding: 0px; overflow: hidden; border-bottom: 1px solid #a2a9b1; font-weight: normal; font-family: 'Linux Libertine', Georgia, Times, serif; line-height: 1.3; background-color: #ffffff;\"><span id=\".E5.80.8B.E4.BA.BA.E7.94.9F.E6.B4.BB\"></span><span id=\"個人生活\" class=\"mw-headline\">个人生活</span><span class=\"mw-editsection\" style=\"font-family: sans-serif; user-select: none; font-size: small; margin-left: 1em; vertical-align: baseline; line-height: 1em; unicode-bidi: isolate; margin-right: 0px;\"><span class=\"mw-editsection-bracket\" style=\"margin-right: 0.25em; color: #54595d;\">[</span><a style=\"text-decoration-line: none; color: #0645ad; background: none; white-space: nowrap;\" title=\"编辑章节：个人生活\" href=\"https://zh.wikipedia.org/w/index.php?title=%E6%96%87%E7%AB%A0_(%E6%BC%94%E5%91%98)&amp;action=edit&amp;section=7&amp;editintro=Template:BLP_editintro\">编辑</a><span class=\"mw-editsection-bracket\" style=\"margin-left: 0.25em; color: #54595d;\">]</span></span></h2>\n<p style=\"margin-top: 0.5em; margin-bottom: 0.5em; color: #202122; font-size: 15.008px; background-color: #ffffff;\">文章的父母都是<a class=\"mw-redirect\" style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"公务员\" href=\"https://zh.wikipedia.org/wiki/%E5%85%AC%E5%8A%A1%E5%91%98\">公务员</a>，父亲在<a class=\"mw-redirect\" style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"中共\" href=\"https://zh.wikipedia.org/wiki/%E4%B8%AD%E5%85%B1\">中共</a><a class=\"mw-redirect\" style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"陕西\" href=\"https://zh.wikipedia.org/wiki/%E9%99%95%E8%A5%BF\">陕西</a>省委办公厅任职，母亲则在<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"陕西省\" href=\"https://zh.wikipedia.org/wiki/%E9%99%95%E8%A5%BF%E7%9C%81\">陕西省</a>政府工作。2006年毕业于<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"中央戏剧学院\" href=\"https://zh.wikipedia.org/wiki/%E4%B8%AD%E5%A4%AE%E6%88%8F%E5%89%A7%E5%AD%A6%E9%99%A2\">中央戏剧学院</a>2002级表演系。与<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"唐嫣\" href=\"https://zh.wikipedia.org/wiki/%E5%94%90%E5%AB%A3\">唐嫣</a>、<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"白百何\" href=\"https://zh.wikipedia.org/wiki/%E7%99%BD%E7%99%BE%E4%BD%95\">白百何</a>、<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"童瑶\" href=\"https://zh.wikipedia.org/wiki/%E7%AB%A5%E7%91%B6\">童瑶</a>、<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"孙坚 (演员)\" href=\"https://zh.wikipedia.org/wiki/%E5%AD%99%E5%9D%9A_(%E6%BC%94%E5%91%98)\">孙坚</a>、<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"郭珍霓\" href=\"https://zh.wikipedia.org/wiki/%E9%83%AD%E7%8F%8D%E9%9C%93\">郭珍霓</a>、<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"曹曦文\" href=\"https://zh.wikipedia.org/wiki/%E6%9B%B9%E6%9B%A6%E6%96%87\">曹曦文</a>、<a class=\"mw-redirect\" style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"徐百卉\" href=\"https://zh.wikipedia.org/wiki/%E5%BE%90%E7%99%BE%E5%8D%89\">徐百卉</a>、<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"张博 (1982年)\" href=\"https://zh.wikipedia.org/wiki/%E5%BC%A0%E5%8D%9A_(1982%E5%B9%B4)\">张博</a>、<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"斓曦\" href=\"https://zh.wikipedia.org/wiki/%E6%96%93%E6%9B%A6\">斓曦</a>、<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"毛俊杰\" href=\"https://zh.wikipedia.org/wiki/%E6%AF%9B%E4%BF%8A%E6%9D%B0\">毛俊杰</a>、<a class=\"new\" style=\"text-decoration-line: none; color: #ba0000; background: none;\" title=\"陈思斯（页面不存在）\" href=\"https://zh.wikipedia.org/w/index.php?title=%E9%99%88%E6%80%9D%E6%96%AF&amp;action=edit&amp;redlink=1\">陈思斯</a>、<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"杨烁\" href=\"https://zh.wikipedia.org/wiki/%E6%9D%A8%E7%83%81\">杨烁</a>、<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"霍政谚\" href=\"https://zh.wikipedia.org/wiki/%E9%9C%8D%E6%94%BF%E8%AB%BA\">霍政谚</a>、<a class=\"new\" style=\"text-decoration-line: none; color: #ba0000; background: none;\" title=\"王雨（页面不存在）\" href=\"https://zh.wikipedia.org/w/index.php?title=%E7%8E%8B%E9%9B%A8&amp;action=edit&amp;redlink=1\">王雨</a>、<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"邹廷威\" href=\"https://zh.wikipedia.org/wiki/%E9%82%B9%E5%BB%B7%E5%A8%81\">邹廷威</a>、<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"张默 (演员)\" href=\"https://zh.wikipedia.org/wiki/%E5%BC%A0%E9%BB%98_(%E6%BC%94%E5%91%98)\">张默</a>等为同班同学。妻子则是艺人<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"马伊琍\" href=\"https://zh.wikipedia.org/wiki/%E9%A9%AC%E4%BC%8A%E7%90%8D\">马伊琍</a>，女方比男方年长8岁，两人在2008年结婚，育有两女，大女儿文君竹。文章右小腿整段的龙型刺青是送给妻子的图腾。2019年7月28日，文章在微博宣布和<a style=\"text-decoration-line: none; color: #0645ad; background: none;\" title=\"马伊琍\" href=\"https://zh.wikipedia.org/wiki/%E9%A9%AC%E4%BC%8A%E7%90%8D\">马伊琍</a>离婚。</p>\n<p><span style=\"background-color: #ffffff; color: #202122; font-size: 15.008px;\">2019年11月8日，文章承认新恋情，女方是一名小12岁的空中小姐任涵晴。2020年2月30日，文章被拍与任涵晴进出妇产科，被爆料女方怀孕。同年7月9日，有一名居住与英国的华人表示看见文章与怀有身孕的任涵晴在英国伦敦散步。2020年7月12日，文章透过经纪公司承认女友已怀孕。同年8月1日，任涵晴产下一子。2020年10月1日，文章表示不会再婚，也不可能与任涵晴注册，原因是自己不想因为一张纸而失去自由。</span><strong><span style=\"color: #e67e23;\">22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222233</span></strong><strong><span style=\"color: #e67e23;\">2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222223333333333333333</span></strong><strong><span style=\"color: #e67e23;\">2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222223333333333333333</span></strong><strong><span style=\"color: #e67e23;\">2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222223333333333333333</span></strong><strong><span style=\"color: #e67e23;\">33333333333333</span></strong><strong><span style=\"color: #e67e23;\">2</span></strong><strong><span style=\"color: #e67e23;\">测试</span></strong><strong><span style=\"color: #e67e23;\">测试</span></strong><strong><span style=\"color: #e67e23;\">测试</span></strong><strong><span style=\"color: #e67e23;\">222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222223333333333333333</span></strong><strong><span style=\"color: #e67e23;\">2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222223333333333333333</span></strong><strong><span style=\"color: #e67e23;\">2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222223333333333333333</span></strong><strong><span style=\"color: #e67e23;\">测试</span></strong><strong><span style=\"color: #e67e23;\">测试</span></strong><strong><span style=\"color: #e67e23;\">测试</span></strong><strong><span style=\"color: #e67e23;\">测试</span></strong></p>",
            "brief": "云和恩墨,测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试2008年，文章在热播剧《奋斗》中出演男二号向南，引起广泛关注。这也是文章和妻子马伊琍的第二次合作。2009年，文章进入电影届，主演第一部电影《走着瞧》。该片在上海国际电影节新片展映单元和东京国际电影节“亚洲风”单元获奖。文章也凭主演的北京青年马杰一角获得第12届上海国际电影节最受关注新人演员奖。2009年，文章主演电视剧《爱在日月潭》，参演热播电视剧《蜗居》，成功饰演配角小贝，知名度得到进一步提高。2010年，文章与李连杰共同主演文艺片《海洋天堂》，文章饰演弱智青年大福，被认为是中国的“达斯汀·霍夫曼”。文章凭此片获得第14届中国电影华表奖优秀新人男演员奖，第13届上海国际电影节最佳男主角奖和第18届北京大学生电影节最受大学生欢迎男演员奖。该片获得上海国际电影节“金爵奖”，中国电影华表奖优秀故事片奖和第18届北京大学生电影节人文关怀奖。同年，文章主演电视剧《雪豹》，该剧被各大电视台反复播放。文章凭借周卫国一角获得第12届四川电视艺术节金熊猫奖电视剧类最佳男演员，第9届中国金鹰电视艺术节最具人气男演员和第26届中国电视金鹰奖最受观众喜爱男演员。\n成名[编辑]\n2011年，文章在滕华弢导演、改编自网络小说的电视剧《裸婚时代》中出演男主角刘易阳，被网友誉为灯笼男。文章在《裸婚时代》中更身兼剧本策划，片中许多经典台词被年轻人推崇。文章凭此片获得2011国剧盛典年度最佳男演员。由文章与白百何主演，滕华弢导演，改编自网络小说的电影《失恋33天》在各大影院上映，创造了小成本电影的票房。文章凭王小贱一角获得第31届大众电影百花奖最佳男演员奖。他是第一个获此殊荣的80后男演员。在电影《万有引力》中，文章饰演其中一个单元的男主角高洋，该片入围加拿大蒙特利尔国际电影节最佳影片。文章也凭此片荣获第三届英国万像国际华语电影节优秀男配角奖。文章还参演了电影《白蛇传说》，饰演了一个非常抢眼的配角能忍。2012年，文章主演贺岁片《亲家过年》饰演男主角张雪伦。2013年，由文章主演的周星驰电影《西游·降魔篇》打破华语片票房记录，收获全球票房2.15亿美元。同年文章自己经营的影视工作室-君竹（北京）影视文化有限公司参与投资制作的第一部影视作品《小爸爸》在大陆四大卫视黄金档播出。文章在该剧中不仅饰演男主角于果，还担任导演并参与剧本策划。这是文章第一次出任导演。文章凭《小爸爸》获2013国剧盛典 观众喜爱的导演，该片同时获得2013国剧盛典十佳电视剧奖。妻子马伊琍在片中饰演女主角，并担任制片人。\n新的起点[编辑]\n2014年，文章参演姜文导演的电影《一步之遥》，饰演主角之一武七。该片入围第65届柏林电影节。2016年，文章主演张黎导演的电视剧《少帅》饰演历史人物张学良。文章凭此片获得2017中国电视剧品质盛典年度品质表演剧星。同年七月，由文章的君竹（上海）影视文化有限公司参与制作的喜剧爱情电影《陆垚知马俐》在中国大陆，美国，加拿大，澳大利亚及新西兰上映。文章不仅担任导演，还兼任编剧。此片以中小成本获得近2亿票房。文章的导演风格被一些影评人誉为“文房四宝”-- “斗嘴皮、飙演技、抖机灵、戳心窝”。文章凭此处女作提名第十九届上海国际电影节之亚洲新人奖最佳导演奖。同年八月《陆垚知马俐》获得第40届加拿大蒙特利尔国际电影节中国电影银奖。2017年，《陆垚知马俐》获得第31届中国电影金鸡奖七项提名 - 最佳导演处女作，最佳男主角，最佳女主角，最佳男配角，最佳女配角，最佳录音和最佳摄影。最后文章荣获最佳导演处女作奖。2017年，文章的君竹（上海）影视文化有限公司参与制作谍战剧《剃刀边缘》，文章担任导演并饰演男主角许从良。妻子马伊俐出演女主角。此片打破以往谍战剧的套路，以小人物的成长为主线，加入爱情，探案等元素。电视剧播出后，口碑收视均取得良好的成绩。\n2017年11月12日，由文章编剧并导演，阿里巴巴创始人马云主演的微电影《功守道》在优酷独家播出。这部只有22分钟的短片汇集了当今中国顶尖功夫明星和武术指导，包括李连杰，甄子丹，吴京，袁和平，洪金宝以及程小东。电影播出不到两天，网络点击率突破1.5亿，评论量1.5万，顶8.1万。\n重返舞台[编辑]\n2017年3月已经签约上海话剧艺术中心的文章出演独角话剧《每一件美妙的小事》，文章一人演满90分钟，以细腻而真挚的表演，将母与子的情感对峙、亲情中爱与恨的挣扎，展现得淋漓尽致。这是一部成长的独角戏，文章以收放自如的表演，体现了忧郁的诗意，荣获2017年上海静安现代戏剧谷“壹戏剧大赏”年度最佳男演员。\n2018年10月18日到11月3日，文章领衔主演中德合作话剧《茶馆》。这部话剧由著名先锋导演孟京辉执导，德国知名戏剧构作塞巴斯蒂安•凯撤担任戏剧构作。这版《茶馆》在乌镇戏剧节成为开幕话剧，开票仅三分钟，4400张票即告售罄。文章在剧中有大段爆发式独白，他以多年的表演功底和艺术能量的积累，用自由真实的表达征服在场观众。这是文章和舞台的亲密接触，更是他对表演和经典的致敬。2019年代表国际当代戏剧最高水准的阿维尼翁IN戏剧节公布官方特邀名单，《茶馆》作为首部中国大陆剧目入围IN戏剧节。\n个人生活[编辑]\n文章的父母都是公务员，父亲在中共陕西省委办公厅任职，母亲则在陕西省政府工作。2006年毕业于中央戏剧学院2002级表演系。与唐嫣、白百何、童瑶、孙坚、郭珍霓、曹曦文、徐百卉、张博、斓曦、毛俊杰、陈思斯、杨烁、霍政谚、王雨、邹廷威、张默等为同班同学。妻子则是艺人马伊琍，女方比男方年长8岁，两人在2008年结婚，育有两女，大女儿文君竹。文章右小腿整段的龙型刺青是送给妻子的图腾。2019年7月28日，文章在微博宣布和马伊琍离婚。\n2019年11月8日，文章承认新恋情，女方是一名小12岁的空中小姐任涵晴。2020年2月30日，文章被拍与任涵晴进出妇产科，被爆料女方怀孕。同年7月9日，有一名居住与英国的华人表示看见文章与怀有身孕的任涵晴在英国伦敦散步。2020年7月12日，文章透过经纪公司承认女友已怀孕。同年8月1日，任涵晴产下一子。2020年10月1日，文章表示不会再婚，也不可能与任涵晴注册，原因是自己不想因为一张纸而失去自由。22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222233222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222333333333333333322222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222233333333333333332222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222223333333333333333333333333333332测试测试测试22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222333333333333333322222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222233333333333333332222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222223333333333333333测试测试测试测试",
            "updateTime": f"{time_stamp}",
            "parentId": ""
        }

        print(add.update_knwl(payload=payload))

