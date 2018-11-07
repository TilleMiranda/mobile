#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask App Tille Souza de Miranda!"

@app.route("/hello/<string:name>/")
def hello(name):
    return render_template('template1.html',name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    


# In[ ]:




