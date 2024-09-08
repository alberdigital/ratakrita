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



