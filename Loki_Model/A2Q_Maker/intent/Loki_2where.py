#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for 2where

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict,
        pattern       str

    Output:
        resultDICT    dict
"""

from random import sample
import json
import os
import sys

INTENT_NAME = "2where"
CWD_PATH = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(os.path.dirname(CWD_PATH), "lib"))

from Account import *
"""
Account 變數清單
[變數] BASE_PATH         => 根目錄位置
[變數] LIB_PATH          => lib 目錄位置
[變數] INTENT_PATH       => intent 目錄位置
[變數] REPLY_PATH        => reply 目錄位置
[變數] ACCOUNT_DICT      => account.info 內容
[變數] ARTICUT           => ArticutAPI (用法：ARTICUT.parse()。 #需安裝 ArticutAPI.)
[變數] USER_DEFINED_FILE => 使用者自定詞典的檔案路徑
[變數] USER_DEFINED_DICT => 使用者自定詞典內容
"""

sys.path.pop(-1)

# userDefinedDICT (Deprecated)
# 請使用 Account 變數 USER_DEFINED_DICT 代替
#userDefinedDICT = {}
#try:
#    userDefinedDICT = json.load(open(os.path.join(CWD_PATH, "USER_DEFINED.json"), encoding="utf-8"))
#except:
#    pass

replyDICT = {}
replyPathSTR = os.path.join(REPLY_PATH, "reply_{}.json".format(INTENT_NAME))
if os.path.exists(replyPathSTR):
    try:
        replyDICT = json.load(open(replyPathSTR, encoding="utf-8"))
    except Exception as e:
        print("[ERROR] reply_{}.json => {}".format(INTENT_NAME, str(e)))
CHATBOT = True if replyDICT else False

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if ACCOUNT_DICT["debug"]:
        print("[{}] {} ===> {}".format(INTENT_NAME, inputSTR, utterance))

def getReply(utterance, args):
    try:
        replySTR = sample(replyDICT[utterance], 1)[0].format(*args)
    except:
        replySTR = ""

    return replySTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern="", toolkitDICT={}):
    debugInfo(inputSTR, utterance)
    if utterance == "[諾快寧口服懸液用粉劑]的儲存[條件]是[本藥]未[開封][可]儲存於[室溫](<[ 30°C])。泡製[後]需冷藏，[可]存放[7天]。":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            pass

    if utterance == "[威洛速膜衣錠 (5/片)]的[產地]是[義大利]":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            articutResultDICT = ARTICUT.parse(args[2])
            if articutResultDICT["result_pos"][0][0].startswith("<LOCATION>"):
                resultDICT["WhereQ"].append(f"{args[0]}的{args[1]}是哪裡")

    if utterance == "[威洛速膜衣錠 (5/片)]的[產地]是[台灣]":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["WhereQ"].append(f"{args[0]}的{args[1]}是哪裡")

    return resultDICT


if __name__ == "__main__":
    from pprint import pprint

    resultDICT = getResult("諾快寧口服懸液用粉劑的儲存條件是本藥未開封可儲存於室溫(< 30°C)。泡製後需冷藏，可存放7天。", "[諾快寧口服懸液用粉劑]的儲存[條件]是[本藥]未[開封][可]儲存於[室溫](<[ 30°C])。泡製[後]需冷藏，[可]存放[7天]。", [], {}, {})
    pprint(resultDICT)