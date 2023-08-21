import stanza

# Initialize the English NLP pipeline
stanza.download('en')
nlp = stanza.Pipeline('en')

# Assume customer_review is a string that contains a customer review
customer_review = "I love the quality of the product. Great job!"

# Apply the NLP pipeline to the customer review
doc = nlp(customer_review)

# Tokenize the review
tokens = [[token.text for token in sentence.tokens] for sentence in doc.sentences]

# Print the tokens
for sentence in tokens:
    print(sentence)

# And the execution will show the following:
# ['I', 'love', 'the', 'quality', 'of', 'the', 'product', '.']
# ['Great', 'job', '!']