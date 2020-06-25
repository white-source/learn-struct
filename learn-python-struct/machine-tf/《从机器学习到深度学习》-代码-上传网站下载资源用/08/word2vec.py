import numpy as np
from sklearn.datasets import fetch_20newsgroups

twenty_train = fetch_20newsgroups(subset='train')
email_data = [" ".join(email.lower().split("\n")[5: -3]).split() for email in twenty_train.data]

sentences = []
for doc in email_data:
    sentence = [word for word in doc if word.isdigit() or word.isalpha()]
    sentences.append(sentence)

from gensim.models.word2vec import Word2Vec

model = Word2Vec(sentences, size=100, window=10, min_count=4000, workers=4)
print(model.wv.vocab)
vocab = list(model.wv.vocab)
X = model[vocab]

from sklearn.manifold import TSNE

tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X)

import matplotlib.pyplot as plt
from adjustText import adjust_text

fig, ax = plt.subplots()
plt.plot(X_tsne[:, 0], X_tsne[:, 1], 'bo')
texts = []
for x, y, s in zip(X_tsne[:, 0], X_tsne[:, 1], vocab):
    texts.append(plt.text(x, y, s))
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='red'))
plt.show()
