# open-food-data-pipeline

A simple ETL pipeline that ingests an Open Food Data CSV into a Postgres database. Uses Python, Docker, and SQL.

# How to Run:

1. Clone repo and ensure Docker is installed.
    git clone https://github.com/Yusha-88/open-food-data-pipeline.git

2. Run docker compose up.
    docker compose up

3. Find the docker network via docker network ls. One will be created when you run docker compose.

4. Run docker build -t for pipeline.py.
    docker build -t open-food-pipeline:v001 .

5. Execute docker run for container using the below. 
    docker run -it \
    --network="your docker network name here": \
    open-food-pipeline:v001 \
        --pg-user=root \                                                              
        --pg-pass=root \
        --pg-host=pgdatabase \
        --pg-port=5432 \
        --pg-db=open_food \
        --target-table=open_food

6. The ETL pipeline script will now run. 

7. Once that's done, log into pgadmin using details in the docker-compose.yaml file.  

8. Right-click "Servers" → Register → Server

Configure:

    General tab: Name: Local Docker
    Connection tab:
        Host: pgdatabase (the container name)
        Port: 5432
        Username: root
        Password: root

Press Save.

9. Go to Servers -> Local Docker -> Databases -> open_food -> Schemas -> Tables -> open_food. You can see and query all the data ingested and transformed by pipeline.py. 

### Change log:

22/09/26 - Wrote instructions on how to run the ETL script in the README. 

23/08/26 - Created docker-compose file.

22/08/26 - Put pipeline.py in a Docker container and connected it to the PostgreSQL container. General tidy-up up of pipeline.py.

18/08/26 - Added try-except block to the load to database function, allowing majority of the 4.5 millions records to be uploaded. 

15/08/26 - Decided to load 1 million rows of data from original CSV into Postgres.

11/08/26 - Fixed issue where only 100,000 records were uploaded to the database at a time. Using a few select columns from original CSV's 155 columns.

10/08/26 - Setup Postgres DB and extract_csv now can input some data to it.