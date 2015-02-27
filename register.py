# -*- encoding: utf-8 -*-
from openerp.osv import osv, fields


class Register(osv.Model):
    _name = "extraescolares.register"

    def _get_selection_semester(self, cursor, user_id, context=None):
        return (('1', 'Primer Semestre'),
                ('2', 'Segundo Semestre'),
                ('3', 'Tercer Semestre'),
                ('4', 'Cuarto Semestre'),
                ('5', 'Quinto Semestre'),
                ('6', 'Sexto Semestre'),
                ('7', 'Septimo Semestre'),
                ('8', 'Octavo Semestre'),
                ('9', 'Noveno Semestre'))

    def _get_selection_carrera(self, cursor, user_id, context=None):
        return(('1', 'Ing. Inovacion Agricola Sustentable'),
               ('2', 'Ing. Gestion Empresarial'),
               ('3', 'Ing. Industrias Alimentarias'),
               ('4', 'Ing. Informatica'),
               ('5', 'Ing. Adaministracion'),
               ('6', 'Lic. Biologia'),
               ('7', 'Contador Publico'))

    def _get_selection_sexo(self, cursor, user_id, context=None):
        return(('H', 'Hombre'),
               ('M', 'Mujer'))

    _columns = {
        'names': fields.char(string="Nombres", size=256, required=True,
                             help="nombres del alumno"),
        'surname': fields.char(string="Apellidos", size=256, required=True,
                               help="apellidos del alumno"),
        'num_control': fields.integer(string="Numero de control", size=8,
                                      required=True, help="numero de control"),
        'sexo': fields.selection(_get_selection_sexo, string='Sexo',
                                 required=True, help="Seleccionar Sexo"),

        'carrera': fields.selection(_get_selection_carrera, string="Carrera",
                                    required=True,
                                    help="Seleccionar nombre de la carrera"),
        'semester': fields.selection(_get_selection_semester, 'Semestre',
                                     required=True, help="Elegir el semestre"),
        'num_telefono': fields.float(string="No.Telefono",
                                     size=10, digits=(10, 0),
                                     help="Numero de telefono"),

        'email': fields.char(string="e-mail", size=256,
                             help="Correo electronico")
    }

    _sql_constraints = [('Numer_unique', 'UNIQUE(num_control)',
                        'El numero de control debe de ser unico'),
                        ('Numer_unique_telefon',
                         'UNIQUE(num_telefono)',
                         'El numero de telefono debe ser unico')]
