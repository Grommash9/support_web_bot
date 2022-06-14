from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ParseMode

from bot_app import markup
from bot_app.misc import bot, dp
from bot_app.state.user import User


@dp.callback_query_handler(text_startswith='user-feedback_')
async def user_feedback_answer(call: CallbackQuery, state: FSMContext):
    await state.set_state(User.SupportMessage.message_text)
    await bot.send_message(call.from_user.id,
                           'Пожалуйста отправьте вопрос который хотите задать: ',
                           parse_mode=ParseMode.HTML,
                           reply_markup=markup.base.cancel_menu())
