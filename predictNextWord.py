# -*- coding: utf-8 -*-

from settings import getSettings
settings = getSettings()

# from passage.preprocessing import Tokenizer
from passage.utils import load

# ---


tokenizer = load(settings['FN_TRAINED_TOKENIZER'])
model = load(settings['FN_MODEL_NEXTWORDPRED'])

while(True):
    sentence = raw_input('>')
    model.predict(tokenizer.transform(sentence))
    print 'best next word for <%s>: None' % (sentence)
