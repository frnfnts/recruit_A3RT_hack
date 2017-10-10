# coding: utf-8
import requests
import os
import sys
import re
from pprint import pprint

class PhraseClient:
    def __init__(self):
        self.suggest_key = os.environ["TEXTKEY"]
        self.typo_key= os.environ["TYPOKEY"]

    def __get_suggestions(self, prev):
        params = {
            "apikey": self.suggest_key,
            "style":"496fe575-1908-4413-bac3-29ec3d10f51d",
            "previous_description": "",
            "separation": 2
        }
        res = requests.get("https://api.a3rt.recruit-tech.co.jp/text_suggest/v2/predict", params=params).json()
        if res["status"] != 0:
            print "Error occurred"
            raise
        return res["suggestion"]

    def check_typo(self, text):
        params = {
            "apikey": self.typo_key,
            "sentence": text
        }
        res = requests.get("https://api.a3rt.recruit-tech.co.jp/proofreading/v1/typo", params=params).json()
        status = res["status"]
        if status == 0 or status == 1:
            return status, res
        else:
            print "Error occurred"
            raise 

    def suggestion_iter(self, text):
        while True:
        #for _ in xrange(3):
            for s in self.__get_suggestions(text):
                yield s

    def process(self, original_text):
        for suggestion in self.suggestion_iter(original_text):
            text = original_text + suggestion
            text = re.sub("\s+", "", text)
            #print text.encode("utf-8")

            status, res = self.check_typo(text)
            if status == 0:
                break
        return text


if __name__ == '__main__':
    client = PhraseClient()
    text = sys.argv[1].decode("shift-jis")
    if client.check_typo(text)[0] == 1:
        print "もっといい文を指定してください"
        exit()
    text = client.process(text)
    print text.encode("utf-8")
