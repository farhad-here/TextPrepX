import streamlit as st
#library
# from bidi.algorithm import get_display
# import arabic_reshaper
import parsivar as pars
import re



class PersianText():
       def __init__(self,text):
              self.text = text

    
       #normalize
       def Norm(self):
              #Normalizer
              normal = pars.Normalizer()
              normalized_text = normal.normalize(self.text)
              #fixing display of persian text in output
              # reshaped_text = arabic_reshaper.reshape(normalized_text)
              # bidi_text = get_display(reshaped_text)
              return normalized_text
       def stopw(self):
              f = psw
              STOPWORDS = set(f.read().decode('utf-8').splitlines())
              words = self.Norm().split()
              filtered = [word for word in words if word not in STOPWORDS]
              self.text = ' '.join(filtered)
              return self.text
       def tokenSen(self):
              #tokenize
              self.text = self.stopw()
              tokenizer = pars.Tokenizer()
              tokenized_sent = tokenizer.tokenize_sentences(self.text)
              return tokenized_sent
       def tokenWor(self):
              self.text = self.Norm()
              tokenizer = pars.Tokenizer()
              tokenized_word = tokenizer.tokenize_words(self.text)
              return tokenized_word
       #stemmer
       def stem(self):
              #Stemmer
              self.text = self.tokenWor()
              stemmer = pars.FindStems()
              stem_token = [stemmer.convert_to_stem(i) for i in self.text]
              self.text = ' '.join(stem_token)
              return self.text
       
       # check spell and punc and remove numbers and etc
       def finalCleaning(self):
              # spell = pars.SpellCheck()
              # misspeled = self.stem()
              self.text = spell.spell_corrector(misspeled)
              self.text = re.sub(r'[^\w\s]', '',self.text)
              self.text = re.sub(r'\d+', '', self.text)
              self.text = re.sub(r'\s+', ' ', self.text).strip()

              return ''.join(self.text)  
               
'''---'''
'''# Persian Text preprocessing'''
st.warning("#### Just for Persian")

'''---'''
'''# Upload file or write'''
upload_file = st.file_uploader('drag file here')
'''### or'''
write_file = st.text_input('write something')
if upload_file:
       text = upload_file.read().decode('utf-8')
elif write_file:
       text = write_file
'''---'''
if upload_file or write_file:
       '''## Text'''
       html_code = f"""
                     <div dir="rtl" style="
                     background-color: #3b2f2f;
                     padding: 16px;
                     border-radius: 10px;
                     border: 1px solid #a67c52;
                     color: #ffd580;
                     font-family: 'monospace', sans-serif;
                     font-size: 24px;
                     line-height: 1.8;
                     ">
                     {text}
                     </div>
                     """
       st.markdown(html_code, unsafe_allow_html=True)
    
       '''---'''
       oop =PersianText(text)
       '''## Normalize'''
       html_code = f"""
                     <div dir="rtl" style="
                     background-color: #3b2f2f;
                     padding: 16px;
                     border-radius: 10px;
                     border: 1px solid #a67c52;
                     color: #ffd580;
                     font-family: 'monospace', sans-serif;
                     font-size: 24px;
                     line-height: 1.8;
                     ">
                     {oop.Norm()}
                     </div>
                     """
       st.markdown(html_code, unsafe_allow_html=True)
       '''---'''
       '''## StopWord in persian'''
       try:
              psw = st.file_uploader('drag persianstopwords.txt')
              html_code = f"""
                     <div dir="rtl" style="
                     background-color: #3b2f2f;
                     padding: 16px;
                     border-radius: 10px;
                     border: 1px solid #a67c52;
                     color: #ffd580;
                     font-family: 'monospace', sans-serif;
                     font-size: 24px;
                     line-height: 1.8;
                     ">
                     {oop.stopw()}
                     </div>
                     """
              st.markdown(html_code, unsafe_allow_html=True)
              '''---'''
              '''# Tokenize word and sent'''


              '''#### sentence'''
              st.dataframe(oop.tokenSen())
              '''#### word'''
              st.dataframe(oop.tokenWor())
              
              '''---'''
              '''## Stem'''
              html_code = f"""
              <div dir="rtl" style="
              background-color: #3b2f2f;
              padding: 16px;
              border-radius: 10px;
              border: 1px solid #a67c52;
              color: #ffd580;
              font-family: 'monospace', sans-serif;
              font-size: 24px;
              line-height: 1.8;
              ">
              {oop.stem()}
              </div>
              """
              st.markdown(html_code, unsafe_allow_html=True)
              '''---'''
              '''## Result'''
              html_code = f"""
              <div dir="rtl" style="
              background-color: #3b2f2f;
              padding: 16px;
              border-radius: 10px;
              border: 1px solid #a67c52;
              color: #ffd580;
              font-family: 'monospace', sans-serif;
              font-size: 24px;
              line-height: 1.8;
              ">
              {oop.finalCleaning()}
              </div>
              """
              st.markdown(html_code, unsafe_allow_html=True)
       


       except:
              st.warning('# You forgot to drag and drop persianstopwords.txt')
       

 
