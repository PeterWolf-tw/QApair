#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

from openai import OpenAI
from random import shuffle


def create_test(medNameDICT):
    qDICT = {"TG":[],
             "gemma29":[],
             "llama38B":[],
             "llama370B":[]
             }

    TG_howLIST    = json.load(open("QA_TG/QA_TG_how.json", "r", encoding="utf-8"))
    TG_whatLIST   = json.load(open("QA_TG/QA_TG_what.json", "r", encoding="utf-8"))
    TG_whereLIST  = json.load(open("QA_TG/QA_TG_where.json", "r", encoding="utf-8"))
    TG_whichLIST  = json.load(open("QA_TG/QA_TG_which.json", "r", encoding="utf-8"))

    gemma29_howLIST   = json.load(open("QA_gemma2_9B/QA_LLM_gemma29b_HOW.json", "r", encoding="utf-8"))
    gemma29_whatLIST  = json.load(open("QA_gemma2_9B/QA_LLM_gemma29b_WHAT.json", "r", encoding="utf-8"))
    gemma29_whereLIST = json.load(open("QA_gemma2_9B/QA_LLM_gemma29b_WHERE.json", "r", encoding="utf-8"))
    gemma29_whichLIST = json.load(open("QA_gemma2_9B/QA_LLM_gemma29b_WHICH.json", "r", encoding="utf-8"))

    llama38_howLIST   = json.load(open("QA_llama3_8B/QA_LLM_llama38B_HOW.json", "r", encoding="utf-8"))
    llama38_whatLIST  = json.load(open("QA_llama3_8B/QA_LLM_llama38B_WHAT.json", "r", encoding="utf-8"))
    llama38_whereLIST = json.load(open("QA_llama3_8B/QA_LLM_llama38B_WHERE.json", "r", encoding="utf-8"))
    llama38_whichLIST = json.load(open("QA_llama3_8B/QA_LLM_llama38B_WHICH.json", "r", encoding="utf-8"))

    llama370_howLIST   = json.load(open("QA_llama3_70B/QA_LLM_llama370B_HOW.json", "r", encoding="utf-8"))
    llama370_whatLIST  = json.load(open("QA_llama3_70B/QA_LLM_llama370B_WHAT.json", "r", encoding="utf-8"))
    llama370_whereLIST = json.load(open("QA_llama3_70B/QA_LLM_llama370B_WHERE.json", "r", encoding="utf-8"))
    llama370_whichLIST = json.load(open("QA_llama3_70B/QA_LLM_llama370B_WHICH.json", "r", encoding="utf-8"))
    counter = 0
    for k, v in medNameDICT.items():
        medLIST = [k]
        medLIST.extend(v)
        counter += len(medLIST)
        for m in medLIST:
            shuffleLIST = []
            for TGLIST in [TG_howLIST, TG_whatLIST, TG_whereLIST, TG_whichLIST]:
                for TG in TGLIST:
                    if m in TG["Q"]:
                        shuffleLIST.append(TG["Q"])
                    #if "" in TG["Q"] or "" in TG["A"]:
                        #shuffleLIST.append(TG["Q"])
            shuffle(shuffleLIST)
            qDICT["TG"].extend(shuffleLIST[:4])

            shuffleLIST = []
            for GMLIST in [gemma29_howLIST, gemma29_whatLIST, gemma29_whereLIST, gemma29_whichLIST]:
                for GM in GMLIST:
                    if m in GM["Q"]:
                        shuffleLIST.append(GM["Q"])
                    #if "" in GM["Q"] or "" in GM["A"]:
                        #shuffleLIST.append(GM["Q"])
            shuffle(shuffleLIST)
            qDICT["gemma29"].extend(shuffleLIST[:4])

            shuffleLIST = []
            for LMLIST in [llama38_howLIST, llama38_whatLIST, llama38_whereLIST, llama38_whichLIST]:
                for LM in LMLIST:
                    if m in LM["Q"]:
                        shuffleLIST.append(GM["Q"])
                    #if "" in LM["Q"] or "" in LM["A"]:
                        #shuffleLIST.append(LM["Q"])
            shuffle(shuffleLIST)
            qDICT["llama38B"].extend(shuffleLIST[:4])

            shuffleLIST = []
            for GMLIST in [llama370_howLIST, llama370_whatLIST, llama370_whereLIST, llama370_whichLIST]:
                for LM in LMLIST:
                    if m in LM["Q"]:
                        shuffleLIST.append(GM["Q"])
                    #if "" in LM["Q"] or "" in LM["A"]:
                        #shuffleLIST.append(LM["Q"])
            shuffle(shuffleLIST)
            qDICT["llama370B"].extend(shuffleLIST[:4])

    print(len(set(qDICT["gemma29"])))
    print(len(set(qDICT["llama38B"])))
    print(len(set(qDICT["llama370B"])))
    print(len(set(qDICT["TG"])))
    print(counter)
    print(qDICT)
    qLIST = []
    for k in qDICT:
        qLIST.extend(qDICT[k])
    qLIST = list(set(qLIST))
    print("總共：", len(qLIST))
    resultLIST = []
    for q in qLIST:
        print("進度：", round(qLIST.index(q)/len(qLIST), 3)*100, "%")
        rephrasedQ = _rephraseByLLM(q)
        resultLIST.append(rephrasedQ)
    return resultLIST

def _rephraseByLLM(srcSTR):
    # 記得key不要洩漏出去
    api_key = json.load(open("./account.info", "r", encoding="utf-8"))["openai_key"]
    client = OpenAI(api_key = api_key)
    completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
          {"role": "assistant", "content": "你是一個專業的藥劑師，正在編寫藥局的手冊。"},
          {"role": "user", "content": f"「{srcSTR}」可改寫為一樣意思的句子："}
        ]
    )
    paraphraseSTR = completion.choices[0].message.content.lstrip("「").rstrip("」")
    return paraphraseSTR

if __name__ == "__main__":
    medNameDICT = json.load(open("./Loki_Model/A2Q_Maker/intent/USER_DEFINED.json", "r", encoding="utf-8"))
    medNameDICT.pop("_asCP", None)
    medNameDICT.pop("_asNoun", None)
    #print(len(medNameDICT))
    qLIST = create_test(medNameDICT)
    print(qLIST)
    with open("./Test/Test_Q.json", "w", encoding="utf-8") as f:
        json.dump(qLIST, f, ensure_ascii=False)


