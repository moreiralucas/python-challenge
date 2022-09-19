# Python Challenge

This is a python challenge proposed in [this link](https://github.com/Luizfanunes/desafio-python).

## Usage

Before start this project, you need create an file with environment variables. Make a copy of ```.env.example``` with the following command:
```sh
cp .env.example .env
```

After create a file with environments, then run the following command to start the Django and postgres containers.
```sh
docker-compose up -d
```

The Django will be available in ```http://localhost:8000/```.

Before handle any request, lets populate the database with a custom command. Run this command in your terminal:

```docker exec -it web_challenge python manage.py insert_users```. This will get data from  https://jsonplaceholder.typicode.com/users website and insert in database.


Now, the database has data and the endpoints can response with something.

The available endpoints are:
```
POST /auth/
GET /users/websites/
GET /users/detail/
GET /users/
```

In the next section are described all endpoints parameters.


## Endpoints

1. The first endpoint is the ```/auth/```. This endpoint is required to get the token to access the remained endpoints.

```sh
curl --request POST \
  --url http://localhost:8000/auth/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "demouser",
	"password": "demo1234"
}'
```

2. This endpoint list all users' websites.
```sh
curl --request GET \
  --url http://localhost:8000/users/websites/ \
  --header 'Authorization: Token 2096ee233408e56fa817f610122c25402197744e'
```

3. This endpoint lists all users (name and email) and the company they work for (in alphabetical order).

```sh
curl --request GET \
  --url http://localhost:8000/users/detail/ \
  --header 'Authorization: Token 2096ee233408e56fa817f610122c25402197744e'
```

4. This endpoint list show all users that contain specific text in the name.
```sh
curl --request GET \
  --url 'http://localhost:8000/users/?name=Leanne' \
  --header 'Authorization: Token 2096ee233408e56fa817f610122c25402197744e'
```

## Tests

To run all tests, execute the following command:
```docker exec -it web_challenge python manage.py test```.
