# -*- coding: utf-8 -*-

import logging

from odoo import models, fields, api, SUPERUSER_ID
from odoo.exceptions import AccessDenied

_logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'res.users'

    website_id = fields.Many2one('website', 'Website')

    _sql_constraints = [
        ('login_key', 'UNIQUE (login,website_id)',  'You can not have two users with the same login !')
    ]

    @classmethod
    def _login(cls, db, login, password):
        '''
        Override function to filter users by website.
        '''
        if not password:
            return False
        user_id = False
        try:
            with cls.pool.cursor() as cr:
                self = api.Environment(cr, SUPERUSER_ID, {})[cls._name]
                user = self.search([('login', '=', login),('website_id','=',self.env['website'].get_current_website().id)])
                if not user:
                    user = self.search([('login', '=', login),('website_id','=',False)])
                if user:
                    user_id = user.id
                    user.sudo(user_id).check_credentials(password)
                    user.sudo(user_id)._update_last_login()
        except AccessDenied:
            _logger.info("Login failed for db:%s login:%s", db, login)
            user_id = False
        return user_id

    @classmethod
    def check(cls, db, uid, passwd):
        '''
        Add check to make sure the user can access the site.
        '''
        cr = cls.pool.cursor()
        self = api.Environment(cr, uid, {})[cls._name]
        if self.env['website'].get_current_website().id != self.browse(uid).website_id.id and self.browse(uid).website_id == False:
            cr.close()
            raise AccessDenied()
        cr.close()
        return super(ResUsers, cls).check(db, uid, passwd)

    def reset_password(self, login):
        users = self.search([('login', '=', login),('website_id','=',self.env['website'].get_current_website().id)])
        if not users:
            users = self.search([('email', '=', login),('website_id','=',self.env['website'].get_current_website().id)])
        if len(users) != 1:
            raise Exception(_('Reset password: invalid username or email'))
        return users.action_reset_password()