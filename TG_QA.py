#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

from pprint import pprint

from Loki_Model.A2Q_Maker.main import askLoki


def QAmaker(inputSTR):
    """
    Covnert 'inputSTR' into a Question and return it with the inputSTR as a QA pair.
    """
    refDICT = {
    "AnotAQ"  :[],
    "HowQ"    :[],
    "HowmuchQ":[],
    "WhatQ"   :[],
    "WhereQ"  :[],
    "WhichQ"  :[],
    "YesNoQ"  :[]
    }
    filterLIST = ["2which",]#, "2how", "2where", "2what"]
    resultDICT = askLoki(content=inputSTR,
                         filterLIST=filterLIST,
                         refDICT=refDICT)
    return resultDICT


if __name__ == "__main__":
    QDICT = {"AnotAQ"  :[],
             "HowQ"    :[],
             "HowmuchQ":[],
             "WhatQ"   :[],
             "WhereQ"  :[],
             "WhichQ"  :[],
             "YesNoQ"  :[]
             }
    inputLIST = json.load(open("statement.json", "r", encoding="utf-8"))
    resultLIST = []
    for i in inputLIST:
        print(i)
        for k in QDICT:
            Qresult = QAmaker(i)
            for q in list(set(Qresult[k])):
                resultLIST.append({"Q":q,
                                   "A":i
                                   })
    pprint(resultLIST)
    with open("./QA_TG/QA_TG_which.json", "w", encoding="utf-8") as f:
        json.dump(resultLIST, f, ensure_ascii=False)

