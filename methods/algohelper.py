#coding=utf-8

import time
import random
import numpy as np
from sklearn import svm
from scipy import interp 
from sklearn import tree
from sklearn.svm import SVC
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import StratifiedKFold
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, classification_report
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

class algohelper(object):
    """docstring for algutil"""
    def __init__(self):
        super(algohelper, self).__init__()
        self.algorithm = {
            "DT": tree.DecisionTreeClassifier(),
            "SVM": SVC(kernel="linear", C=0.025),
            "AdaBoost": AdaBoostClassifier(), 
            "KNN": KNeighborsClassifier(n_neighbors=600),
            "NBM": GaussianNB(),
            "SGD": SGDClassifier(loss="hinge", penalty="l2"), 
            "RF": RandomForestClassifier()
        }
    
    def classify(self, classifierName, train_data, train_label, test_data):
        start = time.time()
        classifier = self.algorithm[classifierName] 
        classifier.fit(train_data, train_label)
        predict_label = classifier.predict(test_data)  
        end = time.time()  

        '''
        The accuracy of algorithm is obtained by cross validation.
        '''
        valid_train, valid_test, valid_train_lbl,  valid_test_lbl \
            = train_test_split(train_data, train_label, test_size = 0.2)
        classifier.fit(valid_train, valid_train_lbl)
        prd_lbl = classifier.predict(valid_test)
        report = classification_report(valid_test_lbl, prd_lbl)
        
        cls_result = {
            'label': predict_label,
            'time': round((end - start) * 1000, 2),
            'accuray': self.get_accuray(report)
        }
        return cls_result

    def get_accuray(self, report):
        stopWords = ['precision', 'recall', 'f1-score', 'support', 'total', '/']
        report = report.split()
        report = list(report)
        for word in stopWords:
            report.remove(word)
        
        result_dict = {
            'precision': report[-4],
            'recall': report[-3],
            'f1-score': report[-2]
        }
        
        return result_dict