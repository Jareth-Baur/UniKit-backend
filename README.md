# UniKit Backend

UniKit Backend provides the API services for the UniKit web application.

The backend is built with FastAPI and Python and is designed to provide processing services such as OCR, image processing, and audio processing.

## Tech Stack

- Python
- FastAPI
- Uvicorn
- EasyOCR
- Pillow
- NumPy

Additional dependencies are listed in `requirements.txt`.

## Project Structure

```text
UniKit-backend/
├── app/
│   ├── main.py
│   ├── routers/
│   ├── services/
│   └── utils/
├── requirements.txt
├── .env
└── README.md
```

## Create a Virtual Environment

From the UniKit backend directory:

```powershell
python -m venv .venv
```

> Note: the command is `python`, not `ppython`.

## Activate the Virtual Environment

PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, you may need to adjust the execution policy for your user account or activate the environment through another supported shell.

## Install Dependencies

After activating the virtual environment:

```powershell
pip install -r requirements.txt
```

## Run the Backend

Start the FastAPI development server:

```powershell
uvicorn app.main:app --reload
```

The API will normally be available at:

```text
http://localhost:8000
```

FastAPI's interactive API documentation is available at:

```text
http://localhost:8000/docs
```

The alternative ReDoc documentation is available at:

```text
http://localhost:8000/redoc
```

## OCR

The OCR service uses EasyOCR to extract text from uploaded images.

Example endpoint:

```text
POST /api/ocr/scan
```

The endpoint accepts an image upload and returns the extracted text together with detected text regions, confidence scores, and bounding boxes.

Example response:

```json
{
  "text": "Extracted text",
  "detections": [
    {
      "text": "Extracted text",
      "confidence": 0.95,
      "bounding_box": [
        [10, 10],
        [200, 10],
        [200, 50],
        [10, 50]
      ]
    }
  ],
  "count": 1
}
```

## Development

The backend uses Uvicorn's reload mode during development:

```powershell
uvicorn app.main:app --reload
```

Stop the server with:

```text
CTRL + C
```

## Environment Variables

If the backend requires environment variables, document them in `.env.example`.

Do not commit private secrets or production credentials to Git.

## CORS

The backend must allow requests from the frontend origin.

During local development, the frontend normally runs on:

```text
http://localhost:5173
```

When deploying, update the backend CORS configuration to allow the deployed frontend domain.

For example:

```text
Development:
http://localhost:5173

Production:
https://your-frontend-domain.com
```

Do not use unrestricted CORS in production unless there is a specific reason to do so.

## Deployment

Deploy the backend separately from the React frontend.

A typical deployment process is:

1. Push the backend to your Git repository.
2. Choose a Python-compatible hosting platform.
3. Install dependencies from `requirements.txt`.
4. Configure backend environment variables.
5. Start the application with a production-compatible command.
6. Configure CORS for the deployed frontend.
7. Update the frontend `VITE_API_URL` to point to the deployed backend.

For production, use a command appropriate for your hosting provider rather than assuming the local development command is sufficient.

## Local Development URLs

```text
Frontend:
http://localhost:5173

Backend:
http://localhost:8000

API Docs:
http://localhost:8000/docs
```

## Notes

- Keep `.venv/` out of Git.
- Keep `.env` out of Git when it contains private values.
- Use `.env.example` to document required configuration.
- Keep API routes, processing logic, and validation separated into routers, services, and utilities.
