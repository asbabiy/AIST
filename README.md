# AIST
This repository contains materials for the AIST conference.

## Data
Both datasets have been **manually** anonymized due to VK's privacy policy. Besides, they were normalized in a bit different way comparing with their initial versions, used in this study.

`msg_with_emoji.csv` is a small dataset (~10k samples), containing annotated messages with emoji.

`train_data.csv` is a relatively large dataset (~54k samples; only half of the dataset is uploaded here, full version will be uploaded a bit later).

## Model
`model.joblib` is a trained MaxEnt model for predicting emotions in Russian text messages.

`vect.joblib` is a TF-IDF vectorizer for the aforementioned model.

## EmotionPredictor
`EmotionPredictor.py` is a pipeline for preprocessing, normalizing text messages, predicting emotions.

## Parser
`Parser.py` is a high-level parser for VK and Telegram text messages.