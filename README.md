1. Созданы модели проекта в файле /News/models.py
2. Созданы представления новостей (view.py) - список новостей, отдельная новость
3. Добавлена пагинация проекта, фильтр поиска новостей (filters.py), возможность создания,
редактирования, удаления новости. С помощью функции clean() реализована возможность "запретных слов".
4. Добавлена аутенфикация и авторизация пользователя, возможность входа allauth (google), созданы группы common и author, любой новый пользователь становится участником группы common, участникам группы author даны дополнительные права. Для создания и редактирования статей нужны дополнительные права. Добавлена возможность редактирования профиля пользователя (только своего!)
5. В модель Category добавлено поле Subscribers через связь ManyToMany. Реализовано возможность подписаться/отписаться от статьи на странице новости. Для определения подписан или не подписан пользователь на категорию просматриваемой страницы, добавлен метод "get_subscribers" в customs_filters. 
На странице редактирования профиля пользователя отображаются подписки. При создании статьи, относящейся к определенным категориям, всем подписчикам приходит уведомление на электронную почту.
Раз в неделю подписчикам приходит список новых статей за последнюю неделю.
Добавлено подтверждение электронной почты.
6. Настроена библиотека CELERY. С помощью нее реализована рассылка подписчикам новостей.
7. Добавлено кэширование страницы со списком новостей, подробной информацией новости. 
Также добавлено кэширование к навигационнйой панели сайта. При изменении содержания статьи  кэширование информации об статье удаляется. 
8. Добавлена команда удалять посты, которые относятся к конкретной категории. Изменен вид моделей Post и Author в админ панели.
9. Добавлено логирование в файл setting.py.