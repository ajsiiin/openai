import openai

def generate_sql_query(classification, parameters, schema_info):
    prompt = f"""
    You are generating an SQL query for a {classification} request. 
    Based on the schema information:
    
    {schema_info}
    
    Create an SQL query using parameters: {parameters}.
    """
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=100
    )
    sql_query = response.choices[0].text.strip()
    return sql_query