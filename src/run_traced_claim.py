from langfuse.openai import openai
from dotenv import load_dotenv
import os

# Load environment variables BEFORE importing Langfuse
load_dotenv()

# Initialize with metadata for better trace organization
completion = openai.chat.completions.create(
    name="claims-triage",  # Descriptive trace name
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": (
                "You are an insurance claims triage assistant. "
                "Do not confirm coverage. Identify likely claim type, "
                "missing information, and whether human review is required."
            ),
        },
        {
            "role": "user",
            "content": (
                "Water damage discovered after long-term leakage under the kitchen floor. "
                "The claimant asks whether this is covered."
            ),
        },
    ],
    metadata={
        "workflow": "claims-triage",
        "prompt_version": "v1",
        "use_case": "insurance-claims",
    },
)

print(completion.choices[0].message.content)
print("✓ Trace sent to Langfuse")
