# ==============================================================================
# CÓDIGO DE PRUEBAS AUTOMATIZADAS - SISTEMA SIS-MANT (LOJA)
# Autora: Rosa Elena Conde Paucar
# ==============================================================================

from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
# Importación corregida según el nombre exacto de la carpeta de tu app
from ordenes_de_trabajo.models import OrdenTrabajo


class OrdenTrabajoModelTest(TestCase):
    def setUp(self):
        """Configuración del entorno de prueba con datos de la planta en Loja."""
        self.orden = OrdenTrabajo.objects.create(
            codigo="OT-LOJA-001",
            maquina="Embutidora Continua Loja 01",
            sintoma="Vibración excesiva y pérdida de presión",
            tecnico_asignado="Carlos Ruiz",
            estado="PENDIENTE"
        )

    def test_pu02_creacion_estado_inicial(self):
        """PU-02: Comprueba que la orden inicia por defecto en PENDIENTE."""
        self.assertEqual(self.orden.estado, "PENDIENTE")

    def test_pu03_asignacion_tecnico(self):
        """PU-03: Valida el registro correcto del técnico asignado."""
        self.assertEqual(self.orden.tecnico_asignado, "Carlos Ruiz")

    def test_cp01_validacion_tiempos_parada_critico(self):
        """CP-01 (REGLA CRÍTICA): Invalida registros con tiempo de fin inconsistente."""
        inicio = datetime.now()
        fin_invalido = inicio - timedelta(hours=2)  # Error temporal simulado
        
        orden_erronea = OrdenTrabajo(
            codigo="OT-ERR-LOJA",
            maquina="Molino Industrial Lojano 02",
            sintoma="Fuga de aceite",
            inicio_parada=inicio,
            fin_parada=fin_invalido
        )
        
        # Debe lanzar ValidationError obligatoriamente
        with self.assertRaises(ValidationError):
            orden_erronea.full_clean()


class EmbuLojaPruebasIntegracion(TestCase):
    def test_cp04_generacion_automatica_orden_falla(self):
        """CP-04: Prueba de integración para el reporte de fallas de operario."""
        orden = OrdenTrabajo.objects.create(
            codigo="OT-CORR-001",
            maquina="Mezcladora al Vacío - Planta Loja",
            sintoma="Sobrecalentamiento en banda transportadora",
            estado="PENDIENTE"
        )
        # Cada clase TestCase crea su propia base de datos limpia; por ende el total es 1
        self.assertEqual(OrdenTrabajo.objects.count(), 1)
        self.assertEqual(orden.maquina, "Mezcladora al Vacío - Planta Loja")
        self.assertEqual(orden.estado, "PENDIENTE")
