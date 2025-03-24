from openai import OpenAI
from dotenv import load_dotenv
import os


def get_chat_response(prompt, role='yor are a helpful data analyst.'):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        # model="gpt-4o",
        messages=[
            {"role": "system", "content": f"{role}"},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content