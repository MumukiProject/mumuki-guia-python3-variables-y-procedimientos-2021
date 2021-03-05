  
  def test_el_perimetro_de_un_circulo_de_radio_1_es_correcto(self):
    self.assertEqual(perimetro_circulo(1), 6.28318530717958)
  
  def test_el_perimetro_de_un_circulo_de_radio_2_es_correcto(self):
    self.assertEqual(perimetro_circulo(2), 12.56637061435916)
  
  def test_el_perimetro_de_un_circulo_de_radio_0_es_correcto(self):
    self.assertEqual(perimetro_circulo(0), 0)
  
  def test_el_area_de_un_circulo_de_radio_1_es_correcto(self):
    self.assertEqual(area_circulo(1), 3.14159265358979)
  
  def test_el_area_de_un_circulo_de_radio_2_es_correcto(self):
    self.assertEqual(area_circulo(2), 12.56637061435916)
  
  def test_el_area_de_un_circulo_de_radio_0_es_correcto(self):
    self.assertEqual(area_circulo(0), 0)

