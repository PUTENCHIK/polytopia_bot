from polytopia_bot.models.Bot import Bot


class BordurBot(Bot):
    def __init__(self, name: str = 'Default bordur', comp: int = 1):
        super().__init__(name, comp)

