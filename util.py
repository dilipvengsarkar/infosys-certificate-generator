def details_to_file_name(name, course):
    name = name.replace(" ", "_").lower()
    course = course.replace(" ", "_").lower()
    return f"{name}_{course}"

def date_to_str(date):
    date_str = date.strftime("%B %d, %Y")
    return date_str