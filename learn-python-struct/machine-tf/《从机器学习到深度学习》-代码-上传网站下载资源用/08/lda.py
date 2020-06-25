
def filt_line(email):
    lines = []
    for line in email.split("\n"):
        line = line.strip()
        if len(line) < 20 or line.startswith("-") or \
           line.find("Subject:")!=0 and line.split()[0][-1]==":":
            continue
        if line.find("Subject:")==0:
            line = line[len("Subject:"):]
        lines.append(line)
    return "\n".join(lines)


import nltk
import string
from nltk.stem.porter import PorterStemmer
def filt_word(email):
    email = email.lower()
    lines = []
    
    ps = PorterStemmer()                      # 词干提取对象
    for line in email.split("\n"):
        words = nltk.word_tokenize(line) # 分词

        words = [w for w in words if w.isalpha()]   # 仅保留英文单词

        taged_words =nltk.pos_tag(words)  # 获取词性标签
        words = [w for w, pos in taged_words if pos in ['NN', 'JJ3',]] #仅保留名词、形容词
#                or pos.startswith('VB')]    # 仅保留动词

        words = [ps.stem(w) for w in words]        #词干化
        lines.append(" ".join(words))
    return "\n".join(lines)

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

twenty_train = fetch_20newsgroups(subset='train')
email_data = twenty_train.data[:50]
original_email = email_data

email_data = [filt_line(email) for email in email_data]
email_data = [filt_word(email) for email in email_data]

count_vect = CountVectorizer(stop_words='english')
X_counts = count_vect.fit_transform(email_data)
lda = LatentDirichletAllocation(n_components=5, learning_method='batch', random_state=0)

doc_topic = lda.fit_transform(X_counts)
topic_word = lda.components_


print(doc_topic.shape, topic_word.shape)

print(doc_topic[0])

import numpy as np
dict_word = {count_vect.vocabulary_[key]: key for key in count_vect.vocabulary_.keys()}
words = np.array([dict_word[idx] for idx in range(len(dict_word))])

def print_top_words(words, topic_word, topic_idx, n=10):
    maxn_index = np.argsort(topic_word[topic_idx])[-n:]
    maxn_index = np.flip(maxn_index, 0)
    maxn_value = topic_word[topic_idx][maxn_index]
    maxn_word = words[maxn_index]
    
    print("topic %s: %s"%(topic_idx, ", ".join(["%0.3f*%s"%(value, word) for value, word in zip(maxn_value, maxn_word)])))

    
def print_doc_topics(words, doc_topic, topic_word, doc_idx, n=3):
    maxn_index = np.argsort(doc_topic[doc_idx])[-n:]
    maxn_index = np.flip(maxn_index, 0)
    maxn_value = doc_topic[doc_idx][maxn_index]
    print("doc %s:"%doc_idx)
    for i in range(n):
        print("   weight: %0.3f "%(maxn_value[i], ), end='')
        print_top_words(words, topic_word, maxn_index[i])
    
print_top_words(words, topic_word, 0)
print_doc_topics(words, doc_topic, topic_word, 0)
print(original_email[0])




from sklearn.model_selection import GridSearchCV
parameters = {'n_components':range(5, 11, 5),
              'doc_topic_prior':(0.001, 0.01, 0.1, 0.5, 1),
              'topic_word_prior':(0.001, 0.01, 0.1, 0.5, 1),
              'learning_method':('batch',),
              'random_state':(0, )}

lda = LatentDirichletAllocation()
model = GridSearchCV(lda, parameters, cv=3)
model.fit(X_counts)

print(model.cv_results_)
best_idx = np.argmax(model.cv_results_['rank_test_score'])
print("Worst params is: ", model.cv_results_['params'][best_idx])

lda = LatentDirichletAllocation(**model.cv_results_['params'][best_idx])
doc_topic = lda.fit_transform(X_counts)
topic_word = lda.components_
print_doc_topics(words, doc_topic, topic_word, 0)


best_idx = np.argmin(model.cv_results_['rank_test_score'])
print("Best params is: ", model.cv_results_['params'][best_idx])

lda = LatentDirichletAllocation(**model.cv_results_['params'][best_idx])
doc_topic = lda.fit_transform(X_counts)
topic_word = lda.components_
print_doc_topics(words, doc_topic, topic_word, 0)
