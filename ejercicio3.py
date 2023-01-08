#red ferrocarriles 

{
  'King's Cross': {'type': 'station', 'connections': ['St. Pancras', 'Cambio de agujas 1']},
  'Waterloo': {'type': 'station', 'connections': ['Cambio de agujas 2']},
  'Victoria Train Station': {'type': 'station', 'connections': ['Cambio de agujas 3']},
  'Liverpool Street Station': {'type': 'station', 'connections': ['Cambio de agujas 4']},
  'St. Pancras': {'type': 'station', 'connections': ['King's Cross', 'Cambio de agujas 5']},
  'Cambio de agujas 1': {'type': 'switch', 'connections': ['King's Cross', 'Cambio de agujas 2', 'Cambio de agujas 3', 'Cambio de agujas 4']},
  'Cambio de agujas 2': {'type': 'switch', 'connections': ['Cambio de agujas 1', 'Waterloo', 'Cambio de agujas 5']},
  'Cambio de agujas 3': {'type': 'switch', 'connections': ['Cambio de agujas 1', 'Victoria Train Station', 'Cambio de agujas 6']},
  'Cambio de agujas 4': {'type': 'switch', 'connections': ['Cambio de agujas 1', 'Liverpool Street Station']},
  'Cambio de agujas 5': {'type': 'switch', 'connections': ['St. Pancras', 'Cambio de agujas 2']},
  'Cambio de agujas 6': {'type': 'switch', 'connections': ['Cambio de agujas 3']}
  }


#para encontrar el camino más corto:
class vertice:
    def __init__(self, name,connections, v_type):
        self.name = name
        self.type = v_type
        self.connections = connections

class grafo:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

#camino mas corto 
"King's Cross -> Cambio de agujas 1 -> Cambio de agujas 2 -> Waterloo"



