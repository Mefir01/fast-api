curl -X POST "http://127.0.0.1:8080/coffees" -H "Content-Type: application/json" -d '{
  "id": 1,
  "name": "Espresso",
  "description": "Strong and black coffee",
  "price": 5.99
}'

curl -X GET "http://127.0.0.1:8080/coffees" -H "Accept: application/json"

curl -X GET "http://127.0.0.1:8080/coffees/1" -H "Accept: application/json"

curl -X PUT "http://127.0.0.1:8080/coffees/1" -H "Content-Type: application/json" -d '{
  "id": 1,
  "name": "Double Espresso",
  "description": "Stronger coffee",
  "price": 6.99
}'

curl -X DELETE "http://127.0.0.1:8080/coffees/1"
