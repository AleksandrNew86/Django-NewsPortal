
from News.models import *
from Articles_and_news import art_news

user1 = User.objects.create_user('Alex')
user2 = User.objects.create_user('Sue')

author1 = Author.objects.create(author=user1)
author2 = Author.objects.create(author=user2)

Category.objects.create(name_category='sport')
Category.objects.create(name_category='politics')
Category.objects.create(name_category='IT')
Category.objects.create(name_category='cars')

post1 = Post.objects.create(author=author1, type_post='AR', title_post=art_news[0]['title'],\
 text_post=art_news[0]['content'])
news1 = Post.objects.create(author=author1, type_post='NW', title_post=art_news[1]['title'],\
 text_post=art_news[1]['content'])
post2 = Post.objects.create(author=author2, type_post='AR', title_post=art_news[2]['title'],\
 text_post=art_news[2]['content'])

post1.category_post.add(Category.objects.get(pk=1))
post1.category_post.add(Category.objects.get(pk=4))
post2.category_post.add(Category.objects.get(pk=3))
news1.category_post.add(Category.objects.get(name_category='politics'))

comment1 = Comment.objects.create(post=post1, user=author1.author, text_comment='Крутая статья. Однозначно лайк!')
comment2 = Comment.objects.create(post=post2, user=author1.author, text_comment='Очень полезно.')
comment3 = Comment.objects.create(post=news1, user=author2.author, text_comment='Не люблю политику. Дизлайк!')
comment4 = Comment.objects.create(post=post1, user=author2.author, text_comment='Хотел бы покататься на таких машинках)')

post1.like()
post1.dislike()
news1.like()
news1.like()
post2.dislike()
comment1.dislike()
comment2.like()
comment3.dislike()
comment4.like()
comment4.like()

authors = Author.objects.all()
for i in authors:
    i.update_rating()

best_author = authors.order_by('-rating_author')[0]
print(f'username лучшего автора: {best_author.author.username}, рэйтинг = {best_author.rating_author}')

best_post = Post.objects.all().order_by('-rating_post')[0]
print(f'Дата добавления: {best_post.date_creation}\n\
username автора: {best_post.author.author.username}\n\
рэйтинг поста: {best_post.rating_post}\n\
заголовок поста: {best_post.title_post}\n\
превью: {best_post.preview()}')

comments = Comment.objects.all().values('date_creation', 'user', 'rating_comment', 'text_comment')

for n, i in enumerate(comments):
    print(f'Комментарий {n+1}: {i}')
