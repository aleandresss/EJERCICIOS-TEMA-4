 
    def _init_(self, izq=None, der=None):
        self.izq = izquierda
        self.der = derecha

    def children(self):
        return self.izq, self.der

    def _str_(self):
        return self.izq, self.der

def huffman_arbol_code(nodo, binString=''):
    if type(nodo) is str:
         return {nodo: binString}

    (l, r) = nodo.children()
    d = dict()
    d.update(huffman_arbol_code(l, binString + '0'))
    d.update(huffman_arbol_code(r, binString + '1'))
    return d

def huffman_arbol_decode(message, nodo_raiz, nodo, msgd=''):
    if len(message) == 0:
        print("descodificado: {}".format(msgd))
        return msgd

    if type(nodo) is str:
        msgd = msgd + nodo
        nodo = nodo_raiz

    (l, r) = nodo.children()
    caracter = message[0]

    if len(message) == 1:
        message = ''
    else:
         message = message[1:]

    if caracter == '1':
        huffman_arbol_decode(message, nodo_raiz, r, msgd=msgd)
    else:
        huffman_arbol_decode(message, nodo_raiz, l, msgd=msgd)
     
def creararbol(nodos):
    print(nodos)
    print('\n')
    while len(nodos) > 1:
        (key1, c1) = nodos[0]
        (key2, c2) = nodos[1]
        nodos = nodos[2:]
        nodo = nodo_arbol(key1, key2)
        nodos.append((nodo, c1 + c2))
        nodos = sorted(nodos, key=lambda x: x[1], reverse=False)
        print(nodos)
        print('\n')
    return nodos[0]

tabla = {
    'A':11,
    'B':2,
    'C':4,
    'D':3,
    'E':14,
    'G':3,
    'I':6,
    'L':6,
    'M':3,
    'N':6,
    'O':7,
    'P':4,
    'Q':1,
    'R':10,
    'S':4,
    'T':3,
    'U':4,
    'V':2,
    ' ':17,
    ',':2
}

#para obtener frecuencias
total = sum(tabla.values())
tabla_frecuencia = {k:v/total_tabla for k,v in tabla.items()}
tabla_frecuencia

#para ordenar alfabéticamente
lista_en_orden = sorted(tabla_frecuencia.items(), key=lambda x: x[1], reverse=False)
lista_en_orden

nodo = creararbol(lista_en_orden)
nodo[0].children()

codificacion = huffman_arbol_code(nodo[0])
for i in codificacion:
    print(f'{i} : {codificacion[i]}')

message_1 = "10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"
message_2 = "0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010"

huffman_arbol_decode(message=message_1, nodo_raiz=nodo[0] , nodo=nodo[0], msgd='')

huffman_arbol_decode(message=message_2, nodo_raiz=nodo[0] , nodo=nodo[0], msgd='')
