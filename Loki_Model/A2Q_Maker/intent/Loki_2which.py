#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for 2which

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

INTENT_NAME = "2which"
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
    if utterance == "[威洛速膜衣錠 (5/片)]的注意[事項]包含[ 1]、[口服][劑型]與含有[Mg2]+、[AL3]+之[制][酸劑]或[多價陽][離子][製劑]([Fe2]+、[Zn2]+)併用時，[會]導致吸收低下，[效果]減弱，請避免併用。[ 2]、[Moxifloxacin]使用於<[18][歲][族群]之[安全][性]尚未確立，[動物]研究觀察到[Moxifloxacin] [會]造成未[成年動物][關節][病變]，[十八][歲][以下]不建議使用。[ 3]、[Moxifloxacin]與[cisapride]、[erythromycin]、[antipsychotics]、[tricyclic] [antidepressants]、[procainamide]、[quinidine]、[amiodarone]、[sotalol]併用[可能][會]延長[QT]間隔，故不建議併用，":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["WhichQ"].append(f"{args[0]}的注意{args[1]}有哪些")
            resultDICT["WhichQ"].append(f"{args[0]}有哪些注意{args[1]}")

    if utterance == "[立普妥膜衣錠]的[健保]規定包含[ 2.6].降[血脂][藥物][ Drugs] [used] [for] [dyslipidemia][ 2.6].[1].[全民][健康]保降[血脂][藥物]給付[規定表] ([86]/[1]/[1]、[87]/[4]/[1]、[87]/[7]/[1]、[91]/[9]/[1]、[93]/[9]/[1]、[97]/[7]/[1]、[102]/[8]/[1]、[108]/[2]/[1])      [全民][健康][保險]降[膽固醇][藥物]給付[規定表] 非[藥物]治療 [起始][藥物]治療 [血脂]值 [血脂目標]值 [處方]規定[ 1].有[急性][冠狀動][脈症候群]病史[ 2].曾接受[心導][管]介入治療或[外科][冠動][脈]搭橋[手術]之[冠狀][動脈粥][狀]硬化[患者]([108]/[2]/[1]) 與[藥物]治療[可]並[行][ LDL-C][≧][70 mg]/[dL][ LDL-C]＜[70 mg]/[dL ]第[一年][應]每[3]-[6個月]抽血檢查[一次]，第[二年][以][後][應][至少]每[6]-[12個月]抽血檢查[一次]，[同時]請注意[副]作用之產生如[肝功能][異常]，[橫][紋肌][溶解症]。 [心][血管][疾病] 或[糖尿病][患者] 與[藥物]治療[可]並[行][ TC][≧][160 mg]/[dL]或[ LDL-C][≧][100 mg]/[dL] [TC]＜[160 mg]/[dL]或[ LDL-C]＜[100 mg]/[dL][ 2個][危險][因子]或[以上]給[藥][前][應]有[3]-[6個月]非[藥物]治療[ TC][≧][200 mg]/[dL]或[ LDL-C][≧][130 mg]/[dL] [TC]＜[200 mg]/[dL]或[ LDL-C]＜[130 mg]/[dL][ 1個][危險][因子]給[藥][前][應]有[3]-[6個月]非[藥物]治療[ TC][≧][240 mg]/[dL]或[ LDL-C][≧][160 mg]/[dL] [TC]＜[240 mg]/[dL]或[ LDL-C]＜[160 mg]/[dL][ 0個][危險][因子]給[藥][前][應]有[3]-[6個月]非[藥物]治療[ LDL-C][≧][190 mg]/[dL][ LDL-C]＜[190 mg]/[dL ][全民][健康][保險]降[三酸甘油酯][藥物]給付[規定表] 非[藥物]治療 [起始][藥物]治療 [血脂]值 [血脂目標]值 [處方]規定 [心][血管][疾病] 或[糖尿病][病人] 與[藥物]治療[可]並[行][ TG][≧][200 mg]/[dL]且([TC]/[HDL-C ]>[ 5 ]或[HDL-C ]<[ 40 mg]/[dL])[ TG]＜[200 mg]/[dL ]第[一年][應]每[3]-[6個月]抽血檢查[一次]，第[二年][以][後][應][至少]每[6]-[12個月]抽血檢查[一次]，[同時]請注意[副]作用之產生如[肝功能][異常]，[橫][紋肌][溶解症]。 無[心血管][疾病][病人]給[藥][前][應]有[3]-[6個月]非[藥物]治療[ TG][≧][200 mg]/[dL]且([TC]/[HDL-C ]>[ 5 ]或[HDL-C ]<[ 40 mg]/[dL])[ TG]＜[200 mg]/[dL ]無[心血管][疾病][病人]與[藥物]治療[可]並[行][ TG][≧][500 mg]/[dL] [TG]＜[500 mg]/[dL ]★[心][血管][疾病]定義： ([一]) [冠狀動脈][粥狀]硬化[病人][患者]包含：[心絞痛][病人]，有[心導][管]證實[或]缺[氧][性][心電圖]變化或[負荷性]試驗[陽性]反應[者](附檢查報告) ([二]) 缺血[型腦][血管][疾病][病人]包含：[ 1].[腦]梗塞。[ 2].[暫時][性腦]缺血[患者]([TIA])。（[診斷][須]由[神經][科醫師]確立）[ 3].有[症狀]之[頸動][脈][狹窄]。（[診斷][須]由[神經][科醫師]確立）  ★[危險][因子]定義：[ 1].[高血壓][ 2].[男性≧][45][歲]，[女性≧][55][歲]或[停經者][ 3].有[早]發性[冠心病][家族][史]([男性≦][55][歲]，[女性≦][65][歲])[ 4].[HDL-C ]<[ 40 mg]/[dL][ 5].吸菸(因吸菸而符合起步治療[準則]之[個案]，若未戒菸而要求[藥物]治 [療]，[應]以自費治療)。 紅[字部分]自[108年2月1日][起]實施":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["WhichQ"].append(f"{args[0]}的{args[1]}規定有哪些")
            resultDICT["WhichQ"].append(f"{args[0]}有哪些{args[1]}規定")

    return resultDICT


