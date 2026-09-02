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



## CI/CD Pipeline & Cloud Deployment

### Continuous Integration

GitHub Actions was used to automate the CI pipeline.

The pipeline runs automatically whenever code is pushed to the `main` branch.

The workflow performs the following checks:

1. Checks out the project code.
2. Sets up Python 3.12.
3. Installs the application dependencies.
4. Runs a Python syntax/quality check using `py_compile`.
5. Builds the Docker image.

### Continuous Deployment

The application was deployed to Render using the existing Dockerfile.

Render is connected to the GitHub repository and deploys the application from the `main` branch.

### Live Application

Live URL:

https://buildlabs-task1.onrender.com/

### Application Endpoints

- `/` - Application information
- `/health` - Application health check
- `/tasks` - List of available tasks

### Environment Configuration

The following environment variable was configured on Render:

| Variable | Value |
|----------|-------|
| APP_ENV | production |

The application also supports the `PORT` environment variable.

### CI/CD Workflow

The CI/CD workflow is located at:

`.github/workflows/ci-cd.yml`

The workflow is triggered automatically when code is pushed to the `main` branch.

### Deployment Process

1. Developed and containerized the Flask application.
2. Created a GitHub Actions workflow.
3. Pushed the workflow to GitHub.
4. GitHub Actions automatically tested the application and built the Docker image.
5. Connected the GitHub repository to Render.
6. Deployed the Dockerized application to Render.
7. Configured the production environment variable.
8. Tested the live application endpoints.

### Reflection

#### Deployment Process

The application was deployed using Docker and Render. GitHub Actions was configured to automatically perform quality checks and build the Docker image whenever changes were pushed to the main branch. Render was then used to host the application in the cloud.

#### Benefits of CI/CD

CI/CD improves software delivery by automating repetitive tasks, detecting errors early, reducing manual deployment work, and making it easier to release updates consistently.

#### Challenges Encountered

One challenge was configuring the application to work correctly in a cloud environment. Understanding environment variables and ensuring that the Flask application listens on the correct host and port were important parts of the deployment process.Make sure Docker Desktop is installed and running.



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



