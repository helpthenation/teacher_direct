# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import request

class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    def _get_param(self, key):
        '''
        Make parameters website specific.
        '''
        if key == 'web.base.url':
            return str(request.httprequest.environ.get('HTTP_ORIGIN', super(IrConfigParameter, self)._get_param(key)))
        elif key == 'auth_signup.template_user_id':
            return str(self.env['website'].get_current_website().template_user_id.id)
        elif key == 'auth_signup.allow_uninvited':
            return str(self.env['website'].get_current_website().auth_signup_uninvited)
        elif key == 'auth_signup.reset_password':
            return str(self.env['website'].get_current_website().auth_signup_reset_password)
        return super(IrConfigParameter, self)._get_param(key)