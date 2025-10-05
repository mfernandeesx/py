import json 

dicionario = {
    'nome': 'Lucas',
    'idade': 22,
    'cidade': 'curitiba',
}
object_json = json.dumps(dicionario, indent=2)
with open('dicionario.json', 'w') as file:
    file.write(object_json)
    
    
    
