import requests

def get_categorias():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    #JSON Lo convierte en lista para iterarlo
    categorias = r.json()
    for categoria in categorias: 
        print(categoria['name'])
    
