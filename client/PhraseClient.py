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
        self.joshis = [
                u"くらい", 
                u"けれど", 
                u"ばかり", 
                u"なり", 
                u"だの", 
                u"まで", 
                u"だけ", 
                u"ほど", 
                u"など", 
                u"やら", 
                u"こそ", 
                u"でも", 
                u"しか", 
                u"さえ", 
                u"だに", 
                u"ても", 
                u"のに", 
                u"ので", 
                u"たつ", 
                u"つつ", 
                u"から", 
                u"より", 
                u"には", 
                u"し", 
                u"は", 
                u"て", 
                u"も", 
                u"が", 
                u"の", 
                u"を", 
                u"に", 
                u"へ", 
                u"と", 
                u"で", 
                u"や", 
                u"ば", 
                u"、",
        ]

    def __get_suggestions(self, prev):
        params = {
            "apikey": self.suggest_key,
            "style":"496fe575-1908-4413-bac3-29ec3d10f51d",
            "previous_description": "",
            "separation": 2
        }
        res = requests.get("https://api.a3rt.recruit-tech.co.jp/text_suggest/v2/predict", params=params).json()
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
            raise 

    def get_typo_position(self, res):
        typo = res["alerts"][0]["word"]
        checked = res["alerts"][0]["checkedSentence"]
        checked = re.sub("\s+", "", checked)
        print checked.encode("utf-8")
        pos = re.search(u"<<{typo}>>".format(typo=typo), checked).start()
        return pos

    def trim(self, text, pos):
        for joshi in self.joshis:
            text = text[:pos]
            if text.endswith(joshi):
                text = text[:-len(joshi)]
                break
        return text

    def suggestion_iter(self, text):
        while True:
            for s in self.__get_suggestions(text):
                yield s

    def process(self, text):
        i = 0
        for suggestion in self.suggestion_iter(text):
            text += suggestion
            text = re.sub("\s+", "", text)

            status, res = self.check_typo(text)
            if status == 0:
                break
            pos = self.get_typo_position(res)
            #pos = re.search(res["alerts"][0]["word"], text).start()
            text = self.trim(text, pos)
            print text.encode("utf-8")
            i += 1
            if i == 10:
                break

        return text

    #def process(self, original_text):
        #for suggestion in self.suggestion_iter(original_text):
        #    text = original_text + suggestion
        #    text = re.sub("\s+", "", text)

        #    status, res = self.check_typo(text)
        #    if status == 0:
        #        break
        #return text



if __name__ == '__main__':
    client = PhraseClient()
    text = sys.argv[1].decode("shift-jis")
    text = client.process(text)
    print text.encode("utf-8")
