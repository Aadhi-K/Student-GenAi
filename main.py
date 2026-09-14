from fastapi import FastAPI
from router.auth_rout import router
from router.pdf_router import router as pdf_router
from router.rag_router import router as rag_router
from router.chat_router import router as chat_router
from router.study_plan_router import router as study_plan_router
from router.mock_test_router import (router as mock_test_router)
from router.assessment_router import (router as assessment_router)
from router.tutor_router import router as tutor_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
app.include_router(rag_router)  
app.include_router(pdf_router)
app.include_router(chat_router)
app.include_router(study_plan_router)
app.include_router(mock_test_router)
app.include_router(assessment_router)
app.include_router(tutor_router)