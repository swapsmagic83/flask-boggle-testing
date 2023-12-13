from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTestCase(TestCase):
    #-- write tests for every view function / feature! #
    
    def test_board_form(self):
        with app.test_client() as client:
            response = client.get('/')
            boardhtml = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('<h1 class="text-center">Boggle Board Game</h1>', boardhtml)

    def test_correct_word(self):
        with app.test_client() as client:
            with client.session_transaction() as session:
                session['board'] = [['A','B','C','D','E'],
                                    ['E','F','G','H','I'],
                                    ['A','B','C','D','E'],
                                    ['E','F','G','H','I'],
                                    ['L','K','A','M','N']]
        response= client.get('/find-word?input=a')
        self.assertEqual(response.json['result'], 'ok')

    def test_word_not_on_board(self):
        with app.test_client() as client:
            with client.session_transaction() as session:
                session['board'] = [['A','B','C','D','E'],
                                    ['E','F','G','H','I'],
                                    ['A','B','C','D','E'],
                                    ['E','F','G','H','I'],
                                    ['L','K','A','M','N']]
        response= client.get('/find-word?input=z')
        self.assertEqual(response.json['result'], 'not-on-board')

    def test_wrong_word(self):
        with app.test_client() as client:
            with client.session_transaction() as session:
                session['board'] = [['A','B','C','D','E'],
                                    ['E','F','G','H','I'],
                                    ['A','B','C','D','E'],
                                    ['E','F','G','H','I'],
                                    ['L','K','A','M','N']]
        response= client.get('/find-word?input=cg')
        self.assertEqual(response.json['result'], 'not-word')
       

    
            

