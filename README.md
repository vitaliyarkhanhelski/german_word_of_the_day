# 🇩🇪 German Word of the Day

A beautiful Streamlit web app that generates a daily German word from the Top 2000 most common words, complete with IPA pronunciation, Polish translation, example sentences, and cultural insights. Powered by Google's Gemini 2.5 Pro AI.

---

## ✨ Features

- 🎯 **Smart Word Selection** - Random words from the Top 2000 German vocabulary list
- 🔊 **Dual Pronunciation** - Both IPA transcription and Polish phonetic guide
- 📚 **Rich Examples** - 3 real-world example sentences with translations
- 🎨 **Modern UI** - Beautiful purple gradient design with smooth animations
- 🎈 **Celebration Effects** - Balloons animation when generating new words
- 🔄 **Auto-Retry** - Smart error handling with automatic fallback to Gemini Flash
- 💾 **Session Memory** - Your last generated word persists until you generate a new one

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get Your Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy your new API key

### 3. Configure Environment

Create a `.env` file in the project root:

```bash
# Create .env file
touch .env
```

Add your API key to the `.env` file:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

⚠️ **Important:** Never commit your `.env` file to git! (It's already in `.gitignore`)

### 4. Launch the App

```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501` 🎉

---

## 📖 Usage

### Web Interface (Recommended)

Simply click the **"✨ Losuj Słówko"** button to generate a new German word!

Each word includes:
- 🇩🇪 **German word** with proper capitalization
- 🔤 **Pronunciation** in IPA format and Polish phonetics
- 📝 **Meaning** in Polish
- 💬 **3 Example sentences** with Polish translations and usage tips
- 🎓 **Cultural insight** (Ciekawostka) with idioms and interesting facts

### Command Line

Run directly from terminal:

```bash
python gemini_api.py
```

### Python Module

Use in your own scripts:

```python
from gemini_api import get_german_word_of_the_day

# Generate a word
word = get_german_word_of_the_day()
print(word)
```

---

## 🏗️ Project Structure

```
german_word_of_the_day/
├── app.py              # Streamlit web interface
├── gemini_api.py       # Core API logic with retry handling
├── constants.py        # Prompts and configuration
├── style.css           # Custom UI styling
├── requirements.txt    # Python dependencies
├── .env               # API key (create this - not in git)
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

---

## 🛠️ Configuration

All settings are in `constants.py`:

- **`PRIMARY_MODEL`** - Default: `gemini-2.5-pro` (best quality)
- **`FALLBACK_MODEL`** - Default: `gemini-2.5-flash` (faster, used when quota exceeded)
- **`MAX_RETRIES`** - Default: `3` attempts per model
- **`RETRY_WAIT_BASE`** - Default: `3` seconds (exponential backoff)

---

## 🔧 Troubleshooting

### API Key Not Working

1. Make sure your `.env` file is in the project root directory
2. Check that the key is on a line starting with `GEMINI_API_KEY=`
3. No quotes needed around the API key
4. Restart the Streamlit app after changing `.env`

### "Model is overloaded" Error

The app automatically retries with exponential backoff and falls back to Gemini Flash if needed. If the error persists:

1. Wait a few minutes and try again
2. The app will use Gemini 2.5 Flash as fallback automatically
3. Check [Google AI Status](https://status.cloud.google.com/)

### Quota Exceeded (429 Error)

The free tier has usage limits. The app automatically switches to Gemini Flash. If both models are exhausted:

1. Wait for quota reset (usually daily)
2. Consider upgrading your API plan
3. Check your usage at [Google AI Studio](https://aistudio.google.com/)

### Streamlit Not Opening

```bash
# Specify port manually
streamlit run app.py --server.port 8501

# Or use a different port
streamlit run app.py --server.port 8080
```

---

## 🎨 Customization

### Change UI Colors

Edit `style.css`:

```css
/* Main background gradient */
.stApp {
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
}

/* Result container background */
[data-testid="column"]:has(.result-box-wrapper) {
    background: rgba(255, 255, 255, 0.25) !important;
}
```

### Modify the Prompt

Edit `constants.py` to change:
- Number of example sentences
- Formatting style
- Additional information to include

---

## 📦 Requirements

- **Python:** 3.10+ (for modern type hints)
- **Dependencies:**
  - `google-genai` >= 0.11.0
  - `python-dotenv` >= 1.0.0
  - `streamlit` >= 1.28.0
  - `markdown` >= 3.5.0

---

## 🤝 Contributing

Feel free to open issues or submit pull requests with improvements!

---

## 📄 License

This project is open source and available for personal and educational use.

---

## 🌟 Tips for Learning German

- **Daily Practice:** Generate a new word every day
- **Write It Down:** Keep a vocabulary notebook
- **Use in Context:** Try making your own sentences
- **Speak Out Loud:** Practice the pronunciation
- **Review Regularly:** Come back to previous words

---

**Made with ❤️ and AI**

*Learning German one word at a time! 🇩🇪🇵🇱*
