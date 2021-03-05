  
  def test_ascensor_sobrecargado_4_con_peso_promedio_persona_en_kilogramos_70(self):
    global peso_promedio_persona_en_kilogramos
    peso_promedio_persona_en_kilogramos = 70
    self.assertFalse(ascensor_sobrecargado(4))

  def test_ascensor_sobrecargado_4_con_peso_promedio_persona_en_kilogramos_80(self):
    global peso_promedio_persona_en_kilogramos
    peso_promedio_persona_en_kilogramos = 80
    self.assertTrue(ascensor_sobrecargado(4))

  def test_ascensor_sobrecargado_2_con_peso_promedio_persona_en_kilogramos_80(self):
    global peso_promedio_persona_en_kilogramos
    peso_promedio_persona_en_kilogramos = 80
    self.assertFalse(ascensor_sobrecargado(2))

  def test_ascensor_sobrecargado_5_con_peso_promedio_persona_en_kilogramos_80(self):
    global peso_promedio_persona_en_kilogramos
    peso_promedio_persona_en_kilogramos = 80
    self.assertTrue(ascensor_sobrecargado(5))





