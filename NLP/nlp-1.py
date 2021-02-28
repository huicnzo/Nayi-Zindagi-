# Computers can understand the structured form of data like spreadsheets and the tables in the database, 
#but human languages, texts, and voices form an unstructured category of data, and it gets difficult for the 
#computer to understand it, and there arises the need for Natural Language Processing.


# NLP pipeline
# Step-1
#Sentence Segmentation - Breaking the piece of text in various sentences.
#For coding a sentence segmentation model,
#we can consider splitting a sentence when it encounters any punctuation mark. 
#But modern NLP pipelines have techniques to split even if the document isn’t formatted properly.


# Step-2
# Breaking the sentence into individual words called as tokens. 
#We can tokenize them whenever we encounter a space, we can train a model in that way.
#Even punctuations are considered as individual tokens as they have some meaning.

#Step- 3
# Predicting parts of speech for each token .
#Input : pre-trained Part of speech classification model 
#Output : Town - common noun
 #        Is - verb 
 #        The - determiner

#Step-4
# Lemmatization
#Feeding the model with the root word.
#child is playing & children are playing should be considered the same .

#Step #5: Identifying stop words
#There are various words in the English language that are used very frequently 
#like ‘a’, ‘and’, ‘the’ etc. 
#These words make a lot of noise while doing statistical analysis. 
#We can take these words out. 


#Some NLP pipelines will categorize these 
#words as stop words, they will be filtered out while doing some statistical analysis. 
#Definitely, they are needed to
#understand the dependency between various tokens to get the exact sense of the sentence. The list of stop words varies and 
#depends on what kind of output are you expecting.



#Step 6.1: Dependency Parsing
#This means finding out the relationship between the words in the sentence and how they are related to each other. 
#We create 
#a parse tree in dependency parsing, with root as the main verb in the sentence. 
#If we talk about the first sentence in our example, then ‘is’ is the main verb and
#it will be the root of the parse tree. We can construct a parse tree of every sentence 
#with one root word(main verb) associated with it. We can also identify the kind of relationship 
#that exists between the two words. In our example, ‘San Pedro’ is the subject and ‘island’ is the 
#attribute. Thus, the relationship between ‘San Pedro’ and ‘is’, and ‘island’ and ‘is’ can be established.
#Just like we trained a Machine Learning model to identify various parts of speech, we can train a model 
#to identify the dependency between words by feeding many words. It’s a complex task though. In 2016,
#Google released a new dependency parser Parsey McParseface which used a deep learning approach.

#Step 6.2: Finding Noun Phrases
#We can group the words that represent the same idea. For example – It is the second-largest town in the Belize District and 
#largest in the Belize Rural South constituency. Here, tokens ‘second’, ‘largest’ and ‘town’ can be grouped together as 
#they together represent the same thing ‘Belize’. We can use the output of dependency parsing to combine such words. 
#Whether to do this step or not
#completely depends on the end goal, but it’s always quick to do this if we don’t want much 
#information about which words are adjective, rather focus on other important details.

#Step #7: Named Entity Recognition(NER)
#San Pedro is a town on the southern part of the island of Ambergris Caye in the 
#2. Belize District of the nation of Belize, in Central America.
#Here, the NER maps the words with the real world places. The places that actually exist in the physical world.
#We can automatically extract the real world places present in the document using NLP.

#If the above sentence is the input, NER will map it like this way:

#San Pedro - Geographic Entity
#Ambergris Caye - Geographic Entity
#Belize - Geographic Entity
#Central America - Geographic Entity
#NER systems look for how a word is placed in a sentence and make use 
#of other statistical models to identify what kind of word actually it is. 
#For example – ‘Washington’ can be a geographical location as well as the last name of any person. A good NER system can identify this.

#Kinds of objects that a typical NER system can tag:

#People’s names. 
#Company names. 
#Geographical locations
#Product names. 
#Date and time. 
#Amount of money. 
#Events.

#Step #8: Coreference Resolution:
#San Pedro is a town on the southern part of the island of Ambergris Caye in the Belize District of
#the nation of Belize, in Central America. According to 2015 mid-year estimates, the town has a population 
#of about 16, 444. It is the second-largest town in the Belize District and largest in the Belize Rural South constituency.

#Here, we know that ‘it’ in the sentence 6 stands for San Pedro, but for a computer, 
#it isn’t possible to understand that both the tokens are same because it treats both the sentences
#as two different things while it’s processing them. Pronouns are used with a high frequency in
#English literature and it becomes difficult for a computer to understand that both things are same.
