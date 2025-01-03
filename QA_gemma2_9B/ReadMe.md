# 格式說明 / Explanations on the format

此處的檔案為利用 Gemma2 9B LLM Model 產生的 QA pairs.其格式說明如下：

```python
[
    {
     "Q": 由 Gemma2 9B Model ，基於 A 生成的 Wh-問句,
     "A:  由原始資料 (https://github.com/PeterWolf-tw/QApair/tree/main/data) 經前處理後產生的直述句。
    },
     ...
]
```
