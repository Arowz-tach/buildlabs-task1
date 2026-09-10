# Architecture Diagram

```mermaid
flowchart LR
    U[Users] --> R[Render Cloud]
    R --> D[Docker Container]
    D --> A[Flask Application]
    A --> H[/health Endpoint]

    DEV[Developer] --> G[GitHub Repository]
    G --> CI[GitHub Actions CI]
    CI -->|CI Checks Pass| R

    CI --> M[Scheduled Health Monitoring]
    M --> H

### Step 2 — Create the incident response guide

```bash
cat > docs/incident-response.md <<'EOF'
# Incident Response Guide

## 1. Application is Down

### Possible Causes
- Failed deployment
- Application crash
- Incorrect configuration
- Container startup failure

### Resolution
1. Check Render deployment status.
2. Check Render logs for errors.
3. Verify the application starts correctly.
4. Check the `/health` endpoint.
5. Redeploy the latest working commit if necessary.

## 2. CI/CD Pipeline Fails

### Possible Causes
- Python syntax error
- Missing dependency
- Docker build failure
- Incorrect GitHub Actions configuration

### Resolution
1. Open GitHub Actions.
2. Identify the failed step.
3. Check the error message.
4. Fix the issue locally.
5. Commit and push the correction.
6. Confirm the pipeline passes.

## 3. Slow Application Response

### Possible Causes
- Cloud instance inactivity
- Network latency
- Resource limitations

### Resolution
1. Check Render metrics.
2. Check application logs.
3. Test the `/health` endpoint.
4. Compare response times across multiple requests.
5. Upgrade resources if sustained high usage occurs.

## 4. Failed Health Check

### Resolution
1. Verify `/health` returns HTTP 200.
2. Check Render logs.
3. Confirm the application is listening on the correct port.
4. Verify the health-check path is `/health`.
5. Restart or redeploy the service if required.
