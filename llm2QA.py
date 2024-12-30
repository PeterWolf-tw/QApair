#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

from partial_json_parser import ensure_json
from pprint import pprint
from requests import post
from time import sleep

url = "https://api.droidtown.co/Loki/Call/" # 中文版

def _llama38B(accountDICT, systemSTR, assistantSTR, userSTR):
    payload = {
      "username": accountDICT["username"],
      "func": "call_llm",
      "data": {
        "model": "Llama3-8B",
        "system": systemSTR,
        "assistant": assistantSTR,
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


def _llama370B(accountDICT, systemSTR, assistantSTR, userSTR):
    payload = {
      "username": accountDICT["username"],
      "func": "call_llm",
      "data": {
        "model": "Llama3-70B",
        "system": systemSTR,
        "assistant": assistantSTR,
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


def _gemma29B(accountDICT, systemSTR, assistantSTR, userSTR):
    payload = {
      "username": accountDICT["username"],
      "func": "call_llm",
      "data": {
        "model": "Gemma2-9B",
        "system": systemSTR,
        "assistant": assistantSTR,
        "user": userSTR
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

def call_LLM(accountDICT=None, llm=None):

    answerLIST = json.load(open("./statement.json", "r", encoding="utf-8"))

    systemSTR = "You are a pharmacist in a big hospital. You are assigned to generate questions out of the information from packet inserts."
    #"Chinese A-not-A question (e.g., 是不是)", "HOW", "HOW MUCH", , "Yes-No question", "WHAT", "WHERE",
    for wh in ["HOW", "WHAT", "WHERE", "WHICH"]:
        userLIST = [f"You will create wh-questions about {wh} to the answer given above in Traditional Chinese.",
                    "Reply in the JSON schema as {'Q':<QUESTION>, 'A':<ANSWER>} Reply in Traditional Chinese."
                   ]
        userSTR = " ".join(userLIST)
        resultLIST = []
        for ans in answerLIST:
            assistantSTR = f"Answer:{ans}"
            if llm == "gemma29B":
                question = _gemma29B(accountDICT, systemSTR, assistantSTR, userSTR)
            elif llm == "llama38B":
                question = _llama38B(accountDICT, systemSTR, assistantSTR, userSTR)
            elif llm == "llama370B":
                question = _llama370B(accountDICT, systemSTR, assistantSTR, userSTR)
            #pprint(question)
            if question == None:
                continue
            try:
                QA = "".join(question["result"][0]["message"]["content"]).replace("\n", " ").lstrip("```json").replace("```", "").rstrip("json\n").replace("'", '"')
                QA = ensure_json(QA)
                resultLIST.append(QA)
                print(QA)
                print("Process:", round(answerLIST.index(ans)/len(answerLIST), 2)*100, "%")
            except:
                pass
        with open(f"QA_LLM_{llm}_{wh}.json", "w", encoding="utf-8") as f:
            json.dump(resultLIST, f, ensure_ascii=False)
    return None

if __name__ == "__main__":
    accountDICT = json.load(open("./account.info", "r", encoding="utf-8"))
    call_LLM(accountDICT=accountDICT, llm="llama38B")