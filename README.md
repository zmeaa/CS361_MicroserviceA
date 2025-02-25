# CS361_MicroserviceA

Given the simplistic nature and scope of this microservice, requesting from the email microservice (MicroserviceA.py) can be done very concisely, and likewise sending data to it (having the microservice receive data, in other words). 

To send data: 
A JSON object must be sent to the microservice so that it can be sent as an email; the microservice will do functionally nothing without an input. To obtain this input, a JSON file must be sent to the HTTP endpoint, http://localhost:5000/send-email, and received by the microservice. The microservice will handle it from there. To send such data, one must POST a JSON object to the endpoint, such that the following psuedocode is relevant: POST(URL, json). 

To request data:
To request data from the microservice, one is requesting the status of the JSON-to-email being sent. This microservice communicates via HTTP, particularly http://localhost:5000/send-email. Therefore, to request data, code must be written to POST data to the microservice, such that the microservice will send the email and return a status JSON object, and then this response must be thusly stored. This is a somewhat laborious way to indicate the following pseduocode: response = POST(URL, json). 
