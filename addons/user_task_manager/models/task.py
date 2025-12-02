from odoo import models, fields, api
from odoo.exceptions import ValidationError

class userTask(models.Model):
    _name = "user.task"
    _description = "User Task"
    _order = 'deadline asc'

    name = fields.char(string='Titulo', required=True)
    description = fields.text(string='Descripción')
    priority= fields.selection(
        [('0', 'Baja'),('1', 'Media'),('2', 'Alta')],
        string='Prioridad',
        default='1',
        required=True
    )
    state= fields.Selection(
        [("drauft", "Borrador"),("in_progress", "En Progreso"),("done", "Completada")],
        string="Estado",
        default="draft",
    )
    deadline = fields.Date(string="Fecha Límite")
    is_done = fields.Boolean(
        string="Completada", compute="_compute_is_done", store=True
    )
    user_id = fields.Many2one(
        "res.users",
        string="Asignado a",
        default=Lambda self: self.env.user,
        required=True,
    )

    @api.depends("state")
    def _compute_is_done(self):
        for record in self:
            record.is_done = record.state == "done"

    @api.contrains("deadline")
    def _check_deadline(self):
        for task in self:
            id task.deadline and taskdeadline < fields.Date.today():
                raise ValidationError("la fecha límite no puede ser anterior a hoy")
    

