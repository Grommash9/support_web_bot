Телеграм бот который демонстрирует идею выгрузки переписки с саппортов в веб интерфейс через fast api. 

Кейс - вам нужно сделать в телеграм боте поддержку пользователей, но вы не хотите подключать CRM систему, в рамках одного вашего окна история переписок с пользователями
будет теряться и вам будет сложно продолжать диалог, идея заключаеться в том, что бы по кнопке админ и пользователь или даже несколько менеджеров и пользователь могли получать
доступ к веб версии чата, где можно видеть историю переписки и писать сообщения друг другу. На данный момент реализована только минимальная версия с просмотром истории сообщений
 так как проект просто демонтрационный - буду дорабатывать его по мере появления свободного времени. 
 
 Так же мы может реализовать общение между пользователями в боте где мы не хотим что бы они переходили в личные сообщения, например для маркетплейсов услуг или p2p обменников. В идеале мы сможем сделать переписку в веб версии между испольнителем заказа и клиентом в фриланс боте или между продвацом и покупателем в п2п боте.
 
 Тестовый экземпляр возможно ещё доступен по юзернейму @web_support_bot


TODO:
- зашифрованные айди в ссылке или методы авторизации
- улучшение вида переписки 
- возможность ответа в вебе
- динамическое обновление страницы и возможность вести переписку в вебе


![alt text](https://github.com/Grommash9/support_web_bot/blob/main/img.png?raw=true)


Что бы просто продемонстрировать работу и бота можно было попробывать, он отвечает сам через 1-5 секунд после вопроса, естественно подразумевается что это были бы ответы от настоящего администратора, но что бы можно было потыкать - сделал так. 