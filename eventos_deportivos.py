# -*- encoding: utf-8 -*-

from openerp.osv import osv, fields
from datetime import datetime, timedelta


class Actividad(osv.Model):
    _name = "extraescolares.eventos_deportivos"

    _columns = {
        'name': fields.char(string="Nombre", size=300, required=True,
                            help="Nombre del evento deportivo"),

        'fecha_inicio': fields.date(string="Fecha Inicio", required=True,
                                    help="Fecha incio del evento deportivo"),

        'fecha_fin': fields.date(string="Fecha Fin", required=True,
                                 help="Fecha fin de la evento deportivo"),

        'horas': fields.integer(string="Horas Asignadas", required=True,
                                size=2, help="Horas Asignadas"),

        'responsable': fields.char(string="Responsable", required=True,
                                   size=256, help="Responsable del evento"),

        'anotaciones': fields.text('Anotaciones', help="Escriba annotaciones")
    }
