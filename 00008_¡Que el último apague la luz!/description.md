Ahora que conocimos a los procedimientos podemos modelar casos de alternancia utilizando `not`. Por ejemplo, prender y apagar una luz :bulb::

```python
luz_prendida = True

def apretar_interruptor():
  global luz_prendida
  luz_prendida = not luz_prendida
```

¡Ahora te toca a vos!

> Definí el procedimiento `usar_cierre` para que podamos abrir y cerrar el cierre de una mochila.