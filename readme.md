### Quickstart

#### Dockerized App + Dockerized Postgres (no Compose)
Run two containers, one for the FastAPI app and one for the Postgres database. We will use a network to allow the containers to communicate with each other.

1. Pull the image from Docker Hub
    ```bash
    docker pull postgres
    ```
1. Create a docker network
This will allow the containers to communicate with each other.
    ```bash
    docker network create demo-network
    ```
1. Start the Postgres container
You can run the `./scripts/run_pg.bat` script which is
    ```bash
    docker run --name demo_pg \ # important to keep this static since it's passed in run command to fastapi app
    --network demo-network \  # this is the network we created in step above
    -e POSTGRES_PASSWORD=demopassword \
    -e POSTGRES_DB=demo_db  \ 
    -p '5432:5432' \ # note double quotes for bat, single for bash
    -d postgres
    ```
1. Verify postgres is running and can create connection
    ```bash
    psql -h localhost -p 5432 -U postgres -d demo_db
    ```
    password: `demopassword`
1. Build the FastAPI image
    ```bash
    docker build -t pavel-gh-2 .
    ```
    Currently `scripts/` is copied in the image (i think) but is not nec.
1. Start the FastAPI container
    ```bash
    docker run -d \
    -p 8000:8000 \
    --network demo-network \
    -e DB_HOST=demo_pg \ # this comes from --name arg in run command for postgres container
    -e DB_PASSWORD=demopassword \
    -e HOST=0.0.0.0 \ # defaults to 127.0.0.1 which is not accessible from outside the container
    pavel-gh-2
    ```
    You should be able to goto `http://localhost:8000/` and get redirected to /docs.
### Notes
- `uvloop` is linux only.
    - could replace with `asyncio` for cross-platform support.