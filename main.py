import os
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ai_consultant_assistant(company_description):
    system_prompt = (
        "You are an experienced AI consultant. "
        "Given a short company description, identify 3-5 AI use cases, "
        "estimate potential ROI or efficiency improvements, "
        "and recommend tools or platforms (e.g., OpenAI, LangChain, Zapier, etc.). "
        "Return the output in clear, concise markdown sections."
    )

    user_prompt = f"Company description: {company_description}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.6,
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    desc = input("Describe the company or process: ")
    result = ai_consultant_assistant(desc)
    print("\n--- AI Consultant Output ---\n")
    print(result)
