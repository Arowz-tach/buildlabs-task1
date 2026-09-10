# BuildLabs DevOps Portfolio

## Project Overview

BuildLabs DevOps Task Manager is a Flask REST API containerized with Docker and deployed to the cloud.

## GitHub Repository

https://github.com/Arowz-tach/buildlabs-task1

## Docker Configuration

The application uses a Python 3.12 slim Docker image and exposes port 5000. Environment variables are supported through the `PORT` variable.

## CI/CD Pipeline

GitHub Actions automatically:
1. Checks out the code.
2. Sets up Python.
3. Installs dependencies.
4. Performs a Python quality check.
5. Builds the Docker image.

## Cloud Deployment

The Dockerized application is deployed to Render.

Live application:

https://buildlabs-task1.onrender.com/

## Monitoring Setup

- GitHub Actions scheduled health checks
- Render HTTP health checks
- CPU monitoring
- Memory monitoring
- Network monitoring
- Application logs

## Architecture Diagram

See `docs/architecture.md`.

## Incident Response Guide

See `docs/incident-response.md`.

## Lessons Learned

This project provided practical experience with Git, GitHub, Docker, CI/CD, cloud deployment, monitoring, automation, and incident response.

Automation reduces manual work, improves reliability, detects problems earlier, and makes software delivery more consistent.

## Future Improvements

With more time, the project could be improved by adding:
- Automated tests
- Application performance monitoring
- Centralized log management
- Database integration
- Infrastructure as Code
- Production-grade alerting
