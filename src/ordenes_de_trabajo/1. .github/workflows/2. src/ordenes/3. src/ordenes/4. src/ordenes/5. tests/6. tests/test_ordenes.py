from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from src.ordenes.models import OrdenTrabajo

class OrdenTrabajoModelTest(TestCase):
    def setUp(self):
        self.orden = OrdenTrabajo.objects.create(
            codigo="OT-LOJA-001",
            maquina="Embutidora Continua Loja 01",
            sintoma="Vibración excesiva y pérdida de presión",
            tecnico_asignado="Carlos Ruiz",
            estado="PENDIENTE"
        )

    def test_pu02_creacion_estado_inicial(self):
        self.assertEqual(self.orden.estado, "PENDIENTE")

    def test_pu03_asignacion_tecnico(self):
        self.assertEqual(self.orden.tecnico_asignado, "Carlos Ruiz")

    def test_cp01_validacion_tiempos_parada_critico(self):
        inicio = datetime.now()
        fin_invalido = inicio - timedelta(hours=2)
        
        orden_erronea = OrdenTrabajo(
            codigo="OT-ERR-LOJA",
            maquina="Molino Industrial Lojano 02",
            sintoma="Fuga de aceite",
            inicio_parada=inicio,
            fin_parada=fin_invalido
        )
        
        with self.assertRaises(ValidationError):
            orden_erronea.full_clean()

class EmbuLojaPruebasIntegracion(TestCase):
    def test_cp04_generacion_automatica_orden_falla(self):
        orden = OrdenTrabajo.objects.create(
            codigo="OT-CORR-001",
            maquina="Mezcladora al Vacío - Planta Loja",
            sintoma="Sobrecalentamiento en banda transportadora",
            estado="PENDIENTE"
        )
        self.assertEqual(OrdenTrabajo.objects.count(), 2)
        self.assertEqual(orden.maquina, "Mezcladora al Vacío - Planta Loja")
        self.assertEqual(orden.estado, "PENDIENTE")
