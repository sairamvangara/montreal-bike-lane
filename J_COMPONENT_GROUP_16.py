#!/usr/bin/env python
# coding: utf-8

# <p><img alt="Colaboratory logo" height="45px" src="/img/colab_favicon.ico" align="left" hspace="10px" vspace="0px"></p>
# 
# <h1>What is Colaboratory?</h1>
# 
# Colaboratory, or "Colab" for short, allows you to write and execute Python in your browser, with 
# - Zero configuration required
# - Free access to GPUs
# - Easy sharing
# 
# Whether you're a **student**, a **data scientist** or an **AI researcher**, Colab can make your work easier. Watch [Introduction to Colab](https://www.youtube.com/watch?v=inN8seMm7UI) to learn more, or just get started below!

# ## **Getting started**
# 
# The document you are reading is not a static web page, but an interactive environment called a **Colab notebook** that lets you write and execute code.
# 
# For example, here is a **code cell** with a short Python script that computes a value, stores it in a variable, and prints the result:

# In[ ]:


seconds_in_a_day = 24 * 60 * 60
seconds_in_a_day


# To execute the code in the above cell, select it with a click and then either press the play button to the left of the code, or use the keyboard shortcut "Command/Ctrl+Enter". To edit the code, just click the cell and start editing.
# 
# Variables that you define in one cell can later be used in other cells:

# In[ ]:


seconds_in_a_week = 7 * seconds_in_a_day
seconds_in_a_week


# Colab notebooks allow you to combine **executable code** and **rich text** in a single document, along with **images**, **HTML**, **LaTeX** and more. When you create your own Colab notebooks, they are stored in your Google Drive account. You can easily share your Colab notebooks with co-workers or friends, allowing them to comment on your notebooks or even edit them. To learn more, see [Overview of Colab](/notebooks/basic_features_overview.ipynb). To create a new Colab notebook you can use the File menu above, or use the following link: [create a new Colab notebook](http://colab.research.google.com#create=true).
# 
# Colab notebooks are Jupyter notebooks that are hosted by Colab. To learn more about the Jupyter project, see [jupyter.org](https://www.jupyter.org).

# ## Data science
# 
# With Colab you can harness the full power of popular Python libraries to analyze and visualize data. The code cell below uses **numpy** to generate some random data, and uses **matplotlib** to visualize it. To edit the code, just click the cell and start editing.

# In[ ]:


import numpy as np
from matplotlib import pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()


# In[ ]:





# You can import your own data into Colab notebooks from your Google Drive account, including from spreadsheets, as well as from Github and many other sources. To learn more about importing data, and how Colab can be used for data science, see the links below under [Working with Data](#working-with-data).

# ## Machine learning
# 
# With Colab you can import an image dataset, train an image classifier on it, and evaluate the model, all in just [a few lines of code](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb). Colab notebooks execute code on Google's cloud servers, meaning you can leverage the power of Google hardware, including [GPUs and TPUs](#using-accelerated-hardware), regardless of the power of your machine. All you need is a browser.

# Colab is used extensively in the machine learning community with applications including:
# - Getting started with TensorFlow
# - Developing and training neural networks
# - Experimenting with TPUs
# - Disseminating AI research
# - Creating tutorials
# 
# To see sample Colab notebooks that demonstrate machine learning applications, see the [machine learning examples](#machine-learning-examples) below.

