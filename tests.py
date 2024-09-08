from combinationcounter import CombinationCounter
from layername import LayerName

class KritaNodeMock:
    _child_nodes = []
    _name = ''
    
    def setName(self, name):
        self._name = name

    def name(self):
        return self._name
    
    def childNodes(self):
        return self._child_nodes
    
kGroups = []

kGroup0 = KritaNodeMock()
kGroup0.setName('Group 0')
kGroups.append(kGroup0)

kLayer00 = KritaNodeMock()
kLayer00.setName('Layer 00')
kGroup0.childNodes().append(kLayer00)

kLayer01 = KritaNodeMock()
kLayer01.setName('Layer 01')
kGroup0.childNodes().append(kLayer01)

kGroup1 = KritaNodeMock()
kGroup1.setName('Group 1')
kGroups.append(kGroup1)

kLayer10 = KritaNodeMock()
kLayer10.setName('Layer 10')
kGroup1.childNodes().append(kLayer10)

kLayer11 = KritaNodeMock()
kLayer11.setName('Layer 11')
kGroup1.childNodes().append(kLayer11)


combinationCounter = CombinationCounter(kGroups);