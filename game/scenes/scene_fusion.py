
n_limit = 170
real_limit = n_limit*2+2+2
scene_name = "prologue"

with open(f"{scene_name}_text.rpy") as f_original:
    original_str = f_original.read().split("\n")
with open(f"{scene_name}_trans_text.rpy") as f_translated:
    translated_str = f_translated.read().split("\n")

new_str = f"{original_str[0]}\n{original_str[1]}\n"
for i in range(2, real_limit, 2):
    new_str = f"{new_str}{original_str[i]}\n{original_str[i+1]}\n{translated_str[i+1]}\n"
for i in range(real_limit, len(original_str), 2):
    new_str = f"{new_str}{original_str[i]}\n{original_str[i + 1]}\n"

with open(f"{scene_name}_text.rpy", "w") as file:
    file.write(new_str)
