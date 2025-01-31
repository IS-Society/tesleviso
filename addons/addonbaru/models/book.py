# -*- coding: utf-8 -*-

from odoo import models, fields, api


class addonbaru(models.Model):
    _name = 'addonbaru.book'
    _description = 'addonbaru.book'

    name = fields.Char(string="Nama Buku")
    author = fields.Char(string="Penulis")
    price = fields.Float(string="Harga")

