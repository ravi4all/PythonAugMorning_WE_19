text_1 = "In technical terms, Python is an object-oriented, high-level programming language with integrated dynamic semantics primarily for web and app development. It is extremely attractive in the field of Rapid Application Development because it offers dynamic typing and dynamic binding options. Python is relatively simple, so it's easy to learn since it requires a unique syntax that focuses on readability. Developers can read and translate Python code much easier than other languages. In turn, this reduces the cost of program maintenance and development because it allows teams to work collaboratively without significant language and experience barriers. Additionally, Python supports the use of modules and packages, which means that programs can be designed in a modular style and code can be reused across a variety of projects."
text_2 = "Python is a general-purpose programming language that can be used on any modern computer operating system. It can be used for processing text, numbers, images, scientific data and just about anything else you might save on a computer. It is used daily in the operations of the Google search engine, the video-sharing website YouTube, NASA and the New York Stock Exchange. These are but a few of the places where Python plays important roles in the success of the business, government, and non-profit organizations; there are many others. Python is an interpreted language. This means that it is not converted to computer-readable code before the program is run but at runtime. In the past, this type of language was called a scripting language, intimating its use was for trivial tasks."

# 1. Tokenization
# 2. Remove Stopwords

token_1 = text_1.lower().split()
token_2 = text_2.lower().split()

# print(token_1)
stopwords = ['is','an','are','the','in','a','at','of','for','on','any','can','be','with','it',
             'and',',','.',';',':','by','this','that',"its",'was','to','where','which',"so",
             "it's","but"]

words_1 = []
words_2 = []

for token in token_1:
    if token not in stopwords:
        words_1.append(token)

for token in token_2:
    if token not in stopwords:
        words_2.append(token)

# print(words_1)
# print(words_2)
punct = [',','.',';',':','-','_']
for i in range(len(words_1)):
    word = ""
    for w in words_1[i]:
        if w not in punct:
            word += w
            words_1[i] = word

for i in range(len(words_2)):
    word = ""
    for w in words_2[i]:
        if w not in punct:
            word += w
            words_2[i] = word

intersection = set(words_1).intersection(words_2)
union = set(words_1).union(words_2)
sim = len(intersection) / len(union) * 100
print("Similarity is",sim)
