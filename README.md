# MongoDB

## Instructions

1)Clone this repo 
2)Navigate to the folder 'mongo' then inside it open the file 'docker-compose.yml'
3)Inside 'docker-compose.yml' correctly indicate the username, password, and database name for your own mongoDB database
4)Make sure that your mongoDB database has a collection called 'mongo' inside it
5)Navigate to 'mongoDB' -> 'mongo' inside terminal. Make sure that docker is open. Then run the command: $ docker-compose up --build
6)Done! The server is now running on port 8080 and is able to receive requests.

## Requests examples

1)POST (Creating)

```python
data = {"key": "key2", "value": "value2"}
response = requests.post("http://localhost:8080/create", json=data)
print(response.json())
```

2)PUT (Updating)

```python
data = {"value": "value1_updated"}
response = requests.put("http://localhost:8080/update/key1", json=data)
print(response.json())
```

3)GET (Reading)

```python
response = requests.get("http://localhost:8080/read/key1")
print(response.json())
```

