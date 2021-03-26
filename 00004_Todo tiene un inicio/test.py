  
  def test_el_ascensor_no_esta_sobrecargado_con_4_personas_si_el_peso_promedio_persona_en_kilogramos_es_70(self):
    global peso_promedio_persona_en_kilogramos
    peso_promedio_persona_en_kilogramos = 70
    self.assertFalse(ascensor_sobrecargado(4))

  def test_el_ascensor_esta_sobrecargado_con_4_personas_si_el_peso_promedio_persona_en_kilogramos_es_80(self):
    global peso_promedio_persona_en_kilogramos
    peso_promedio_persona_en_kilogramos = 80
    self.assertTrue(ascensor_sobrecargado(4))

  def test_el_ascensor_no_esta_sobrecargado_con_2_personas_si_el_peso_promedio_persona_en_kilogramos_es_80(self):
    global peso_promedio_persona_en_kilogramos
    peso_promedio_persona_en_kilogramos = 80
    self.assertFalse(ascensor_sobrecargado(2))

  def test_el_ascensor_esta_sobrecargado_con_5_personas_si_el_peso_promedio_persona_en_kilogramos_es_80(self):
    global peso_promedio_persona_en_kilogramos
    peso_promedio_persona_en_kilogramos = 80
    self.assertTrue(ascensor_sobrecargado(5))