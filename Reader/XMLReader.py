from .INodeReader import INodeReader, getAttributePathByName
import yaml

from xml.etree.ElementTree import iterparse

class XMLReader(INodeReader):
    def __init__(self,configPath):
        self.configPath=configPath
        self.attributePathes=[] #{name:string,path:string}


    def propertyByIdName(self,name):
        path=(path for path in self.attributePathes if path.name==name)
        if(path):
            self.__addAttributePath(name)
        if(len(path.path)==0):
            raise Warning("skipping "+name+"because path could not be found")
        
        print("ur path",path)
  
        # with open("badge.csv","w") as csvout:
        #     for event, elem in iterparse("badges.xml"):
        #         if event == 'end' and elem.tag == 'row': # Complete row tag
        #             # some processing here
        #             csv_out.write(line)
        #             elem.clear()

    def __addAttributePath(self,name):
        print("this is was what was loaded",yaml.safe_load(open(self.configPath,"r")))
        path=getAttributePathByName(yaml.safe_load(open(self.configPath,"r")),name)
        self.attributePathes.append({name:name,path:path})
        
