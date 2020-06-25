import numpy as np
from bayespy import nodes


n_documents = 3
n_words = 30

word_documents = nodes.Categorical(np.ones(n_documents)/n_documents,
                                   plates=(n_words,)).random()
n_vocabulary = 10
n_topics = 2

p_topic = nodes.Dirichlet(5e-1*np.ones(n_topics),
                          plates=(n_documents,)).random()

p_word = nodes.Dirichlet(1e-1*np.ones(n_vocabulary),
                         plates=(n_topics,)).random()

topic = nodes.Categorical(p_topic[word_documents],
                          plates=(n_words,)).random()
corpus = nodes.Categorical(p_word[topic],
                           plates=(n_words,)).random()

print(word_documents, p_topic, p_word, topic, corpus)

print(",,,,", nodes.Multinomial(1, p_topic).random())
print(p_topic[word_documents])


p_topic = nodes.Dirichlet(np.ones(n_topics),
                          plates=(n_documents,),
                          name='p_topic')
p_word = nodes.Dirichlet(np.ones(n_vocabulary),
                         plates=(n_topics,),
                         name='p_word')
from bayespy.inference.vmp.nodes.categorical import CategoricalMoments
document_indices = nodes.Constant(CategoricalMoments(n_documents), word_documents,
                                  name='document_indices')
topics = nodes.Categorical(nodes.Gate(document_indices, p_topic),
                           plates=(len(corpus),),
                           name='topics')
words = nodes.Categorical(nodes.Gate(topics, p_word),
                          name='words')
print("!!!", p_topic, p_word, document_indices, topics, words, nodes.Gate(topics, p_word).get_moments())


words.observe(corpus)
p_topic.initialize_from_random()
p_word.initialize_from_random()
from bayespy.inference import VB
Q = VB(words, topics, p_word, p_topic, document_indices)
Q.update(repeat=1000)
import bayespy.plot as bpplt
bpplt.pyplot.figure()
bpplt.hinton(Q['p_topic'])
bpplt.pyplot.show()
