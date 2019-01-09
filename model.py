from odoo import fields, models


class categoriasRecord(models.Model):
	_name = "agenda.categorias"
	nombre = fields.Char(string="Categorias", required=True)

class registrosRecord(models.Model):
	_name = "agenda.registros"
	nombre = fields.Char(string="Nombres", required=True)
	apellido = fields.Char(string="Apellidos", required=True)
	correo = fields.Char(string="Correo Electronico", required=True)
	direccion = fields.Text(string="Direccion")
	telefono = fields.Char(string="Telefono")
	categoria = fields.Many2one("agenda.categorias", "Categorias")
