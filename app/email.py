from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from . import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    try:
        subject_str = app.config.get('VZII_MAIL_SUBJECT_PREFIX', '[Vzii] ') + subject
        sender = app.config.get('VZII_MAIL_SENDER', 'Vzii Admin <gongyuzicong@163.com>')
        to = [to]
        app.logger.info('发送email...{}, {}, {}'.format(subject_str, sender, to))
        msg = Message(subject_str, sender=sender, recipients=to)
        msg.body = render_template(template + '.txt', **kwargs)
        msg.html = render_template(template + '.html', **kwargs)
        thr = Thread(target=send_async_email, args=[app, msg])
        thr.start()
        # mail.send(msg)
    except Exception as e:
        app.logger.error(e)
        return None
    else:
        return thr
