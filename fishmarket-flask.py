from flask import Flask, render_template, request
import pickle
import  os
import pandas as pd

app = Flask(__name__,template_folder='templates', static_folder='static_Files')
filename = 'Model/fishdata_model.pkl'
fish_model = pickle.load(open(filename, 'rb'))
port = int(os.environ.get("PORT", 8000))

@app.route('/')
def index():
    return render_template(r'index.html')

@app.route('/predictions', methods=['POST'])
def predictions():
    print(dict(request.form))
    # form = request.form.values()
    # vals = [float(i) for i in list(form)]
    df = pd.DataFrame(dict(request.form),index=[0])
    print(df)
    df.columns = ['Vlength', 'Dlength', 'Clength', 'Height', 'Width']
    print(df)
    predictedvalue = fish_model.predict(df)
    
    print(predictedvalue)
    
    return render_template('index.html', prediction_text='The predicted fish weight is: {}'.format(predictedvalue[0]))
    # return render_template('predictions.html', Weight=predictedvalue)


if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=port)