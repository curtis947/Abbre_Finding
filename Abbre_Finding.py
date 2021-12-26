#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 11:09:32 2021

@author: curtis947
"""

import re
import pandas as pd
# book path
book1="Book path"# please edit this

# import book
f=open(book1,"r")
mytext=f.read()
f.close

# find abbreviation
myabb=re.findall(r"\b[A-Z]{2,}\b", mytext)
myabb = list(set(myabb))# remove repeat terms
abb_u=[]#unknown abbreviation
abb_u_p=[]# information of the unknown abbreviation

for i in myabb:
    sent_find=re.findall(r'.*?\('+i+'\)', mytext)
    if sent_find != []:
        abb_u.append(i)
        abb_u_p.append(sent_find)
        print(i)
        print(sent_find)
        
        
        
abb_udf=pd.DataFrame(abb_u)
abb_u_pdf=pd.DataFrame(abb_u_p)
outdf=pd.concat([abb_udf, abb_u_pdf], axis=1, join='inner')# combine abbre and information
outpath="outpath"# please edit this
outdf.to_excel(outpath)

