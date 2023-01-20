  
  def test_al_principio_el_agua_del_termo_esta_en_1000(self):
    self.assertEqual(agua_del_termo, 1000, "el agua del termo debe inicializarse en 1000")

  def test_cebar_mate_disminuye_en_30_ml_el_agua_del_termo(self):
    global agua_del_termo
    agua_del_termo = 1000
    cebar_mate()
    self.assertEqual(agua_del_termo, 970)


  def test_cebar_3_mates_disminuye_en_90_ml_el_agua_del_termo(self):
    global agua_del_termo
    agua_del_termo = 1000
    cebar_mate()
    cebar_mate()
    cebar_mate()
    self.assertEqual(agua_del_termo, 910)
    
    
      