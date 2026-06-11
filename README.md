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

---

## Phase 3 Progress

Implemented in Phase 3:

- JWT Authentication
- User Registration and Login
- Password Hashing with bcrypt
- Protected Routes using JWT tokens
- Role-Based Access Control (Admin, Doctor, Patient)
- Pydantic Input Validation
- API Rate Limiting with SlowAPI

## Live Deployment

Public API URL:

https://clinic-appointment-booking-api-cabo.onrender.com

Swagger Documentation:

https://clinic-appointment-booking-api-cabo.onrender.com/docs

## Frontend Demo

A simple frontend interface has been deployed to demonstrate the main API features, including:

* User Registration
* User Login
* Doctor Management
* Appointment Type Management
* Appointment Booking
* Available Slot Viewing
* Patient Record Management

Frontend URL:

https://clinic-appointment-booking-api-cabo.onrender.com/frontend/

---

## Repository

GitHub Repository:

https://github.com/ahmettsnl/clinic-appointment-booking-api

---

## API Documentation

Swagger UI:

https://clinic-appointment-booking-api-cabo.onrender.com/docs

---

## Deployment

Application successfully deployed on Render with:

* Docker Containerization
* Docker Compose Configuration
* GitHub Actions Continuous Integration
* PostgreSQL Database
* MongoDB Database
* Public Production URL
