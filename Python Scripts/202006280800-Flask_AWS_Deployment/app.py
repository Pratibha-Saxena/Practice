#!/usr/bin/env python
# coding: utf-8

# In[1]:


import flask as f
import pickle as pkl


# In[2]:


# Initialize your application with a name
app = f.Flask(__name__)
model = pkl.load(open("model.pkl", "rb"))


# In[3]:


@app.route("/")
def home():
    return f.render_template("index.html")


# In[4]:


@app.route("/predict", methods=["POST"])
def predict():
    A=[]
    for i in f.request.form.values():
        A.append(int(i))
    pred_profit = model.predict([[A[0], A[1]]])
    return f.render_template("index.html", pred="Predicted_Profit: %.2f"%pred_profit)


# In[6]:


if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:





# In[ ]:




