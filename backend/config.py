import os
from dotenv import load_dotenv

load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")

HINDSIGHT_API_KEY = os.getenv("HINDSIGHT_API_KEY")

HINDSIGHT_BASE_URL = os.getenv(
    "HINDSIGHT_BASE_URL",
    "https://api.hindsight.vectorize.io"
)


if not GROQ_API_KEY:
    print("WARNING: GROQ_API_KEY is not configured.")

if not HINDSIGHT_API_KEY:
    print("WARNING: HINDSIGHT_API_KEY is not configured.")