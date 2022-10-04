import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

year = [5,7,12,23,25,28,29,34,35,40]
salary = [82,80,103,118,172,127,204,189,99,166]

df = pd.DataFrame(columns=['Years','Salary'])
df.Years = year
df.Salary = salary

plt.scatter(x=df.Years,y=df.Salary)
plt.show()

df1 = df
for i in range(2):
    f = df.Salary.mean()
    if(i>0):
        df['f'+str(i)] = df['f'+str(i-1)] + df['h'+str(i)]
    else:
        df['f'+str(i)] = f
    df['y-f'+str(i)] = df.Salary - df['f'+str(i)]
    splitIndex = np.random.randint(0,df.shape[0]-1)
    a= []
    h_upper = df['y-f'+str(i)][0:splitIndex].mean()
    h_bottom = df['y-f'+str(i)][splitIndex:].mean()
    for j in range(splitIndex):
        a.append(h_upper)
    for j in range(df.shape[0]-splitIndex):
        a.append(h_bottom)
    df['h'+str(i+1)] = a

for i in range(100):
    f = df.Salary.mean()
    if(i>0):
        df['f'+str(i)] = df['f'+str(i-1)] + df['h'+str(i)]
    else:
        df['f'+str(i)] = f
    df['y-f'+str(i)] = df.Salary - df['f'+str(i)]
    splitIndex = np.random.randint(0,df.shape[0]-1)
    a= []
    h_upper = df['y-f'+str(i)][0:splitIndex].mean()
    h_bottom = df['y-f'+str(i)][splitIndex:].mean()
    for j in range(splitIndex):
        a.append(h_upper)
    for j in range(df.shape[0]-splitIndex):
        a.append(h_bottom)
    df['h'+str(i+1)] = a

plt.figure(figsize=(15,10))
plt.scatter(df.Years,df.Salary)
plt.plot(df.Years,df.f1,label = 'f1')
plt.plot(df.Years,df.f10,label = 'f10')
plt.plot(df.Years,df.f99,label = 'f99')
plt.legend()
plt.show()
