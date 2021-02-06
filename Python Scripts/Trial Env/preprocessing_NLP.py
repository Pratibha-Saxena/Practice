#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk
import ssl

try:
    _create_unverified_https_context=ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download()


# In[3]:


def rem_spl_chars(rev):
    import re
    rev = rev.lower()
    return re.sub("[^a-zA-Z. ]","",rev)

def tokenize(A):
    from nltk.tokenize import word_tokenize
    A1 = word_tokenize(A)
    return A1

def sw(A3):
    from nltk.corpus import stopwords
    sw = stopwords.words("english")
    A4 = []
    for i in A3:
        if i not in sw:
            A4.append(i)
    return A4

def stem(A4):
    from nltk.stem import PorterStemmer
    ps = PorterStemmer()
    A5 = []
    for i in A4:
        A5.append(ps.stem(i))
    return A5

def lem(A5):
    from nltk.stem import WordNetLemmatizer
    wnlmt = WordNetLemmatizer()
    A6 = []
    for i in A5:
        A6.append(wnlmt.lemmatize(i))
    return A6

def preproc(A):
    B = rem_spl_chars(A)
    B1 = tokenize(B)
    B2 = sw(B1)
    B3 = stem(B2)
    B4 = lem(B3)
    return B4

def dealwithssl():
    import ssl
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context


# In[ ]:




