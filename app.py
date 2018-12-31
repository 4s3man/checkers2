from flask import Flask, render_template, request, session, url_for, redirect
from service.checkers_service import ChecersService


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
    board = Board(extended_circle_state())
    z = board.get_state()

    b1 = Board(extended_circle_state())
    b1.enemy_side = PawnColor('BLACK')
    moevs = b1.get_jump_moves(b1.white_pawns[0])

    session['board_state'] = z.to_json()

    return render_template('games/hot_seat.jinja2')

@app.route('/move', methods=['POST'])
def move():
    return session['board_state']

if __name__ == '__main__':
    app.run()
