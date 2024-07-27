Assumptions and Design Considerations for the KV Store
`1. Application is a HTTP API based key value store written using python FASTAPI framework to speed up the development process and also automatically generate the API Documentation at /doc and /redoc paths`

`2. Data is stored using the Dictonary data structure in python.`

`3. This is a simple application to demonstrate the Key Value functionality and does not include any form of encryption, security and authentication to any of the endpoints`.

`4. Performance and concurrency might be an issue as that is not taken into consideration during the development and concurrent requests may lead to race conditions.`

`5. Detailed documentation is available at /doc and /redoc url paths`

`6. Advanced Error handling is not considered in this implementation process like errors leading to 5xx server side errors`


Run application by deploying kubernetes manifests:
`Docker Desktop must be installed if not available`

`Docker image must be built and should be available in the local registry`

`Ensure Nginx Ingress Controller is available on local machine`

`Change directory to kubernetes-manifests`

`Run : kubectl apply -f .`

View the application on the following URLs:
`1. localhost`

`2. localhost/docs`

`3. localhost/redoc`

Sometimes the Ingress resource might cause an issue in local it might take sometime to be available, so the same can be viewed via the service using below urls:

`1. localhost:31212`

`2. localhost:31212/docs`

`3. localhost:31212/redoc`