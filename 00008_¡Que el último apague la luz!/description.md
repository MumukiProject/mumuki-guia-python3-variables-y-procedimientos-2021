¿Te acordás del operador de negación `not` :thought_balloon: ? Si tengo un booleano representado por `tiene_hambre`, su complemento será `not tiene_hambre`.

Ahora que contamos con variables, podemos usarlo también para modelar casos de alternancia como por ejemplo prender y apagar una luz :bulb::

```python
luz_prendida = True

def apretar_interruptor():
  global luz_prendida
  luz_prendida = not luz_prendida
```

¡Ahora te toca a vos!

> Definí el procedimiento `usar_cierre` para que podamos abrir y cerrar el cierre de una mochila.