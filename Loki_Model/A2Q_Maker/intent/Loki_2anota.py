#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for 2anota

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

INTENT_NAME = "2anota"
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
    if utterance == "喜華膜衣錠的小孩劑量是 Chlid ≧ 3 mo: 125 mg q12h. For otitis media: < 2 yr, 125 mg q12h; ≧ 2 yr: 250 mg q12h.":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["AnotAQ"].append(inputSTR.replace("是", "是不是", 1))

    if utterance == "喜華膜衣錠的注意事項是若對penicillin過敏的患者，使用cephalosporin類藥品應特別小心。":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["AnotAQ"].append(inputSTR.replace("是", "是不是", 1))

    if utterance == "喜華膜衣錠的用藥指導是味覺差，不宜磨粉；請按時服藥至療程結束":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["AnotAQ"].append(inputSTR.replace("是", "是不是", 1))

    if utterance == "威洛速膜衣錠 (5/片)的注意事項包含 1、口服劑型與含有Mg2+、AL3+之制酸劑或多價陽離子製劑(Fe2+、Zn2+)併用時，會導致吸收低下，效果減弱，請避免併用。 2、Moxifloxacin使用於<18歲族群之安全性尚未確立，動物研究觀察到Moxifloxacin 會造成未成年動物關節病變，十八歲以下不建議使用。 3、Moxifloxacin與cisapride、erythromycin、antipsychotics、tricyclic antidepressants、procainamide、quinidine、amiodarone、sotalol併用可能會延長QT間隔，故不建議併用，":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["AnotAQ"].append(inputSTR.replace("包含", "是不是包含", 1))
            resultDICT["AnotAQ"].append(inputSTR.replace("包含", "有沒有包含", 1))

    if utterance == "安寶錠的儲存條件是 25°C以下儲存":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["AnotAQ"].append(inputSTR.replace("是", "是不是", 1))

    if utterance == "安寶錠的學名成份1是 Ritodrine 10 mg":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["AnotAQ"].append(inputSTR.replace("是", "是不是", 1))

    if utterance == "安寶錠的藥品是 Ritodrine 口服 10mg/tab (Anpo)":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["AnotAQ"].append(inputSTR.replace("是", "是不是", 1))

    if utterance == "安寶錠的藥理分類是 [8420] Uterine Relaxants":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["AnotAQ"].append(inputSTR.replace("是", "是不是", 1))

    if utterance == "安寶錠的規格含量是 10mg/tab":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["AnotAQ"].append(inputSTR.replace("是", "是不是", 1))

    if utterance == "康是鉀持續性藥效錠的儲存條件是室溫(< 25°C)":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["AnotAQ"].append(inputSTR.replace("是", "是不是", 1))

    if utterance == "康是鉀持續性藥效錠的注意事項是單次口服投與K+ > 40 mEq通常會造成無法耐受的腸胃不適，一般建議單次劑量不要超過25 mEq/dose以減輕腸胃道副作用。":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["AnotAQ"].append(inputSTR.replace("是", "是不是", 1))

    if utterance == "立普妥膜衣錠的健保規定包含 2.6.降血脂藥物 Drugs used for dyslipidemia 2.6.1.全民健康保降血脂藥物給付規定表 (86/1/1、87/4/1、87/7/1、91/9/1、93/9/1、97/7/1、102/8/1、108/2/1)      全民健康保險降膽固醇藥物給付規定表 非藥物治療 起始藥物治療 血脂值 血脂目標值 處方規定 1.有急性冠狀動脈症候群病史 2.曾接受心導管介入治療或外科冠動脈搭橋手術之冠狀動脈粥狀硬化患者(108/2/1) 與藥物治療可並行 LDL-C≧70 mg/dL LDL-C＜70 mg/dL 第一年應每3-6個月抽血檢查一次，第二年以後應至少每6-12個月抽血檢查一次，同時請注意副作用之產生如肝功能異常，橫紋肌溶解症。 心血管疾病 或糖尿病患者 與藥物治療可並行 TC≧160 mg/dL或 LDL-C≧100 mg/dL TC＜160 mg/dL或 LDL-C＜100 mg/dL 2個危險因子或以上給藥前應有3-6個月非藥物治療 TC≧200 mg/dL或 LDL-C≧130 mg/dL TC＜200 mg/dL或 LDL-C＜130 mg/dL 1個危險因子給藥前應有3-6個月非藥物治療 TC≧240 mg/dL或 LDL-C≧160 mg/dL TC＜240 mg/dL或 LDL-C＜160 mg/dL 0個危險因子給藥前應有3-6個月非藥物治療 LDL-C≧190 mg/dL LDL-C＜190 mg/dL 全民健康保險降三酸甘油酯藥物給付規定表 非藥物治療 起始藥物治療 血脂值 血脂目標值 處方規定 心血管疾病 或糖尿病病人 與藥物治療可並行 TG≧200 mg/dL且(TC/HDL-C > 5 或HDL-C < 40 mg/dL) TG＜200 mg/dL 第一年應每3-6個月抽血檢查一次，第二年以後應至少每6-12個月抽血檢查一次，同時請注意副作用之產生如肝功能異常，橫紋肌溶解症。 無心血管疾病病人給藥前應有3-6個月非藥物治療 TG≧200 mg/dL且(TC/HDL-C > 5 或HDL-C < 40 mg/dL) TG＜200 mg/dL 無心血管疾病病人與藥物治療可並行 TG≧500 mg/dL TG＜500 mg/dL ★心血管疾病定義： (一) 冠狀動脈粥狀硬化病人患者包含：心絞痛病人，有心導管證實或缺氧性心電圖變化或負荷性試驗陽性反應者(附檢查報告) (二) 缺血型腦血管疾病病人包含： 1.腦梗塞。 2.暫時性腦缺血患者(TIA)。（診斷須由神經科醫師確立） 3.有症狀之頸動脈狹窄。（診斷須由神經科醫師確立）  ★危險因子定義： 1.高血壓 2.男性≧45歲，女性≧55歲或停經者 3.有早發性冠心病家族史(男性≦55歲，女性≦65歲) 4.HDL-C < 40 mg/dL 5.吸菸(因吸菸而符合起步治療準則之個案，若未戒菸而要求藥物治 療，應以自費治療)。 紅字部分自108年2月1日起實施":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["AnotAQ"].append(inputSTR.replace("包含", "是不是包含", 1))
            resultDICT["AnotAQ"].append(inputSTR.replace("包含", "有沒有包含", 1))

    if utterance == "立普妥膜衣錠的常用劑量是 PO. Adults, initially, 10-20 mg qd; maintenance, 10-80 mg qd. Children 10-17 y/o, initially, 10 mg qd, may increase to max. 20 mg/day.":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["AnotAQ"].append(inputSTR.replace("是", "是不是", 1))

    if utterance == "立普妥膜衣錠的懷孕藥品分級是 X; 懷孕分級說明":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["AnotAQ"].append(inputSTR.replace("是", "是不是", 1))

    if utterance == "立普妥膜衣錠的注意事項是 1. Concomitant use of atorvastatin and cyclosporine should be avoided. 2. In patients receiving clarithromycin, itraconazole, ritonavir (plus darunavir, fosamprenavir, lopinavir, or saquinavir), atorvastatin dose exceeding 20 mg/day requires clinical assessment to ensure the lowest effect dosage is employed. 3. Rhabdomyolysis with renal dysfunction secondary to myoglobinuria has been reported. 4. Liver function test should be performed before starting statin therapy and as clinically indicated thereafter. 5. Potent CYP3A4 inhibitors such as cyclosporin, azole antifungals, macrolide antibiotics, HIV protease inhibitors, nefazodone and large quantities of grapefruit juice (> 1 quart/day) can raise the plasma level of HMG-CoA reductase inhibitors and may increase the risk of myopathy. 6. Combination of HMG-CoA reductase inhibitors and fibrates may increase the risk of myopathy. 7. Statins are contraindicated in patients with active liver disease or unexplained persistent elevations of serum transaminases. Statins are contraindicated in pregnant or lactation women. 8. The risk of myopathy appears to be increased in patients receiving higher dose of statins; in patients with multisystem diseases, e.g. renal or hepatic impairment concurrent serious infections or hypothyroidism; small body frame and frailty; and in patients undergo surgery.":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["AnotAQ"].append(inputSTR.replace("是", "是不是", 1))

    if utterance == "立普妥膜衣錠的藥品八碼是 LIP4FD35":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["AnotAQ"].append(inputSTR.replace("是", "是不是", 1))

    if utterance == "立普妥膜衣錠的藥品異動是自批號HH1255起，採用新防偽標籤。   公告日期： 2024/02/05":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["AnotAQ"].append(inputSTR.replace("是", "是不是", 1))

    if utterance == "芙琳亞錠15毫克的成人劑量是 Overdosage of folic acid antagonists: IVD, up to 75 mg within 12 hr, followed by 12 mg IM q6h for 4 doses. Leucovorin rescue: Begin within 24 hr of methotrexate administration. Doses of up to 120 mg > 12-24 hr by IM or IVD, followed by IM 12-15 mg or PO 15 mg q6h for next 48 hr with low doses of methotrexate, PO 15 mg q6h. Megaloblastic anaemia: IM, PO, not more than 1 mg/day.":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["AnotAQ"].append(inputSTR.replace("是", "是不是", 1))

    if utterance == "諾快寧口服懸液用粉劑的儲存條件是本藥未開封可儲存於室溫(< 30°C)。泡製後需冷藏，可存放7天。":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["AnotAQ"].append(inputSTR.replace("是", "是不是", 1))

    if utterance == "諾快寧口服懸液用粉劑的小孩劑量是 Usual dose: Infants ≥3 months, Children, Adolescents <40 kg: amoxicillin 20 to 40 mg/kg/day divided into 3 doses; Max: amoxicillin 90 mg/kg/day":
        if CHATBOT:
            replySTR = getReply(utterance, args)
            if replySTR:
                resultDICT["response"] = replySTR
                resultDICT["source"] = "reply"
        else:
            resultDICT["AnotAQ"].append(inputSTR.replace("是", "是不是", 1))

    return resultDICT


if __name__ == "__main__":
    from pprint import pprint

    resultDICT = getResult("安寶錠的規格含量是 10mg/tab", "安寶錠的規格含量是 10mg/tab", [], {}, {})
    pprint(resultDICT)