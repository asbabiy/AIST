# imports
import re
import pandas as pd
import json
from glob import glob
import dpath.util as dp
import html
from bs4 import BeautifulSoup as bs4

# parser
class Parser:
    """
    При mtype='vk' в path нужно передать путь к папке со всеми сообщениями.
    При mtype='tg' в path нужно передать директорию с JSON-файлами.
    """

    def __init__(self, path, mtype=None):
        self.path = path
        self.mtype = mtype

    def parse(self):

        text = []

        if self.mtype == 'tg':
            files = glob(f"{self.path}/**/*.json", recursive=True)

            for i in files:
                with open(i, encoding='utf-8') as obj:
                    ms = json.load(obj)

                    for msg in dp.values(ms, '/**/messages/*'):
                        if msg['type'] == 'message' and type(msg['text']) == str:
                            text.append(msg['text'])

        elif self.mtype == 'vk':
            files = glob(f"{self.path}/**/*.html", recursive=True)

            for k in files:
                with open(k, encoding='windows-1251') as obj:
                    contents = obj.read()

                msg = re.findall(r'(?<=<div>).+?(?=<div class="kludges"><div class="attachment">|<div class="kludges">|</div>)', contents)
                text.extend(msg)

        else:
            raise ValueError("MType value is invalid or isn't specified! It can be either 'tg' or 'vk'.")

        df = pd.DataFrame(data={'text': text})
        df = df[df.text.str.len() > 0]
        df.text = df.text.apply(html.unescape)
        
        return df
