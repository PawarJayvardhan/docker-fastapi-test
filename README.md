


#After cloning the repository use following commands  

cd docker-fastapi-test

docker-compose build 

docker-compose up


#for adding data

curl -X POST "http://localhost/users" -H "Content-Type: application/json" -d '{
  "id": 1,
  "name": "test",
  "email": "docker.test.fastapi@example.com"
}'

