import json
import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_workload(description):
    prompt = (
        "Given the following workload description, estimate:\n"
        "- Number of vCPUs\n"
        "- RAM in GB\n"
        "- Whether a GPU is required\n"
        "- Estimated duration in minutes\n\n"
        f"Workload: {description}\n\n"
        "Respond in JSON format like:\n"
        "{\n"
        "  \"cpu\": 2,\n"
        "  \"ram_gb\": 4,\n"
        "  \"gpu\": false,\n"
        "  \"duration_min\": 10\n"
        "}"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    reply = response.choices[0].message.content
    return json.loads(reply)
