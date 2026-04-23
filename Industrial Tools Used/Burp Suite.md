# API Security Testing using Burp Suite

## Overview

Burp Suite was used to intercept, analyze, and manipulate API requests to simulate real-world attacks.

### Tested manually by the Burp Suite tool
#### 1. Intercepting API Requests
To analyze how data is sent to the server
- Configured Burp Proxy
- Captured request from browser/Postman
- Intercepted API calls

Screenshot:
<img width="1365" height="734" alt="4" src="https://github.com/user-attachments/assets/5d1c7935-5578-403a-b6e6-e683818573c8" />

### 2. BOLA Attack using Repeater
- Sent request to /user/1
- Forwarded to Repeater
Modified:
- GET /user/2
- Sent request again

Result:
- Accessed another user’s data → Unauthorized access

Screenshot:
<img width="1365" height="727" alt="5" src="https://github.com/user-attachments/assets/a35ed347-3859-4705-b0a8-7db18287fbd0" />

### 3. Rate Limiting Test using Intruder
- Sent /data request to Intruder
- Configured attack type: Sniper
- Sent multiple automated requests

Result:
- Server allowed unlimited requests → No rate limiting

Screenshot:
<img width="1362" height="724" alt="6" src="https://github.com/user-attachments/assets/a0a39d51-daa6-490e-9694-c7f3d1756cd7" />

### 4. API Key Exposure Analysis
- Intercepted /config request
- Observed response
Result:
- API key visible in response → Sensitive data exposure

Screenshot:
<img width="1363" height="734" alt="7" src="https://github.com/user-attachments/assets/ab610bf6-7647-4cbb-809c-1d6a9fbceb5d" />