if __name__ == "__main__":
    from pprint import pprint

    resultDICT = getResult("威洛速膜衣錠 (5/片)的注意事項包含 1、口服劑型與含有Mg2+、AL3+之制酸劑或多價陽離子製劑(Fe2+、Zn2+)併用時，會導致吸收低下，效果減弱，請避免併用。 2、Moxifloxacin使用於<18歲族群之安全性尚未確立，動物研究觀察到Moxifloxacin 會造成未成年動物關節病變，十八歲以下不建議使用。 3、Moxifloxacin與cisapride、erythromycin、antipsychotics、tricyclic antidepressants、procainamide、quinidine、amiodarone、sotalol併用可能會延長QT間隔，故不建議併用，", "[威洛速膜衣錠 (5/片)]的注意[事項]包含[ 1]、[口服][劑型]與含有[Mg2]+、[AL3]+之[制][酸劑]或[多價陽][離子][製劑]([Fe2]+、[Zn2]+)併用時，[會]導致吸收低下，[效果]減弱，請避免併用。[ 2]、[Moxifloxacin]使用於<[18][歲][族群]之[安全][性]尚未確立，[動物]研究觀察到[Moxifloxacin] [會]造成未[成年動物][關節][病變]，[十八][歲][以下]不建議使用。[ 3]、[Moxifloxacin]與[cisapride]、[erythromycin]、[antipsychotics]、[tricyclic] [antidepressants]、[procainamide]、[quinidine]、[amiodarone]、[sotalol]併用[可能][會]延長[QT]間隔，故不建議併用，", [], {}, {})
    pprint(resultDICT)