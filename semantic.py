# Lesson SE-T38
# Task 1

# semantic.py--a demonstration of semantic similarities.

# Import spacy and load language model
import spacy

'''  If the language model "en_core_web_sm" is loaded instead of "en_core_web_md",
     a warning message will be displayed that the model being used does not have
     word vectors loaded. The user could add their own word vectors or a larger
     model could be used instead.
'''
nlp = spacy.load("en_core_web_md")  


# Similarity between words
word1 = nlp('cat')
word2 = nlp('monkey')
word3 = nlp('banana')
word4 = nlp('dog')

print('''
        ---Similarity between words---
                                        ''')

print("  Cat and monkey:", word1.similarity(word2))
print("  Banana and monkey:", word3.similarity(word2))
print("  Banana and cat:", word3.similarity(word1))
print("  Cat and dog:", word1.similarity(word4))

''' 
    Cat and monkey (0.59) seem to be similar because the are both animals.

    Banana and monkey (0.40) similarity seems to be due to the fact that monkeys eat bananas.

    Banana and cat (0.22) although to a low degree, may be that in some countries (inluding
    certain regions in Switzerland) are both a food source for humans.
    
    Cat and dog's (0.82)  high degree of similarity may be due to the fact that they are both 
    animals and pets.
'''

# Working with vectors
print('''
        ---Working with vectors---
                                        ''')

tokens = nlp("cat monkey banana dog")

for token1 in tokens:
    for token2 in tokens:
        print(" ", token1.text, token2.text, token1.similarity(token2))
print()


# Working with sentences
print('''
        ---Working with sentences---
                                    ''')

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
        "Hello, there is my car",
        "I\'ve lost my car in my car",
        "I\'d like my boat back",
        "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

print("  Model sentence: Why is my cat on the car")
print()

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(" ", sentence, "-", similarity)
print()
