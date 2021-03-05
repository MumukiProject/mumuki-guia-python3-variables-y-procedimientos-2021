Mirá el siguiente programa con atención :eyes: :

```python
volumen = 40

def subir_volumen(decibeles):
	global volumen
	volumen += decibeles

def bajar_volumen(decibeles):
	global volumen
	volumen -= decibeles

def es_volumen_saludable():
	return volumen <= 75
```

> Marcá las afirmaciones correctas: