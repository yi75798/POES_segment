#!/usr/bin/python
# -*- encoding: utf-8 -*-
# File    :    Segment.py
# Time    :   2021/12/02 14:45:43
# Author  :   Hsu, Liang-Yi
# Email:   yi75798@gmail.com

import jieba
import numpy as np
import pandas as pd
import os
os.chdir(os.getcwd())

# 停用詞表
stopwords = []
for word in open('stopwords.txt', 'r'):
    stopwords.append(word.strip())

# 讀取使用者自訂詞典
jieba.load_userdict('userdict.txt')

# 讀入原始文本檔案
df = pd.read_csv('TextData.csv', encoding='utf_8_sig').dropna(
    subset=['Text'])  # 文字欄位缺漏視為遺漏值排除

# 建立儲存輸出的dataframe
output = pd.DataFrame(columns=['id', 'words'])

# 開始斷詞
for i in df.index:
    result = [seg for seg in jieba.cut(df.loc[i, 'Text'].replace(" ", "").replace("　", ''),
                                       cut_all=False) if seg not in stopwords]  # 以迴圈一一抓出每個文本並斷詞
    # 文本空格先去除

    output = output.append(pd.DataFrame({'id': [df.loc[i, 'id']] * len(result),  # 存進output
                                         'words': result}), ignore_index=True)


# 輸出檔案
output.to_excel('data_seg.xlsx', index=False, encoding='utf_8_sig')
