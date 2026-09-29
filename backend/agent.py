from groq import Groq

from config import GROQ_API_KEY

from memory import (
    recall_memory,
    retain_memory
)

from prompts import build_support_prompt


# --------------------------------------------------
# GROQ CLIENT
# --------------------------------------------------

groq_client = Groq(
    api_key=GROQ_API_KEY
)


# --------------------------------------------------
# GENERATE SUPPORT RESPONSE
# --------------------------------------------------

def generate_response(
    customer_id: str,
    customer_name: str,
    message: str,
    memory_enabled: bool = True
):

    # ----------------------------------------------
    # STEP 1 — RECALL MEMORY
    # ----------------------------------------------

    memories = []

    if memory_enabled:
        memories = recall_memory(
    customer_id=customer_id,
    query=f"customer technical environment, previous support issues, successful solutions, database connection pool, API timeouts, {message}"
)

    # ----------------------------------------------
    # STEP 2 — CREATE PROMPT
    # ----------------------------------------------

    prompt = build_support_prompt(
        customer_name=customer_name,
        user_message=message,
        memories=memories
    )

    # ----------------------------------------------
    # STEP 3 — CALL GROQ
    # ----------------------------------------------

    try:

        response = groq_client.chat.completions.create(
    model="openai/gpt-oss-120b",
    reasoning_effort="low",
    include_reasoning=False,
    messages=[
    
        

                {
                    "role": "system",
                    "content": (
                        "You are SupportPilot, "
                        "a customer support agent."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.2,
            max_tokens=500
        )

        answer = response.choices[0].message.content

    except Exception as error:

        print(f"Groq API error: {error}")

        answer = (
            "I'm temporarily unable to generate "
            "a support response. Please try again."
        )

    # ----------------------------------------------
    # STEP 4 — RETAIN NEW INFORMATION
    # ----------------------------------------------

    if memory_enabled:

        memory_to_store = f"""
Customer: {customer_name}

Customer message:
{message}

SupportPilot response:
{answer}
"""

        retain_memory(
            customer_id=customer_id,
            content=memory_to_store
        )

    # ----------------------------------------------
    # RETURN RESULT
    # ----------------------------------------------

    return {
        "answer": answer,
        "memories": memories
    }