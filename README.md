# NaturalLanguageProcessing

- Corpus (C) - if my dataset have 10k rows of reviews and I concatenate all into a single string that is called corpus.

- Vocabulary (V) - how many unique words are there in all the reviews that is called vocabulary.

- Document (D) - every single reviews called as document.

- Word (W) -  every single word of documents are called as word.

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
- Skip-gram -