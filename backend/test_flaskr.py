import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{user}:{password}@{host}/{database}".format(
                                                                user='postgres',
                                                                password='ayush882',
                                                                host='localhost:5432',
                                                                database=self.database_name,
                                                                )
        setup_db(self.app, self.database_path)

        self.new_question = {
            'question':"What is know as the powerhouse of cell?",
            'answer':"MITOCHONDRIA",
            'difficulty':2,
            'category':1,
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_paginated_questions(self):
        response = self.client().get('/questions')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['categories'])

    def test_404_sent_requesting_invalid_page(self):
        response = self.client().get('/questions?page=999')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_question(self):
        response = self.client().delete('/questions/5')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['deleted'])

    def test_422_delete_invalid_question(self):
        response = self.client().delete('/questions/999')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_create_question(self):
        response = self.client().post('/questions', json=self.new_question)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['created'])

    def test_search_questions(self):
        response = self.client().post('/questions/search', json={
                                                        'searchTerm':'What'
                                                        })
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        print(data['questions'])
        self.assertTrue(data['questions'])

    def test_category_questions(self):
        response = self.client().get('/categories/4/questions')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        print(data['questions'])
        self.assertTrue(data['questions'])
        self.assertTrue(data['current_category'])

    def test_play_quizzes(self):
        response = self.client().post('/quizzes', json={
                                                    'quiz_category':'5',
                                                    'previous_questions':[2,4]
        })
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        print(data['question'])
        self.assertTrue(data['question'])
        self.assertTrue(data['current_category'])

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
