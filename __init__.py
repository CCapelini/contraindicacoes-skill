from mycroft import MycroftSkill, intent_file_handler


class Contraindicacoes(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('contraindicacoes.intent')
    def handle_contraindicacoes(self, message):
        self.speak_dialog('contraindicacoes')


def create_skill():
    return Contraindicacoes()

