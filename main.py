import os
from google import genai
from dotenv import load_dotenv


def get_german_word_of_the_day():
    """
    Calls Gemini 2.5 Pro model to get a German word of the day with pronunciation and examples.
    
    Returns:
        str: The response from Gemini containing the German word of the day
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Initialize the client
    client = genai.Client()
    
    # Prompt for German word of the day
    prompt = "Słówko dnia poniemiecku z listy Top 2000 wraz z wymową i przykładami. Zacznij od: Słówko dnia na dziś:"
    
    # Generate response
    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt
    )
    
    return response.text


if __name__ == "__main__":
    try:
        result = get_german_word_of_the_day()
        print(result)
    except Exception as e:
        print(f"Error: {e}")

