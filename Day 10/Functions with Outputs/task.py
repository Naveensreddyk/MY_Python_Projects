def format_names(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You haven't provided any inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f" {formatted_f_name} {formatted_l_name}"

print(format_names("naveen", "reddy"))
