#Stemming
#use to find out the stem of the word
#PorterStemmer is the most popular Stemmer to be used
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
print(stemmer.stem('Working'))
print(stemmer.stem('Worked'))

#------------------------------------------------------
#SnowballStemmer is support 13 type of language
#print(SnowballStemmer.languages)
#'danish', 'dutch', 'english', 'finnish', 'french', 'german', 'hungarian', 'italian', 'norwegian', 'porter', 'portuguese', 'romanian', 'russian', 'spanish', 'swedish'
from nltk.stem import SnowballStemmer

french_stemmer = SnowballStemmer('french')
print(french_stemmer.stem("French word"))

#----------------------------------
#Different between a Stemmer and WordNet

stem = PorterStemmer()
print(stem.stem('increases'))

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('increases'))
#Stemmer would find the stem(real word)
#but WordNetLemmatizer would find the synonyms

#---------------------------------
#Find the verb, noun, adjective and relative
#This could be the best way to cut off
#or can be said as minimize the scope of 
#the script
#as you have specify what type of the
#word that you want it to be
find = WordNetLemmatizer()
print(find.lemmatize('playing', pos='v'))
print(find.lemmatize('playing', pos='n'))
print(find.lemmatize('playing', pos='a'))
print(find.lemmatize('playing', pos='r'))

#----------------------------------------
#Difference between Stemmer and WordNet
#Stemmer is faster but it does not care of the spelling
#WordNet would be slower but it is accurate as it is finding
#the synonym, but never get spelling wrong

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
print(stemmer.stem('stones'))
print(stemmer.stem('speaking'))
print(stemmer.stem('bedroom'))
print(stemmer.stem('jokes'))
print(stemmer.stem('lisa'))
print(stemmer.stem('purple'))
print('----------------------')
print(lemmatizer.lemmatize('stones'))
print(lemmatizer.lemmatize('speaking'))
print(lemmatizer.lemmatize('bedroom'))
print(lemmatizer.lemmatize('jokes'))
print(lemmatizer.lemmatize('lisa'))
print(lemmatizer.lemmatize('purple'))