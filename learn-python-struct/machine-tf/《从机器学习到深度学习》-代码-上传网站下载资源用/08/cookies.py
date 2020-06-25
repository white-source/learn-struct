import numpy as np
X = np.array([[1, 1, 3], [2, 1, 2], [3, 1.2, 1], [4, 1, 2], [5, 0.8, 0.3], [6, 1, 3.5]])
from sklearn.decomposition import NMF

model = NMF(n_components=2)
W = model.fit_transform(X)
H = model.components_

print(X)
print(W)
print(H)


print("############## LSA ###############")


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD

count_vect = CountVectorizer(stop_words=None)
X_counts = count_vect.fit_transform(["I love machine learning",
                                     "I love python",
                                     "The weather is good"])
lsa = TruncatedSVD(n_components=2)

doc_topic = lsa.fit_transform(X_counts)
topic_word = lsa.components_

print("shape of bag of words: ", X_counts.shape)
print("shape of topic_word is ", topic_word.shape)
print("doc_topic:\n", doc_topic)

print( count_vect.vocabulary_)

print("############### LDA ###################")

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

count_vect = CountVectorizer(stop_words=None)
X_counts = count_vect.fit_transform(["I love machine learning",
                                     "I love python",
                                     "The weather is good"])
lda = LatentDirichletAllocation(n_components=2, learning_method='online')

doc_topic = lda.fit_transform(X_counts)
topic_word = lda.components_

print("shape of bag of words: ", X_counts.shape)
print("shape of topic_word is ", topic_word.shape)
print("doc_topic:\n", doc_topic)

