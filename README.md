# myJobApp

A minimal FastAPI application with simple job listing endpoints.

## Run locally

1. Create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the app:

   ```bash
   uvicorn main:app --reload
   ```

4. Open API docs at `http://127.0.0.1:8000/docs`.

## Endpoints

- `GET /` - API root
- `GET /health` - health check
- `GET /jobs` - list all jobs
- `GET /jobs/{job_id}` - retrieve a job by ID
