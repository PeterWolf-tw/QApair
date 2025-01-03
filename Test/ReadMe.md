# 格式說明 / Explanations on the format

此處的檔案為利用 Gemma2 9B LLM Model 回答從 1086 個的 [Question](https://github.com/PeterWolf-tw/QApair/tree/main/Test) 中抽出 100 題來測試 Gemma2 9B 模型在沒有 QA pair 做為參考資料的條件下，是否具備對藥品的相關知識。

```python
[

     由原始資料 (https://github.com/PeterWolf-tw/QApair/tree/main/data) 經前處理後產生的直述句，再經過 Llama3 8B, Llama3 70B 和 TG 三個 model 產出問句，再將這些問句交由 ChatGPT-4o-mini 進行換句話說地重寫後得到 1086 個問句。
     ...
]
```
