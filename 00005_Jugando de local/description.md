Hay veces que no queremos, o simplemente no tiene sentido, que nuestras variables sean accedidas por todas las funciones. Por suerte, podemos inicializar variables tanto directamente en el programa, como dentro de un `def`:

```python
def el_doble_es_mayor_a_diez(numero):
  el_doble = numero * 2
  if el_doble > 10:
    return el_doble
  else:
    return 0
```

Las variables inicializadas dentro de un `def`, conocidas como _variables locales_, no presentan mayor misterio. Sin embargo, hay que tener un particular cuidado :warning: ya que sólo se pueden utilizar dentro del `def` en cuestión. Si quiero referenciarla desde un programa:

```python
el_cuadruple = el_doble * 4
```

Boom, ¡se romperá! :collision:

Sin embargo, las variables inicializadas directamente en el programa, conocidas como _variables globales_, pueden ser leídas desde cualquier `def`. Por ejemplo:

```python
peso_maximo_del_equipaje_en_gramos = 5000

def puede_llevar(peso_equipaje):
  return peso_equipaje <= peso_maximo_del_equipaje_en_gramos
````
 
> Definí la función `` que .....