"""
German Word of the Day - Gemini API Integration

Core module for generating German vocabulary using Google's Gemini AI models.
Implements robust error handling with automatic retries and model fallback.

Main Features:
- Primary model: Gemini 2.5 Pro (best quality)
- Fallback model: Gemini 2.5 Flash (when quota exceeded)
- Exponential backoff retry logic for server errors (503, UNAVAILABLE)
- Immediate fallback for quota errors (429, RESOURCE_EXHAUSTED)
- Production logging to stdout for debugging

Error Handling Strategy:
1. Server errors (503, UNAVAILABLE): Retry with exponential backoff
2. Quota errors (429, RESOURCE_EXHAUSTED): Immediately switch to Flash model
3. Other errors: Fail immediately without retry

Usage:
    from gemini_api import get_german_word_of_the_day
    
    word = get_german_word_of_the_day()
    print(word)

Environment Requirements:
    - GEMINI_API_KEY must be set in .env file
    - Valid Google Gemini API key with sufficient quota

Author: Powered by Google Gemini AI
"""

import time
import os
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


def _log_model_response(model: str, response_text: str) -> None:
    """
    Log model response to stdout for debugging in production.
    
    Args:
        model: Name of the model used
        response_text: Generated response text
    """
    os.write(1, b'\n' + b'='*80 + b'\n')
    os.write(1, f'RAW RESPONSE FROM {model}:\n'.encode('utf-8'))
    os.write(1, b'='*80 + b'\n')
    os.write(1, response_text.encode('utf-8') + b'\n')
    os.write(1, b'='*80 + b'\n\n')


def _is_retryable_error(error: Exception) -> tuple[bool, bool]:
    """
    Check if error is quota-related or server-related.
    
    Returns:
        tuple: (is_quota_error, is_server_error)
    """
    error_message = str(error)
    
    is_quota_error = (
        '429' in error_message or
        'RESOURCE_EXHAUSTED' in error_message or
        'quota' in error_message.lower()
    )
    
    is_server_error = (
        isinstance(error, ServerError) or
        '503' in error_message or
        'UNAVAILABLE' in error_message or
        'overloaded' in error_message.lower()
    )
    
    return is_quota_error, is_server_error


def _try_model_with_retries(client: genai.Client, model: str) -> str:
    """
    Try to generate content with retries for server errors.
    
    Args:
        client: Gemini API client
        model: Model name to use
        
    Returns:
        Generated text content
        
    Raises:
        Exception: If all retries fail or non-retryable error occurs
    """
    for attempt in range(MAX_RETRIES):
        try:
            response = client.models.generate_content(
                model=model,
                contents=WORD_OF_THE_DAY_PROMPT
            )
            # Log raw response for debugging in production
            _log_model_response(model, response.text)
            return response.text
        except Exception as e:
            is_quota_error, is_server_error = _is_retryable_error(e)
            
            # If quota exceeded or server error on last attempt, fail
            if is_quota_error or (is_server_error and attempt == MAX_RETRIES - 1):
                raise e
            
            # If server error and we have retries left, wait and retry
            if is_server_error and attempt < MAX_RETRIES - 1:
                wait_time = RETRY_WAIT_BASE * (attempt + 1)
                time.sleep(wait_time)
                continue
            
            # Non-retryable error, raise immediately
            raise e


def get_german_word_of_the_day() -> str:
    """
    Get a German word of the day from Gemini API.
    
    Uses Gemini 2.5 Pro by default, with automatic fallback to Gemini 2.5 Flash
    if quota is exceeded or server errors persist. Implements exponential backoff
    retry logic for temporary server issues.
    
    Returns:
        str: Formatted German word with pronunciation, meaning, examples and trivia
        
    Raises:
        Exception: If both primary and fallback models fail
    """
    load_dotenv()
    client = genai.Client()
    
    # Try primary model
    try:
        return _try_model_with_retries(client, PRIMARY_MODEL)
    except Exception as e:
        is_quota_error, is_server_error = _is_retryable_error(e)
        
        # Only try fallback if it was a quota or server error
        if not (is_quota_error or is_server_error):
            raise e
    
    # Try fallback model
    return _try_model_with_retries(client, FALLBACK_MODEL)


if __name__ == "__main__":
    try:
        result = get_german_word_of_the_day()
        print(result)
    except Exception as e:
        print(f"Error: {e}")
