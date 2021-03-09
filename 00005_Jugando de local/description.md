Hay veces que no queremos, o simplemente no tiene sentido, que nuestras variables sean accedidas por todas las funciones. Por suerte, podemos inicializar variables tanto directamente en el programa, como dentro de un `def`:

```python
def el_mas_largo_sin_espacios(un_string, otro_string):
  #str.strip retorna un nuevo string sin espacios al principio ni al final
  un_string_sin_espacios = str.strip(un_string)
  otro_string_sin_espacios = str.strip(otro_string)
  if(len(un_string_sin_espacios) > len(otro_string_sin_espacios)):
    return un_string_sin_espacios
  else:
    return otro_string_sin_espacios
```

Las variables inicializadas dentro de un `def`, conocidas como _variables locales_, no presentan mayor misterio. Sin embargo, hay que tener un particular cuidado :warning: ya que sólo se pueden utilizar dentro del `def` en cuestión. Si quiero referenciarla desde un programa...

```python
pregunta = "¿" + un_string_sin_espacios + "?"
```

...¡boom! ¡se romperá! :collision:

Sin embargo, las variables inicializadas directamente en el programa, conocidas como _variables globales_, pueden ser leídas desde cualquier `def`. Por ejemplo:

```python
peso_maximo_del_equipaje_en_gramos = 5000

def puede_llevar(peso_equipaje):
  return peso_equipaje <= peso_maximo_del_equipaje_en_gramos
````
 
> Definí la función `` que .....