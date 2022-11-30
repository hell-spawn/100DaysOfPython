class Australian():
    is_human = True
    enjoys_sport = True
     
    @classmethod
    def is_sporty_human(cls):
        return cls.is_human and cls.enjoys_sport


print(Australian.is_sporty_human())
aussie = Australian()
print(aussie.is_sporty_human())
