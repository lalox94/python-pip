import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('datos.csv')

  #MUESTRA GRAFICO DEL PORCENTAJE DE LOS PAISES DE SUDAMERICA
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)


  #MUESTRA GRAFICO DE LA POBLACION DE UN PAIS A TRAVES DE LOS AÑOS
  country = input('Escribe pais => ')
  result = utils.population_by_country(data, country)
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)


'''
Permite ejecutar el archivo como un script
Al ejecutarlo desde la consolta realizara lo que se tiene dentro
Si se llama desde otro archivo se debe ejecutar mediante una funcion

PUNTO DE ENTRADA
'''
if __name__ == '__main__':
  run()
  