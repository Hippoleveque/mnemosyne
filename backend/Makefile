clean:
	rm -rf backend/cards/__pycache__
	rm -rf backend/decks/__pycache__
	rm -rf backend/users/__pycache__
	rm -rf backend/users/migrations
	rm -rf backend/cards/migrations
	rm -rf backend/decks/migrations
	rm db.sqlite3

makemigrations:
	python manage.py makemigrations users
	python manage.py makemigrations decks
	python manage.py makemigrations cards
	python manage.py makemigrations


migrate: makemigrations
	python manage.py migrate users
	python manage.py migrate decks
	python manage.py migrate cards
	python manage.py migrate

init:migrate
	python init_db.py

run:
	python manage.py runserver