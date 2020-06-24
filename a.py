import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

age = np.array([25.43, 33.00, 23.01, 28.15, 34.25, 28.14, 15.01, 8.0, 19.3, 24.0, 10.01, 15.00, 16.11, 30.5, 35.1])
weight = np.array([80.00, 76.22, 60.11, 58.21, 66.11, 78.25, 50.21, 30.41, 68.11, 69.11, 50.11, 48.33, 52.3, 70.8, 82.6])
height = np.array([180.25, 175.3, 168.4, 165.5, 174.5, 179.3, 158.2, 130.5, 173.11, 169.5, 142.0, 138.8, 175.2, 174.5, 188.6])
gender = np.array(['남', '남', '여', '여', '남', '남', '여', '여', '여', '남', '남', '여', '남', '여', '남'])

#평균 오차 함수
def mse_line2(x0,x1,t,w):
    y=w[0]*x0+w[1]*x1+w[2]
    mse=np.mean((y-t)**2)
    return mse

#평균 제곱 오차의 기울기
def dmse_line2(x0,x1, t, w):
    y=w[0]*x0+w[1]*x1+w[2]
    d_w0=2*np.mean((y-t)*x0)
    d_w1=2*np.mean((y-t)*x1)
    d_w2=2*np.mean(y-t)
    return d_w0,d_w1,d_w2

#경사 하강법
def fit_line_num2(x0,x1,t):
    w_init=[1,3,100]
    alpha=0.0001
    i_max=100000
    eps=0.1
    w_i=np.zeros([i_max,3])
    w_i[0,:]=w_init
    for i in range(1,i_max):
        dmse=dmse_line2(x0,x1,t,w_i[i-1])
        w_i[i,0]=w_i[i-1,0]-alpha*dmse[0]
        w_i[i,1]=w_i[i-1,1]-alpha*dmse[1]
        w_i[i,2]=w_i[i-1,2]-alpha*dmse[2]
        if max(np.absolute(dmse))<eps:
            break
    w_0=w_i[i,0]
    w_1=w_i[i,1]
    w_2=w_i[i,2]
    w_i=w_i[:i,:]
    return w_0,w_1,w_2,dmse,w_i

#2차원 데이터의 표시 (w값 표시)
def show_data(ax,x0,x1,t):
    for i in range(len(x0)):
         ax.plot([x0[i],x0[i]],[x1[i],x1[i]],[95,t[i]],'gray',)
    ax.plot(x0,x1,t,'o',color='cornflowerblue',markeredgecolor='black',
            markersize=6,markeredgewidth=0.5)
    ax.view_init(25,-75)

W0,W1,W2,dMSE,W_history=fit_line_num2(age,weight,height)

print('반복 횟수 {0}'.format(W_history.shape[0]))
print('W=[{0:.6f}, {1:.6f}, {2:.6f}]'.format(W0, W1, W2))
print('dMSE=[{0:.6f}, {1:.6f}, {2:.6f}]'.format(dMSE[0], dMSE[1], dMSE[2]))

ax1=[]
ax2=[]
ax3=[]
for i in range(1000):
    ax1.append(W_history[i,0])
    ax2.append(W_history[i,1])
    ax3.append(W_history[i,2])
ax1=np.array(ax1)
ax2=np.array(ax2)
ax3=np.array(ax3)

plt.figure(figsize=(6,5))
ax=plt.subplot(1,1,1,projection='3d')
show_data(ax,ax1,ax2,ax3)
plt.show()
