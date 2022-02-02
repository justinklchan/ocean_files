# 3/3/4
import numpy as np
import matplotlib.pyplot as plt

def read_timstamp(name):
    text_file = open(name, "r")
    lines = text_file.readlines()
    time_list = []
    for t in lines:
        time_list.append(int(t))
    
    new_time_list = []
    for i in range(1, len(time_list)):
        new_time_list.append((time_list[i] - time_list[0])/1000)
    return new_time_list


folder = '../'
f1 = read_timstamp('../5_1643764952236/Alice-Sounding-log.txt')
f2 = read_timstamp('../5_1643764957994/Alice-Sounding-log.txt')
f3 = read_timstamp('../5_1643764953769/Bob-Feedback-log.txt')

f1=np.asarray(f1)
f2=np.asarray(f2)
f3=np.asarray(f3)

f1=f1-f1[1]
f2=f2-f2[0]-2.45
f3=f3-f3[0]-4.15

y_sounding = np.ones(len(f1))
y_sounding2 = np.ones(len(f2))
y_feedback = np.ones(len(f3))

print (f1)
print (f2)

plt.figure(1)
plt.subplot(311)
plt.stem(f1, y_sounding,  'r-x', label='sounding')
plt.xlim([0,120])
plt.subplot(312)
plt.stem(f2, y_sounding2,  'k-x', label='sounding')
plt.xlim([0,120])
plt.subplot(313)
plt.stem(f3, y_feedback,  'b-x', label='feedback')
plt.xlim([0,120])
plt.show()
