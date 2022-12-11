from src.enums.user_enums import Status
from src.generators.player_localization import PlayerLocalization


class Player:

    def __init__(self):
        self.result = {

        }
        self.reset()

    def set_status(self, status=Status.ACTIVE.value):
        self.result["account status"] = status
        return self

    def set_balance(self, balance=0):
        self.result["balance"] = balance
        return self

    def set_avatar(self, avatar="https://www.google.com/"):
        self.result["avatar"] = avatar
        return self

    def reset(self):
        self.set_status()
        self.set_avatar()
        self.set_balance()
        self.result["localize"] = {
            "en": PlayerLocalization("en_US").build(),
            "ua": PlayerLocalization("uk_UA").build()
        }
        return self

    def build(self):
        return self.result


a = Player().build()  # available using set_methods to modify data
print(a)
