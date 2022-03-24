# Installation Set-up:
from cltk import NLP
import os
from unicodedata import normalize
#bondia
def analitzar (txt):
    #cltk_nlp = NLP(language="lat")
    #cltk_doc = cltk_nlp.analyze(text=txt)
    #cltk_tokens = (cltk_doc.tokens)
    #....
    print(txt)

def buscar_textos(path, all_files):
    for it in all_files:
        path_aux = path + "/" + it 
        if ".git" in it:
            print("Atenció aquest va malament: " + path_aux)
        elif ".txt" in it:
            text = llegir(path_aux)
            print(path_aux)
            analitzar(text)
        else:
            all_files_aux = os.listdir(path_aux)
            buscar_textos(path_aux,all_files_aux)
    

def llegir (path):
    
    with open(path, 'r', encoding='utf-8') as f: 
        test_1 = f.read()
        return test_1 

path = "../cltk_data/lat/text/lat_text_latin_library"
all_files = os.listdir(path)
buscar_textos(path, all_files)
#print(all_files)

