import os
import time
from google import genai
from google.genai.errors import ServerError
from dotenv import load_dotenv
from constants import (
    WORD_OF_THE_DAY_PROMPT, 
    MAX_RETRIES, 
    RETRY_WAIT_BASE,
    PRIMARY_MODEL,
    FALLBACK_MODEL
)


def get_german_word_of_the_day():
    """
    Calls Gemini 2.5 Pro model to get a German word of the day with pronunciation and examples.
    Implements retry logic for 503 errors (server overloaded).
    
    Returns:
        str: The response from Gemini containing the German word of the day
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Initialize the client
    client = genai.Client()
    
    # Try primary model with retries
    primary_failed = False
    for attempt in range(MAX_RETRIES):
        try:
            response = client.models.generate_content(
                model=PRIMARY_MODEL,
                contents=WORD_OF_THE_DAY_PROMPT
            )
            return response.text
        except Exception as e:
            # Check if it's a quota error or server error
            error_message = str(e)
            
            # Check for quota exceeded - switch to Flash immediately
            is_quota_error = (
                '429' in error_message or
                'RESOURCE_EXHAUSTED' in error_message or
                'quota' in error_message.lower()
            )
            
            # Check for other server errors (503, unavailable, etc.)
            is_server_error = (
                isinstance(e, ServerError) or 
                '503' in error_message or 
                'UNAVAILABLE' in error_message or
                'overloaded' in error_message.lower()
            )
            
            # If quota exceeded, switch to Flash immediately
            if is_quota_error:
                primary_failed = True
                break
            
            # If it's a server error and we have retries left, wait and retry
            if is_server_error and attempt < MAX_RETRIES - 1:
                wait_time = RETRY_WAIT_BASE * (attempt + 1)  # Exponential backoff
                time.sleep(wait_time)
                continue
            elif is_server_error and attempt == MAX_RETRIES - 1:
                # All retries exhausted, mark primary as failed
                primary_failed = True
                break
            else:
                # Not a quota/server error, raise immediately
                raise e
    
    # If primary model failed after all retries, try fallback model
    if primary_failed:
        for attempt in range(MAX_RETRIES):
            try:
                response = client.models.generate_content(
                    model=FALLBACK_MODEL,
                    contents=WORD_OF_THE_DAY_PROMPT
                )
                return response.text
            except Exception as e:
                # Check if it's a server error or quota exceeded
                error_message = str(e)
                is_server_error = (
                    isinstance(e, ServerError) or 
                    '503' in error_message or 
                    '429' in error_message or
                    'UNAVAILABLE' in error_message or
                    'RESOURCE_EXHAUSTED' in error_message or
                    'quota' in error_message.lower() or
                    'overloaded' in error_message.lower()
                )
                
                # If it's a server error/quota and we have retries left, wait and retry
                if is_server_error and attempt < MAX_RETRIES - 1:
                    wait_time = RETRY_WAIT_BASE * (attempt + 1)
                    time.sleep(wait_time)
                    continue
                else:
                    # Either not a server error, or we're out of retries
                    raise e


if __name__ == "__main__":
    try:
        result = get_german_word_of_the_day()
        print(result)
    except Exception as e:
        print(f"Error: {e}")

