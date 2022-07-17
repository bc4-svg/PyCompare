from abc import ABC, abstractclassmethod,ABCMeta
from distutils.command.config import config


class INodeReader():
    @abstractclassmethod
    def readPropByIndex():
        """
        function that returns the index node
        """
        pass
    @abstractclassmethod
    def findPropByIdName():
        """
        function that returns the parent node it can be found in
        """
        pass


def getAttributePathByName(configRootNode,attributeName):
    """
    finds the path of an attributeName by name_alias
    """
    path=""
    if(type(configRootNode)==dict):
        configRootNode=configRootNode["props"]
    for configNode in configRootNode:
        print("now checking",configNode)
        if("name" in configNode):
            if(configNode["name"]==attributeName):
                path+="/"+configNode["name_alias"]
                break
            else:
                if("props" in configNode):
                    var=getAttributePathByName(configNode["props"],attributeName)
                    if(len(var)):
                        print(len(var),var)
                        path+="/"+configNode["name_alias"]+"/"
                        break
                    else:
                        continue
        else:
            raise SyntaxWarning("Please update your props because dataset_name is not set in",path+"\ncontinueing with other nodes")
    if(len(path)==0):
        raise Warning("Could not find the requested attributeName:",attributeName)
    print(path,"!!!!!!!!!!!")
    return path
