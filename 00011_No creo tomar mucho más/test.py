
  def test_cargar_500_en_termo_con_200_aumenta_en_500_el_agua_del_termo_y_queda_en_700(self):
    global agua_del_termo
    agua_del_termo = 200
    cargar_termo(500)
    self.assertEqual(agua_del_termo, 700)

  def test_cargar_500_en_termo_con_100_aumenta_en_500_el_agua_del_termo_y_queda_en_600(self):
    global agua_del_termo
    agua_del_termo = 100
    cargar_termo(500)
    self.assertEqual(agua_del_termo, 600)

  def test_cargar_300_en_termo_con_250_aumenta_en_250_el_agua_del_termo_y_queda_en_550(self):
    global agua_del_termo
    agua_del_termo = 300
    cargar_termo(250)
    self.assertEqual(agua_del_termo, 550)