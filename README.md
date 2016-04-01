# API Gateway + Lambda ping demo

Simple demo that shows how to map inputs from (in this case) a POST and map them to inputs for the Lambda function that will do something with that data. In this case, the "do something" is just returning the data as JSON. The mapping template will handle input from:
- path parameters (in the API's URI)
- JSON payload
- headers

When creating your API in API Gateway, create a resource with the path {path_parameter}, as this will be passed using the mapping, when POSTing to the API endpoint. Define the mapping template in the integration request (under body mapping templates) as 'application/json'.

Note that the API must be deployed before it functions.

Test your API using the following:

```curl -H "Content-Type: application/json" -X POST -d '{"foo":"test_string","bar":12345}' https://your.api.gateway.endpoint/API_STAGE_NAME/HELLO_WORLD```
