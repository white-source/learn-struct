# encoding=utf-8

import jieba

doc = "人工智能来源于机器人学"
seg_list = jieba.cut(doc, cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))

seg_list = jieba.cut(doc, cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  


doc = "《三国演义》是根据三国时期的史实和民间传说创作而成的优秀历史小说。它的内容丰富多彩，为读者留下了深厚多而的认识价值。故事远起汉灵帝年间刘、关、张桃园结义民间传说，描述了东汉末年和三国时期近百年发生的重大历史事件，和众多的叱咤风云的英雄人物。"
print("/ ".join(jieba.cut(doc)))
