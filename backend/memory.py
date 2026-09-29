from hindsight_client import Hindsight

from config import (
    HINDSIGHT_API_KEY,
    HINDSIGHT_BASE_URL
)


# --------------------------------------------------
# HINDSIGHT CLIENT
# --------------------------------------------------

hindsight = Hindsight(
    base_url=HINDSIGHT_BASE_URL,
    api_key=HINDSIGHT_API_KEY
)


# --------------------------------------------------
# CUSTOMER BANK
# --------------------------------------------------

def get_bank_id(customer_id: str) -> str:

    """
    Creates a unique Hindsight memory bank
    for every customer.
    """

    return f"supportpilot-{customer_id}"


# --------------------------------------------------
# INITIALIZE CUSTOMER MEMORY
# --------------------------------------------------

def initialize_customer(customer_id: str):

    bank_id = get_bank_id(customer_id)

    try:

        hindsight.create_bank(
            bank_id=bank_id,
            name=f"SupportPilot Memory - {customer_id}"
        )

        print(f"Created memory bank: {bank_id}")

    except Exception as error:

        # Bank may already exist.
        print(
            f"Memory bank already exists or could not be created: "
            f"{error}"
        )

    return bank_id


# --------------------------------------------------
# RETAIN MEMORY
# --------------------------------------------------

def retain_memory(
    customer_id: str,
    content: str
) -> bool:

    """
    Stores useful customer information
    in Hindsight.
    """

    bank_id = initialize_customer(customer_id)

    try:

        hindsight.retain(
            bank_id=bank_id,
            content=content,
            context="customer-support"
        )

        print(
            f"Memory retained for customer: {customer_id}"
        )

        return True

    except Exception as error:

        print(
            f"Memory retain error: {error}"
        )

        return False


# --------------------------------------------------
# RECALL MEMORY
# --------------------------------------------------

def recall_memory(
    customer_id: str,
    query: str
):
    bank_id = initialize_customer(customer_id)

    try:
        result = hindsight.recall(
            bank_id=bank_id,
            query=query
        )

        memories = []

        if hasattr(result, "results"):
            for item in result.results:
                if hasattr(item, "text"):
                    memories.append(item.text)

                elif isinstance(item, dict):
                    text = item.get("text")

                    if text:
                        memories.append(text)

        # Remove noisy SupportPilot test/failure memories
        filtered_memories = []

        for memory in memories:
            lower_memory = memory.lower()

            if (
                "supportpilot failed" in lower_memory
                or "supportpilot requested" in lower_memory
                or "temporarily unable" in lower_memory
            ):
                continue

            filtered_memories.append(memory)

        print(
            f"Recalled {len(filtered_memories)} useful memories "
            f"for customer: {customer_id}"
        )

        return filtered_memories

    except Exception as error:
        print(
            f"Memory recall error: {error}"
        )

        return []