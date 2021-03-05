¿Te acordás del operador `not` ? Se lo denomina negación o complemento lógico y sirve para negar un valor booleano.

Si tengo el booleano representado por `tiene_hambre`, el complemento será `not tiene_hambre`.

¿Y esto para qué sirve? :thought_balloon: Por ejemplo, para modelar casos de alternancia como por ejemplo prender y apagar una luz :bulb::

```python
luz_prendida = True

def apretar_interruptor():
  global luz_prendida
  luz_prendida = not luz_prendida
```

¡Ahora te toca a vos!

> Definí el procedimiento `usar_cierre` para que podamos abrir y cerrar el cierre de una mochila.