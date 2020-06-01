build:
	docker-compose build --no-cache

down:
	docker-compose down

clean:
	rm -rf backend/cards/__pycache__
	rm -rf backend/decks/__pycache__
	rm -rf backend/users/__pycache__
	rm -rf backend/users/migrations
	rm -rf backend/cards/migrations
	rm -rf backend/decks/migrations
	rm -rf backend/static/

makemigrations:
	docker-compose run backend python manage.py makemigrations users
	docker-compose run backend python manage.py makemigrations decks
	docker-compose run backend python manage.py makemigrations cards
	docker-compose run backend python manage.py makemigrations
	

migrate: makemigrations
	docker-compose run backend python manage.py migrate users
	docker-compose run backend python manage.py migrate decks
	docker-compose run backend python manage.py migrate cards
	docker-compose run backend python manage.py migrate
	
shell: migrate
	docker-compose run backend python manage.py shell

init:migrate
	docker-compose run backend python init_db.py

up: 
	docker-compose up
