import re
from joblib import load
from rnnmorph.predictor import RNNMorphPredictor
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import f1_score


vect = load(r'PASTE YOUR PATH HERE')
model = load(r'PASTE YOUR PATH HERE')
lemma = RNNMorphPredictor(language="ru")


class EmotionPredictor():
    
    def __init__(self, data=None, true=None, option=None, vectorizer=vect, estimator=model, 
                 lemmatizer=lemma):
        self.data = data
        self.true = true
        self.vectorizer = vectorizer
        self.estimator = estimator
        self.option = option
        self.prediction = None
        self.lemmatizer = lemmatizer
        self.labels = {0: 'Радость', 1: 'Грусть', 2: 'Агрессия', 3: 'Заинтересованность', 4: 'Нейтральность'}
        
        
    def process(self):
        
        def preprocess(text):
        
            text = text.lower()
            text = re.sub(r'([а-яА-ЯёЁ])\1{2,}', r'\1', text)
            text = re.findall(r'[0-9а-яА-ЯёЁ-]+|[?!)(.]', text)
            text = self.lemmatizer.predict(text)
            text = [text[i].normal_form for i in range(len(text))]
            text = " ".join(text)
            return text
        
        assert len(self.data) > 0, 'Ввод не должен быть пустым!'
        
        if type(self.data) != str:
            corpus = self.data.copy()
            for index, text in enumerate(corpus):
                corpus[index] = preprocess(text)
        else:
            corpus = preprocess(self.data)
            corpus = np.array([corpus])

        self.data = corpus

        return self.data
    
    
    def predict(self):
        
        self.process()
        features = self.vectorizer.transform(self.data)
        prediction = self.estimator.predict(features)
        self.prediction = prediction
        
        if self.option == 'report':
            print(classification_report(self.true, self.prediction, target_names=self.labels.values()))
            
        if self.option == 'plot':
            cm = confusion_matrix(self.true, self.prediction)
            cmn = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            fig, ax = plt.subplots(figsize=(12, 10))
            sns.heatmap(cmn, annot=True, fmt='.2f', xticklabels=self.labels.values(), yticklabels=self.labels.values())
            plt.ylabel('Actual')
            plt.xlabel('Predicted')
            plt.show(block=False)
        
        if self.option == 'accuracy':
            print(f'Model Accuracy: {f1_score(self.true, self.prediction, average="weighted")}')
            
        if len(self.prediction) == 1:
            return self.labels[int(self.prediction)]
        else:
            return self.prediction