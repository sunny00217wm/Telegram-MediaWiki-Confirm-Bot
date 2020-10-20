class Ac:
    def __init__(self, telegram_id: int):
        self.confirmed = False
        self.confirming = False
        self.telegram_id: int = telegram_id
        self.wikimedia_username: str = ''
        self.confirmed_time: int = 0
        self.restricted_until: int = 0
        self.init_confirm_time: int = 0

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data: dict):
        obj = cls(data['telegram_id'])
        obj.confirmed = data['confirmed']
        obj.confirming = data['confirming']
        obj.wikimedia_username = data['wikimedia_username']
        obj.confirmed_time = data['confirmed_time']
        obj.restricted_until = data['restricted_until']
        obj.init_confirm_time = data['init_confirm_time']

        return obj
