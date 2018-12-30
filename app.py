from flask import Flask, render_template, request, session, url_for, redirect
from checkers.board import *

app = Flask(__name__)
app.secret_key = '$$_asdoi20z1|}2!{_012!!_\z!@669xcz^[%mmaq'

@app.route('/', methods=['GET', 'POST'])
def choose_game():
    return render_template('choose_game.html')

@app.route('/game/hotseat', methods=['POST', 'GET'])
def hot_seat():
    board = Board()
    for pawn in board.black_pawns:
        print(pawn.position)
    return render_template('games/hot_seat.jinja2')

if __name__ == '__main__':
    app.run()
