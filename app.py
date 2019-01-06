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
    board = Board(queen_extended_circle_state())

    #todo dodać do testów zrobić get_jump_move do końca
    board.enemy_side = PawnColor('BLACK')
    gens = board.resolve_for_queen(board.white_pawns[0])

    z = board.get_state()
    for i in range(len(gens)):
        print('assert moves[{i}].position_after_move == {p}\n assert moves[{i}].beated_pawns == {b}'.format(p=gens[i].position_after_move, b=gens[i].beated_pawns, i=i))

    session['board_state'] = z.to_json()

    return render_template('games/hot_seat.jinja2')

@app.route('/move', methods=['POST'])
def move():
    return session['board_state']

if __name__ == '__main__':
    app.run()
