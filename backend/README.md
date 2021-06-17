# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application.

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle GET requests for all available categories.
4. Create an endpoint to DELETE question using a question ID.
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score.
6. Create a POST endpoint to get questions based on category.
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422 and 500.

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code.

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs.
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

## Documentation
```
Trivia Quiz API Project
	The users are able to
		1. Play quizzes.
		2. Add or delete questions but only one at a time.
		3. View all the questions and their answers.
		4. Search questions.

Getting Started
	Prerequisites & Installation
		Developers using this project should already have Python3, pip and node installed on their local machines.

	Backend
		The requirements.txt file in backend/ folder contains all the packages required by this project. To install those packages run 'pip install requirements.txt' from the backend/ folder.

		To get the application running run the following commands:
			For bash:
				export FLASK_APP=flaskr
				export FLASK_ENV=development
				flask run

			For command prompt:
				set FLASK_APP=flaskr
				set FLASK_ENV=development
				flask run

		These commands put the application in development and directs the application to use the __init__.py file in flaskr/ folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made.

		The application runs on http://127.0.0.1:5000/ by default.

	Frontend
		From the frontend/ folder run the following commands
			-to install the dependencies:
				npm install
			-to start the client:
				npm start

		By default, the frontend will run on localhost:3000

	Tests
		To run the tests navigate to the backend/ folder and run the following commands:
			dropdb trivia_test
			createdb trivia_test
			psql trivia_test < trivia.psql
			python test_flaskr.py

API Reference
	Endpoints
		GET '/categories'
			- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
			- Request Arguments: None
			- Returns: An object with a two keys, success and categories, success conatins a boolean value indicating whether the request was success or not and categories contains a object of id: category_string key:value pairs.
			Request: curl http://127.0.0.1:5000/categories
			Response:{'1' : "Science",
								'2' : "Art",
								'3' : "Geography",
								'4' : "History",
								'5' : "Entertainment",
								'6' : "Sports"
							}

		GET '/questions'
			- Fetches a list of all questions in a set of 10
			- Request Arguments: page (Optional)
			- Returns: An object with a four keys, success, questions, total_questions and  categories.
				'success'- contains a boolean value indicating whether the request was success or not.
				'questions'- contains a list of dictionaries. Each dictionary a object of key:value pairs for keys 'id', 'question', 'answer', 'difficulty' and 'category'.
				'total_questions'- contains a integer value for total number of questions.
				'categories'- contains a object of id: category_string key:value pairs.

				Request: curl http://127.0.0.1:5000/questions?page=2
				Response:	{
									  "categories": {
									    "1": "Science",
									    "2": "Art",
									    "3": "Geography",
									    "4": "History",
									    "5": "Entertainment",
									    "6": "Sports"
									  },
									  "questions": [
									    {
									      "answer": "Agra",
									      "category": 3,
									      "difficulty": 2,
									      "id": 15,
									      "question": "The Taj Mahal is located in which Indian city?"
									    },
									    {
									      "answer": "Escher",
									      "category": 2,
									      "difficulty": 1,
									      "id": 16,
									      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
									    },
									    {
									      "answer": "Mona Lisa",
									      "category": 2,
									      "difficulty": 3,
									      "id": 17,
									      "question": "La Giaconda is better known as what?"
									    },
									    {
									      "answer": "One",
									      "category": 2,
									      "difficulty": 4,
									      "id": 18,
									      "question": "How many paintings did Van Gogh sell in his lifetime?"
									    },
									    {
									      "answer": "Jackson Pollock",
									      "category": 2,
									      "difficulty": 2,
									      "id": 19,
									      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
									    },
									    {
									      "answer": "The Liver",
									      "category": 1,
									      "difficulty": 4,
									      "id": 20,
									      "question": "What is the heaviest organ in the human body?"
									    },
									    {
									      "answer": "Alexander Fleming",
									      "category": 1,
									      "difficulty": 3,
									      "id": 21,
									      "question": "Who discovered penicillin?"
									    },
									    {
									      "answer": "Blood",
									      "category": 1,
									      "difficulty": 4,
									      "id": 22,
									      "question": "Hematology is a branch of medicine involving the study of what?"
									    },
									    {
									      "answer": "Scarab",
									      "category": 4,
									      "difficulty": 4,
									      "id": 23,
									      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
									    },
									    {
									      "answer": null,
									      "category": null,
									      "difficulty": null,
									      "id": 24,
									      "question": null
									    }
									  ],
									  "success": true,
									  "total_questions": 32
									}

		DELETE 'questions/<question_id>'
			- Delete a question with the id passed as the request argument
			- Request Arguments: question_id
			- Returns: An object with a three keys, success, deleted, total_questions.
				'success'- contains a boolean value indicating whether the request was success or not.
				'deleted'- contains a integer value for the id of the question which was deleted
				'total_questions'- contains a integer value for total number of questions after deleting the question.

				Request: curl -X DELETE http://127.0.0.1:5000/questions/31
				Response:{
				  "deleted": 31,
				  "success": true,
				  "total_questions": 31
				}

		POST '/questions'
			- Creates a question
			- Request Arguments: question_text, answer_text, category_id, difficulty
			- Returns: An object with a three keys, success, created, total_questions.
				'success'- contains a boolean value indicating whether the request was success or not.
				'created'- contains a integer value for the id of the question which was created
				'total_questions'- contains a integer value for total number of questions after creating the question.

				Request:
				Response: 

		POST '/questions/search'
			- Searches and returns a list of questions dictionaries which contains the passed string as a substring.
			- Request Arguments:  searchTerm
			- Returns: An object with a four keys, success, questions, total_questions.
				'success'- contains a boolean value indicating whether the request was success or not.
				'questions'- contains a list of dictionaries. Each dictionary a object of key:value pairs for keys 'id', 'question', 'answer', 'difficulty' and 'category'.
				'total_questions'- contains a integer value for total number of questions after creating the question.

		GET '/categories/<category>/questions'
			- Fetches a list of all questions in a set of 10 belonging to a particular category
			- Request Arguments: category_id
			- Returns: An object with a four keys, success, questions, total_questions and  current_category.
				'success'- contains a boolean value indicating whether the request was success or not.
				'questions'- contains a list of dictionaries. Each dictionary a object of key:value pairs for keys 'id', 'question', 'answer', 'difficulty' and 'category'.
				'current_category'- category passed as the request argument.
				'total_questions'- contains a integer value for total number of questions after creating the question.

				Request: curl http://127.0.0.1:5000/categories/4/questions
				Response: {
									  "current_category": "4",
									  "questions": [
									    {
									      "answer": "Maya Angelou",
									      "category": 4,
									      "difficulty": 2,
									      "id": 5,
									      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
									    },
									    {
									      "answer": "Muhammad Ali",
									      "category": 4,
									      "difficulty": 1,
									      "id": 9,
									      "question": "What boxer's original name is Cassius Clay?"
									    },
									    {
									      "answer": "George Washington Carver",
									      "category": 4,
									      "difficulty": 2,
									      "id": 12,
									      "question": "Who invented Peanut Butter?"
									    },
									    {
									      "answer": "Scarab",
									      "category": 4,
									      "difficulty": 4,
									      "id": 23,
									      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
									    }
									  ],
									  "success": true,
									  "total_questions": 4
									}

		POST '/quizzes'
			- To play the quiz.
			- Request Arguments: quiz_category
			- Returns: An object with a four keys, success, questions, current_category, total_questions.
				'success'- contains a boolean value indicating whether the request was success or not.
				'question'- contains a dictionary a question object of key:value pairs for keys 'id', 'question', 'answer', 'difficulty' and 'category'.
				'current_category'- category passed as the request argument.
				'total_questions'- contains a integer value for total number of questions after creating the question.
```
