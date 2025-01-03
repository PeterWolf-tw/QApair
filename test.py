#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

from random import shuffle
from requests import post
from time import sleep
url = "https://api.droidtown.co/Loki/Call/" # 中文版

def _phi3382B(accountDICT, sytemSTR, assitantSTR, userSTR):
    payload = {
      "username": accountDICT["username"],
      "func": "call_llm",
      "data": {
        "model": "Phi3-3B",
        "system": sytemSTR,
        "assistant": assitantSTR,
        "user": userSTR
      }
    }
    try:
        result = post(url, json=payload).json()
    except:
        try:
            result = post(url, json=payload).json()
        except:
            return None
    return result


def _nemotron4B(accountDICT, sytemSTR, assitantSTR, userSTR):
    payload = {
      "username": accountDICT["username"],
      "func": "call_llm",
      "data": {
        "model": "Nemotron-4B",
        "system": sytemSTR,
        "assistant": assitantSTR,
        "user": userSTR
      }
    }
    try:
        result = post(url, json=payload).json()
    except:
        try:
            result = post(url, json=payload).json()
        except:
            return None
    return result

def _llama370B(accountDICT, sytemSTR, assitantSTR, userSTR):
    payload = {
      "username": accountDICT["username"],
      "func": "call_llm",
      "data": {
        "model": "Llama3-70B",
        "system": sytemSTR,
        "assistant": assitantSTR,
        "user": userSTR
      }
    }

    try:
        result = post(url, json=payload).json()
    except:
        try:
            result = post(url, json=payload).json()
        except:
            return None
    return result

def _llama38B(accountDICT, sytemSTR, assitantSTR, userSTR):
    payload = {
      "username": accountDICT["username"],
      "func": "call_llm",
      "data": {
        "model": "Llama3-8B",
        "system": sytemSTR,
        "assistant": assitantSTR,
        "user": userSTR
      }
    }

    try:
        result = post(url, json=payload).json()
    except:
        try:
            result = post(url, json=payload).json()
        except:
            return None
    return result

def _gemma29B(accountDICT, sytemSTR, assitantSTR, userSTR):
    payload = {
      "username": accountDICT["username"],
      "func": "call_llm",
      "data": {
        "model": "Gemma2-9B",
        "system": sytemSTR,
        "assistant": assitantSTR,
        "user": assitantSTR+userSTR
      }
    }
    try:
        result = post(url, json=payload).json()
    except:
        sleep(10)
        try:
            result = post(url, json=payload).json()
        except:
            return None
    return result

def QAtest(accountDICT, medKnowledgeLIST, userSTR, model):
    """"""
    systemSTR = "你是藥局裡的藥劑師。(You will not mention this.)"
    if medKnowledgeLIST == []:
        assistantSTR = ""
        qSTR = f"以繁體中文盡可能簡短回答「{userSTR}」。"
    else:
        assistantSTR = f"<reference>{str(medKnowledgeLIST)}</reference>"
        qSTR = "從前述參考資料中尋找可以回答「" + userSTR + "」的答案。以繁體中文盡可能簡短回答。"

    if model == "phi3382B":
        response = _phi3382B(accountDICT, systemSTR, assistantSTR, qSTR)
    elif model == "nemotron4B":
        response = _nemotron4B(accountDICT, systemSTR, assistantSTR, qSTR)
    elif model == "llama38B":
        response = _llama38B(accountDICT, systemSTR, assistantSTR, qSTR)
    elif model == "llama370B":
        response = _llama370B(accountDICT, systemSTR, assistantSTR, qSTR)
    elif model == "gemma29":
        response = _gemma29B(accountDICT, systemSTR, assistantSTR, qSTR)
    aSTR = response
    return aSTR


