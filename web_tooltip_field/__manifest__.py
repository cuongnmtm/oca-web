{
    "name": "Web Tooltip Field",
    "summary": "Showing a Field ToolTip in Odoo",
    "author": "Komit Consulting, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/web",
    "category": "Tools",
    "version": "14.0.1.0.0",
    "depends": ["base", "web"],
    "data": [
        "security/ir.model.access.csv",
        "views/ir_model_fields_help_tooltip_view.xml",
    ],
    "license": "AGPL-3",
    "application": True,
    "installable": True,
}
