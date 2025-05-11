init -3 python:
    LANG_ENG = "english"
    LANG_ESP = "spanish"
    selected_language = LANG_ESP

    languages = [LANG_ENG, LANG_ESP]

    class EvolvedString:
        def __init__(self, values):
            self.values = values

        def __str__(self):
            global selected_language
            return self.values[selected_language] if selected_language in self.values else self.values[LANG_ENG]

        def __eq__(self, other):
            return other == self.values[LANG_ENG]

        def __hash__(self):
            return hash(self.values[LANG_ENG])

        def __iter__(self):
            return self.__str__().__iter__()

        def __next__(self):
            return self.__str__().__next__()

        def __getattr__(self, name):
            return self.__str__()

        def __add__(self, other):
            return self.__str__() + other

        def __radd__(self, other):
            return other + self.__str__()
