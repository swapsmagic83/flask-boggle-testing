from flask import Flask, render_template, session, request, jsonify,json
from boggle import Boggle


app = Flask(__name__)
app.config['SECRET_KEY'] = "flask boggle testing"

boggle_game = Boggle()

@app.route('/')
def make_board(): 
    board=boggle_game.make_board()
    session['board'] = board 
    return render_template('board.html',board=board)

@app.route('/find-word')
def find_word():
    board = session['board']
    word = request.args['input']
    response = boggle_game.check_valid_word(board,word)
    return jsonify({'result':response})

@app.route('/send-score',methods=['POST'])
def send_score():
    bestscore = request.json['bestscore']
    session['bestscore'] = bestscore
    count= request.json['count']
    session['count'] = count
    return jsonify({'bestscore':bestscore,'count':count})

