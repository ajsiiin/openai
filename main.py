from classify_agent import classify_request
from query_generation_agent import generate_sql_query
from validation_agent import validate_sql_query
from response_format_agent import format_response
from embeddings_faiss import search_with_embeddings
import openai

def process_request(description, parameters):
    # Step 1: Classify the request
    classification = classify_request(description)
    print(f"Classification: {classification}")
    
    # Step 2: Generate SQL query based on classification and parameters
    schema_info = {
        "trades": ["trade_id", "status", "trade_date", "amount", "user_id"],
        "users": ["user_id", "name", "email", "department"]
    }
    sql_query = generate_sql_query(classification, parameters, schema_info)
    print(f"Generated SQL Query: {sql_query}")
    
    # Step 3: Validate the SQL query
    validation_feedback = validate_sql_query(sql_query)
    if "Unsafe" in validation_feedback:
        raise ValueError("SQL query validation failed.")
    
    # Step 4: Execute query in DB and retrieve raw data (simulated here)
    raw_data = execute_sql(sql_query)  # You will implement execute_sql()
    
    # Step 5: Format the response
    formatted_response = format_response(raw_data, classification)
    print("Formatted Response:", formatted_response)

    # Step 6: Use FAISS to search and retrieve additional embeddings-based information
    search_results = search_with_embeddings(description)
    print("Search Results:", search_results)
    
    return formatted_response

# Sample usage
if __name__ == "__main__":
    description = "Retrieve all failed trades from the last month."
    parameters = {"date_range": "last month"}
    response = process_request(description, parameters)
