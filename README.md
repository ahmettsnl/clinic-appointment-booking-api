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

---

## Phase 2 Progress

Implemented in Phase 2:

- FastAPI backend application
- PostgreSQL connection using Docker
- MongoDB Atlas connection
- Doctor endpoints
- Appointment type endpoints
- Appointment endpoints
- Patient record endpoints using MongoDB
- Smart slot availability endpoint
- Appointment conflict prevention
- Appointment status lifecycle update
- AI-generated frontend prototype using Lovable