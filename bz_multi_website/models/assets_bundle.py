# -*- coding: utf-8 -*-

import base64

from odoo.addons.base.ir.ir_qweb.assetsbundle import AssetsBundle

class AssetsBundle(AssetsBundle):

    def clean_attachments(self, type):
        '''
        Override function to add website filter.
        '''
        ira = self.env['ir.attachment']
        domain = [
            ('url', '=like', '/web/content/%-%/{0}%.{1}'.format(self.name, type)),  # The wilcards are id, version and pagination number (if any)
            '!', ('url', '=like', '/web/content/%-{}/%'.format(self.version)),
            '|', ('website_id','=',False), ('website_id','=',self.env['website'].get_current_website().id)
        ]
        # force bundle invalidation on other workers
        self.env['ir.qweb'].clear_caches()
        return ira.sudo().search(domain).unlink()

    def get_attachments(self, type, ignore_version=False):
        '''
        Override function to add website filter.
        '''
        version = "%" if ignore_version else self.version
        url_pattern = '/web/content/%-{0}/{1}{2}.{3}'.format(version, self.name, '.%' if type == 'css' else '', type)
        self.env.cr.execute("""
            SELECT max(id)
            FROM ir_attachment
            WHERE url like %s
                AND website_id = %s
            GROUP BY datas_fname
            ORDER BY datas_fname
        """, [url_pattern, self.env['website'].get_current_website().id])
        attachment_ids = [r[0] for r in self.env.cr.fetchall()]
        return self.env['ir.attachment'].sudo().browse(attachment_ids)

    def save_attachment(self, type, content, inc=None):
        '''
        Add website id when saving attachments.
        '''
        ira = self.env['ir.attachment']
        fname = '%s%s.%s' % (self.name, ('' if inc is None else '.%s' % inc), type)
        values = {
            'name': "/web/content/%s" % type,
            'datas_fname': fname,
            'res_model': 'ir.ui.view',
            'res_id': False,
            'type': 'binary',
            'public': True,
            'datas': base64.b64encode(content.encode('utf8')),
            'website_id': self.env['website'].get_current_website().id
        }
        attachment = ira.sudo().create(values)
        url = '/web/content/%s-%s/%s' % (attachment.id, self.version, fname)
        values = {
            'name': url,
            'url': url,
        }
        attachment.write(values)
        if self.env.context.get('commit_assetsbundle') is True:
            self.env.cr.commit()
        self.clean_attachments(type)
        return attachment