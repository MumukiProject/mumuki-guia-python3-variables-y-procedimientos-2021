_Todo muy lindo hasta acá, pero ¿por qué se llaman variables si no varian?_ :face_with_raised_eyebrow:

Bueno, es que en realidad si pueden variar :sunglasses: . Veamos un ejemplo:

```python
# inicializamos la variable...
dias_sin_accidentes_con_velocirraptores = 0

# ...y más adelante, la actualizamos
dias_sin_accidentes_con_velocirraptores = dias_sin_accidentes_con_velocirraptores + 1
```

Sin embargo, hay que tener un cuidado particular si trabajamos con variables globales: si queremos modificarlas dentro de una función, deberemos anteponer `global` a su nombre:

```python
# inicializamos la variable al inicio de nuestro programa
dias_sin_accidentes_con_velocirraptores = 0

def pasar_un_dia_normal():
  # indicamos a Python que vamos a realizar modificaciones sobre la variable global
  global dias_sin_accidentes_con_velocirraptores

  # acá adentro la actualizamos
  dias_sin_accidentes_con_velocirraptores = dias_sin_accidentes_con_velocirraptores + 1
```

> Probá en la consola lo siguiente:
>
> * `dias_sin_accidentes_con_velocirraptores`
> * `pasar_un_dia_normal()`
> * `pasar_un_dia_normal()`
> * `pasar_un_dia_normal()`
> * `dias_sin_accidentes_con_velocirraptores`