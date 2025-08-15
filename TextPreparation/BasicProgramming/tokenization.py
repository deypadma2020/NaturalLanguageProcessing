import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt_tab')
nltk.download('punkt')

sample_text = """
Natural Language Processing is fun and powerful. 
Tokenization splits text into words or sentences. 
Python provides several libraries for NLP tasks. 
TextBlob, NLTK, and spaCy are popular choices. 
Each has its own strengths and use cases. 
Preprocessing text is important before modeling. 
Removing stopwords can improve accuracy. 
Stemming and lemmatization help normalize words. 
Machine learning models use tokens as features. 
Clean data is the foundation of good NLP results.
"""

# Sentence tokenization
sentences = sent_tokenize(sample_text)
print(sentences)
print()

# Word tokenization
for sentence in sentences:
    print(word_tokenize(sentence))
