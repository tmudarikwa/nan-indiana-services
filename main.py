from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr

app = FastAPI(title='NAN Indiana API', version='1.0.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


class NewsletterSubscription(BaseModel):
    email: EmailStr


@app.get('/api/health')
def health_check() -> dict[str, str]:
    return {'status': 'ok'}


@app.post('/api/newsletter/subscribe')
def subscribe_newsletter(payload: NewsletterSubscription) -> dict[str, str]:
    email = str(payload.email).strip().lower()
    if not email:
        raise HTTPException(status_code=400, detail='An email is required.')

    return {
        'message': f'Thank you, {email}! You have joined the newsletter.',
    }
