# BuildLabs DevOps Task Manager



A simple Flask-based task management API created as part of the BuildLabs DevOps Internship Task 1.



This project demonstrates application development, Git version control, GitHub collaboration, Docker containerization, and environment variable usage.



## Features



* Flask-based REST API

* Health check endpoint

* Task listing endpoint

* JSON responses

* Docker containerization

* Environment variable support



## Technologies Used



* Python

* Flask

* Git

* GitHub

* Docker



## Project Structure



```text

buildlabs-task1/

├── app.py

├── requirements.txt

├── Dockerfile

├── .gitignore

└── README.md

```



## Application Endpoints



### Home



`GET /`



Returns information about the application.



### Health Check



`GET /health`



Returns the health status of the application.



### Tasks



`GET /tasks`



Returns the available tasks.



## Local Setup



### Prerequisites



Make sure Python 3.x and Git are installed.



### Install Dependencies



```bash

pip install -r requirements.txt

```



### Run the Application



```bash

python app.py

```



The application will be available at:



`http://localhost:5000`



## Docker



The application can be built and run inside a Docker container.



### Prerequisites



Make sure Docker Desktop is installed and running.



### Build the Docker Image



```bash

docker build -t buildlabs-task1 .

```



### Run the Docker Container



```bash

docker run -d -p 5000:5000 -e PORT=5000 --name buildlabs-task1-container buildlabs-task1

```



### Verify the Container



```bash

docker ps

```



The expected port mapping is:



`0.0.0.0:5000->5000/tcp`



### Test the Application



Open:



`http://localhost:5000`



Health check:



`http://localhost:5000/health`



Tasks:



`http://localhost:5000/tasks`



### Environment Variables



The application uses the `PORT` environment variable to configure the Flask server port.



Example:



```bash

docker run -d -p 5000:5000 -e PORT=5000 --name buildlabs-task1-container buildlabs-task1

```



If the `PORT` environment variable is not provided, the application uses port `5000` by default.



### View Container Logs



```bash

docker logs buildlabs-task1-container

```



### Stop the Container



```bash

docker stop buildlabs-task1-container

```



### Remove the Container



```bash

docker rm buildlabs-task1-container

```



## Testing



The application was successfully tested inside a Docker container.



The `/` and `/health` endpoints returned HTTP 200 responses.



The Docker container was verified using:



```bash

docker ps

```



The PORT environment variable was verified using:



```bash

docker exec buildlabs-task1-container printenv PORT

```



## Author



Arowolo Riliwan



## Project



BuildLabs DevOps Internship - Task 1



