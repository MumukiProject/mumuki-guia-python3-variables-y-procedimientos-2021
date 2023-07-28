  
  def test_cebar_mate_disminuye_en_30_ml_el_agua_del_termo(self):
    global agua_del_termo
    agua_del_termo = 1000
    cebar_mate()
    self.assertEqual(agua_del_termo, 970, "si agua_del_termo está en 1000, luego de invocar cebar_mate(), agua_del_termo debe quedar en 970")

  def test_cebar_3_mates_disminuye_en_90_ml_el_agua_del_termo(self):
    global agua_del_termo
    agua_del_termo = 1000
    cebar_mate()
    cebar_mate()
    cebar_mate()
    self.assertEqual(agua_del_termo, 910, "si agua_del_termo está en 1000, el luego de invocar 3 veces cebar_mate(), agua_del_termo debe quedar en 910")
    
  def test_cebar_mate_aumenta_en_30_ml_el_agua_del_mate(self):
    global agua_del_mate
    agua_del_mate = 0
    cebar_mate()
    self.assertEqual(agua_del_mate, 30, "si agua_del_mate está en 0, luego de invocar cebar_mate(), agua_del_mate debe quedar en 30")
    
  def test_tomar_mate_deja_en_0_ml_el_agua_del_mate(self):
    global agua_del_mate
    agua_del_mate = 20
    tomar_mate()
    self.assertEqual(agua_del_mate, 0, "si agua_del_mate está en 20, luego de invocar tomar_mate(), agua_del_mate debe quedar en 0")