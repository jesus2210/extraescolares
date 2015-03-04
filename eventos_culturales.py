# -*- encoding: utf-8 -*-
from openerp.osv import osv, fields
from datetime import datetime, timedelta


class actividad(osv.Model):
    _name = "extraescolares.eventos"

    _columns = {
        'name': fields.char(string="Nombre", size=300, required=True,
                            help="Nombre de la actividad"),
        'fecha_inicio': fields.date(string="Fecha Inicio", required=True,
                                    help="Fecha de incio de la actividad"),
        'fecha_fin': fields.date(string="Fecha Fin", required=True,
                                 help="Fecha de fin de la actividad"),
        'horas': fields.integer(string="Horas Asignadas", required=True,
                                size=2, help="Horas Asignadas"),
        'responsable': fields.char(string="Responsable", required=True,
                                   size=256, help="Responsable del evento"),
        'anotaciones': fields.text('Anotaciones', help="Escriba anotaciones"),

        'num_control_ids': fields.one2many('extraescolares.asistentes',
                                           'name',
                                           string="Alumnos",
                                           required=True, ondelete='cascade')
    }
    _defaults = {
        'fecha_inicio': fields.date.today
    }

actividad()


class asistentes(osv.Model):
    _name = "extraescolares.asistentes"

    _columns = {
        'name': fields.many2one('extraescolares.eventos',
                                string="many2one obligado"
                                ),
        'num_control': fields.many2one('extraescolares.register',
                                       'Numero de control'),

    }

asistentes()
