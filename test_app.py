from unittest import TestCase
from app import app
from flask import session, json
from boggle import Boggle


class FlaskTestCase(TestCase):
    #-- write tests for every view function / feature! #
    
    def test_board_form(self):
        with app.test_client() as client:
            response = client.get('/')
            boardhtml = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('<h1 class="text-center">Boggle Board Game</h1>', boardhtml)

    def test_word_form(self):
        with app.test_client() as client:
            with client.session_transaction() as session:
                session['board'] = [['a','b','c','d','e'],
                                    ['e','f','g','h','i'],
                                    ['a','b','c','d','e'],
                                    ['e','f','g','h','i'],
                                    ['l','k','a','m','n']]
            # htmlBoardResponse = client.get('/')
            response = client.post('/find-word?word=elf')
            # boardhtml = response.get_data(as_text=True)
            self.assertEqual(response.json['result'], 'ok')
            

