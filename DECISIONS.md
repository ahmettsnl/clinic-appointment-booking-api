# Technical Decisions

## Why FastAPI?

FastAPI was selected because it is a modern and high-performance Python framework for building RESTful APIs. It provides automatic API documentation, fast development speed, and strong support for asynchronous programming.

---

## Why PostgreSQL?

PostgreSQL is used for structured relational data such as:

- Doctors
- Patients
- Appointments
- Working hours
- Appointment types

These entities have clear relationships and require strong consistency and relational integrity.

---

## Why MongoDB?

MongoDB is used for flexible medical records and visit notes.

Patient records may contain:

- Visit notes
- Prescriptions
- Diagnoses
- Medical history
- Dynamic data structures

MongoDB is more suitable for storing semi-structured and evolving medical information.

---

## Appointment Availability Logic

The availability engine dynamically calculates available booking slots instead of returning hardcoded times.

The algorithm works as follows:

1. Retrieve doctor working hours
2. Retrieve existing appointments for the selected date
3. Retrieve appointment type duration
4. Apply buffer time between appointments
5. Remove conflicting time ranges
6. Return only available slots

This approach simulates real-world clinic scheduling systems.

---

## Authentication Strategy

JWT authentication will be used to secure API endpoints.

The system will support role-based access control for:

- Patients
- Doctors
- Clinic administrators

---

## Deployment Strategy

The application will be containerized using Docker and deployed using Render.

GitHub Actions CI will be used for automated testing and deployment workflows.