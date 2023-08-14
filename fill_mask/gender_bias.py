import re

CATCH_WORD_TO_PRONOUNS = {
    'he/she': ['he', 'she'],
    'him/her': ['him', 'her'],
    'his/her': ['his', 'her'],
    'they': ['he', 'she'],
    'he': ['he', 'she'],
    'she': ['he', 'she'],
    'them': ['him', 'her'],
    'him': ['him', 'her'],
    'his': ['him', 'her'],
    'her': ['him', 'her']
}


def is_male(token):
    for x  in ["he", "his", "him"]:
        if x ==  token:
            return True
    return False


def is_female(token):
    for x in  ["she", "her"]:
        if x ==  token:
            return True
    return False
 

def get_masked_str_and_targets(text):
    text_words = text.split(' ')  # splits the string into a list
    masked_str_and_targets = []
    for i in range(len(text_words)):
        pronouns = CATCH_WORD_TO_PRONOUNS.get(text_words[i], None)
        if pronouns:
            masked_str = ' '.join(  # joins all the elemnts into one string
                text_words[:i] + ['[MASK]'] + text_words[i + 1:])
            yield (masked_str, pronouns)


def remove_words(text, token):
    text = text.replace(token, " ")
    return text



