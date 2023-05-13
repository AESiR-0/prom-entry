from flask import *
from searcher_csv import csv_parse

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def search():
    if(request.method=='POST'):
        global name
        name = request.form['name']
        return redirect(url_for("results"))
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
    data = csv_parse(name=name)
    return render_template('results.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)