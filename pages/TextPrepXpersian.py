import streamlit as st
import parsivar as pars
import re

class PersianText():
    def __init__(self, text):
        self.text = text

    # Normalization
    def Norm(self):
        normal = pars.Normalizer()
        normalized_text = normal.normalize(self.text)
        return normalized_text

    # Remove stop words
    def stopw(self, stopwords_file):
        try:
            # Read stopwords file
            STOPWORDS = set(stopwords_file.read().decode('utf-8').splitlines())
            words = self.Norm().split()
            filtered = [word for word in words if word not in STOPWORDS]
            self.text = ' '.join(filtered)
            return self.text
        except Exception as e:
            return f"Error: {str(e)}"

    # Tokenize sentence
    def tokenSen(self):
        self.text = self.stopw()
        tokenizer = pars.Tokenizer()
        tokenized_sent = tokenizer.tokenize_sentences(self.text)
        return tokenized_sent

    # Tokenize word
    def tokenWor(self):
        self.text = self.Norm()
        tokenizer = pars.Tokenizer()
        tokenized_word = tokenizer.tokenize_words(self.text)
        return tokenized_word

    # Stemmer
    def stem(self):
        self.text = self.tokenWor()
        stemmer = pars.FindStems()
        stem_token = [stemmer.convert_to_stem(i) for i in self.text]
        self.text = ' '.join(stem_token)
        return self.text

    # Final cleaning (spell check, punctuation removal, etc.)
    def finalCleaning(self):
        try:
            spell = pars.SpellCheck()
            misspelled = self.stem()
            self.text = spell.spell_corrector(misspelled)
            self.text = re.sub(r'[^\w\s]', '', self.text)  # Remove punctuation
            self.text = re.sub(r'\d+', '', self.text)  # Remove numbers
            self.text = re.sub(r'\s+', ' ', self.text).strip()  # Remove extra spaces
            return self.text
        except Exception as e:
            return f"Error: {str(e)}"

'''---'''
'''# Persian Text Preprocessing'''
st.warning("#### Just for Persian")

'''---'''
# Upload file or write
upload_file = st.file_uploader('Drag file here')
write_file = st.text_input('Write something')
stopwords_file = st.file_uploader('Drag and drop the Persian stopwords file (persianstopwords.txt)', type='txt')

if upload_file:
    text = upload_file.read().decode('utf-8')
elif write_file:
    text = write_file

'''---'''
if (upload_file or write_file) and stopwords_file:
    '''## Text Display'''
    html_code = f"""
                <div dir="rtl" style="
