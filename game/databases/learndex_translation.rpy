init python:
    for element in learndex:
        for i in range(3, len(element)):
            split_movement = element[i].split(" - ")
            level_movement = split_movement[0]
            name_movement = split_movement[1]
            translated_learndex_movement = {
                LANG_ENG: name_movement,
            }
            for language in languages:
                if language != LANG_ENG and name_movement in move_translations[language]:
                    translated_learndex_movement[language] = move_translations[language][name_movement][0]
            element[i] = EvolvedString(translated_learndex_movement, prefix=f"{level_movement} - ")