# ## More Resources
# 
# ### Working with Notebooks in Colab
# - [Overview of Colaboratory](/notebooks/basic_features_overview.ipynb)
# - [Guide to Markdown](/notebooks/markdown_guide.ipynb)
# - [Importing libraries and installing dependencies](/notebooks/snippets/importing_libraries.ipynb)
# - [Saving and loading notebooks in GitHub](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)
# - [Interactive forms](/notebooks/forms.ipynb)
# - [Interactive widgets](/notebooks/widgets.ipynb)
# - <img src="/img/new.png" height="20px" align="left" hspace="4px" alt="New"></img>
#  [TensorFlow 2 in Colab](/notebooks/tensorflow_version.ipynb)
# 
# <a name="working-with-data"></a>
# ### Working with Data
# - [Loading data: Drive, Sheets, and Google Cloud Storage](/notebooks/io.ipynb) 
# - [Charts: visualizing data](/notebooks/charts.ipynb)
# - [Getting started with BigQuery](/notebooks/bigquery.ipynb)
# 
# ### Machine Learning Crash Course
# These are a few of the notebooks from Google's online Machine Learning course. See the [full course website](https://developers.google.com/machine-learning/crash-course/) for more.
# - [Intro to Pandas DataFrame](https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/pandas_dataframe_ultraquick_tutorial.ipynb)
# - [Linear regression with tf.keras using synthetic data](https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/linear_regression_with_synthetic_data.ipynb)
# 
# 
# <a name="using-accelerated-hardware"></a>
# ### Using Accelerated Hardware
# - [TensorFlow with GPUs](/notebooks/gpu.ipynb)
# - [TensorFlow with TPUs](/notebooks/tpu.ipynb)

# <a name="machine-learning-examples"></a>
# 
# ## Machine Learning Examples
# 
# To see end-to-end examples of the interactive machine learning analyses that Colaboratory makes possible, check out these  tutorials using models from [TensorFlow Hub](https://tfhub.dev).
# 
# A few featured examples:
# 
# - [Retraining an Image Classifier](https://tensorflow.org/hub/tutorials/tf2_image_retraining): Build a Keras model on top of a pre-trained image classifier to distinguish flowers.
# - [Text Classification](https://tensorflow.org/hub/tutorials/tf2_text_classification): Classify IMDB movie reviews as either *positive* or *negative*.
# - [Style Transfer](https://tensorflow.org/hub/tutorials/tf2_arbitrary_image_stylization): Use deep learning to transfer style between images.
# - [Multilingual Universal Sentence Encoder Q&A](https://tensorflow.org/hub/tutorials/retrieval_with_tf_hub_universal_encoder_qa): Use a machine learning model to answer questions from the SQuAD dataset.
# - [Video Interpolation](https://tensorflow.org/hub/tutorials/tweening_conv3d): Predict what happened in a video between the first and the last frame.
# 

# In[ ]:


import pandas as pd
d=pd.read_csv('/content/excel j comp3.csv')
print(d)


# In[ ]:


x1=d['Boyer']
y=d['Berri1']
print(x1,y)


# In[ ]:


ee=[]
import numpy as np
mm=[]
cc=[]
def liner(m1,c):
  ye=[]
  yp=[]
  sum=0
  mm.append(m1)
  cc.append(c)
  for i in range(0,len(x1)):
    yp.append(m1*x1[i]+c)
    ye.append((y[i]-yp[i])**2)
  #print(ye)
  for i in range(0,len(x1)):
    sum=sum+ye[i]
  ee1=np.mod(sum,len(x1))
  print(ee1)
  ee.append(ee1)
  #print(ee1)


# In[ ]:


a=np.array(ee).min()
print(a)
ind=ee.index(a)
print(ind)
print(mm[ind],cc[ind])
print(len(ee))
print("lll",ee[22])


# In[ ]:


for i in range(0,50):
  liner(i+10,i+20)


# In[ ]:


from matplotlib import pyplot as pt
import numpy as np
x=[]
for i in range(0,50):
  x.append(i)
pt.plot(x,ee)


# In[ ]:


from matplotlib import pyplot as plt
plt.scatter(x1,y)


# In[ ]:


x2=d['lipian']
y=d['Berri1']
print(x2,y)


# In[ ]:


