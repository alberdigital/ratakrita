import re
import json
from krita import *
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLineEdit, QPushButton
class LayerName:
    
    layer_name = ''

    def __init__(self, layer_name):
        self.layer_name = layer_name

    
    def extract_cats(self):
        """ Extrae las categorías a las que pertenece una capa. 
        Las categorías están definidas en el nombre de la capa, con el formato:
        <nombre arbitrario>#<título categoría 1>:<valor categoría 1>|<título categoría 2>:<valor categoría 2>|...
        Añade el resultado a un diccionario en la siguiente forma:
        {
            <título categoría 1>: <valor categoría 1>,
            <título categoría 2>: <valor categoría 2>
        }

        layer_name : str 
            Nombre de la capa, con el formato previsto.
        cats : array
            Objeto al que se añadirán las categorías.
        """
    
        cats = {}
        if '#' in self.layer_name:
            name_cats = self.layer_name.split('#').pop().split('|')
            for name_cat in name_cats:
                name_cat_parts = name_cat.split(':')
                cats[name_cat_parts[0]] = name_cat_parts[1]

        return cats


    def extract_brackets_content(self):
        result = re.findall(r'\[(.*?)\]', self.layer_name)
        if len(result) > 0:
            # Devuelve el texto entre corchetes
            return result[0]
        else:
            # Si no se encuentra texto entre corchetes, devuelve None
            return None



class CombinationCounter:

    num_groups = 0
    groups = []
    random_generated_log = []
    combination_log = []
    
    def __init__(self, k_groups):
        
        for g, k_group in enumerate(k_groups):
            layers = []

            for l, k_layer in enumerate(k_group.childNodes()):
                layer_name = k_layer.name()

                # Extrae el peso de cada capa.
                weight_str = LayerName(layer_name).extract_brackets_content()
                weight = 1 if weight_str is None else int(weight_str)

                layers.append({
                    'index': l,
                    'layer_name': layer_name,
                    'weight': weight,
                    'cats': LayerName(layer_name).extract_cats()
                })
            

            self.groups.append({
                'group_name': k_group.name(),
                'current_layer': 0,
                'layers': layers
            })
    
    def reset(self):
        for group in self.groups:
            group.currentLayer = 0

    def categories_are_compatible(self, cats1, cats2):
        # Comprueba si las categorías de cat2 son compatibles con las de cat1.
        combination_is_valid = True
        for cat_title in cats2:
            if cat_title in cats1 and cats1[cat_title] != cats2[cat_title]:
                # La combinación no es válida.
                combination_is_valid = False
                break
        return combination_is_valid

        
    def to_string(self):
        group_strs = []
        for group in self.groups:
            group_strs.append(group['group_name'] + ": " + str(group['current_layer']) + "/" + str(len(group['layers']) - 1))
        
        return ', '.join(group_strs)

    def to_json(self):
        return json.dumps(self.groups)


# Número máximo de intentos de obtener una combinación no generada previamente.
MAX_ATTEMPTS_TO_GET_A_NEW_COMBINATION = 1000

# Número máximo de combinaciones que se pueden contar. A partir de este número no se informará
# de las combinaciones válidas.
MAX_VALID_COMBINATIONS_TO_COUNT = 500

def show_options_dialog():
    
    wLayout = QHBoxLayout()
    collectionNameInput = QLineEdit()
    collectionNameInput.setPlaceholderText("Collection name")
    wLayout.addWidget(collectionNameInput)

    w = QDialog()
    w.setWindowTitle('New collection')
    w.setLayout(wLayout)

    w.exec_()

  
def main():
    application = Krita.instance()
    currentDoc = application.activeDocument()

    kGroups = currentDoc.topLevelNodes()

    combination_counter = CombinationCounter(kGroups)

    print(combination_counter.to_string())

    show_options_dialog()


    # Pruebas:
    compatible = combination_counter.categories_are_compatible(
            combination_counter.groups[2]['layers'][0]['cats'], 
            combination_counter.groups[3]['layers'][2]['cats'])

    print('cat1: ' + combination_counter.groups[2]['layers'][0]['layer_name'])
    print('cat2: ' + combination_counter.groups[3]['layers'][2]['layer_name'])

    print('compatible? ' + str(compatible))




