# Natural Language Processing (NLP)

Natural Language Processing (NLP) is the field of Artificial Intelligence that deals with teaching machines to understand, interpret, and generate human language.  

This document explains **basic NLP concepts, representations, and project pipelines** in a beginner-friendly way.

---

## 📖 Key Terminology

- **Corpus (C)**  
  A collection of text.  
  Example: If you have 10,000 reviews in your dataset and you put them together, that forms the **corpus**.

- **Vocabulary (V)**  
  The set of unique words in the corpus.  
  Example:  
  Reviews → ["I love NLP", "I love Python"]  
  Vocabulary = {"I", "love", "NLP", "Python"} → size = 4

- **Document (D)**  
  A single piece of text in the corpus.  
  Example: Each review is considered a document.

- **Word (W)**  
  Each token (individual word) in a document.  
  Example: "I love NLP" → Words = ["I", "love", "NLP"]

- **Sparsity**  
  When most values in a matrix are zeros. Very common in NLP representations (like one-hot encoding and BoW).

- **Sparse Array**  
  An array with mostly zero values.  
  Example: If vocabulary size = 10,000 and a sentence contains only 10 words, then 9,990 positions are zero.

- **OOV (Out Of Vocabulary)**  
  Words that are not present in the training vocabulary but appear in new/test data.  
  Example: If your model only knows words from movie reviews, the word "blockchain" might be OOV.

---

## 🔡 Text Representation Methods

### 1. One-Hot Encoding
Represents each word as a vector where one position is "1" and all others are "0".

Example: Vocabulary = ["I", "love", "NLP"]  
- "I" → [1, 0, 0]  
- "love" → [0, 1, 0]  
- "NLP" → [0, 0, 1]  

**Flaws**:
1. Produces very sparse vectors.  
2. Vocabulary keeps growing (no fixed size).  
3. Fails with OOV words.  
4. Cannot capture meaning (semantic relationships).

---

### 2. Bag of Words (BoW)
Represents text as word counts or presence/absence.  
Example:  
Documents = ["I love NLP", "I love Python"]  
Vocabulary = {"I", "love", "NLP", "Python"}  
- D1 → [1, 1, 1, 0]  
- D2 → [1, 1, 0, 1]  

**Hyperparameters**:
- `binary=True` → Only indicates presence (0 or 1).  
- `max_features` → Use only top N most frequent words.

**Flaws**:
- Produces sparse vectors.  
- May cause overfitting on small datasets.  
- Suffers from OOV problem.  
- Ignores word order ("good movie" vs "movie good").

---

### 3. Bag of N-grams
Similar to BoW but considers sequences of words (bigrams, trigrams, etc.) for better context.  

Example: Sentence = "I love NLP"  
- Unigrams → ["I", "love", "NLP"]  
- Bigrams → ["I love", "love NLP"]  

**Flaws**:
- Increases dimensionality drastically.  
- Still faces OOV issues.

---

### 4. TF-IDF (Term Frequency – Inverse Document Frequency)
Improves BoW by giving importance to rare words.  

- **TF** = Frequency of word in a document.  
- **IDF** = log(total documents / number of documents containing the word).  
- Rare words get higher weight, common words (like "the", "is") get lower weight.

Example:  
If "Python" appears in 2/1000 documents → it gets higher importance than "the" appearing in 900/1000.

**Use Case**: Search engines (e.g., matching query with relevant documents).  

**Flaws**:
- Still sparse.  
- High dimensionality.  
- Cannot capture semantic similarity (e.g., "king" and "queen").

---

### 5. Word2Vec (Neural Network-based Embeddings)
Word2Vec maps words into **dense, low-dimensional vectors** where similar words are close in vector space.

- Example:  
  "king" – "man" + "woman" ≈ "queen"

- **Advantages**:
  - Captures semantic meaning.  
  - Produces dense vectors (fewer zeros).  
  - Typically uses ~100 dimensions, avoiding sparsity.

- **Models**:
  - **CBOW (Continuous Bag of Words)**  
    Predicts target word from surrounding context words.  
    Example: Context = ["I", "NLP"], Target = "love".  
    - Fast, works well with small datasets.  

  - **Skip-Gram**  
    Predicts surrounding context words from a target word.  
    Example: Target = "love", Context = ["I", "NLP"].  
    - Works better with large datasets.

---

## ⚙️ NLP Project Pipeline

1. **Data Acquisition**  
   Collect text data (reviews, tweets, articles, etc.).

2. **Text Preprocessing**  
   - Lowercasing  
   - Removing punctuation, numbers, and stopwords  
   - Tokenization  
   - Lemmatization / Stemming  

3. **Text Vectorization**  
   Choose a method (BoW, TF-IDF, Word2Vec, BERT embeddings, etc.).

4. **Modeling**  
   - **Machine Learning**: Naive Bayes, Random Forest, SVM, etc.  
   - **Deep Learning**:  
     - RNN (e.g., LSTM) → remembers sequence  
     - CNN → extracts local patterns  
     - Transformers (e.g., BERT) → state-of-the-art for NLP  

5. **Evaluation**  
   Metrics: Accuracy, Precision, Recall, F1-score, Confusion Matrix.

6. **Deployment**  
   Deploy trained models using cloud platforms (e.g., AWS, GCP, Azure).

---

## 📝 Parts of Speech (POS)

- **Coarse-grained POS** → General categories (e.g., noun, verb, adjective).  
- **Fine-grained POS** → More specific tags (e.g., proper noun vs. common noun, past tense verb vs. present tense).  

Example:  
Sentence = "The cat is sleeping."  
- "The" → Determiner (DET)  
- "cat" → Noun (NOUN)  
- "is" → Verb (AUX)  
- "sleeping" → Verb (VERB)  

---

## 🚀 Summary

- Start with **Corpus, Vocabulary, Documents, Words**.  
- Represent text using **One-Hot, BoW, TF-IDF, or Word2Vec**.  
- Train ML/DL models.  
- Evaluate and deploy your NLP pipeline.  

This step-by-step knowledge forms the foundation of Natural Language Processing.  
