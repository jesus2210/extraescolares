# -*- encoding: utf-8 -*-

from openerp.osv import fields, osv


class asistentes(osv.Model):
    _name = "extraescolares.asistentes"

    _columns = {
        'num_control': fields.many2one('extraescolares.register',
                                       string="Alumnos",
                                       required=True, ondelete='cascade')
    }
