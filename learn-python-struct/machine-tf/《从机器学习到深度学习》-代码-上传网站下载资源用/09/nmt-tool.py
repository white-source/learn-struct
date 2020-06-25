
import sys
import os
import random
import re

src = "en"
tgt = "deu"

prefix = "data-nmt/en-deu"
origin_file = "deu.txt"
corpus_file = "corpus"
train_file = "train_topic"
validate_file = "dev_topic"
test_file = "test_topic"
vocabulary_file = "vocab_topic"

origin_src_file = os.path.join(prefix, origin_file)

corpus_src_file = os.path.join(prefix, corpus_file+"."+src)
corpus_tgt_file = os.path.join(prefix, corpus_file+"."+tgt)
train_src_file = os.path.join(prefix, train_file+"."+src)
train_tgt_file = os.path.join(prefix, train_file+"."+tgt)
validate_src_file = os.path.join(prefix, validate_file+"."+src)
validate_tgt_file = os.path.join(prefix, validate_file+"."+tgt)
test_src_file = os.path.join(prefix, test_file+"."+src)
test_tgt_file = os.path.join(prefix, test_file+"."+tgt)

voca_src_file = os.path.join(prefix, vocabulary_file+"."+src)
voca_tgt_file = os.path.join(prefix, vocabulary_file+"."+tgt)

special_strings = ["<unk>", "<s>", "</s>"]
import random

def gen_corpus():
    global src, tgt, prefix, special_strings
    global origin_src_file,  corpus_src_file, corpus_tgt_file    
   
    origin_lines = [line for line in open(origin_src_file)]
    with open(corpus_src_file, 'w') as f_corpus_src:
        with open(corpus_tgt_file, 'w') as f_corpus_tgt:
            for i, line in enumerate(origin_lines):
                sentenses = line.split("\t")
                for ss in special_strings:
                    line = line.replace(ss, "")
                f_corpus_src.write(sentenses[0]+"\n")
                f_corpus_tgt.write(sentenses[1])
    if src=="zh":
        split_words(corpus_src_file)
    if tgt=="zh":
        split_words(corpus_tgt_file)

def split_sets():
    global corpus_src_file, corpus_tgt_file
    global train_src_file, train_tgt_file, validate_src_file, validate_tgt_file, test_src_file, test_tgt_file

    f_corpus_src = open(corpus_src_file)
    f_corpus_tgt = open(corpus_tgt_file)
    corpus = list(zip(f_corpus_src.readlines(), f_corpus_tgt.readlines()))
    print()
    f_corpus_src.close()
    f_corpus_tgt.close()
    
    random.shuffle(corpus) 
    lines = len(corpus)
    with  open(train_src_file, 'w') as f_src:
        f_src.writelines([ x[0] for x in corpus[:lines*80//100]])
        
    with open(train_tgt_file, 'w') as f_tgt:
        f_tgt.writelines([ x[1] for x in corpus[:lines*80//100]])

    with  open(validate_src_file, 'w') as f_src:
        f_src.writelines([ x[0] for x in corpus[lines*80//100: lines*90//100]])
        
    with open(validate_tgt_file, 'w') as f_tgt:
        f_tgt.writelines([ x[1] for x in corpus[lines*80//100: lines*90//100]])

    with  open(test_src_file, 'w') as f_src:
        f_src.writelines([ x[0] for x in corpus[lines*90//100:]])
        
    with open(test_tgt_file, 'w') as f_tgt:
        f_tgt.writelines([ x[1] for x in corpus[lines*90//100:]])

def split_words(corpus_file):
    import jieba
    result = []
    with open(corpus_file) as f:
        for line in f:
            jieba_tokens = list(jieba.cut(line, cut_all=False))
            line = " ".join(jieba_tokens)
            result.append(line)

    with open(corpus_file, 'w') as f:
        f.writelines(result)
            
    
def gen_vocab_file(corpus_file, vocab_file):
    global special_strings
    
    import nltk

    file_content = open(corpus_file).read()
    tokens = nltk.word_tokenize(file_content)

    # import jieba
    # jieba_tokens = list(jieba.cut(file_content, cut_all=False))
    # if len(jieba_tokens)> len(tokens):
    #     tokens = jieba_tokens
        
    unique_list = []
    for token in tokens:
        token = re.sub("[\r\n\s]", "", token)
        if token not in unique_list and len(token)>0:
            unique_list.append(token)
    print(unique_list[:10])
    with open(vocab_file, 'w') as f:
        f.writelines("\n".join(special_strings + list(unique_list)))
    
def gen_vocabulary():
    global corpus_src_file, corpus_tgt_file, special_strings
    global voca_src_file, voca_tgt_file
    global train_src_file, train_tgt_file, validate_src_file, validate_tgt_file, test_src_file, test_tgt_file
    gen_vocab_file(train_src_file, voca_src_file)
    gen_vocab_file(train_tgt_file, voca_tgt_file)
    return
    import nltk
    file_content = open(corpus_src_file).read()
    tokens = set(nltk.word_tokenize(file_content))
    with open(voca_src_file, 'w') as f_src:
        f_src.writelines("\n".join(special_strings + list(tokens)))

    file_content = open(corpus_tgt_file).read()
    tokens = set(nltk.word_tokenize(file_content))
    with open(voca_tgt_file, 'w') as f_tgt:
        f_tgt.writelines("\n".join(special_strings + list(tokens)))    
    
    
if __name__ == '__main__':
    import getopt

    opts, args = getopt.getopt(sys.argv[1:], "gsv", [])
    argDict = dict(opts)
    

    if argDict.get('-g') is not None:
        gen_corpus()
    if argDict.get('-s') is not None:
        split_sets()
    if argDict.get('-v') is not None:
        gen_vocabulary()

