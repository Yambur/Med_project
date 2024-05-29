# Проект сайта медицинской диагностики

___
При создании проекта использовались язык программирования Python, язык разметки HTML, фреймворк Django, шаблоны
Bootstrap. Сайт готов к работе после наполнения данными: необходимо загрузить в базу данных информацию о врачах,
пациентах, услугах клиники, также существует возможность постоянного внесения данных об открытых записях на диагностику,
чтобы авторизованные пользователи могли записываться на прием через сайт. Кроме того, можно при желании публиковать на
сайте посты с новостями или любой интересной/полезной информацией для клиентов.

___

## Установка зависимостей

Для работы приложения необходимо установить зависимости. Для этого в консоли пишем команду:

- pip install -r requirements.txt

___

## Создание суперпользователя

Для автоматического создания администратора с полным набором прав необходимо прописать в консоли команду:

- .\manage.py csu - на windows
- python3 manage.py csu - на linux

___

## Заполнение сайта контентом

Перед началом работы необходимо зайти в административную панель и создать там, по меньшей мере, экземпляры
специализаций, врачей, услуг, записей на прием. По мере заполнения базы данных на сайте будут отображаться всё новые
элементы.

