sample_text = """
Ths is a smple txt with som speling erors.  
I realy enjy learnng Pythn and naturall langauge procesing.  
Hop you find this exmple usefull!
"""

from textblob import TextBlob

txtBlb = TextBlob(sample_text)
clean_text = txtBlb.correct()

print(clean_text.strip())