ee=[]
import numpy as np
mm=[]
cc=[]
def liner(m1,m2,c):
  ye=[]
  yp=[]
  sum=0
  mm.append(m1)
  cc.append(c)
  for i in range(0,len(x1)):
    yp.append(m1*x1[i]+m2*x2[i]+c)
    ye.append((y[i]-yp[i])**2)
  for i in range(0,len(x1)):
    sum=sum+ye[i]
  ee1=np.mod(sum,len(x1))
  ee.append(ee1)
  print(ee1)


# In[ ]:


a=np.array(ee).min()
print(a)
ind=ee.index(a)
print(ind)
print(mm[ind],cc[ind])
print(len(ee))
print("lll",ee[16])


# In[ ]:


for i in range(0,50):
  liner(i+10,i+20,i+i)


# In[ ]:


from matplotlib import pyplot as pt
import numpy as np
x=[]
for i in range(0,50):
  x.append(i)
pt.plot(x,ee)


# In[ ]:


from matplotlib import pyplot as plt
plt.scatter(x2,y)


# In[ ]:


x3=d['california']
y=d['Berri1']
print(x3,y)


# In[ ]:


ee=[]
import numpy as np
mm=[]
cc=[]
def liner(m1,m2,m3,c):
  ye=[]
  yp=[]
  sum=0
  mm.append(m1)
  cc.append(c)
  
  for i in range(0,len(x1)):
    yp.append(m1*x1[i]+m2*x2[i]+m3*x3[i]+c)
    ye.append((y[i]-yp[i])**2)
  for i in range(0,len(x1)):
    sum=sum+ye[i]
  ee1=np.mod(sum,len(x1))
  ee.append(ee1)
  print(ee1)


# In[ ]:


a=np.array(ee).min()
print(a)
ind=ee.index(a)
print(ind)
print(mm[ind],cc[ind])
print(len(ee))
print("lll",ee[90])


# In[ ]:


for i in range(0,100):
  liner(i+50,i+100,i+i,i+1)


# In[ ]:


from matplotlib import pyplot as pt
import numpy as np
x=[]
for i in range(0,100):
  x.append(i)
pt.plot(x,ee)


# In[ ]:


from matplotlib import pyplot as plt
plt.scatter(x3,y)


# In[ ]:


x4=d['Maisonneuve_2']
y=d['Berri1']
print(x4,y)


# In[ ]:


ee=[]
import numpy as np
mm=[]
cc=[]
def liner(m1,m2,m3,m4,c):
  ye=[]
  yp=[]
  sum=0
  mm.append(m1)
  cc.append(c)
  
  for i in range(0,len(x1)):
    yp.append(m1*x1[i]+m2*x2[i]+m3*x3[i]+m4*x4[i]+c)
    ye.append((y[i]-yp[i])**2)
  for i in range(0,len(x1)):
    sum=sum+ye[i]
  ee1=np.mod(sum,len(x1))
  ee.append(ee1)
  print(ee1)


# In[ ]:


a=np.array(ee).min()
print(a)
ind=ee.index(a)
print(ind)
print(mm[ind],cc[ind])
print(len(ee))
print("lll",ee[18])


# In[ ]:


for i in range(0,50):
  liner(i+10,i+30,i+i,i+1,i+5)


# In[ ]:


from matplotlib import pyplot as pt
import numpy as np
x=[]
for i in range(0,50):
  x.append(i)
pt.plot(x,ee)


# In[ ]:


from matplotlib import pyplot as plt
plt.scatter(x4,y)


# In[ ]:


x5=d['Maisonneuve_3']
y=d['Berri1']
print(x5,y)


# In[ ]:


ee=[]
import numpy as np
mm=[]
cc=[]
def liner(m1,m2,m3,m4,m5,c):
  ye=[]
  yp=[]
  sum=0
  mm.append(m1)
  cc.append(c)
  for i in range(0,len(x1)):
    yp.append(m1*x1[i]+m2*x2[i]+m3*x3[i]+m4*x4[i]+m5*x5[i]+c)
    ye.append((y[i]-yp[i])**2)
  for i in range(0,len(x1)):
    sum=sum+ye[i]
  ee1=np.mod(sum,len(x1))
  ee.append(ee1)
  print(ee1)


