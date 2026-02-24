# Foodie App (Ordering & Billing System)
Implemented as per the Requirement Mapping document for the Final Project.

## Project Overview
The Foodie App is an integrated REST API that manages the full lifecycle of a food delivery business. It combines **Restaurant Management** with a complete **Ordering & Billing System**, ensuring that only admin-approved restaurants can serve customers.

## Core Features & Modules
- **Restaurant Onboarding**: Handles registration of new restaurant partners.
- **Admin Control**: A verification module for approving or rejecting restaurants.
- **Dish Management**: Allows restaurants to manage their menus and pricing.
- **User Management**: Dedicated system for customer account registration.
- **Ordering & Billing**: Processes customer orders, calculates totals, and maintains billing history.

## Automation & Testing Frameworks
To ensure the reliability of the billing logic, this project includes:
1. **Pytest**: Unit testing for all 5 modules and API endpoints.
2. **Robot Framework**: Keyword-driven automated acceptance testing.
3. **Postman Collection**: Fully documented requests with saved success examples for all 18 requirements.

## How to Run
1. **Navigate to Project Directory**:
   ```bash
   cd "Project 01"