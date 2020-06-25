# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:44:20 2017

@author: zfh
"""
from skimage import io,transform
import tensorflow as tf
import numpy as np
import os
import time
import struct

try:  
    import matplotlib.pyplot as plt  
except:  
    raise  
import networkx as nx

animal_dict = {0:'0',1:'1',2:'2',3:'3'}
startTime = time.time()
w=100
h=100
c=3
#定义分批策略
batch = 10
result_out = []
startTime = time.time()
def read_one_image(path):
    img = io.imread(path)
    img = transform.resize(img,(w,h))
    return np.asarray(img)
string = os.listdir("C:/Users/dyw/Desktop/daima/RadarImage_recosys/test")
data = []
path = []
for load in string:
    new_load = "C:/Users/dyw/Desktop/daima/RadarImage_recosys/test/"+load
    path.append(load)
    l_data = read_one_image(new_load)
    data.append(l_data)
    
#    print(path)
#    识别检测函数
def reco_result(data,n):
    feed_dict = {x:data}
    output = []
    logits = graph.get_tensor_by_name("logits_eval:0")
    classification_result = sess.run(logits,feed_dict)
    output = tf.argmax(classification_result,1).eval()
    for i in range(batch):
#    step,norain_nowind,norain_wind,rain_nowind,rain_wind = 0,0,0,0,0
        print(path[n]+'的类型是:'+animal_dict[output[i]])
        n = n+1
        result_out.append(animal_dict[output[i]])
        
with tf.Session() as sess:
    saver = tf.train.import_meta_graph('C:/Users/dyw/Desktop/daima/RadarImage_recosys/radar_net3/model.ckpt.meta')
    saver.restore(sess,tf.train.latest_checkpoint('C:/Users/dyw/Desktop/daima/RadarImage_recosys/radar_net3'))
    graph = tf.get_default_graph()
    x = graph.get_tensor_by_name("x:0")
    name = path[1]
#    indices = np.arange(10)
    for i in range(len(data) // batch):
        t = data[i*batch:(i+1)*batch]
        reco_result(t,i*batch)
        print(len(result_out))
        #print(result_out)
#        output = []
 #       logits = graph.get_tensor_by_name("logits_eval:0")
  #      classification_result = sess.run(logits,feed_dict)
   #     output = tf.argmax(classification_result,1).eval()
   
G=nx.grid_2d_graph(1,1)    
pos=nx.spring_layout(G,iterations=1,k=0)
    #开始画各个小方格  
    #对方格进行上色
for j in range(0,900):
    plt.subplot(30,30,1+j)  
    if result_out == 0:
        nx.draw(G,pos,node_color = '#00ECEC',node_size=70,with_labels=False,font_size=1,width=10)  
    elif result_out == 1:
        nx.draw(G,pos,node_color = '#00A0F8',node_size=70,with_labels=False,font_size=1,width=10)
    elif result_out == 2:
        nx.draw(G,pos,node_color = '#FF0000',node_size=70,with_labels=False,font_size=1,width=10)
    else:
        nx.draw(G,pos,node_color = '#9600B4',node_size=70,with_labels=False,font_size=1,width=10)
    
shijian=name.split('_',4)[2]  #完整时间
shijian1=shijian[0:8]         #8位数时间         
station = 'Z9551'
        
         #创建文件夹
try:
     os.makedirs("D:/product/"+shijian1+"/"+station)
except OSError:
     pass

    # 修改当前工作目录
os.chdir("D:/product/"+shijian1+"/"+station)
    #生成识别图片
plt.savefig(shijian1+'.png')
plt.show()  
    
    
def str2Bytes(a):
    b = bytes(a,encoding='utf-8')
    return struct.pack(str(len(a))+'s',b)

shijian=name.split('_',4)[2]

Year = int(shijian[0:4])
Year = str2Bytes('Year=%i,'%Year)

Month = int(shijian[5:6])
Month = str2Bytes('Month=%i,'%Month)

Day = int(shijian[7:8])
Day = str2Bytes('Day=%i,'%Day)

Hour = int(shijian[9:10])   
Hour = str2Bytes('Hour=%i,'%Hour)

Minute = int(shijian[11:12])
Minute = str2Bytes('Minute=%i,'%Minute)

XNumGrids = 30
YNumGrids = 30
XNumGrids = str2Bytes('XNumGrids=%i,'%XNumGrids)
YNumGrids = str2Bytes('YNumGrids=%i,'%YNumGrids)

RadarCount = 1
RadarCount = str2Bytes('RadarCount=%i,'%RadarCount)

StartLon = 115.0080
StartLat = 34.1170
EndLon = 119.5080
EndLat = 29.6170
StartLon = str2Bytes('StartLon=%f,'%StartLon)
StartLat = str2Bytes('StartLat=%f,'%StartLat)
EndLon = str2Bytes('EndLon=%f,'%EndLon)
EndLat = str2Bytes('EndLat=%f,'%EndLat)

XReso = 15
YReso = 15
XReso = str2Bytes('XReso=%f,'%XReso)
YReso = str2Bytes('YReso=%f,'%YReso)

RadarStationName="合肥"
RadarStationName = str2Bytes('RadarStationName=%s,'%RadarStationName)

RadarLongitude = 117.258
RadarLatitude = 31.867
MosaicFlag = 1
RadarLongitude = str2Bytes('RadarLongitude=%f,'%RadarLongitude)
RadarLatitude = str2Bytes('RadarLatitude=%f,'%RadarLatitude)
MosaicFlag = str2Bytes('MosaicFlag=%f,'%MosaicFlag)


output = result_out

title='Nowcasting_RAINWIND'+'_'+shijian+'_'+station       #bin文件名字
file = open(title+'.bin','wb')         
#写数据
file.write(Year)
file.write(Month)
file.write(Day)
file.write(Hour)
file.write(Minute)

file.write(XNumGrids)
file.write(YNumGrids)
file.write(RadarCount)
file.write(StartLon)
file.write(StartLat)
file.write(EndLon)
file.write(EndLat)   

file.write(XReso)
file.write(YReso)
file.write(RadarStationName)
file.write(RadarLongitude)
file.write(RadarLatitude)
file.write(MosaicFlag)             #头文件

#for load in string: 
#    file.write(output)             #结果文件
file = open(title+'.bin','rb')
#读数据
#file.read()
    
    
endTime = time.time()
print(endTime - startTime)
        
#        logits = graph.get_tensor_by_name("logits_eval:0")
        
#    classification_result = sess.run(logits,feed_dict)
  
#    output = []
#    output = tf.argmax(classification_result,1).eval()
#    step,norain_nowind,norain_wind,rain_nowind,rain_wind = 0,0,0,0,0
#    for i in range(len(output)):
#        if animal_dict[output[i]] == "norain-nowind":
#            norain_nowind += 1
#        elif animal_dict[output[i]] == "norain-wind":
#            norain_wind += 1
#        elif animal_dict[output[i]] == "rain-nowind":
#            rain_nowind += 1
#        elif animal_dict[output[i]] == "rain-wind":
#            rain_wind += 1
#        print(path[i]+'的类型是:'+animal_dict[output[i]])
#        step += 1
#    print(classification_result)
#    endTime = time.time()
#    print("无雨无风率:"+str(norain_nowind/step),"无雨有风率:"+str(norain_wind/step),"有雨无风率:"+str(rain_nowind/step),"有雨有风率:"+str(rain_wind/step))
#    print(endTime-startTime)
