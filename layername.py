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


