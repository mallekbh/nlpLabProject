import nltk
import requests
from arabicstemmer.arabic_stemmer import ArabicStemmer as ArabStemmer
import re
import os
from lxml import etree as xml
from xml.dom import minidom
from bs4 import BeautifulSoup as bsp

class Corpus:
    def __init__(self,path):
        self.path = path
        self.epochs = os.listdir(path)
        self.cats = []
        for epoch in self.epochs:
            for cat in os.listdir(path+"/"+epoch):
                self.cats.append(cat)
        self.cats = set(self.cats)

    def file_ids(self, epochs=[], categories=[]):
        """ 
            returns files names from the corpus folder, search by epoch/category
            {'epoch1': {'cat1': ['file1',...,'filen]},...,'epochn':{'cat1': ['file1',...,'filen]}}
        """
        output = []
        if(len(epochs)==0 and len(categories) == 0):
                for epoch in self.epochs:
                    for cat in self.cats:
                        files = os.listdir(self.path+"/"+epoch+"/"+cat+"/")
                        for file in files:
                            output.append(file)
        elif(len(epochs) > 0):
            if(len(categories) > 0):
                for epoch in set(epochs):
                    for cat in set(categories):
                        files = os.listdir(self.path+"/"+epoch+"/"+cat+"/")
                        for file in files:
                            output.append(file)
            else:
                for epoch in set(epochs):
                    for cat in self.cats:
                        files = os.listdir(self.path+"/"+epoch+"/"+cat+"")
                pass
                #retuns all files ids for all categories for given epochs
        return output

    # def get_sents(self, epochs=[], categories=[]):
    #     ''' returns list of sents from the corpus, search by epoch/category '''
    #      output = []
    #     if(len(epochs)==0 and len(categories) == 0):
    #             for epoch in self.epochs:
    #                 for cat in self.cats:
    #                     files = os.listdir(self.path+"/"+epoch+"/"+cat+"/")
    #                     for file in files:
    #                         output.append(file)
    #     elif(len(epochs) > 0):
    #         if(len(categories) > 0):
    #             for epoch in set(epochs):
    #                 for cat in set(categories):
    #                     files = os.listdir(self.path+"/"+epoch+"/"+cat+"/")
    #                     for file in files:
    #                         output.append(file)
    #         else:
    #             for epoch in set(epochs):
    #                 for cat in self.cats:
    #                     files = os.listdir(self.path+"/"+epoch+"/"+cat+"")
    #             pass
    #             #retuns all files ids for all categories for given epochs
    #     return output
    
    def createSamples(self,term):
        """ returns a list of samples for the given term """
        output = open("output.txt","w")
        results = []
        pattern = re.compile('(^(.)*?'+term+'(.)*?$)')
        stemmer = ArabStemmer()
        for era in self.epochs:
            for cat in self.cats:
                files = os.listdir('corpus/'+era+'/'+cat+"/")
                for file in files:
                    root = xml.parse('corpus/'+era+'/'+cat+"/"+file).getroot()
                    elements = root.findall('element')
                    for element in elements:
                        lines = element.findall('line')
                        for line in lines:
                            #useing a regular expression
                            # if(pattern.match(line.text)):
                            #     results.append({'cat':cat,'title':element.attrib['title'], 'author':element.attrib['author'], 'sample':line.text})
                            #     output.write('cat : '+cat+" "+"author : "+element.attrib['author']+" title: "+era+" "+line.text+"\n")
                            #using a stemming procedure
                            #tokens = [stemmer.stemWord(token) for token in nltk.word_tokenize(line.text)]
                            tokens = stemmer.stemWords(nltk.word_tokenize(line.text))
                            if(stemmer.stemWord(term) in tokens):
                                results.append({'cat':cat,'title':element.attrib['title'], 'author':element.attrib['author'], 'sample':line.text})
        return results

   