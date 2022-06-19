All docker containers can be started using `start.sh` script. Docker and
docker-compose are required to run the demo. Moreover, for
debugging purposes, they will expose their services on the localhost on the
following ports:

- postgres database: 5433
- main API: 8001
- calculation API: 8002

Open API specification for both calculation and main API are available on
`api/docs` endpoints of respective services.
