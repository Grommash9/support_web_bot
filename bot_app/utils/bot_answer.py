import random
from bot_app import markup, db
from bot_app.misc import bot


answers = ['Нет, так делать не стоит!',
           'Да, так можно сделать',
           'Если у вас есть возможность - лучше не такого не совершать',
           'Ваше предложение по улучшению сервиса приянто, мы обязательно станем лучше!',
           'Пожалуйста расскажите подробнее о вашей проблеме'
           'Не лучшая из возможных идей',
           'Да, мы уже получали такие сообщения, спасибо!',
           'Мы обязательно разберемся более детально в сложившейся ситуации, спасибо!']


async def send_answer(user_id):
    bot_data = await bot.get_me()
    message = await bot.send_message(user_id,
                           f'<b>Ответ от администрации:</b>\n'
                           f'{random.choice(answers)}',
                           reply_markup=markup.user_m.new_admin_answer_markup(user_id, bot_data.id))
    await db.message.new_bot_message(message)
