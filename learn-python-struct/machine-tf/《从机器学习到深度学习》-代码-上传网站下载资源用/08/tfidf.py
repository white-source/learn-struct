import numpy as np
from sklearn.datasets import fetch_20newsgroups
twenty_train = fetch_20newsgroups(subset='train')

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer(stop_words='english', max_df=0.8, min_df=0.001)
email_data = ["\n".join(email.split("\n")[5:]) for email in twenty_train.data]
X_train_counts = count_vect.fit_transform(email_data)
dict_word = {count_vect.vocabulary_[key]: key for key in count_vect.vocabulary_.keys()}
words = np.array([dict_word[idx] for idx in range(len(dict_word))])
print(type(X_train_counts), X_train_counts.shape)

from sklearn.feature_extraction.text import TfidfTransformer
X_train_tfidf = TfidfTransformer(use_idf=True).fit_transform(X_train_counts)
print(type(X_train_tfidf), X_train_tfidf.shape)


print("tf-idf created!")

def get_keywords(doc_index):
    KEYWORD_COUNT = 5
    tfidf_row = X_train_tfidf.getrow(doc_index).toarray().flatten()
    maxn_index = np.argsort( tfidf_row)[-KEYWORD_COUNT:]
    maxn_index = np.flip(maxn_index, 0)
    maxn_value = tfidf_row[maxn_index]
    maxn_word = words[maxn_index]
    for i in range(KEYWORD_COUNT):
        print("%s:%0.3f, "%(maxn_word[i], maxn_value[i]), end="")
    print("")

for i in range(20):
    print("email %s: "%i, end="")
    get_keywords(i)


# from sklearn.cluster import SpectralClustering
# labels = SpectralClustering(n_clusters=len(twenty_train.target_names), eigen_solver='arpack').fit(X_train_tfidf).labels_
# print(labels)


# from sklearn import metrics
# print(metrics.adjusted_rand_score(twenty_train.target, labels))
