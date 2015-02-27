# -*- encoding: utf-8 -*-

from openerp.osv import osv, fields
from datetime import datetime, timedelta


class Actividad(osv.Model):
    _name = "extraescolares.eventos_civicos"

    _columns = {
        'name': fields.char(string="Nombre", size=300, required=True,
                            help="Nombre del evento"),
        'fecha_inicio': fields.date(string="Fecha Inicio", required=True,
                                    help="Fecha de incio de la evento"),
        'fecha_fin': fields.date(string="Fecha Fin", required=True,
                                 help="Fecha de fin de la evento"),
        'horas': fields.integer(string="Horas Asignadas", required=True,
                                size=2, help="Horas Asignadas"),
        'responsable': fields.char(string="Responsable", required=True,
                                   size=256, help="Responsable del evento"),
        'anotaciones': fields.text('Anotaciones', help="Escriba annotaciones")
    }
