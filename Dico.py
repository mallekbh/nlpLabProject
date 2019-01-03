from lxml import etree as xml
from xml.dom import minidom
import requests
from bs4 import BeautifulSoup as bsp
import nltk
from Corpus import Corpus


class Dico:
    def __init__(self,DicoPath, CorpusPath):
        '''  '''
        self.tree = xml.parse(DicoPath)
        self.root = self.tree.getroot()
        self.corpus = Corpus(CorpusPath)
    
    def getSamples(self,term):
        """ returns list of samples for the provided term, empty list if term doesnt exist """
        samples = []
        for child in self.root:
            if(term == child.find("term").text):
                for sample in child.iter("sample"):
                    l = {"text": sample.text, "epoch": sample.attrib["epoch"], "category":sample.attrib["category"] , "title": sample.attrib["title"],"author": sample.attrib["author"]}
                    samples.append(l)
        return samples

    def getDefinition(self,term): 
        """ returns a definition if the term exists, None otherwise """
        if(sleexists(self,term)):
            definition = ""
            for child in self.root:
                if(term == child.find("term").text):
                    definition =  child.find("definition").text
            return definition
        else:
            return None

    def setDefinition(self,term,definition):
        """ 
            returns a booelan: sets the definition for the provided term if it exists and
            returns true, returns false otherwise
        """
        if(exists(self,term)):
            pass  
        else:
            pass

    def addNewEntry(self,term):
        """ returns a boolean: creates a new entry in the dico file and populate it with relative info """

        if(not self.exists(slef,term)):
            text = self.findDescription(term)
            entry = xml.SubElement(self.root,'entry', {'state':'final'})
            element= xml.SubElement(entry, 'term', {})
            element.text = term
            definition = xml.SubElement(entry, 'definition', {})
            definition.text = text
            samples = xml.SubElement(entry, 'samples', {})
            found_samples = self.corpus.findSamples(term)
            for found_sample in found_samples :
                sample = xml.SubElement(samples, 'sample', {'epoch':found_sample.era, 'category':found_sample.cat, 'title':found_sample.title, 'author':found_sample.author})
                sample.text = found_sample.sample
        self.tree.write('dico.xml',encoding="utf-8")
    
    def removeEntry(self,term):
        return False

    def updateEntry(self,term,definition):
        element = None
        for child in self.root:
            if term == child.find("term").text:
                element = child
                print(element)
        element.find("definition").text = definition
        self.tree.write('dico.xml',encoding="utf-8")

    def exists(self,term):
        """ return boolean: true if term exists in dico file, false otherwise """
        for child in root:
            if term == child.find("term").text:
                return True
        return False

    def findDescription(self,term):
        """ to be refactored or moved to another module """
        file = open("test.txt","w")
        source = requests.get("https://www.maajim.com/dictionary/"+term)
        source.encoding = "widows-1256"
        soup = bsp(source.content,"html.parser")
        results = list(soup.select("div.result div.result-detail"))
        return results[2].get_text()

    def findSamples(self,term):
        epochs = os.listdir(path)
    
    # manual mode functions

    def addEntry(self,entry):
        pass

dico = Dico("dico.xml","corpus/")
dico.updateEntry("house","a place to live in")