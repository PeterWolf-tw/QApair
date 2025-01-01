#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#from linguistics_support import syntactician
import json
import os
import re

chinesePat = re.compile("(?<=[一-龥]) (?=[一-龥])")
udPat = re.compile('((?<=包含)|(?<=是))[^是，]+[^一-龥]$|(?<=包含)[^是]+[^一-龥]$')
mdPat = re.compile("^.+(?=\()")

def statementMaker(keySTR, valueSTR, topicSTR=""):
    resultSTR = ""
    if topicSTR!="":
        de="的"
    if valueSTR == "":
        pass
    elif keySTR == topicSTR:
        pass
    elif "、" in valueSTR:
        resultSTR = f"{topicSTR}{de}{keySTR}包含 {valueSTR}"
    elif ".2. " in valueSTR:
        resultSTR = f"{topicSTR}{de}{keySTR}包含 {valueSTR}"
    else:
        resultSTR = f"{topicSTR}{de}{keySTR}是 {valueSTR}"

    resultSTR = chinesePat.sub("", resultSTR)
    return resultSTR


if __name__ == "__main__":
    udDICT = {"_asCP":[], "_asNoun":["字號", "學名"]}
    resultLIST = []
    mdTypeLIST = ["持續性藥效膜衣錠", "持續性藥效錠", "加強型口服溶液用粉劑", "輸注溶液", "口服懸液用粉劑", "口服懸液用顆粒", "口服懸浮液", "口服懸液劑", "口服液", "長效錠", "膠囊", "錠"]
    inputSTR = "data"
    for i in os.listdir(f"./{inputSTR}"):
        if i.startswith("."):
            pass
        else:
            with open(f"./{inputSTR}/{i}", "r", encoding="utf-8") as f:
                inputDICT = json.load(f)
            for k, v in inputDICT.items():
                #print(k)
                if k == "劑型":
                    mdTypeLIST.append(v)
                statementSTR = statementMaker(k, v, topicSTR=inputDICT["中文名"]).replace("\n", " ")
                if inputDICT["中文名"] not in udDICT:
                    udDICT[inputDICT["中文名"]] = []
                udDICT["_asCP"].append(v.replace("\n", " "))
                while "" in udDICT["_asCP"]:
                    udDICT["_asCP"].remove("")
                mdLIST = [m.group(0) for m in mdPat.finditer(statementSTR.split("的")[0])]
                udDICT[inputDICT["中文名"]].extend(mdLIST)
                if len(statementSTR) != 0:
                    resultLIST.append(statementSTR)

    mdTypeLIST = list(set(mdTypeLIST))
    for u in udDICT:
        udDICT[u] = list(set(udDICT[u]))
        for md in mdTypeLIST:
            if md in u:
                udDICT[u].append(u.split(md)[0])


    with open("./statement.json", "w", encoding="utf-8") as f:
        json.dump(resultLIST, f, ensure_ascii=False)
    with open("./ud.json", "w", encoding="utf-8") as f:
        json.dump(udDICT, f, ensure_ascii=False)

