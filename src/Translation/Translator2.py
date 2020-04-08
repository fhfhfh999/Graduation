# 百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json


class Translator2:
    def __init__(self):
        self.appid = '20200406000413281'  # 填写你的appid
        self.secretKey = 'odv6OE3A2xy3V9bBWfzx'  # 填写你的密钥
        self.httpClient = None
        self.myurl = '/api/trans/vip/translate'
        self.fromLang = 'zh'  # 原文语种
        self.toLang = 'en'  # 译文语种
        self.salt = random.randint(32768, 65536)

    def translate(self, sentence):
        q = sentence
        sign = self.appid + q + str(self.salt) + self.secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()

        myurl = self.myurl + '?appid=' + self.appid + '&q=' + urllib.parse.quote(
            q) + '&from=' + self.fromLang + '&to=' + self.toLang + '&salt=' + str(
            self.salt) + '&sign=' + sign

        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)

            # result的格式：{'from': 'zh', 'to': 'en', 'trans_result': [{'src': '这是一个测试用例', 'dst': 'This is a test case'}]}
            return result.get('trans_result')[0].get('dst')

        except Exception as e:
            print(e)
            return None
        finally:
            if httpClient:
                httpClient.close()


def getTranslator():
    translator = Translator2()
    return translator


if __name__ == "__main__":
    translator = getTranslator()
    translation = translator.translate("今天天气真好")
    print(translation)
