# -*- encoding: utf-8 -*-
from openerp.osv import osv, fields
from datetime import datetime, timedelta


class Actividad(osv.Model):
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
                                           'num_control',
                                           string="Alumnos",
                                           required=True, ondelete='cascade')

        #'event_line': fields.one2many('extraescolares.eventos_line',
         #                             'event_id',
          #                            string="Add Alumnos",
           #                           help="Añadir los alumnos al evento"
            #                          )
    }


#class eventos_line(osv.Model):
    #_name = "extraescolares.eventos_line"

   # _columns = {
       # 'name': fields.char(string="nombre", size=160),
      #  'event_id': fields.many2one('extraescolares.eventos', 'Order Reference',
     #                               required=True, ondelete='cascade', select=True),

    #}
class asistentes(osv.Model):
    _name = "extraescolares.asistentes"

    _columns = {
        'num_control': fields.many2one('extraescolares.register',
                                       string="Alumnos",
                                       required=True, ondelete='cascade'),

    }
