from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
import config

class IsAdminFilter(BoundFilter):
    """
    Custom Filter
    """
    key = "is_owner"

    def __init__(self, is_owner) -> None:
        self.is_owner = is_owner

    async def check(self, message: types.Message):
        return message.from_user.id == config.BOT_OWNER
