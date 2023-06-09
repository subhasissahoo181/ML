# -*- coding: utf-8 -*-
"""Matplotlib.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G5aspIt5jBYoEYF4FYlAY5C_Gr6LliG_
"""

!pip install matplotlib

"""Matplotlib:

Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias.

grid():

 function to add grid lines to the plot.

marker/linestyle/color/width:

 both are keyword argument. marker to emphasize each point with a specified marker. linestyle, or shorter ls, to change the style of the plotted line.

 Title/Label:
 
 xlabel() and ylabel() functions to set a label for the x- and y-axis. create a Title for lable.


"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
#http://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html

x = np.linspace(0,10,100)
print(x)

plt.plot( x , np.sin(x) )
plt.plot( x , np.cos(x) );

"""Two modes

1. %matplotlin inline (default mode)

2. %matplotlib notebook
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib notebook
plt.plot( x , np.sin(x) )
plt.plot( x , np.cos(x) );

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
plt.plot( x , np.sin(x) )
plt.plot( x , np.cos(x) );

plt.figure()
plt.subplot(2,1,1)
plt.plot(x,np.sin(x))
plt.subplot(2,1,2)
plt.plot(x,np.cos(x));

plt.figure(figsize=(16,4))
plt.subplot(1,2,1)
plt.plot(x,np.sin(x))
plt.subplot(1,2,2)
plt.plot(x,np.cos(x));

plt.figure()
plt.subplot(2,2,1)
plt.plot(x,np.sin(x))
plt.subplot(2,2,2)
plt.plot(x,np.cos(x));
plt.subplot(2,2,3)
plt.plot(x,np.tan(x));

plt.figure(figsize=(15,4))
plt.subplot(2,2,1)
plt.plot(x,np.sin(x))
plt.subplot(2,2,2)
plt.plot(x,np.cos(x));
plt.subplot(2,2,3)
plt.plot(x,np.tan(x));

plt.figure(figsize=(15,4))
plt.subplot(221)
plt.plot(x,np.sin(x))
plt.subplot(222)
plt.plot(x,np.cos(x));
plt.subplot(2,2,3)
plt.plot(x,np.tan(x));

import warnings
warnings.simplefilter('ignore')
import pandas as pd

df=pd.read_csv("/content/student_records.csv")
df.head()

plt.plot(df['ResearchScore'],df['ProjectScore'],marker='*',ls = 'dotted', c = '#4CAF50', linewidth = '2.5');   # marker, color, width and line use

plt.scatter(df['ResearchScore'],df['ProjectScore'],marker='o');

plt.plot(x,np.sin(x),color='blue')
plt.plot(x,np.sin(x-1),color='g')
plt.plot(x,np.sin(x-2),color='0.75') # grayscale 0 and 1, 0=dark, 1=white
plt.plot(x,np.sin(x-3),color='#FFDD44')
plt.plot(x,np.sin(x-4),color=(1.0,0.2,0.3))

plt.plot(x,x+0,linestyle='solid')
plt.plot(x,x+1,linestyle='dashed')
plt.plot(x,x+2,linestyle='dotted')
plt.plot(x,x+3,linestyle='dashdot')

plt.plot(x,x+4,linestyle='-')
plt.plot(x,x+5,linestyle='--')
plt.plot(x,x+6,linestyle=':')
plt.plot(x,x+7,linestyle='-.');

plt.plot(x,x+0,'-g')
plt.plot(x,x+1,'--c')
plt.plot(x,x+2,'-.k')
plt.plot(x,x+3,':r');

plt.plot(x,np.sin(x))
font1 = {'family':'serif','color':'blue','size':20}
plt.title("A Sine Curve", loc="left", fontdict = font1)    # location and font use
plt.xlabel("x")
plt.ylabel("sin(x)");

plt.plot(x,np.sin(x),'-g',label='sin(x)')
plt.plot(x,np.cos(x),':b',label='cos(x)')
plt.legend();

plt.plot(x,np.sin(x),'s',color='black');
#plt.plot(x,np.sin(x),'d',color='black');
# x + o d - 1 2 3 4

plt.scatter(x,np.sin(x),marker='d');

for i in range(1,7):
    plt.subplot(2,3,i)
    plt.text(0.5,0.5,(2,3,i),fontsize=10,ha='center')



"""Seaborn"""

!pip install seaborn

import seaborn as sns

sns.get_dataset_names()

len(sns.get_dataset_names())

tips = sns.load_dataset('tips')
tips.head()

tips.shape

print(tips['sex'].value_counts())
print(tips['smoker'].value_counts())
print(tips['day'].value_counts())
print(tips['time'].value_counts())

y = tips[tips['sex']=='Male'].sample(100)
y

"""## Seaborn Continuous Plots"""

# distplot
# It shows the distribution of univariate set of observations
# Use it when you have one continuous variable
sns.distplot(tips['total_bill']);

sns.distplot(tips['total_bill'] , kde=False);

sns.distplot(tips['total_bill'] , kde=False , bins=30);

tips.columns

# jointplot(): It is used for bivariate data
# Use it when you have two continuous variables

sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter');

sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex');

sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg'); # Regression Line

sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde');

# pairplot
# It plots pairwise relationship for the ENTIRE DATAFRAME
# It also supports a color hue argument(for categorical data)
sns.pairplot(tips);

sns.pairplot(tips,hue='sex');

sns.pairplot(tips,hue='sex',palette='coolwarm');

# https://seaborn.pydata.org/generated/seaborn.color_palette.html
# https://seaborn.pydata.org/tutorial/color_palettes.html



"""## Seaborn Categorical Plots"""

# barplot: It is a general plot that helps us to aggregate the data
# Categorical vs Continuous

sns.barplot(x='sex',y='total_bill',data=tips);

# estimator is basically the function to be applied
sns.barplot(x='sex',y='total_bill',data=tips, estimator=np.std);

# countplot: It is same as barplot except the estimator here is explicitly counting
# the no of occurences
# Therefore we only pass x value

sns.countplot(x='sex',data=tips);

# boxplot/ box-and-whisker plot:
# It shows the distribution of quantitative data and helps in
# identifying the Outliers
# x is a categorical point
# y is a numeric point

sns.boxplot(x='day',y='total_bill',data=tips,palette='rainbow');

sns.boxplot(data=tips,palette='rainbow');
plt.xticks(rotation=75)

sns.boxplot(data=tips,palette='rainbow',orient='h');

"""Seaborn Matrix plots"""

flights = sns.load_dataset("flights")
flights.head()

flights['year'].value_counts()

flights.shape

tips.corr() # correlation matrix

sns.heatmap( tips.corr());

sns.heatmap( tips.corr() , cmap='coolwarm' , annot=True );

