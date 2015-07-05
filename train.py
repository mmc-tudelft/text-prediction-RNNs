# -*- coding: utf-8 -*-

from settings import getSettings
settings = getSettings()

from libDataset import Dataset

from passage.preprocessing import Tokenizer
from passage.layers import Embedding, GatedRecurrent, Dense
from passage.models import RNN
from passage.utils import save

import sys

# ---

# ---

print 'loading dataset'
d = Dataset(settings['FN_DATASET'], settings['FN_VOCABULARY'])
d.load()

print 'generating labeled training set'
train_text,train_labels = d.getNextWordPredTrainset(10)
#for t,l in zip(train_text,train_labels):
#    print t,'->',l

tokenizer = Tokenizer()
train_tokens = tokenizer.fit_transform(train_text)
save(train_tokens, settings['FN_TRAINED_TOKENIZER'])

layers = [
    Embedding(size=128, n_features=tokenizer.n_features),
    GatedRecurrent(size=128),
    Dense(size=1, activation='sigmoid')
]

model = RNN(layers=layers, cost='BinaryCrossEntropy')
model.fit(train_tokens, train_labels)

save(model, settings['FN_MODEL_NEXTWORDPRED'])
