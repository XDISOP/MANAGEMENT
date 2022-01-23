# Made By @Madepranav On Telegram & Github Id Superboyfan
import random

from telegram import Update
from telegram.ext import CallbackContext, run_async

import Natsuki.modules.animequotesstring as animequotesstring
from Natsuki import dispatcher
from Natsuki.modules.disable import DisableAbleCommandHandler


def animequotes(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(animequotesstring.ANIMEQUOTES))


ANIMEQUOTES_HANDLER = DisableAbleCommandHandler("animequotes", animequotes, run_async=True)

dispatcher.add_handler(ANIMEQUOTES_HANDLER)
