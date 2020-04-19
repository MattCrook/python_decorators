'''
A decorator in JavaScript => 

const letterPress = () => "Adaptogen tote bag drinking vinegar, letterpress pabst locavore migas hella"
const taxidermy = () => "Taxidermy health goth locavore, pickled post-ironic pork belly kale chips tofu PBR&B bicycle rights"
const mustache = () => "Umami hexagon stumptown enamel pin, mustache echo park readymade celiac"
const lumberSexual = () => "Jean shorts lumbersexual stumptown tumeric everyday carry readymade"

console.log(letterPress())
console.log(taxidermy())
console.log(mustache())
console.log(lumberSexual())

const reversal = sentenceFunc => {
    const originalSentence = sentenceFunc()
    return originalSentence.split("").reverse().join("")
}


In this scenario, the reversal() function is considered a decorator because
it consumes the output of the original method and then outputs something different.
'''

# The Pythonic way
def reversal(sentence_func):
    def reversed_sentence(*args, **kwargs):
        original_sentence = sentence_func(*args, **kwargs)
        return f"Reversed: {''.join(reversed(original_sentence))}"
    return reversed_sentence


@reversal
def letterPress():
    return "Adaptogen tote bag drinking vinegar, letterpress pabst locavore migas hella"
def taxidermy():
    return "Taxidermy health goth locavore, pickled post-ironic pork belly kale chips tofu PBR&B bicycle rights"
@reversal
def mustache():
    return "Umami hexagon stumptown enamel pin, mustache echo park readymade celiac"
def lumberSexual():
    return "Jean shorts lumbersexual stumptown tumeric everyday carry readymade"


print(letterPress())
print(taxidermy())
print(mustache())
print(lumberSexual())


# ****************************************** #
def laundry():
    return "The dirty laundry was cleaned"
def garbage():
    return "The garbage was taken out"
def dust():
    return "The house was dusted"
def groom():
    return "The dog was brushed"

'''
Write a decorator function named @kids that, when placed above a function, 
will modify the return value of that function to have "by the kids" appended to the end.
'''

def kids(chore_func):
    def assigned_chore(*args, **kwargs):
        original_chore = chore_func(*args, **kwargs)
        return f"{''.join(original_chore)} by the kids."
    return assigned_chore

@kids
def garbage():
    return "The garbage was taken out"

result = garbage()
print(result)  # "The garbage was taken out by the kids"

# Write another for Dad

def dad(chore_func):
    def assigned_chore(*args, **kwargs):
        original_chore = chore_func(*args, **kwargs)
        return f"{''.join(original_chore)} by dad because mom got mad at him."
    return assigned_chore



@dad
def laundry():
    return "The dirty laundry was cleaned"

dad_chore = laundry()
print(dad_chore)
