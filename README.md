# Python Decorators



 One of the features of JavaScript is the concept of functions being **first-class objects**. You can pass functions as parameters to other functions just like strings or numbers.

Imagine that you want to build an application that tests the ability of a person to read text that is printed normally, but also if the text is printed backwards so that you can measure their reading comprehension skills.

You will ocaassionally switch which one of these functions will have the characters reversed. You certainly don't want to manually modify this code each time you want to change which ones are normal and which ones are reversed.

You will create a function to reverse any string.

```js
const reversal = sentenceFunc => {
    const originalSentence = sentenceFunc()
    return originalSentence.split("").reverse().join("")
}
```
## Python Reveral Decorator

 Decorators are a specific syntax to do exactly what was done in the example above - send functions to other functions to extend their capabilities. 

## The Basics

1. Read the "[A guide to Python's function decorators](https://www.thecodeship.com/patterns/guide-to-python-function-decorators/)" article and do all of the exercises in it to learn the basic vocabulary and syntax of what a decorator is.
1. Read the "[Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)" article and do all of the exercises in it to explore decorator in greater depth.

## Practice: Family Report with Decorators

You need to write functions to represent tasks that members of a family need to perform on a regular basis.

```py
def laundry():
    return "The dirty laundry was cleaned"

def garbage():
    return "The garbage was taken out"

def dust():
    return "The house was dusted"

def groom():
    return "The dog was brushed"
```

Write a decorator function named `@kids` that, when placed above a function, will modify the return value of that function to have "by the kids" appended to the end. For example, if the decorator is above the `garbage()` function, when you invoke the method, it should return "The garbage was taken out by the kids"


## Practice: Michael's Mortuary


Build an initial class, then refactor the `ORDER BY` clause because it is the exact same all of the SQL statements.

This is a perfect opportunity to implement a decorator, which will ensure that each query is always written the same way. Thus, reducing the possibility of errors in the future.

The task is to write a decorator function named `sort_by_name` that you can use on `vendors`, `employees`, `customers`, and `deceased` so that the `ORDER BY last_name ASC, first_name ASC` clause is added to them.
