  
  def test_vaciar_termo_deja_en_0_el_agua_del_termo_si_tenia_500(self):
    global agua_del_termo
    agua_del_termo = 500
    vaciar_termo()
    self.assertEqual(agua_del_termo, 0)

  
  def test_vaciar_termo_deja_en_0_el_agua_del_termo_si_tenia_200(self):
    global agua_del_termo
    agua_del_termo = 200
    vaciar_termo()
    self.assertEqual(agua_del_termo, 0)


  def test_vaciar_termo_deja_en_0_el_agua_del_termo_si_tenia_1000(self):
    global agua_del_termo
    agua_del_termo = 1000
    vaciar_termo()
    self.assertEqual(agua_del_termo, 0)


  def test_vaciar_termo_sigue_dejando_en_0_el_agua_si_ya_estaba_en_0(self):
    global agua_del_termo
    agua_del_termo = 0
    vaciar_termo()
    self.assertEqual(agua_del_termo, 0)

  def test_llenar_termo_deja_en_1000_el_agua_del_termo_si_tenia_inicialmente_80(self):
    global agua_del_termo
    agua_del_termo = 80
    llenar_termo()
    self.assertEqual(agua_del_termo, 1000)

  def test_llenar_termo_deja_en_1000_el_agua_del_termo_si_tenia_inicialmente_180(self):
    global agua_del_termo
    agua_del_termo = 180
    llenar_termo()
    self.assertEqual(agua_del_termo, 1000)

  def test_llenar_termo_deja_en_1000_el_agua_del_termo_si_tenia_inicialmente_840(self):
    global agua_del_termo
    agua_del_termo = 840
    llenar_termo()
    self.assertEqual(agua_del_termo, 1000)