from flask import Flask, render_template, session, request, jsonify
from boggle import Boggle


app = Flask(__name__)
app.config['SECRET_KEY'] = "flask boggle testing"

boggle_game = Boggle()

@app.route('/')
def make_board():
    # session['count'] = session.get('count',0) + 1
    board=boggle_game.make_board()
    session['board'] = board 
    return render_template('board.html',board=board)

@app.route('/find-word',methods=['POST'])
def find_word():
    board = session['board']
    word = request.json['input']
    response = boggle_game.check_valid_word(board,word) 
    return jsonify({'result':response})
    # return redirect('/')

@app.route('/send-score',methods=['POST'])
def send_score():
    bestscore = request.json['bestscore']
    session['bestscore'] = bestscore
    
    count= request.json['count']
    session['count'] = count
    return jsonify({'bestscore':bestscore,'count':count})

