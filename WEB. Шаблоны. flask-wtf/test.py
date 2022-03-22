from json import dump
d = {
    'Энди': {'surname': 'Уир',
             'image': '/static/image/энди.png',
             'specialties': ('астрогеолог', 'специалист по радиационной защите')},
    'Ридли': {'surname': 'Скотт',
             'image': '/static/image/ридли.png',
             'specialties': ('пилот дронов', 'инженер по терраформированию', 'строитель')},
    'Марк': {'surname': 'Уотни',
             'image': '/static/image/марк.png',
             'specialties': ('врач', 'экзобиолог')},
    'Шон': {'surname': 'Бин',
            'image': '/static/image/шон.png',
            'specialties': ('киберинженер', 'инженер-исследователь')},
    'Бобик': {'surname': 'Томсон',
              'image': '/static/image/бобик.png',
              'specialties': ('психолог', 'инженер-исследователь', 'климатолог')}
}

with open('templates/members.json', 'w') as f:
    dump(d, f)