from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    active = fields.Boolean(default=True, string="Archive") 

class FeedbackForm(models.Model):
    _name = 'hr.feedback.form'
    _description = 'Feedback Form'

    title = fields.Char(string="Title", required=True)
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)
    manager_id = fields.Many2one('hr.employee', string="Manager", required=True)
    feedback_type = fields.Selection([
        ('one_month_after_joining', 'One Month After Joining'),
        ('post_interview_feedback', 'Post Interview Feedback')
    ], string="Feedback Type", required=True)
    feedback_date = fields.Date(string="Date", required=True, default=fields.Date.context_today)

    comments = fields.Text('Feedback Comments')
