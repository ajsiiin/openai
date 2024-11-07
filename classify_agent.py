import openai

def classify_request(description):
    prompt = f"Classify the following request:\n\n'{description}'\n\nCategories: Data Issue, Trade Failure, Report Generation."
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=20
    )
    classification = response.choices[0].text.strip()
    return classification