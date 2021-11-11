##This is a string concatenation tutorial
## Below are 3 ways of doing string concat
## in python

#relation= "love"

#print(input("Hello my "+ relation))
#print(input("Hello my {}".format(relation)))
#print(input( f"Hello my {relation}"))

adj= input("Adjective: ")
verb1=input ("Verb: ")
verb2=input ("Verb: ")
secure_site=input("Secure Site: ")
madlib=f"Walking with Jesus is so {adj}! He soothes my soul.\
    I love to {verb1}. Stay with Jesus and feel safe like a {secure_site}!"

print (madlib)