# -*- coding: utf-8 -*-

import numpy as np
from random import shuffle

MIN_CONTEXT_LENGTH = 3

class Dataset(object):
    
    def __init__(self, fn_dataset, fn_vocabulary):
        self.fn_dataset = fn_dataset
        self.fn_vocabulary = fn_vocabulary
        self.S = None
        self.V = None
    
    def load(self):
        self._loadSentences()
        self._loadVocabulary()
    
    def getSentences(self):
        return self.S
    
    def getVocabulary(self):
        return self.V
    
    def getNextWordPredTrainset(self, N = None):
        global MIN_CONTEXT_LENGTH
        
        train_text = []
        train_labels = []
        
        S = self.S
        if N is not None and N < len(S):
            S += []
            shuffle(S)
            S = S[0:N]
            
        for sentence in S:
            l = len(sentence)
            for i in range(MIN_CONTEXT_LENGTH+1,l):
                train_text.append( sentence[0:i] ) # TODO lookup word indexes in the vocabulary for one-hot representation
                train_labels.append( sentence[i] ) # TODO  " " "
        
        return train_text,train_labels
    
    def _loadSentences(self):
        self.S = []
        with open(self.fn_dataset) as f:
            for l in f:
                l = l.strip()
                if '' == l:
                    continue
                self.S.append( l.split() )
    
    def _loadVocabulary(self):
        self.V = {}
        with open(self.fn_vocabulary) as f:
            for l in f:
                l = l.strip()
                if '' == l:
                    continue
                (word,freq) = l.split()
                self.V[word] = np.int64(freq)
        