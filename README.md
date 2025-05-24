# project1.2

## Overview

This project demonstrates a cloud-native architecture using AWS infrastructure, Docker containers, and GitLab CI/CD pipelines. It consists of two backend services and a frontend, all orchestrated via Docker Compose and deployed to AWS.

## Project Structure

```
project1.2/
│
├── backend_rds/         # Backend service with RDS (PostgreSQL) integration
├── backend_redis/       # Backend service with Redis integration
├── frontend/            # Static frontend (HTML/JS)
├── docker-compose.yml   # Multi-service orchestration
├── .gitlab-ci.yml       # CI/CD pipeline configuration
└── README.md
```

## Services

- **backend_rds**: Python-based backend connected to AWS RDS (PostgreSQL).
- **backend_redis**: Python-based backend using Redis for caching or fast data access.
- **frontend**: Static web application (HTML/JS).

## Quick Start (Local)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/orlivskavaleriia/project1.2.git
   cd project1.2
   ```

2. **Set environment variables:**
   Create a `.env` file or export variables required by `docker-compose.yml`:
   ```
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=your_db_host
   REDIS_HOST=your_redis_host
   REDIS_DB=0
   ```

3. **Run all services:**
   ```bash
   docker-compose up --build
   ```

4. **Access services:**
   - `backend_rds`: http://localhost:8000
   - `backend_redis`: http://localhost:8001
   - `frontend`: Open `frontend/index.html` in your browser

## CI/CD & Deployment

- **CI/CD** is managed via `.gitlab-ci.yml`:
  - Builds Docker images for both backends and pushes them to AWS ECR.
  - Deploys backend services to an AWS EC2 instance using Docker Compose.
  - Syncs the frontend to an AWS S3 bucket and invalidates the CloudFront cache.

## AWS Integration

- **ECR**: Stores Docker images for backend services.
- **EC2**: Hosts and runs backend containers.
- **S3**: Hosts static frontend files.
- **CloudFront**: Distributes frontend globally with cache invalidation on deploy.

## Requirements

- Docker & Docker Compose
- AWS account with ECR, EC2, S3, and CloudFront configured
- GitLab (for CI/CD) or manual deployment

## License

MIT License