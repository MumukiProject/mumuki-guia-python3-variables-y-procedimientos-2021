_Todo muy lindo hasta acá, pero ¿por qué se llaman variables si no varian?_ :face_with_raised_eyebrow:

Bueno, es que en realidad si pueden variar :sunglasses: . Veamos un ejemplo:

```python
# inicializamos la variable para que valga 0...
dias_sin_accidentes_con_velocirraptores = 0

# ...y más adelante, la actualizamos
dias_sin_accidentes_con_velocirraptores = dias_sin_accidentes_con_velocirraptores + 1

# ¡ahora vale 1!
dias_sin_accidentes_con_velocirraptores
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

> Probá en la consola, en orden, lo siguiente:
>
> 1. `dias_sin_accidentes_con_velocirraptores`
> 2. `pasar_un_dia_normal()`
> 3. `pasar_un_dia_normal()`
> 4. `pasar_un_dia_normal()`
> 5. `dias_sin_accidentes_con_velocirraptores`

> Podés usar las flechas de tu teclado para navegar entre comandos ejecutados previamente. :arrow_up_small: :arrow_down_small: