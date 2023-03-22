import spacy

nlp = spacy.load("en_core_web_sm")

gardenpathSentences = ["Southern European people like Italians like dishes like pasta.",
                       "They painted the wall with cracks.",
                       "Stolen painting found by tree.",
                       "The dog that I had really loved bones.",
                       "The cotton clothing is made of grows in Mississippi.",
                        ]

#  Tokenisation:
print("Tokenisation:")
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print([token.orth_ for token in doc if not token.is_punct | token.is_space])
print()

# tagging of the sentences:
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print([(w.text, w.pos_) for w in doc])
print()


# Entity Recognition:
print("Entity Recognition:")
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print([(i.text, i.label_, i.label) for i in doc.ents])
print()

print("NORP:", spacy.explain("NORP"))
print("GPE:", spacy.explain("GPE"))

# I lookep up NORP and GPE entities above.
# The explanation of NORP is 'Nationalities or religious or political groups'.
# The explanation of GPE is 'Countries, cities, states'.
# The both entities make sense in terms of the word associated with. Italian is the nationality of Italy.
# And Mississippi is a state of United Stated of America.


