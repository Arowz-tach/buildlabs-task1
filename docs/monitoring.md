# Monitoring Documentation

## Monitoring Tools

### GitHub Actions
A scheduled health-check workflow runs every 15 minutes and can also be triggered manually.

It checks:
- Application availability
- HTTP status
- Response time

### Render Monitoring
Render is configured with an HTTP health check using:

`/health`

Render also provides resource monitoring for:
- CPU
- Memory
- Network bandwidth

## Monitoring Results

The application health endpoint consistently returned HTTP 200 during testing.

Manual monitoring recorded response times ranging from approximately 747 ms to 12.1 seconds. The variation is consistent with cloud instance wake-up and network conditions on the free hosting environment.

## Automation

The application uses automated health monitoring and automated cloud deployment after successful CI checks.
