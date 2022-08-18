
from django.core.mail import send_mail
from .models import Post
from django.template.loader import render_to_string
from celery import shared_task


@shared_task
def notify_new_post(model):


    print(model)
    # subject = post.title_post
    # categories = post.category_post.all()
    # for category in categories:
    #     subscribers = category.subscribers.all()
    #     for subscriber in subscribers:
    #         if subscriber.email:
    #             html_content = render_to_string(
    #                 'News/mail_message.html',
    #                 {
    #                     'post': model,
    #                     'category': subject,
    #                     'subscriber': subscriber,
    #                     },
    #             )
    #             send_mail(
    #                 subject=subject,
    #                 message=html_content,
    #                 from_email='seleznevaiu86@mail.ru',
    #                 recipient_list=[subscriber.email],
    #                 fail_silently=False,
    #                 html_message=html_content,
    #             )
    # return
