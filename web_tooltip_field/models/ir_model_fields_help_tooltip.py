from odoo import fields, models


class IrModelFieldsHelpTooltip(models.Model):
    _name = "ir.model.fields.help.tooltip"
    _description = "Help Tooltip for Fields"
    _rec_name = "field_id"

    field_id = fields.Many2one(
        "ir.model.fields", required=True, ondelete="cascade", index=True
    )
    model_id = fields.Many2one("ir.model", related="field_id.model_id", store=True)
    help = fields.Text()
