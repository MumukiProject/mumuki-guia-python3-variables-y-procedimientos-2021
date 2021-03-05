  
  def test_vaciar_termo_deja_en_0_el_agua_del_termo(self):
    global agua_del_termo
    agua_del_termo = 1000
    vaciar_termo()
    self.assertEqual(agua_del_termo, 0)


  def test_llenar_termo_deja_en_1000_el_agua_del_termo(self):
    global agua_del_termo
    agua_del_termo = 80
    llenar_termo()
    self.assertEqual(agua_del_termo, 1000)