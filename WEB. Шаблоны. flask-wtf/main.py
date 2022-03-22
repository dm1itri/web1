from flask import Flask, render_template, request
from answerform import AnswerForm


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
    if request.method == 'GET':
        return render_template('galery.html')
    elif request.method == 'POST':

        with open('static/image/load_image3.png', 'wb') as f:
            with open('static/image/load_image2.png', 'rb') as f1:
                f.write(f1.read())
        with open('static/image/load_image2.png', 'wb') as f:
            with open('static/image/load_image1.png', 'rb') as f1:
                f.write(f1.read())
        with open('static/image/load_image1.png', 'wb') as f:
            f.write(request.files['file'].read())
        return render_template('galery.html')


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



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')