# In[ ]:


a=np.array(ee).min()
print(a)
ind=ee.index(a)
print(ind)
print(mm[ind],cc[ind])
print(len(ee))
print("lll",ee[46])


# In[ ]:


for i in range(0,50):
  liner(i+10,i+20,i+30,i+i,i+5,i+9)


# In[ ]:


from matplotlib import pyplot as pt
import numpy as np
x=[]
for i in range(0,50):
  x.append(i)
pt.plot(x,ee)


# In[ ]:


from matplotlib import pyplot as plt
plt.scatter(x5,y)


# In[ ]:


x6=d['Notre-Dame']
y=d['Berri1']
print(x6,y)


# In[ ]:


ee=[]
import numpy as np
mm=[]
cc=[]
def liner(m1,m2,m3,m4,m5,m6,c):
  ye=[]
  yp=[]
  sum=0
  mm.append(m1)
  cc.append(c)
  for i in range(0,len(x1)):
    yp.append(m1*x1[i]+m2*x2[i]+m3*x3[i]+m4*x4[i]+m5*x5[i]+m6*x6[i]+c)
    ye.append((y[i]-yp[i])**2)
  for i in range(0,len(x1)):
    sum=sum+ye[i]
  ee1=np.mod(sum,len(x1))
  ee.append(ee1)
  print(ee1)


# In[ ]:


a=np.array(ee).min()
print(a)
ind=ee.index(a)
print(ind)
print(mm[ind],cc[ind])
print(len(ee))
print("lll",ee[7])


# In[ ]:


for i in range(0,50):
  liner(i+10,i+20,i+30,i+i,i+5,i+9,i+13)


# In[ ]:


from matplotlib import pyplot as pt
import numpy as np
x=[]
for i in range(0,50):
  x.append(i)
pt.plot(x,ee)


# In[ ]:


from matplotlib import pyplot as plt
plt.scatter(x6,y)


# In[ ]:


x7=d['Parc']
y=d['Berri1']
print(x7,y)


# In[ ]:


ee=[]
import numpy as np
mm=[]
cc=[]
def liner(m1,m2,m3,m4,m5,m6,m7,c):
  ye=[]
  yp=[]
  sum=0
  mm.append(m1)
  cc.append(c)
  for i in range(0,len(x1)):
    yp.append(m1*x1[i]+m2*x2[i]+m3*x3[i]+m4*x4[i]+m5*x5[i]+m6*x6[i]+m7*x7[i]+c)
    ye.append((y[i]-yp[i])**2)
  for i in range(0,len(x1)):
    sum=sum+ye[i]
  ee1=np.mod(sum,len(x1))
  ee.append(ee1)
  print(ee1)


# In[ ]:


a=np.array(ee).min()
print(a)
ind=ee.index(a)
print(ind)
print(mm[ind],cc[ind])
print(len(ee))
print("lll",ee[36])


# In[ ]:


for i in range(0,50):
  liner(i+10,i+20,i+30,i+i,i+5,i+9,i+13,i+15)


# In[ ]:


from matplotlib import pyplot as pt
import numpy as np
x=[]
for i in range(0,50):
  x.append(i)
pt.plot(x,ee)


# In[ ]:


from matplotlib import pyplot as plt
plt.scatter(x7,y)


# In[ ]:


x8=d['PierDup']
y=d['Berri1']
print(x8,y)


# In[ ]:


