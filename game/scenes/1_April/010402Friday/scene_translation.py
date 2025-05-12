CHARACTER_NAMES = [
    # Special
    "narrator", "extend", "face", "mace",
    # Red and Mom
    "red", "redmind", "mom",
    # Protagonists
    "blue",
    # Professors
    "oak",
    # Last Year Student Council
    "roxanne", "brawly",

    # Other male students
    "silver",
]
INMUTABLE_TEXTS = ["[ellipse]", "[ellipses]"]
SPECIAL_COMMAND_CHARACTER = "Character"

SPECIAL_CHARACTER = "\\\""
SPECIAL_CHARACTER_TO_REPLACE = "#!#"

LANGUAGE = "LANG_ENG"

global pos_var


def str_init_text_file(var_name):
    return f"init -1 python:\n    {var_name} = [\n        "


def str_add_text_file(value):
    new_str = "EvolvedString({\n"
    new_str += f'            {LANGUAGE}: "{value}",\n'
    new_str += "        }), "
    return new_str


def str_end_text_file():
    return "\n    ]"


def write_output_file(line, file):
    global pos_var
    line = line.replace(SPECIAL_CHARACTER_TO_REPLACE, SPECIAL_CHARACTER)
    file.write(str_add_text_file(line))
    pos_var += 1


def process_single_text(line_to_process, file):
    processed_line = ""
    if "[" in line_to_process:
        spl = line_to_process.split("[")
        processed_line = f'"[{var_name}[{pos_var}]]'
        write_output_file(spl[0], file)
        for i in range(1, len(spl)):
            spl_element = spl[i].split("]")
            processed_line = f'{processed_line}[{spl_element[0]}]'
            if len(spl_element) == 2:
                processed_line = f'{processed_line}[{var_name}[{pos_var}]]'
                write_output_file(spl_element[1], file)
        processed_line += '"'
    else:
        processed_line = f'"[{var_name}[{pos_var}]]"'
        write_output_file(line_to_process, file)
    return processed_line


def replace_line_and_write_output(line, file):
    global pos_var
    split_line_comma = line.split('"')
    new_text = line + "\n"
    if split_line_comma[1] not in INMUTABLE_TEXTS:
        new_text = split_line_comma[0] + process_single_text(split_line_comma[1], file) + split_line_comma[2]
        for i in range(3, len(split_line_comma)):
            new_text += '"' + split_line_comma[i]
    return new_text + '\n'


if __name__ == "__main__":
    scene_name = "prologue.rpy"
    var_name = f"{scene_name.split('.')[0]}_scene_text"
    global pos_var
    pos_var = 0

    print(f"Adjusting scene {scene_name} for translation...")
    new_scene_text = ""
    all_scene_info = None
    output_file = open(f"{scene_name.split('.')[0]}_text.rpy", 'w')
    output_file.write(str_init_text_file(var_name))

    path_scene = scene_name
    with open(path_scene) as file:
        # all_scene_info = file.read().split("\n")
        all_scene_info = file.read().split("\n")

    for line in all_scene_info:
        split_line_space = line.split(" ")
        pos_first_word = 0
        while pos_first_word < len(split_line_space) and split_line_space[pos_first_word] == '':
            pos_first_word += 1
        if pos_first_word >= len(split_line_space):
            # It is a blank line
            new_scene_text += line + "\n"
        else:
            line = line.replace(SPECIAL_CHARACTER, SPECIAL_CHARACTER_TO_REPLACE)
            if 'TempCharacter' in line or SPECIAL_COMMAND_CHARACTER in line:
                split_line_comma = line.split('"')
                new_text = line + "\n"
                if split_line_comma[0] not in INMUTABLE_TEXTS:
                    new_text = (split_line_comma[0] + f'"[{var_name}[{pos_var}]]"' +
                                split_line_comma[2] + f'"[{var_name}[{pos_var+1}]]"' + split_line_comma[4])
                    write_output_file(split_line_comma[1], output_file)
                    write_output_file(split_line_comma[3], output_file)
                new_scene_text += new_text + '\n'
            elif split_line_space[pos_first_word] in CHARACTER_NAMES:
                # It is a character line
                new_scene_text += replace_line_and_write_output(line, output_file)
            elif '"' in split_line_space[pos_first_word]:
                # Command start with string, so probably are menu options
                new_scene_text += replace_line_and_write_output(line, output_file)
            elif 'renpy.input(' in line:
                new_scene_text += replace_line_and_write_output(line, output_file)
            else:
                new_scene_text += line + "\n"

    output_file.write(str_end_text_file())
    with open(path_scene, 'w') as f:
        f.write(new_scene_text)

