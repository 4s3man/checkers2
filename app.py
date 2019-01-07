from flask import Flask, render_template, request, session, url_for, redirect
from service.checkers_service import *


from checkers.board import *
import json
from checkers.tests.fixtures.state_fixtures import *

app = Flask(__name__)
app.secret_key = '$$_asdoi20z1|}2!{_012!!_\z!@669xcz^[%mmaq'

@app.route('/', methods=['GET', 'POST'])
def choose_game():
    return render_template('choose_game.jinja2')

@app.route('/game/hotseat', methods=['POST', 'GET'])
def hot_seat():
    ChecersService.init_game(session, GameMode('HOT_SEATS'))
    print(session)

    return render_template('games/hot_seat.jinja2')

@app.route('/move', methods=['POST'])
def move():
    response = ChecersService.create_response_from_session(session, GameMode('HOT_SEATS'))
    return response

if __name__ == '__main__':
    app.run()
