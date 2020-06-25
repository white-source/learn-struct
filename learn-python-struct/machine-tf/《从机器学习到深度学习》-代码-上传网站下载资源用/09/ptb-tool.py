
import sys
import os
import random
import re


def shuffle_file(file_name):
    shuffled = []
    with open(file_name) as f:
        for line in f:
            words = line.split()
            random.shuffle(words)
            shuffled.append(" ".join(words))

    with open(file_name, 'w') as f:
        for line in shuffled:
            f.write(line)
            f.write("\n")


def find_poet(line, k=5):
    chars = []
    for ch in line: 
         if u'\u4e00' <= ch <= u'\u9fff':
             chars.append(ch)
    if len(chars)==k*2:
        return " <s> " + " ".join(chars[:k])+" , " + " ".join(chars[k:])+ " "
    return None
 
def gen_poet_library(src_file, dest_dir, k=5):
    library = []
    with open(src_file) as f:
        for line in f:
            poet = find_poet(line, k)
            if poet:
                library.append(poet)
                print(poet)
    total = len(library)
    with open(os.path.join(dest_dir, "ptb.train.txt"), 'w') as f:
        for line in library[:total*10//10]:
            f.write(line)
            f.write("\n")

    with open(os.path.join(dest_dir, "ptb.valid.txt"), 'w') as f:
        for line in library[total*0//10: total*10//10]:
            f.write(line)
            f.write("\n")

    with open(os.path.join(dest_dir, "ptb.test.txt"), 'w') as f:
        for line in library[total*0//10:]:
            f.write(line)
            f.write("\n")
    print("total %d sentences"%total)
    
    
if __name__ == '__main__':
    import getopt

    opts, args = getopt.getopt(sys.argv[1:], "sg", ["file=","k="])
    argDict = dict(opts)

    if argDict.get('-s') is not None:
        shuffle_file(argDict.get("--file"))
    if argDict.get('-g') is not None:
        my_path = os.path.dirname(os.path.abspath(__file__))
        gen_poet_library(os.path.join(my_path, 'data-ptb', 'poet', 'tangshi.txt'),
                         os.path.join(my_path, 'data-ptb', 'poet'), int(argDict.get("--k", 5)))
