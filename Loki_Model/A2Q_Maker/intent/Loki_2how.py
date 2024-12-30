#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for 2how

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

INTENT_NAME = "2how"
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
    if utterance == "[依普芬口服懸液劑]的[用藥]指導包含[使用前須搖勻; 用藥後若發生喉痛、口腔/黏膜潰瘍、皮疹等症狀，應考慮可能為藥品不良反應，宜立即就醫並考慮停藥]":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["HowQ"].append(f"{args[0]}怎麼使用？")

    if utterance == "[優力黴素口服懸液用顆粒]的注意[事項]是 [1.請勿直接倒出乾粉服用。 2.請先酌量加冷開水濕潤藥粉，接著持續加冷開水至60cc處。完成泡製後，再遵照藥袋上用法說明服用。 3.泡製後需冰箱冷藏，使用前請搖勻。 4.若對penicillin過敏的患者，使用cephalosporin類藥品應特別小心。]":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["HowQ"].append(f"{args[0]}怎麼使用？")

    if utterance == "[喜華膜衣錠]的[用藥]指導是[味覺差，不宜磨粉；請按時服藥至療程結束]":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["HowQ"].append(f"{args[0]}怎麼使用？")

    if utterance == "[安寶錠]的[用法]是[口服]":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            if "法" in args[1]:
                resultDICT["HowQ"].append(f"{args[0]}怎麼使用？")

    if utterance == "[安寶錠]的儲存[條件]是 [25°C以下儲存]":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["HowQ"].append(f"{args[0]}怎麼儲存？")

    if utterance == "[康是鉀持續性藥效錠]的儲存[條件]是[室溫](<[ 25°C])":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["HowQ"].append(f"{args[0]}怎麼儲存？")

    if utterance == "[諾快寧口服懸液用粉劑]的儲存[條件]是[本藥]未[開封][可]儲存於[室溫](<[ 30°C])。泡製[後]需冷藏，[可]存放[7天]。":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["HowQ"].append(f"{args[0]}怎麼儲存？")

    return resultDICT


if __name__ == "__main__":
    from pprint import pprint

    resultDICT = getResult("安寶錠的用法是口服", "[安寶錠]的[用法]是[口服]", [], {}, {})
    pprint(resultDICT)