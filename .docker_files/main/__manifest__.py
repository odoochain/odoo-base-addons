# Copyright 2024-today Numigi and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Main Module",
    "version": "1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "website": "https://www.numigi.com",
    "license": "LGPL-3",
    "category": "Other",
    "summary": "Install all addons required for testing.",
    "depends": [
        "base",
        "admin_light_base",
        "admin_light_calendar",
        "admin_light_gamification",
        "attachment_minio",
        "lang_fr_activated",
        "mail_template_default",
        "test_http_request",
    ],
    "installable": True,
}
