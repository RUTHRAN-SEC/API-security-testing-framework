# API Testing using Postman

## Overview
Postman was used to manually test API endpoints and simulate real-world attack scenarios.

## What was tested
### 1. Authentication (JWT Token)
- Sent POST request to /login
- Generated JWT token
- Used token in headers for authenticated requests

**Screenshot:**
<img width="1363" height="726" alt="2026-04-23_10-49" src="https://github.com/user-attachments/assets/a6851453-cad8-446d-9af5-36ce25f83be9" />

### 2. BOLA (Broken Object Level Authorization)
- Sent GET request:
/user/1
- Modified user ID to:
/user/2
- Accessed another user’s data without authorization

Screenshot:
<img width="1365" height="736" alt="1" src="https://github.com/user-attachments/assets/c5ac6fbb-e881-4096-b36c-2eb24260da09" />

### 3. Rate Limiting Test
- Sent multiple requests to:
/data
- Observed no restriction or blocking

Screenshot:
<img width="1365" height="736" alt="2" src="https://github.com/user-attachments/assets/bf62fcfd-db09-418d-8eb0-75aa7f520757" />

### 4. API Key Exposure
- Sent GET request to:
/config
- API returned sensitive API key in response

Screenshot:
<img width="1360" height="726" alt="3" src="https://github.com/user-attachments/assets/36ee3be8-d31d-4726-8775-869db59953e3" />
