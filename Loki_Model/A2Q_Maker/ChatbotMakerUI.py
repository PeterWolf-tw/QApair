#!/usr/bin/env python3
# -*- coding:utf-8 -*-

try:
    from .lib.Account import *
except:
    from lib.Account import *

from lib.ChatbotMaker import COLOR_DICT
from lib.ChatbotMaker import setColor
from lib.ChatbotMaker import generateReply


LOGO = f"""------------------------------------------
     ##        #######  ##    ## ####
     ##       ##     ## ##   ##   ##
     ##       ##     ## ##  ##    ##
     ##       ##     ## #####     ##
     ##       ##     ## ##  ##    ##
     ##       ##     ## ##   ##   ##
     ########  #######  ##    ## ####
------------------------------------------
      {setColor("Loki ChatbotMaker 回覆產生工具", COLOR_DICT["YELLOW"])}"""

def getMenu():
    chatbotModeDICT = getChatbotModeMsg()
    menuSTR = f"""
------------------------------------------
{setColor("任務清單", COLOR_DICT["CYAN"])}

1. {setColor(chatbotModeDICT["text"], chatbotModeDICT["color"])}
2. 設置 ChatbotMaker Prompt
3. 產生所有文本內容的回覆
4. {setColor("離開", COLOR_DICT["RED"])}
------------------------------------------

請輸入要執行的任務編號[1~4]："""
    return menuSTR

def getChatbotModeMsg():
    return {
        "color": COLOR_DICT["RED"] if ACCOUNT_DICT["chatbot_mode"] else COLOR_DICT["GREEN"],
        "text": "停用 Chatbot 模式" if ACCOUNT_DICT["chatbot_mode"] else "啟用 Chatbot 模式"
    }

def getPrompt():
    promptDICT = {
        "system": "",
        "assistant": "",
        "user": "",
        "resp_header": [],
    }
    if "llm_prompt" in ACCOUNT_DICT:
        for k in promptDICT:
            if k in ACCOUNT_DICT["llm_prompt"]:
                promptDICT[k] = ACCOUNT_DICT["llm_prompt"][k]

    return promptDICT

def setPrompt(promptDICT):
    for k in promptDICT:
        if k in ACCOUNT_DICT["llm_prompt"]:
            ACCOUNT_DICT["llm_prompt"][k] = promptDICT[k]

    return saveAccount()

def saveAccount():
    try:
        json.dump(ACCOUNT_DICT, open(os.path.join(BASE_PATH, "account.info"), "w", encoding="utf-8"), ensure_ascii=False, indent=4)
        return True
    except:
        return False


if __name__ == "__main__":
    print(LOGO)
    while True:
        print(getMenu(), end="")
        index = str(input())
        if index == "1":
            chatbotModeDICT = getChatbotModeMsg()
            ACCOUNT_DICT["chatbot_mode"] = not ACCOUNT_DICT["chatbot_mode"]
            status = saveAccount()
            if status:
                print(setColor(f"[完成] {chatbotModeDICT['text']}", COLOR_DICT["GREEN"]))
            else:
                print(setColor(f"[失敗] {chatbotModeDICT['text']}", COLOR_DICT["RED"]))

        elif index == "2":
            promptDICT = getPrompt()
            print(f"\n{setColor('設置 ChatbotMaker Prompt', COLOR_DICT['CYAN'])}")
            print("------------------------------------------")
            print(f"System: {promptDICT['system']}")
            print(f"Assistant: {promptDICT['assistant']}")
            print(f"User: {promptDICT['user']}")
            print("------------------------------------------")
            while True:
                print("是否調整 Prompt System?[Y/N]: ", end="")
                status = str(input()).upper()
                if status in ["Y", "N"]:
                    if status == "Y":
                        print("System prompt: ", end="")
                        promptDICT["system"] = str(input())
                    break

            while True:
                print("是否調整 Prompt Assistant?[Y/N]: ", end="")
                status = str(input()).upper()
                if status in ["Y", "N"]:
                    if status == "Y":
                        print("Assistant prompt: ", end="")
                        promptDICT["assistant"] = str(input())
                    break

            while True:
                print("是否調整 Prompt User?[Y/N]: ", end="")
                status = str(input()).upper()
                if status in ["Y", "N"]:
                    if status == "Y":
                        print("User prompt: ", end="")
                        promptDICT["user"] = str(input())
                    break

            status = setPrompt(promptDICT)
            if status:
                print(setColor("[完成] 設置 ChatbotMaker Prompt", COLOR_DICT["GREEN"]))
            else:
                print(setColor("[失敗] 設置 ChatbotMaker Prompt", COLOR_DICT["RED"]))

        elif index == "3":
            print(f"\n{setColor('產生所有文本內容的回覆', COLOR_DICT['CYAN'])}")
            print("------------------------------------------")
            status = generateReply()
            if status:
                print(setColor("[完成] 產生所有文本內容的回覆", COLOR_DICT["GREEN"]))
            else:
                print(setColor("[失敗] 產生所有文本內容的回覆", COLOR_DICT["RED"]))

        elif index == "4":
            break