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

- sparsity -

- sparse array - 

- OOV (Out Of Vocabulary) -

- One Hot Encoding - 
    - flaws - 1. sparsity, 2. No fixed size, 3. OOV, 4. No capturing of semantic meaning


- Bag Of Words - use in text classification (semantic meaning capture)

    - hyperparameter - 
        for sentiment analysis binary = True(0,1)
        max_features -
    

    - flaws - 
        - sparsity
        - overfitting
        - oov
        - ignore order

- Bag of N-grams - 
    - better semantic meaning
    - flaws - 
        - dimentionality - slows down the algo
        - oov

- Tf-ldf - (term frequency(probability of existence- total no of document)- Inverse document frequecy(log -frequency high - lower, rare - high weitage   )) 
    rare word should get higher weitage

    - information retrieval(search engine) - use

    -flaws -
        - sparsity
        - oov
        - dimension
        - semantic relation

- Word2Vec (deep learning) -
    1. can capture semantic meaning
    2. low dimension(mostly within 100)
    3. dense vector(mostly non-zero dimension values) - prevent over-fitting


- cBow - Continuous Bag Of Words
    - need to take 3/5/... window, middle one is target word and both side words are context word
    - good for small data and very fast
- Skip-gram -
    - good for large data


- The pipeline of a NLP PROJECT
    - Data Acuisation
    - Text Preprocessiing
    - Text Vectorization
    - Modelling -> 
        - ML -> Naive Bayes, Random Forest Classifier, SVM, ...
        - DL -> 
            - RNN -> LSTM
            - CNN
            - BERT(PRE-TRAINED)
    - Evaluation -> ACCURACY, CONFUSION MATTRIX
    - Deploy -> AWS


-  parts of speech(_pos):
    - fine trained pos
    - core trained pos