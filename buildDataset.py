# -*- coding: utf-8 -*-

import os,sys
import re

# ---

# get the Brown corpus from http://www.nltk.org/nltk_data/packages/corpora/brown.zip
# and unpack it in the PATH_BROWN directory
PATH_BROWN = 'dataset/brown'

# output
FN_DATASET = 'dataset/dataset.txt'
FN_VOCABULARY = 'dataset/vocabulary.txt'

# ---

def parseFile(fn, V):
    S = []
    status = 'idle'
    sentence = []
    with open(fn) as f:
        for l in f:
            l = l.strip()
            if '' == l:
                if 'idle' == status:
                    continue
                else:
                    S.append(' '.join(sentence))
                    sentence = []
                    status = 'idle'
                    continue
            elif 'idle' == status:
                status = 'parsing'
            words = [ w.split('/')[0] for w in l.split() ]
            words = [ w for w in words if len(w.split()) > 0 ]
            for w in words:
                if not V.has_key(w):
                    V[w] = 0
                V[w] += 1
            sentence.extend( words )
    return S

# ----

re_dataset_file = re.compile('^c[a-z][0-9]{2}$')

if os.path.exists(FN_DATASET):
    print 'dataset already built'
    sys.exit(1)

print 'building the dataset'
V = {} # init vocabulary (with frequencies)  
f_dataset = open(FN_DATASET, 'w')
for fn in os.listdir(PATH_BROWN):
    if re_dataset_file.match(fn) is None:
        continue
    print 'adding sentences from %s' % fn
    for sentence in parseFile('%s/%s' % (PATH_BROWN,fn), V):
        f_dataset.write('%s\n' % sentence)
f_dataset.close()

print 'saving the vocabulary'
with open(FN_VOCABULARY, 'w') as f:
    for word,freq in V.iteritems():
        f.write('%s %d\n' % (word,freq))

sys.exit(0)
