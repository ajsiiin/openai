import openai

def format_response(raw_data, classification):
    prompt = f"""
    Format this data for an Ops team based on a {classification} request:
    
    Data: {raw_data}
    
    Provide a concise summary for non-technical users.
    """
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=150
    )
    formatted_response = response.choices[0].text.strip()
    return formatted_response