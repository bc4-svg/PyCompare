import yaml


class PyCompare:
    @staticmethod
    def compare(configFiles=[""]):
        compareNodes=PyCompare._createCompareConfig(configFiles)
        print("these values will be compared",compareNodes)
    
    @staticmethod
    def _createCompareConfig(configFiles):
        compareNodes=[]
        for configPath in configFiles:
            config=yaml.load(open(configPath,"r"))
            try:
                compareNodes=PyCompare.__extractCompareConfig(config["props"])
            except yaml.YAMLError as e:
                print("The config you provided is not valid:",e)
        return compareNodes

    @staticmethod
    def __extractCompareConfig(configNodes):
        """
        returns a list of toCompare Node keywords
        """
        if(type(configNodes)!=list):
            raise TypeError("type of props should be array/list")
        compareNames=[]
        for node in configNodes:
            if(node["bCompare"]):
                compareNames.append(node["name"])
            if("props" in node):
                compareNames+=PyCompare.__extractCompareConfig(node["props"])
        return compareNames