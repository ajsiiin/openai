import openai

def validate_sql_query(sql_query):
    prompt = f"Validate this SQL query:\n\n{sql_query}\n\nCheck for security and efficiency."
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=50
    )
    validation_feedback = response.choices[0].text.strip()
    return validation_feedback