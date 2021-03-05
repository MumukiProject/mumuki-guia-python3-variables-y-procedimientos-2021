  
  def test_el_aumentar_fortuna_duplica_variable_global_pesos_en_mi_billetera(self):
    global pesos_en_mi_billetera
    pesos_en_mi_billetera = 100
    aumentar_fortuna()
    self.assertEqual(pesos_en_mi_billetera, 200)


  def test_el_aumentar_fortuna_se_puede_llamar_muchas_veces(self):
    global pesos_en_mi_billetera
    pesos_en_mi_billetera = 30
    aumentar_fortuna()
    aumentar_fortuna()
    aumentar_fortuna()
    self.assertEqual(pesos_en_mi_billetera, 240)