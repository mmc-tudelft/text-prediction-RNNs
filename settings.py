# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.abspath('lib'))

def getSettings():
    settings = {}
    
    settings['FN_DATASET'] = 'dataset/dataset.txt'
    settings['FN_VOCABULARY'] = 'dataset/vocabulary.txt'
    
    settings['FN_TRAINED_TOKENIZER'] = 'trained-models/tokenizer.pkl'
    settings['FN_MODEL_NEXTWORDPRED'] = 'trained-models/nextwordpred.pkl'

    return settings
