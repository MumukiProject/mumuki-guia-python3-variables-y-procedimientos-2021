  
  def test_cargar_termo_con_200_como_argumento_aumenta_en_200_el_agua_del_termo(self):
    global agua_del_termo
    agua_del_termo = 600
    cargar_termo(200)
    self.assertEqual(agua_del_termo, 800)


  def test_cargar_termo_con_500_como_argumento_aumenta_en_500_el_agua_del_termo(self):
    global agua_del_termo
    agua_del_termo = 200
    cargar_termo(500)
    self.assertEqual(agua_del_termo, 700)