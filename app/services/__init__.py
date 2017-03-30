## -*- coding: utf-8 -*-

from flask import flash
from app import mail
from flask_mail import Message
from wtforms import widgets

# Flash messages
def errorMessage(msg):
    return flash(unicode(msg), 'error')
def successMessage(msg):
    return flash(unicode(msg), 'success')

# SendMail
def sendMail(subject, sender, recipients, text_body, html_body):
    mesg = Message(subject, sender=sender, recipients=recipients)
    mesg.body = text_body
    mesg.html = html_body
    mail.send(mesg)

# WTForms widgets
# Select2 widget
class select2Widget(widgets.Select):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('data-role', u'select2')

        allow_blank = getattr(field, 'allow_blank', False)
        if allow_blank and not self.multiple:
            kwargs['data-allow-blank'] = u'1'

        return super(select2Widget, self).__call__(field, **kwargs)

# Select2 multiple widget
class select2MultipleWidget(widgets.Select):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('data-role', u'select2')
        allow_blank = getattr(field, 'allow_blank', False)
        if allow_blank and not self.multiple:
            kwargs['data-allow-blank'] = u'1'

        return super(select2MultipleWidget, self).__call__(field, multiple = True, **kwargs)
