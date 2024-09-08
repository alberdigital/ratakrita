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

