# 格式說明 / Explanations on the format

此處的檔案為利用 Gemma2 9B LLM Model 回答從 1086 個的 [Question](https://github.com/PeterWolf-tw/QApair/tree/main/Test) 中抽出 100 題來測試 Gemma2 9B 模型在由 Llama3 70B 產出的 QA pair 做為參考資料的條件下，是否具備對藥品的相關知識。

本測試共進行三次。三次都是獨立抽出 100 題！

```python
[
    {
        "Q": 從 1086 個問句裡抽出的 100 題之一,
        "A": Gemma2 9B 在沒有 QA pair 做為參考資料的條件下做出的回答,
        "KG": n, #KG 為 Knowledge 的縮寫。其後的數字 n 表示在這一題的測試中，受測模型 (此時為 Gemma2 9B) 接收到 Q 的同時，也拿到幾組 QA pair 做為參考。此值為 0 時表示「沒有 QA pair 做為參考資料」。
        "PASS":"False" #人力判讀 A 欄中的答案是否和原始藥品仿單中的內容資訊一致。若一致，本欄值為 True，若不一致，則為 False。本欄採寬鬆判斷，只要有部份和仿單內容一樣，就視為 True。
    },
     ...
]
```
