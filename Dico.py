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
        self.periods = {"1pre_islamic_era":"العصر الجاهلي", "2islamAndAmaoui_era":"العصر الأموي", "3Abbasi_era":"العصر العباسي", "4modern_era":"العصر الحديث"}
        self.types = {"poem":"الشعر", "prose":"النثر"}
        
    
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
        if(exists(self,term)):
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

        if(not self.exists(term)):
            text = self.findDescription(term)
            entry = xml.SubElement(self.root,'entry', {'state':'final'})
            element= xml.SubElement(entry, 'term', {})
            element.text = term
            definition = xml.SubElement(entry, 'definition', {})
            definition.text = text
            samples = xml.SubElement(entry, 'samples', {})
            found_samples = self.corpus.createSamples(term)
            for found_sample in found_samples :
                print(found_sample)
                sample = xml.SubElement(samples, 'sample', {'epoch':found_sample["epoch"], 'category':found_sample["cat"], 'title':found_sample['title'], 'author':found_sample["author"]})
                sample.text = found_sample["sample"]
        self.tree.write('dico.xml',encoding="utf-8")
    
    def removeEntry(self,term):
        return False

    def getEntry(self,term):
        element = None
        for child in self.root:
            if term == child.find("term").text:
                element = child
        return element

    def updateEntry(self,term,definition):
        element = None
        for child in self.root:
            if term == child.find("term").text:
                element = child
        element.find("definition").text = definition
        self.tree.write('dico.xml',encoding="utf-8")

    def exists(self,term):
        """ return boolean: true if term exists in dico file, false otherwise """
        for child in self.root:
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
    
    def FindEntry(self,entry,periodFilter,typeFilter):
        """ return samples for requested entry following search filters """
        
        result = {"definition":"", "samples":""}
        element = self.getEntry(entry)
        result['definition'] = element.find("definition").text
        samples = element.find("samples").findall("sample")
        output = open("output.txt","w")
        if(len(periodFilter) == 0):
            if(len(typeFilter) == 0):
                for sample in samples:
                    result['samples'] += "العنوان: "+sample.attrib["title"]+"\t"+"الكاتب: "+sample.attrib["author"]+"\t"+"العصر: "+self.periods[sample.attrib["epoch"]]+"\t"+"النوع: "+self.types[sample.attrib['category']]+"\n\n"
                    result["samples"] += result["samples"]+sample.text+"\n\n\n"     
            else:
                for sample in samples:
                    if(sample.attrib['type'] in typeFilter):
                        result['samples'] += "العنوان:"+sample.attrib["title"]+"\t"+"الكاتب:"+sample.attrib["author"]+"\t"+"العصر:"+self.periods[sample.attrib["epoch"]]+"النوع:"+self.types[sample.attrib['category']]+"\n\n"
                        result["samples"] += result["samples"]+sample.text+"\n\n\n"
        else:
            if(len(typeFilter) == 0):
                for sample in samples:
                    if(sample.attrib['epoch'] in periodFilter):
                        result['samples'] += "العنوان:"+sample.attrib["title"]+"\t"+"الكاتب:"+sample.attrib["author"]+"\t"+"العصر:"+self.periods[sample.attrib["epoch"]]+"النوع:"+self.types[sample.attrib['category']]+"\n\n"
                        result["samples"] += result["samples"]+sample.text+"\n\n\n"
                        output.write(result["samples"])
            else:
                for sample in samples:
                    if(sample.attrib['epoch'] in periodFilter and sample.attrib["type"] in typeFilter):
                        result['samples'] += "العنوان:"+sample.attrib["title"]+"\t"+"الكاتب:"+sample.attrib["author"]+"\t"+"العصر:"+self.periods[sample.attrib["epoch"]]+"النوع:"+self.types[sample.attrib['category']]+"\n\n"
                        result["samples"] += result["samples"]+sample.text+"\n\n\n"
        output.close()
        return result

dico = Dico("dico.xml","corpus/")
dico.FindEntry("الفراش",["1pre_islamic_era"],[])
