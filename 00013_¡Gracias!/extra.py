agua_del_mate = 0
agua_del_termo = 1000

def cebar_mate():
  global agua_del_mate
  global agua_del_termo
  agua_del_termo -= 30
  agua_del_mate += 30
  
def tomar_mate():
  global agua_del_mate
  agua_del_mate = 0
  
def pasar():
  pass