import pandas as pd
import numpy as np
from sklearn import preprocessing,cross_validation,svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import datetime
from sklearn.metrics import mean_squared_error
from math import sqrt

style.use('ggplot')

df=pd.read_csv('summerfinal.csv')
m=72
df=df[['Year','Month','Day','Hour','Minute','Pressure','Relative Humidity','Wind Speed','Wind Direction','Temperature','Dew Point'],axis=1]
x=np.array(df[['Pressure','Relative Humidity','Wind Speed','Wind Direction','Dew Point']])

ti=np.array(df[['Year','Month','Day','Hour','Minute']])

y=np.array(df['Temperature'])

b=y.shape[0]


new_data = [datetime.datetime(*x) for x in ti]

df['mm/dd/time - 2014']=pd.Series(new_data)


x=preprocessing.scale(x)
x1=x[0:-m]
x_train,x_test,y_train,y_test=cross_validation.train_test_split(x1,y[0:-m],test_size=0.2)

clf=svm.SVR(gamma=1)
clf.fit(x_train,y_train)
a=clf.score(x_test,y_test)
print(a)
ypre=clf.predict(x[-m:])
print(ypre)
np.savetxt("summertable.csv", ypre)
rms = sqrt(mean_squared_error(y[-m:], ypre))
print(rms)

z=np.zeros(b-m)
z[:]=np.nan

predict=np.append(z,ypre)
temperature1=np.append(z,y[-m:])

df['predict']=pd.Series(predict)
df['temperature1']=pd.Series(temperature1)

df = df.set_index('mm/dd/time - 2014')

df['predict'].plot()
df['temperature1'].plot()
plt.ylabel('Temperature')
plt.legend(loc=4)
plt.show()
