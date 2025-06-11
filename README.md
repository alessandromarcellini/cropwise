# Cropwise
A decision-support web application for farmers, powered by real-time environmental sensor data. Cropwise helps farmers make data-driven decisions by monitoring environmental conditions and providing actionable insights.

## Features
- Real-time environmental monitoring
- Data visualization and analytics
- Smart farming recommendations
- User-friendly dashboard

## Tech Stack
- Frontend: React
- Backend: Fastapi
- Database: Posgre, Firebase
- Containerization: Docker

## Prerequisites
- Docker Desktop
- Git

## Installation & Setup

1. Clone the repository
```bash
git clone https://github.com/alessandromarcellini/cropwise.git
cd cropwise
```

2. Start the application

Making sure you've already started docker desktop:
```bash
# Start all services
docker compose up

# Or start specific services
docker compose up <container_name>
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Backend IoT: http://localhost:9000

## Development

To run the services individually in development mode, refer to the documentation in each service's directory.