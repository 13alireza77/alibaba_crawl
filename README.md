# Crawl

you can use it to get the number of repetitions of pattern in the web page and its child links that specify by level
## Install requirements

after clone and create virtual env run:
```bash
pip install -r requirements.txt
```

## Usage
run:
```bash
python app.py
```
## Request Example

```json
{
	"info": {
		"_postman_id": "671b3c46-47a1-4c8b-a379-89a45530b232",
		"name": "alibaba",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
	},
	"item": [
		{
			"name": "http://127.0.0.1:5000/crawl",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "formdata",
					"formdata": [
						{
							"key": "url",
							"value": "https://www.w3schools.com/python",
							"type": "text"
						},
						{
							"key": "pattern",
							"value": "[a-z]{10}",
							"type": "text"
						},
						{
							"key": "level",
							"value": "3",
							"type": "text"
						}
					]
				},
				"url": {
					"raw": "http://127.0.0.1:5000/crawl",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"crawl"
					]
				},
				"description": "takes url,pattern,level in the body and in response gives the number of pattern repetitions in each link\r\nit tokk some.\r\nIt takes time depending on the number of links per page."
			},
			"response": []
		}
	]
}
```