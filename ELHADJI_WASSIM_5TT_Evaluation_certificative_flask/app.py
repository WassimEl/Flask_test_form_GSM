import json
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    numero = request.form['numero']
    modele = request.form['modele']
    marque = request.form['marque']
    annee = request.form['annee']
  
    try:
        with open('data.json', 'r') as infile:
            file_data = infile.read()
            if file_data.strip():
                data = json.loads(file_data)
            else:
                data = []
    except FileNotFoundError:
        data = []

    new_data = {
        'numero': numero,
        'modele': modele,
        'marque': marque,
        'annee': annee
    }
    data.append(new_data)

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)

    return redirect('/result')

@app.route('/result', methods=['GET'])
def result():
    try:
        with open('data.json', 'r') as infile:
            file_data = infile.read()
            if file_data.strip():
                users = json.loads(file_data)
            else:
                users = []
    except FileNotFoundError:
        users = []

    return render_template('result.html', data=users)

if __name__ == '__main__':
    app.run(debug=True)
