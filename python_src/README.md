# Python Translation

This directory provides a lightweight Python translation of the container server.
It exposes the same basic routes as the original TypeScript server:

- `/` and `/container` – health check
- `/error` – test error route
- `/process-issue` – stub endpoint for issue processing

Run the server locally with:

```bash
pip install -r requirements.txt
python app.py
```
