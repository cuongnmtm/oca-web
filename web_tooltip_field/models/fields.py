from odoo.fields import Field


def _description_help(self, env):
    help_tooltip = env["ir.model.fields.help.tooltip"].search(
        [
            ("field_id.name", "=", self.name),
            ("field_id.model", "=", self.base_field.model_name),
        ],
        limit=1,
    )
    if help_tooltip and help_tooltip.help:
        return help_tooltip.help
    if self.help and env.lang:
        model_name = self.base_field.model_name
        field_help = env["ir.translation"].get_field_help(model_name)
        return field_help.get(self.name) or self.help
    return self.help


Field._description_help = _description_help
