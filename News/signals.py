from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Post
from django.template.loader import render_to_string


@receiver(m2m_changed, sender=Post.category_post.through)
def notify_new_post(sender, instance, action, **kwargs):
    subject = instance.title_post
    if action == 'post_add':
        categories = instance.category_post.all()
        for category in categories:
            subscribers = category.subscribers.all()
            for subscriber in subscribers:
                if subscriber.email:
                    html_content = render_to_string(
                        'News/mail_message.html',
                        {
                            'post': instance,
                            'category': category,
                            'subscriber': subscriber,
                            },
                    )
                    send_mail(
                        subject=subject,
                        message=html_content,
                        from_email='seleznevaiu86@mail.ru',
                        recipient_list=[subscriber.email],
                        fail_silently=False,
                        html_message=html_content,
                    )
    return
