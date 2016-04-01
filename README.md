# API Gateway + Lambda ping demo

Simple demo that shows how to map inputs from (in this case) a POST and map them to inputs for the Lambda function that will do something with that data. In this case, the "do something" is just returning the data as JSON. The mapping template will handle input from:
- path parameters (in the API's URI)
- JSON payload
- headers
