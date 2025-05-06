import streamlit as st
import parsivar as pars
import re
import os
import zipfile
import requests

# === Download spell check model ===
def download_and_extract_spell_data():
    url = "https://www.dropbox.com/scl/fi/4lspgdqw0yym6w2ewhcs7/spell.zip?rlkey=fl0moighiw7s46pgorz1xjtg0&dl=1"
    dest_folder = "resources"
    zip_path = os.path.join(dest_folder, "spell.zip")

    os.makedirs(dest_folder, exist_ok=True)

    if not os.path.exists(os.path.join(dest_folder, "mybigram_lm.pckl")):
        with requests.get(url, stream=True) as r:
            with open(zip_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(dest_folder)

        os.remove(zip_path)

download_and_extract_spell_data()

# === Text Preprocessing Class ===
class PersianText:
    def __init__(self, text, stopwords_list):
        self.text = text
        self.stopwords_set = set(stopwords_list)

    def normalize(self):
        normalizer = pars.Normalizer()
        return normalizer.normalize(self.text)

    def remove_stopwords(self):
        normalized = self.normalize()
        words = normalized.split()
        filtered = [word for word in words if word not in self.stopwords_set]
        self.text = ' '.join(filtered)
        return self.text

    def tokenize_sentences(self):
        tokenizer = pars.Tokenizer()
        return tokenizer.tokenize_sentences(self.text)

    def tokenize_words(self):
        tokenizer = pars.Tokenizer()
        return tokenizer.tokenize_words(self.text)

    def stem(self):
        tokens = self.tokenize_words()
        stemmer = pars.FindStems()
        stemmed = [stemmer.convert_to_stem(word) for word in tokens]
        self.text = ' '.join(stemmed)
        return self.text

    def final_cleaning(self):
        spell = pars.SpellCheck()
        corrected = spell.spell_corrector(self.text)
        cleaned = re.sub(r'[^\w\s]', '', corrected)
        cleaned = re.sub(r'\d+', '', cleaned)
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()
        return cleaned

# === Streamlit App ===
st.title("🔤 Persian Text Preprocessing App")
st.warning("This app is only for Persian text")

uploaded_text_file = st.file_uploader("Upload a .txt file with Persian text", type=["txt"])
manual_text = st.text_input("Or type your Persian text here")

if uploaded_text_file or manual_text:
    if uploaded_text_file:
        input_text = uploaded_text_file.read().decode('utf-8')
    else:
        input_text = manual_text

    st.markdown("### 📝 Original Text")
    st.markdown(f"<div dir='rtl' style='background:#222;padding:10px;color:#ffd580;border-radius:10px'>{input_text}</div>", unsafe_allow_html=True)

    stopwords_file = st.file_uploader("Upload `persianstopwords.txt`", type=["txt"])
    if stopwords_file:
        # FIX: read the file contents before decoding
        stopwords_text = stopwords_file.read().decode("utf-8").splitlines()
        pt = PersianText(input_text, stopwords_text)

        st.markdown("### 🔧 Normalized")
        st.markdown(pt.normalize(), unsafe_allow_html=True)

        st.markdown("### ✂️ Stopwords Removed")
        st.markdown(pt.remove_stopwords(), unsafe_allow_html=True)

        st.markdown("### 📚 Tokenized Sentences")
        st.dataframe(pt.tokenize_sentences())

        st.markdown("### 🧩 Tokenized Words")
        st.dataframe(pt.tokenize_words())

        st.markdown("### 🧬 Stemmed")
        st.markdown(pt.stem(), unsafe_allow_html=True)

        st.markdown("### ✅ Final Cleaned Result")
        st.markdown(pt.final_cleaning(), unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please upload `persianstopwords.txt`")
