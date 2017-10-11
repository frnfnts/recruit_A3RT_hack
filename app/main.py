#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from PhraseClient import PhraseClient

def main(argv):
    sample_terms = [u"私", u"幸せ", u"神", u"人間", u"幸福", u"人生", u"酒", u"不幸", u"孤独", u"時", u"金"]

    if len(argv) < 1:
        idx = random.randint(0, len(sample_terms)-1)
        text = sample_terms[idx]
    else:
        text = argv[0].decode("shift-jis")

    client = PhraseClient()
    if client.check_typo(text)[0] == 1:
        print "正しい日本語の単語を入力してください"
        return
    text = client.process(text)
    print text.encode("utf-8")
