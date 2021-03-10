def saludar_a(quien, horario):
  if horario < 12:
    return "¡Buenos días " + quien + "!"
  elif horario < 19:
    return "¡Buenas tardes " + quien + "!"
  else: 
    return "¡Buenas noches " + quien + "!"