import csv 
def read_csv(path):
  #ABRIR ARCHIVO CON PERMISOS DE LECTURA
  with open(path, 'r') as csvfile:
    #MUESTRA LOS DATOS DEL ARCHIVO OCUPANDO EL METODO READER DE LA LIBRIA CSV LOS PARAMETROS SON EL ARCHIVO Y EL DELIMITADOR 
    reader = csv.reader(csvfile, delimiter = ',')
    #OBTIENE LA PRIMERA LINEA DEL ARCHIVO
    header = next(reader) 
    data = []
    for row in reader:
     #UNE EL HEADER Y LA FILA EN UNA SOLO EN UN ARRAY DE TUPLAS PRIMERA POSICION LA COLUMNA, LA SEGUNDA EL ROW
      #zip : une uno o mas iterable y cada union resulta una tupla
      iterable = zip(header, row)
      #CONVIERTE LA LISTA ANTERIOR EN UN DICCIONARIO OBTENIENDO LA LLAVE VALOR DE ITERABLE
      country_dict = {key: value for key, value in iterable}
      #AGREGA UNA 
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/datos.csv')
  print(data)