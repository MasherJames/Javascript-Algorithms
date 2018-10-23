
Artificial Intelligence

Context

Create a Python project of a Magic 8 Ball which is a toy used for fortune-telling or seeking advice.

Task

Create a Python project of a Magic 8 Ball which is a toy used for fortune-telling or seeking advice.

Allow the user to input their question.

Show an in progress message.

Create 10/20 responses, and show a random response.

Allow the user to ask another question/advice or quit the game.

TDD

Include tests for this program.


Question 2:

Additive Sequence

Context

Write a Python program to find whether a string contains an additive sequence or not.

Task

Write a Python program to find whether a string contains an additive sequence or not.


The additive sequence is a sequence of numbers where the sum of the first two numbers is equal to the third one.

Sample additive sequence: 6, 6, 12, 18, 30

In the above sequence 6 + 6 =12, 6 + 12 = 18, 12 + 18 = 30....

Also, you can split a number into one or more digits to create an additive sequence.

TDD

Include unit tests for this solution.


Question 3:

Simple Pig Latin Converter

Context

Pig latin is a language game where English words are altered by moving some letters to the end of the word and/or by adding a suffix.

Task

Write a program that will take a word and output the pig latin version of the word by following the following rules:


1. If the word starts with a consonant or group of consonants, move all letters before the first vowel to the end of the word then add "ay".

Example:

will -> illway

dog -> ogday

category -> ategorycay

chatter -> atterchay

trash -> ashtray


2. If the word starts with a vowel, simply add "way" to the end of the word.

Example:

andela - andelaway

electrician - electricianway

TDD

Include unit tests for this solution.



Question 4:


Even Fibonacci numbers

Context

Each new term in the Fibonacci sequence is generated by adding the previous two terms.

Task

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

TDD

Include tests



Question 5:


Question Marks

Context

Take an input string parameter and determine if exactly 3 question marks exist between every pair of numbers that add up to 10.

Task

Take an input string parameter and determine if exactly 3 question marks exist between every pair of numbers that add up to 10. If so, return true, otherwise return false. Some examples test cases are below:

Input:"aa6?9"

Output:"false"

Input:"acc?7??sss?3rr1??????5"

Output:"true"

TDD

Include tests

Test.assertEquals(numberOfRoutes(1, 1), 2);
Test.assertEquals(numberOfRoutes(5, 1), 6);
Test.assertEquals(numberOfRoutes(3, 4), 35);
You have a grid with m rows and n columns.
Return number of ways that you can start from point A to reach point B.
you are only allowed to move right and up.

alt text

In the picture, there are 10 pathes from A to B.


Complete the method so that it does the following:
Removes any duplicate query string parameters from the url
Removes any query string parameters specified within the 2nd argument (optional array)
Examples:
stripUrlParams('www.codewars.com?a=1&b=2&a=2') // returns 'www.codewars.com?a=1&b=2'
stripUrlParams('www.codewars.com?a=1&b=2&a=2', ['b']) // returns 'www.codewars.com?a=1'
stripUrlParams('www.codewars.com', ['b']) // returns 'www.codewars.com'

* Finding the first non-repeating character
if all characters are repeating return an empty string e.g ""