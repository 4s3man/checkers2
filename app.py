from flask import Flask, render_template, request, session, url_for, redirect
from service.checkers_service import ChecersService


from checkers.board import *
import json

app = Flask(__name__)
app.secret_key = '$$_asdoi20z1|}2!{_012!!_\z!@669xcz^[%mmaq'

hem = ''

@app.route('/', methods=['GET', 'POST'])
def choose_game():
    return render_template('choose_game.jinja2')

@app.route('/game/hotseat', methods=['POST', 'GET'])
def hot_seat():
    # session.clear()
    # if not 'board_state' in session:
    #     session['board_state'] = json.dumps(state, default=(lambda x: x.__dict__))


    return render_template('games/hot_seat.jinja2')

@app.route('/move', methods=['POST'])
def move():
    board = Board()
    state = board.get_state()
    return json.dumps(state, default=(lambda x: x.__dict__))

if __name__ == '__main__':
    app.run()
