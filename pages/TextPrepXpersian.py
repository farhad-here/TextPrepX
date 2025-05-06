import streamlit as st
import parsivar as pars
import re

# Define a class for Persian text preprocessing
class PersianText:
    def __init__(self, text, stopwords_file):
        # Original input text
        self.text = text
        # Stopword file provided by user
        self.stopwords_file = stopwords_file

    # Normalize the Persian text using Parsivar
    def normalize(self):
        normalizer = pars.Normalizer()
        return normalizer.normalize(self.text)

    # Remove Persian stopwords from text
    def remove_stopwords(self):
        # Read stopwords from file and decode from bytes to string
        stopwords = set(self.stopwords_file.read().decode('utf-8').splitlines())
        # Normalize first and split into words
        words = self.normalize().split()
        # Filter out words that are in the stopword list
        filtered = [word for word in words if word not in stopwords]
        # Update internal text with filtered content
        self.text = ' '.join(filtered)
        return self.text

    # Sentence tokenization (split text into sentences)
    def tokenize_sentences(self):
        # Apply stopword removal before tokenizing
        self.text = self.remove_stopwords()
        tokenizer = pars.Tokenizer()
        return tokenizer.tokenize_sentences(self.text)

    # Word tokenization (split text into words)
    def tokenize_words(self):
        # Apply normalization before tokenizing
        self.text = self.normalize()
        tokenizer = pars.Tokenizer()
        return tokenizer.tokenize_words(self.text)

    # Apply stemming (reduce words to their base/stem)
    def stem(self):
        self.text = self.tokenize_words()
        stemmer = pars.FindStems()
        stemmed = [stemmer.convert_to_stem(word) for word in self.text]
        self.text = ' '.join(stemmed)
        return self.text

    # Final cleaning: spell check + remove punctuation/numbers + trim whitespaces
    def final_cleaning(self):
        spell = pars.SpellCheck()
        misspelled = self.stem()
        self.text = spell.spell_corrector(misspelled)  # Correct spelling
        self.text = re.sub(r'[^\w\s]', '', self.text)  # Remove punctuation
        self.text = re.sub(r'\d+', '', self.text)      # Remove digits
        self.text = re.sub(r'\s+', ' ', self.text).strip()  # Remove extra spaces
        return self.text


# ========== Streamlit User Interface ==========

# Page title
st.title("📝 Persian Text Preprocessing Tool")

# Info about usage
st.info("This tool is designed to preprocess Persian (Farsi) text. You can upload a Persian text file and a stopword list to clean and process the text step-by-step.")

# Upload a Persian text file (.txt)
uploaded_text_file = st.file_uploader("Upload a Persian text file (.txt)", type=["txt"])

# Or manually enter text
text_input = st.text_area("Or write your text below:")

# Upload the Persian stopwords list
stopwords_file = st.file_uploader("Upload persianstopwords.txt file", type=["txt"])

# If user provided either a file or wrote text, and uploaded stopwords
if (uploaded_text_file or text_input) and stopwords_file:
    # Read uploaded file or text input
    text = uploaded_text_file.read().decode('utf-8') if uploaded_text_file else text_input

    # Create processor object
    processor = PersianText(text, stopwords_file)

    # Display original text (right-to-left aligned)
    st.subheader("📌 Original Text")
    st.markdown(f'<div dir="rtl" style="background-color:#f0f0f0;padding:10px;border-radius:10px;">{text}</div>', unsafe_allow_html=True)

    # Normalize text
    st.subheader("🔧 Normalized Text")
    st.markdown(f'<div dir="rtl" style="background-color:#e7f3fe;padding:10px;border-radius:10px;">{processor.normalize()}</div>', unsafe_allow_html=True)

    # Remove stopwords
    st.subheader("🚫 Stopwords Removed")
    st.markdown(f'<div dir="rtl" style="background-color:#fef9e7;padding:10px;border-radius:10px;">{processor.remove_stopwords()}</div>', unsafe_allow_html=True)

    # Sentence tokenization
    st.subheader("🪪 Tokenized Sentences")
    st.dataframe(processor.tokenize_sentences())

    # Word tokenization
    st.subheader("🔤 Tokenized Words")
    st.dataframe(processor.tokenize_words())

    # Stemming
    st.subheader("🌱 Stemmed Words")
    st.markdown(f'<div dir="rtl" style="background-color:#d5f5e3;padding:10px;border-radius:10px;">{processor.stem()}</div>', unsafe_allow_html=True)

    # Final cleaned output
    st.subheader("✅ Final Cleaned Text")
    st.markdown(f'<div dir="rtl" style="background-color:#d1f2eb;padding:10px;border-radius:10px;">{processor.final_cleaning()}</div>', unsafe_allow_html=True)

# Warn if stopwords file is missing
elif (uploaded_text_file or text_input) and not stopwords_file:
    st.warning("⚠️ Please upload the 'persianstopwords.txt' file to proceed.")
