"""
Constants for the German Word of the Day application.
"""

# Gemini API prompt for generating German word of the day
WORD_OF_THE_DAY_PROMPT = """Wygeneruj słówko dnia z listy Top 2000 niemieckich słów z wymową, znaczeniem i 3 przykładami.

Napisz w przyjazny, lekki sposób — jak dla znajomego uczącego się niemieckiego.
Użyj emoji, flagi 🇩🇪 przy niemieckich słowach, flagi 🇵🇱 przy polskich tłumaczeniach.

⚠️ BARDZO WAŻNE: Twoja odpowiedź MUSI zaczynać się DOKŁADNIE od tekstu "Słówko dnia na dziś:"
NIE DODAWAJ żadnego wprowadzenia, powitania ani tekstu przed "Słówko dnia na dziś:"!

FORMATOWANIE MARKDOWN:
- Dla nagłówka słowa użyj ###
- **pogrubienie** dla etykiet (Wymowa, Znaczenie, etc.)
- Dla poziomej linii użyj: ---
- Puste linie między sekcjami

DOKŁADNA STRUKTURA (skopiuj dokładnie ten format):

Słówko dnia na dziś:

### słowo 🇩🇪

**Wymowa:** [transkrypcja IPA] – **po polsku:** [jak-to-brzmi]

**Znaczenie:** znaczenie po polsku

**Przykładowe zdania:**

1. 🇩🇪 Pierwsze zdanie niemieckie z emoji. 😊  
   🇵🇱 Pierwsze polskie tłumaczenie. (Opcjonalna wskazówka)

2. 🇩🇪 Drugie zdanie niemieckie z emoji. 🎉  
   🇵🇱 Drugie polskie tłumaczenie. (Opcjonalna wskazówka)

3. 🇩🇪 Trzecie zdanie niemieckie z emoji. 🌟  
   🇵🇱 Trzecie polskie tłumaczenie. (Opcjonalna wskazówka)

---

**Ciekawostka:** Idiom, kontekst kulturowy lub zabawne skojarzenie związane ze słowem. WSZYSTKIE niemieckie wyrazy i frazy w tej sekcji MUSZĄ być w backticks: `jak kod inline`.

KRYTYCZNIE WAŻNE FORMATOWANIE:
- **Wymowa:** MUSI zawierać zarówno transkrypcję IPA (np. [ˈɪmɐ]) JAK I polską fonetyczną (np. po polsku: [imer])
- Używaj [] dla transkrypcji IPA
- **Ciekawostka:** WSZYSTKIE niemieckie słowa/frazy otaczaj backticksami `tak jak kod` dla lepszej czytelności
- Każdy punkt (1., 2., 3.) to osobna pozycja na liście
- Po niemieckim zdaniu dwie spacje + nowa linia
- Polskie tłumaczenie z wcięciem (3 spacje na początku)
- NIE WSTAWIAJ pustych linii między 🇩🇪 a 🇵🇱 w tym samym punkcie
- NIE WSTAWIAJ pustych linii między punktami 1, 2, 3
- Zachowaj ciągłość numeracji!

⚠️ PIERWSZA LINIA ODPOWIEDZI: "Słówko dnia na dziś:" (bez żadnego tekstu przed tym!)"""


# Model configuration
PRIMARY_MODEL = "gemini-2.5-pro"
FALLBACK_MODEL = "gemini-2.5-flash"

# Retry configuration
MAX_RETRIES = 3
RETRY_WAIT_BASE = 3  # Base wait time in seconds for exponential backoff

