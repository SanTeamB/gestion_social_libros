# -*- coding: utf-8 -*-

from odoo import models, fields, api

class libro(models.Model):
     _name = 'gestion_social_libros.libro'

     name = fields.Char(string = "ID", required = True)
     titulo = fields.Char(string = "Titulo", required = True)
     numPags = fields.Integer(string="Numero de paginas", required = True)
     comentario = fields.One2many("gestion_social_libros.comentario", "libro", string = "Comentarios")
     calificacion = fields.One2many("gestion_social_libros.calificacion", "libro", string = "Calificaciones")

     @api.depends('value')
     def _value_pc(self):
         self.value2 = float(self.value) / 100


class comentario(models.Model):
    _name = "gestion_social_libros.comentario"

    name = fields.Char(string = "ID", required = True)
    contenido = fields.Char(string = "Contenido", required = True)
    pagina = fields.Integer(string = "Pagina", required = True)
    libro = fields.Many2one("gestion_social_libros.libro", string = "Libro")
    usuario = fields.Many2one("gestion_social_libros.usuario", string = "Usuario")

class usuario(models.Model):
    _name = "gestion_social_libros.usuario"

    name = fields.Char(string = "Nick", required = True)
    nombre = fields.Char(string = "Nombre", required = True)
    correo = fields.Char(string = "Correo electronico", required = True)
    comentario = fields.One2many("gestion_social_libros.comentario", "usuario", required = True)
    calificacion = fields.One2many("gestion_social_libros.calificacion", "usuario", required = True)

class calificacion(models.Model):
    _name = "gestion_social_libros.calificacion"

    name = fields.Char(string = "ID", required = True)
    valor = fields.Integer(string = "Calificaion")
    usuario = fields.Many2one("gestion_social_libros.usuario", required = True)
    libro = fields.Many2one("gestion_social_libros.libro", required = True)

class estado(models.Model):
    _name = "gestion_social_libros.estado"

    name = fields.Char(string = "ID", required = True)
    usuario = fields.Many2one("gestion_social_libros.usuario", string = "Usuario")
    estado = fields.Selection([('0', 'Leyendo'), ('1', 'Completado'), ('2', 'Pendiente'), ('3', 'Sin registro')], string = "Estado", default = "3")
    libro = fields.Many2one("gestion_social_libros.libro", string = "Libro")
