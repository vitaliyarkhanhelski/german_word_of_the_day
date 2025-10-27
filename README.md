# German Word of the Day

A Python project that uses Google's Gemini 2.5 Pro model to generate a German word of the day from the Top 2000 list, complete with pronunciation and examples.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Key:**
   - Copy `.env.example` to `.env`
   - Add your Gemini API key to the `.env` file:
     ```
     GEMINI_API_KEY=your_actual_api_key_here
     ```

## Usage

### Run the Streamlit Web App (Recommended):
```bash
streamlit run app.py
```

This will open a beautiful web interface in your browser where you can generate German words with a single button click!

### Run the script directly:
```bash
python gemini_api.py
```

### Use as a module:
```python
from gemini_api import get_german_word_of_the_day

result = get_german_word_of_the_day()
print(result)
```

## Function

- `get_german_word_of_the_day()`: Calls the Gemini 2.5 Pro model and returns a German word of the day with pronunciation and examples.

## Requirements

- Python 3.7+
- genai
- python-dotenv
- streamlit

## Getting a Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key to your `.env` file

