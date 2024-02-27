from flask import Flask, render_template

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pessoas')
def html():
    return render_template('pessoas.html')

@app.route('/profissoes')
def profs():
    return render_template('profissoes.html')



if __name__ == '__main__':
    app.run()
