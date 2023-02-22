
def text_to_list(input_text):
    words = input_text.split()
    return words

def sum_of_elements(list_of_elements):
    return sum(list_of_elements)

def list_to_dict(list_of_words):
    output_dict = {}
    for name in list_of_words:
        if name in output_dict:
            output_dict[name] += 1
        else:
            output_dict[name] = 1
    return output_dict

