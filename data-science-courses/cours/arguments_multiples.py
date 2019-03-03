# les arguments multiples

def clean_string(string, change_string):
    replacement_string = ""
    cleaned_string = string.replace(change_string,replacement_string)
    return(cleaned_string)

text = "Hello World !!!"
test_clean_string = clean_string(text, "!")
print(test_clean_string)

def clean_text(text_string, replace_text, replace_value):
    cleaned_text = text_string.replace(replace_text,replace_value)
    return(cleaned_text)

test_clean_text = clean_text(text,"!",".")
print(test_clean_text)