from flask import Flask, render_template, request, redirect
from answerform import AnswerForm
from login import LoginForm
from datetime import datetime
from os import listdir

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<ol>')
def list_prof(ol):
    return render_template('list_prof.html', ol=ol)


@app.route('/galery', methods=['GET', 'POST'])
def galery():
    if request.method == 'POST':
        my_file = open(f'static/image/galery/load_image{datetime.now().strftime("%H_%M_%S__%d_%m_%Y")}.png', 'wb+')
        my_file.write(request.files['file'].read())
        my_file.close()
    images = [i for i in listdir('static/image/galery') if i.endswith('.png') and i != 'load_image1.png']
    return render_template('galery.html', images=images)


@app.route('/answer', methods=['GET', 'POST'])
@app.route('/auto_answer', methods=['GET', 'POST'])
def answer():
    form = AnswerForm()

    if form.validate_on_submit():
        auto_answer = request.form.to_dict()
        print(auto_answer)
        del auto_answer['csrf_token']
        del auto_answer['submit']
        auto_answer['ready'] = "ДА" if auto_answer['ready'] == 'y' else 'НЕТ'
        return render_template('auto_answer.html', auto_answer=auto_answer, title=auto_answer['title'])
    return render_template('answer.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(f'/index/{request.form["id"]}')
    return render_template('login.html', form=form)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')