from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def name():
    return """<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Марс</title>
                    <link rel="shortcut icon" href="static/head.png" type="image/x-icon">
                  </head>
                  <body>
                    <h1>Миссия Колонизация Марса</h1>
                  </body>
                </html>"""


@app.route('/promotion')
def promotion():
    return """Человечество вырастает из детства.<br/>
Человечеству мала одна планета.<br/>
Мы сделаем обитаемыми безжизненные пока планеты.<br/>
И начнем с Марса!<br/>
Присоединяйся!"""


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                    <link rel="shortcut icon" href="static/head.png" type="image/x-icon">
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="static/img_planet.png">
                    <p>Вот она какая, красная планета</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
                    <title>Колонизация</title>
                    <link rel="shortcut icon" href="static/head.png" type="image/x-icon">
                    <link rel="stylesheet" type="text/css" href="static/style/promotion_image.css">
                  </head>
                  <body>
                    <h1 >Жди нас, Марс!</h1>
                    <img src="static/img_planet.png">
                    <p class="text-light bg-dark">Человечество вырастает из детства.</p>
                    <p class="bg-warning">Человечеству мала одна планета.</p>
                    <p class="text-light bg-dark">Мы сделаем обитаемыми безжизненные пока планеты.</p>
                    <p class="bg-success">И начнем с Марса!</p>
                    <p class="bg-secondary">Присоединяйся!</p>

                  </body>
                </html>"""


@app.route('/choice/<planet_name>')
def choice(planet_name):
    d = {'Марс': ['Близок к Земле', 'Много ресурсов', 'Яндекс сказал, что на нем есть вода', 'Красивый'],
         'Юпитер': ['Увесистый', 'Раньше владел наибольшим количеством спутников в Солнечной системе', 'Защищиает Землю от метеоритов', 'Машины на нем имеют хорошую управляемость'],
         'Меркурий': ['Самый маленькая', 'Приезжайте сюда, если ты теплолюбивый человек', 'Можно поставить рекорд по прыжкам в высоту', 'Быстро вращается вокруг Солнца'],
         'Земля': ['Комфортная для жизни', 'Происходит много политических событий', 'Сможешь сделать вдох', 'К сожалению, здесь заставляют работать']}
    d = d.get(planet_name, ['Наш телескоп ещё не исследовал эту планету' for _ in range(4)])
    return f"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
                    <title>Варианты выбора</title>
                    <link rel="shortcut icon" href="static/head.png" type="image/x-icon">
                  </head>
                  <body>
                    <h1 align="center">Моё предложение: {planet_name}</h1>
                    <p class="text-light bg-dark">{d[0]}</p>
                    <p class="bg-warning">{d[1]}</p>
                    <p class="bg-success">{d[2]}</p>
                    <p class="bg-secondary">{d[3]}</p>
                  </body>
                </html>"""


@app.route('/results/<nickname>/<level>/<rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
                    <title>Варианты выбора</title>
                    <link rel="shortcut icon" href="static/head.png" type="image/x-icon">
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии: {nickname}</h2>
                    <p class="bg-success">Поздравляем! Ваш рейтинг после {level} этапа отбора</p>
                    <p>составляет {rating} балла!</p>
                    <p class="bg-warning">Желаем удачи!</p>
                    
                  </body>
                </html>"""


@app.route('/carousel')
def carousel():
    return """
    <!doctype html>
<html lang="ru">
  <head>
    <!-- Обязательные метатеги -->
    <meta charset="utf-8">
    <link rel="stylesheet" href="style.css">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
    <title>Марс</title>
    <link rel="shortcut icon" href="static/head.png" type="image/x-icon">
  </head>
    <body>
        <h1 align="center"> Картинки Марса </h1>
        <div id="carouselExampleCaptions" class="carousel slide" data-ride="carousel">
            <ol class="carousel-indicators">
            <li data-target="#carouselExampleCaptions" data-slide-to="0" class="active"></li>
            <li data-target="#carouselExampleCaptions" data-slide-to="1"></li>
            <li data-target="#carouselExampleCaptions" data-slide-to="2"></li>
            </ol>
            <div class="carousel-inner">
            <div class="carousel-item active">
                <img src="static/img.png" class="d-block w-100" alt="здесь должна быть картинка">
            </div>
            <div class="carousel-item">
                <img src="static/img_1.png" class="d-block w-100" alt="здесь должна быть картинка">
            </div>
            <div class="carousel-item">
                <img src="static/img_2.png" class="d-block w-100" alt="здесь должна быть картинка">
            </div>
            </div>
            <a class="carousel-control-prev" href="#carouselExampleCaptions" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden"></span>
            </a>
            <a class="carousel-control-next" href="#carouselExampleCaptions" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden"></span>
            </a>
        </div>
    </body>
</html>
"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')