ee=[]
import numpy as np
mm=[]
cc=[]
def liner(m1,m2,m3,m4,m5,m6,m7,m8,c):
  ye=[]
  yp=[]
  sum=0
  mm.append(m1)
  cc.append(c)
  for i in range(0,len(x1)):
    yp.append(m1*x1[i]+m2*x2[i]+m3*x3[i]+m4*x4[i]+m5*x5[i]+m6*x6[i]+m7*x7[i]+m8*x8[i]+c)
    ye.append((y[i]-yp[i])**2)
  for i in range(0,len(x1)):
    sum=sum+ye[i]
  ee1=np.mod(sum,len(x1))
  ee.append(ee1)
  print(ee1)


# In[ ]:


a=np.array(ee).min()
print(a)
ind=ee.index(a)
print(ind)
print(mm[ind],cc[ind])
print(len(ee))
print("lll",ee[25])


# In[ ]:


for i in range(0,50):
  liner(i+10,i+20,i+30,i+i,i+5,i+9,i+13,i+15,i+20)


# In[ ]:


from matplotlib import pyplot as pt
import numpy as np
x=[]
for i in range(0,50):
  x.append(i)
pt.plot(x,ee)


# In[ ]:


from matplotlib import pyplot as plt
plt.scatter(x8,y)


# In[ ]:


x9=d['Rachel ']
y=d['Berri1']
print(x9,y)


# In[ ]:


ee=[]
import numpy as np
mm=[]
cc=[]
def liner(m1,m2,m3,m4,m5,m6,m7,m8,m9,c):
  ye=[]
  yp=[]
  sum=0
  mm.append(m1)
  cc.append(c)
  for i in range(0,len(x1)):
    yp.append(m1*x1[i]+m2*x2[i]+m3*x3[i]+m4*x4[i]+m5*x5[i]+m6*x6[i]+m7*x7[i]+m8*x8[i]+m9*x9[i]+c)
    ye.append((y[i]-yp[i])**2)
  for i in range(0,len(x1)):
    sum=sum+ye[i]
  ee1=np.mod(sum,len(x1))
  ee.append(ee1)
  print(ee1)


# In[ ]:


a=np.array(ee).min()
print(a)
ind=ee.index(a)
print(ind)
print(mm[ind],cc[ind])
print(len(ee))
print("lll",ee[20])


# In[ ]:


for i in range(0,50):
  liner(i+10,i+20,i+30,i+i,i+5,i+9,i+13,i+15,i+20,i+25)


# In[ ]:


from matplotlib import pyplot as pt
import numpy as np
x=[]
for i in range(0,50):
  x.append(i)
pt.plot(x,ee)


# In[ ]:


from matplotlib import pyplot as plt
plt.scatter(x9,y)


# In[ ]:


x10=d['Rachel / Papineau']
y=d['Berri1']
print(x10,y)


# In[ ]:


ee=[]
import numpy as np
mm=[]
cc=[]
def liner(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,c):
  ye=[]
  yp=[]
  sum=0
  mm.append(m1)
  cc.append(c)
  for i in range(0,len(x1)):
    yp.append(m1*x1[i]+m2*x2[i]+m3*x3[i]+m4*x4[i]+m5*x5[i]+m6*x6[i]+m7*x7[i]+m8*x8[i]+m9*x9[i]+m10*x10[i]+c)
    ye.append((y[i]-yp[i])**2)
  for i in range(0,len(x1)):
    sum=sum+ye[i]
  ee1=np.mod(sum,len(x1))
  ee.append(ee1)
  print(ee1)


# In[ ]:


a=np.array(ee).min()
print(a)
ind=ee.index(a)
print(ind)
print(mm[ind],cc[ind])
print(len(ee))
print("lll",ee[21])


# In[ ]:


for i in range(0,50):
  liner(i+10,i+20,i+30,i+i,i+5,i+9,i+13,i+15,i+20,i+25,i+26)


# In[ ]:


from matplotlib import pyplot as pt
import numpy as np
x=[]
for i in range(0,50):
  x.append(i)
pt.plot(x,ee)


# In[ ]:


from matplotlib import pyplot as plt
plt.scatter(x10,y)

