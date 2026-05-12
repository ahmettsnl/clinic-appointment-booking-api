# Clinic Appointment Booking API

Backend API project for a clinic appointment booking system developed for SFWE477 — Backend Development & DevOps Fundamentals.

## Project Overview

This project is a backend system for managing:

- Doctor profiles
- Patient accounts
- Appointment booking
- Smart slot availability calculation
- Medical visit records

The frontend will be generated using AI tools. The main focus of this project is backend architecture, API development, database design, authentication, and deployment.

---

## Technologies

- FastAPI
- PostgreSQL
- MongoDB
- Docker
- JWT Authentication
- GitHub Actions
- Render Deployment

---

## Core Features

- Doctor working hours management
- Dynamic appointment slot calculation
- Appointment lifecycle management
- Patient medical records
- Role-based authentication
- RESTful API design

---

## Unique Feature

Smart Slot Availability Engine with appointment duration and buffer time support.

The system dynamically calculates available booking slots based on:

- Doctor working hours
- Existing appointments
- Appointment duration
- Buffer time between appointments

---

## Project Phases

### Phase 1 — Design
- ERD
- API Contract
- Technical decisions document

### Phase 2 — Build
- FastAPI endpoints
- PostgreSQL & MongoDB integration

### Phase 3 — Secure
- JWT Authentication
- Role-based access control
- Validation and rate limiting

### Phase 4 — Deploy
- Docker Compose
- GitHub Actions CI
- Render deployment