import requests
import json

url = "http://localhost:5000/api/request"

payload = "{\n    \"jsonrpc\": \"2.0\",\n    \"method\": \"createProject\",\n    \"id\": 123,\n    \"params\": {\n        \"payload\": {\n            \"template\": {\n                \"name\": \"create_project\"\n            },\n            \"data\": {\n  \"title\":\"Water project\",\n  \"ownerName\":\"Don\",\n  \"ownerEmail\":\"don@gmail.com\",\n  \"shortDescription\":\"Project for water\",\n  \"longDescription\":\"project to save water for areas with drought\",\n  \"impactAction\":\"litres of water saved\",\n  \"projectLocation\":\"ZA\",\n  \"sdgs\":[\"12.2\",\"3\",\"2.4\"],\n  \"requiredClaims\":30,\n  \"templates\":{\n    \"claim\":{\n      \"schema\":\"\",\n      \"form\": \"\"\n    }\n  },\n  \"evaluatorPayPerClaim\":\"0\",\n  \"socialMedia\":{\n    \"facebookLink\":\"https://www.facebook.com/ixofoundation/\",\n    \"instagramLink\":\"\",\n    \"twitterLink\":\"\",\n    \"webLink\":\"https://ixo.foundation\"\n  },\n  \"imageLink\":\"\",\n  \"founder\":{\n    \"name\":\"Nicd\",\n    \"email\":\"nic@test.co.za\",\n    \"countryOfOrigin\":\"ZA\",\n    \"shortDescription\":\"primary description for founder\",\n    \"websiteURL\":\"www.water.com\",\n    \"logoLink\":\"\"\n  }\n}\n        },\n         \"signature\": {\n            \"type\": \"ed25519-sha-256\",\n            \"created\": \"2018-06-05T12:35:02Z\", \n            \"creator\": \"did:sov:E1GuPmqF5FjoWJzEPDq181\", \n            \"signatureValue\": \"2579229E2996843EFC2569077F376E95038354BCF890DB9D1010A1380C3F491A7B71F87C05050F94DCDB0FFD855DEE902FE84D5C1D56B3CF75B36797948E560D\"\n        }\n    }\n}"

datastore = json.dumps({
    "jsonrpc": "2.0",
    "method": "createProject",
    "id": 123,
    "params": {
        "payload": {
            "template": {
                "name": "create_project"
            },
            "data": {
  "title":"Water project",
  "ownerName":"Don",
  "ownerEmail":"don@gmail.com",
  "shortDescription":"Project for water",
  "longDescription":"project to save water for areas with drought",
  "impactAction":"litres of water saved",
  "projectLocation":"ZA",
  "sdgs":["12.2","3","2.4"],
  "requiredClaims":30,
  "templates":{
    "claim":{
      "schema":"",
      "form": ""
    }
  },
  "evaluatorPayPerClaim":"0",
  "socialMedia":{
    "facebookLink":"https://www.facebook.com/ixofoundation/",
    "instagramLink":"",
    "twitterLink":"",
    "webLink":"https://ixo.foundation"
  },
  "imageLink":"",
  "founder":{
    "name":"Nic",
    "email":"nic@test.co.za",
    "countryOfOrigin":"ZA",
    "shortDescription":"primary description for founder",
    "websiteURL":"www.water.com",
    "logoLink":""
  }
}
        },
         "signature": {
            "type": "ed25519-sha-256",
            "created": "2018-06-05T12:35:02Z",
            "creator": "did:sov:E1GuPmqF5FjoWJzEPDq181",
            "signatureValue": "2579229E2996843EFC2569077F376E95038354BCF890DB9D1010A1380C3F491A7B71F87C05050F94DCDB0FFD855DEE902FE84D5C1D56B3CF75B36797948E560D"
        }
    }
})

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "71f6d419-a0e9-c76a-3ae3-4b16d0305cb9"
    }

print(json.dumps(datastore))
response = requests.request("POST", url, data=datastore, headers=headers)

print(response.text)