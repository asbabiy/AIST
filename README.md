# AIST
This repository contains materials for the _AIST_ conference.

## Data
Both datasets have been **manually** anonymized due to VK's privacy policy. Besides, they were normalized in a bit different way comparing with their initial versions, used in this study.

`msg_with_emoji.csv` is a small dataset (~10k samples), containing annotated messages with emoji.

`train_data.csv` is a relatively large dataset (~54k samples; only half of the dataset is uploaded here).

## Model
`model.joblib` is a trained MaxEnt model for predicting emotions in Russian text messages.

`vect.joblib` is a TF-IDF vectorizer for the aforementioned model.

## Parser
`Parser.py` is a high-level parser for text messages requested from VK and Telegram.

It requires the path to the folder with messages and recursively iterates through all files. 

VK parser looks into `*.html` files and TG parser checks `*.json` files.

### Usage
```
from Parser import Parser
parser = Parser('PATH', mtype='tg') # parse TG messages
parser = Parser('PATH', mtype='vk') # parse VK messages
parser.parse() # returns a DataFrame with text messages
```