if __name__ == "__main__":
    accountDICT = json.load(open("./account.info", "r", encoding="utf-8"))
    testQLIST = json.load(open("Test_Q2.json", "r", encoding="utf-8"))
    shuffle(testQLIST)
    testQLIST = testQLIST[:100]
    baseline = False
    testingOnModel = "Llama370B" #Llama38B, Llama370B

    QArefLIST = []

    QA_TG = []
    for i in ["./QA_TG/QA_TG_how.json", "./QA_TG/QA_TG_what.json", "./QA_TG/QA_TG_where.json", "./QA_TG/QA_TG_which.json"]:
        QA_TG.extend(json.load(open(i, "r", encoding="utf-8")))

    QA_Llama38 = []
    for i in ["./QA_llama3_8B/QA_LLM_llama38B_HOW.json", "./QA_llama3_8B/QA_LLM_llama38B_WHAT.json", "./QA_llama3_8B/QA_LLM_llama38B_WHERE.json", "./QA_llama3_8B/QA_LLM_llama38B_WHICH.json"]:
        QA_Llama38.extend(json.load(open(i, "r", encoding="utf-8")))

    QA_Llama370 = []
    for i in ["./QA_llama3_70B/QA_LLM_llama370B_HOW.json", "./QA_llama3_70B/QA_LLM_llama370B_WHAT.json", "./QA_llama3_70B/QA_LLM_llama370B_WHERE.json", "./QA_llama3_70B/QA_LLM_llama370B_WHICH.json"]:
        QA_Llama370.extend(json.load(open(i, "r", encoding="utf-8")))

    #QA_TG = []
    #for i in ["./QA_TG/QA_TG_how.json", "./QA_TG/QA_TG_what.json", "./QA_TG/QA_TG_where.json", "./QA_TG/QA_TG_which.json"]:
        #QA_TG.extend(json.load(open(i, "r", encoding="utf-8")))

    if testingOnModel == "TG":
        QArefLIST = QA_TG
    elif testingOnModel == "Llama38B":
        QArefLIST = QA_Llama38
    elif testingOnModel == "Llama370B":
        QArefLIST = QA_Llama370

    medNameDICT = json.load(open("./Loki_Model/A2Q_Maker/intent/USER_DEFINED.json", "r", encoding="utf-8"))
    medNameDICT.pop("_asCP", None)
    medNameDICT.pop("_asNoun", None)

    resultLIST = []
    for q in testQLIST:
        print(q)
        knowledgeLIST = []
        medLIST = []
        for m in medNameDICT:
            if q.find(m) > -1:
                medLIST.append(m)
                medLIST.extend(medNameDICT[m])
            for i in medNameDICT[m]:
                if q.find(i) > -1:
                    medLIST.append(m)
                    medLIST.extend(medNameDICT[m])


        aSTR = ""
        medLIST = list(set(medLIST))
        for m in medLIST:
            for r in QArefLIST:
                if m in r["Q"]:
                    knowledgeLIST.append(r)
        print(len(knowledgeLIST))
        if baseline == True:
            knowledgeLIST=[]

        try:
            knowledgeLength = len(knowledgeLIST)
            aSTR = QAtest(accountDICT, knowledgeLIST, q, "gemma29")  #llama38B  phi3382B gemma29
            aSTR = aSTR["result"][0]["message"]["content"]
        except:
            print("蛤？", aSTR)
            try:
                knowledgeLength = int(len(knowledgeLIST)*0.8)
                aSTR = QAtest(accountDICT, knowledgeLIST[:knowledgeLength], q, "gemma29")  #llama38B  phi3382B gemma29
                aSTR = aSTR["result"][0]["message"]["content"]
            except:
                print("蛤蛤？", aSTR)
                try:
                    knowledgeLength = int(len(knowledgeLIST)*0.8**2)
                    aSTR = QAtest(accountDICT, knowledgeLIST[:knowledgeLength], q, "gemma29")  #llama38B  phi3382B gemma29
                    aSTR = aSTR["result"][0]["message"]["content"]
                except:
                    print("蛤蛤蛤？", aSTR)
        print(aSTR)
        print("="*10)
        resultLIST.append({"Q":q, "A":aSTR, "KG":knowledgeLength})
    with open(f"./Result/TestingResult_{testingOnModel}_03.json", "w", encoding="utf-8") as f:
        json.dump(resultLIST, f, ensure_ascii=False)