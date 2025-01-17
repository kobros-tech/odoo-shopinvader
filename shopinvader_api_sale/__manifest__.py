# Copyright 2023 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


{
    "name": "Shopinvader API Sale",
    "summary": "Sale FastApi for exposing sale order",
    "version": "16.0.1.1.4",
    "development_status": "Alpha",
    "category": "Uncategorized",
    "website": "https://github.com/shopinvader/odoo-shopinvader",
    "author": " Akretion",
    "license": "AGPL-3",
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "shopinvader_schema_sale",
        "shopinvader_api_security_sale",
        "shopinvader_filtered_model",
        "extendable_fastapi",
        "report_generate_helper",
    ],
    "data": [],
    "demo": [],
}
