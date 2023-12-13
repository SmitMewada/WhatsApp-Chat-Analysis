import re

def extract_info(input_string):
    '''
        This function extracts Date, Username, and Message from the text file which contains text.
    '''
    result = []

    pattern = r"\[(.*?)\] ([^:]+): (.*)"
    matches = re.findall(pattern, input_string)

    for match in matches:

        time = match[0]
        user = match[1]
        message = match[2]

        user = re.sub(r'\W', '', user)
        entry = {
            "Date": time,
            "User": user,
            "Message": message
        }
        result.append(entry)

    return result