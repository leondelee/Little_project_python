#!/usr/bin/env python
#coding:utf-8
"""
created on 24.08.2017
author:Leon Lee
User-Agent:{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0'}
"""
import tkinter
from tkinter import *
import re
import requests
from bs4 import BeautifulSoup
import os
import time
if __name__ == '__main__':
    def proxies_gen():
        ippools={}
        with open('ippools.txt','r') as file:
            lines = file.readlines()
            for ip in lines:
                ippools.update({'http':ip})
            file.close()
        return ippools
    with open('需要翻译的单词.txt','r') as file1:
        text=file1.read()
        file1.close()
    text=text.replace('/','\n 1. ')
    print(text)
    reexp=re.compile('[0-9]*\.\s*(.*?)\s+')
    conts=reexp.findall(text)
    all=''
    count=1
    for con in conts:
        ippools= proxies_gen()
        print('正在翻译%s'%con)
        url='http://www.iciba.com/%s'%con
        tongyi_url='http://www.thesaurus.com/browse/%s?s=t'%con
        page=requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0'}).text
        page_tong=requests.get(tongyi_url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0'}).text
        soup=BeautifulSoup(page,'lxml')
        soup_tongyi=BeautifulSoup(page_tong,'lxml')
        contents=soup.find('ul',class_='base-list switch_part')
        tongyi_conts=soup_tongyi.find_all('span',class_='text')
        means=''
        tongyi=''
        for conss in contents.stripped_strings:
            means+=conss+'\n'
        if len(tongyi_conts)>=10:
            for i in range(0,5):
                tongyi+=tongyi_conts[i].string+','
        elif 0<len(tongyi_conts)<10:
            for i in range(0,len(tongyi_conts)):
                tongyi=tongyi_conts[i].string+','
        all+=('%s.'%count)+con+'\n'+means+'\n同义词:'+tongyi+'\n'
        count+=1
        time.sleep(0.25)
    with open('翻译结果.txt','w') as file:
        file.write(all)
        file.close()
        print('ok')
    exit()

