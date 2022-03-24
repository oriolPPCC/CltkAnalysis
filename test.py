from cltk import NLP
vitruvius = " Tum ille: 'Rem a me saepe deliberatam ei multum agitatam requiris. itaque non haesitans respondebo, sed ea dicam quae mihi sunt in promptu, quod ista ipsa de re multum ut dixi et diu cogitavi. nam cum philosophium viderem diligentissime Graecis litteris explicatam, existimavi si qui de nostris eius studio tenerentur, si essent Graecis doctrinis eruditi, Graeca potius quam nostra lecturos, sin a Graecorum artibus et disciplinis abhorrerent, ne haec quidem curaturos, quae sine eruditione Graeca intellegi non possunt. itaque ea nolui scribere quae nec indocti intellegere possent nec docti legere curarent. Vides autem eadem ipse; didicisti enim non posse nos Amafinii aut Rabirii similes esse, qui nulla arte adhibita de rebus ante oculos positis vulgari sermone disputant, nihil definiunt nihil partiuntur nihil apta interrogatione concludunt nullam denique artem esse nec dicendi nec disserendi putant; nos autem praeceptis dialecticorum et oratorum etiam, quoniam utramque vim virtutem esse nostri putant, sic parentes ut legibus verbis quoque novis cogimur uti, qune docti ut dixi a Graecis petere malent, indocti ne a nobis quidem accipient, ut frustra omnis suscipiatur <labor>." 

vitruvius2 = " In nova fert animus mutatas dicere formas corpora; di, coeptis (nam vos mutastis et illas) adspirate meis primaque ab origine mundi ad mea perpetuum deducite tempora carmen! Ante mare et terras et quod tegit omnia caelum"
cltk_nlp = NLP(language="lat")
cltk_doc = cltk_nlp.analyze(text=vitruvius)

#from cltk.data.fetch import FetchCorpus
#corpus_downloader = FetchCorpus(language="lat")
#corpus_downloader.list_corpora
#['example_distributed_latin_corpus', 'lat_text_perseus', 'lat_treebank_perseus', 'lat_text_latin_library', 'phi5', 'phi7', 'latin_proper_names_cltk', 'lat_models_cltk', 'latin_pos_lemmata_cltk', 'latin_treebank_index_thomisticus', 'latin_lexica_perseus', 'latin_training_set_sentence_cltk', 'latin_word2vec_cltk', 'latin_text_antique_digiliblt', 'latin_text_corpus_grammaticorum_latinorum', 'latin_text_poeti_ditalia', 'lat_text_tesserae']
#corpus_downloader.import_corpus("lat_text_latin_library")

#print(cltk_doc)
cltk_tokens = (cltk_doc.tokens)

#cltk_pos = (cltk_doc.pos)
cltk_pos = (cltk_doc.morphosyntactic_features)
aux = 0

for x in cltk_doc.tokens:

    #if cltk_pos[aux] == "VERB":
    print(x)
    print(cltk_pos[aux])
    aux = aux+1


#POS
#print(cltk_doc.pos)
#from cltk.languages.pipelines import LatinPipeline
    #a_pipeline = LatinPipeline()
    #a_pipeline.description
    #'Pipeline for the Latin language'
    #a_pipeline.language
    #Language(name='Latin', glottolog_id='lati1261', latitude=41.9026, longitude=12.4502, dates=[], family_id='indo1319', parent_id='impe1234', level='language', iso_639_3_code='lat', type='a')
    #a_pipeline.language.name
    #'Latin'
    #a_pipeline.processes(text=vitruvius)