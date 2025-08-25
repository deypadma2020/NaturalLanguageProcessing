import re
import string
import spacy
from textblob import TextBlob
from nltk.corpus import stopwords

# Download stopwords if not already
import nltk
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

def clean_text_full(text):
    # 1. Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    
    # 2. Lowercase
    text = text.lower()
    
    # 3. Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    
    # 4. Remove emojis
    emoji_pattern = re.compile("[" 
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags
        "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)
    
    # 5. Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # 6. Remove digits
    text = re.sub(r'\d+', '', text)
    
    # 7. Spell correction
    text = str(TextBlob(text).correct())
    
    # 8. Remove stopwords
    words = [w for w in text.split() if w not in stop_words]
    text = ' '.join(words)
    
    # 9. Tokenization using spaCy
    doc = nlp(text)
    tokens = [token.text for token in doc]
    
    return tokens

# Example usage
sample_text = """
<p>Hello 😊! Visit https://example.com. I have 2 apples, 3 oranges & bananas.</p>
"""

cleaned_tokens = clean_text_full(sample_text)
print(cleaned_tokens)
