# coding: utf-8
from django.http import HttpResponseRedirect

from libs.utils.com_redis import rd
from libs.utils import ajax
from com.common import add_login

def getList(request):
    """
    获取电影列表接口
    :param request:
    :return:
    """
    data = [
        {
            "title": "冰雪奇缘",
            "year": "2013",
            "image": "https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=3177904474,804197209&fm=58&s=380ECF14CC5070C48E8103E30300E0B6"
        },
        {
            "title": "少年的你",
            "year": "2019",
            "image": "https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=2975901083,2518363767&fm=58"
        },
        {
            "title": "决战中途岛",
            "year": "2017",
            "image": "https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3968843651,3142886574&fm=58&app=83&f=JPEG?w=200&h=266&s=F185B5541A523FDC6A21501C030010D2"
        },
        {
            "title": "天气之子",
            "year": "2020",
            "image": "https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=856216442,2449137646&fm=58&s=9B3B608488406EDC40360C510300C0BA"
        },
        {
            "title": "终结者:黑暗命运",
            "year": "2019",
            "image": "https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=592768200,348740025&fm=58&s=27449D4F1AAB96DE0C5D4DB703001042"
        },
        {
            "title": "寄生虫",
            "year": "2019",
            "image": "https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3717282104,1079711651&fm=58&s=6A292DC0420F22FA2A73CB08030040CD"
        },
        {
            "title": "小丑",
            "year": "2019",
            "image": "https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=164951256,3171893138&fm=58&app=83&f=JPEG?w=400&h=533&s=BF904CCFD40458FC6B94843003002053"
        },
        {
            "title": "罗小黑战记",
            "year": "2018",
            "image": "https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=1926260292,4161349232&fm=58&s=6E8166854412B7FF8C39B5A603007001"
        },
        {
            "title": "海上钢琴师",
            "year": "2018",
            "image": "https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=2638357740,420644212&fm=58&s=B3367084D05EB5CC4EA749110300D09A"
        },
        {
            "title": "安娜",
            "year": "2016",
            "image": "https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=3442822375,1298138196&fm=58&s=B55A637F0542474946E024DE0100C032"
        },
    ]

    return ajax.ajax_ok(request, {"movie_list": data})