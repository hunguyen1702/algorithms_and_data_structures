# -*- coding: utf-8 -*-
# Here’s a self check that really covers everything so far. You may have heard of the infinite monkey theorem? The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare. Well, suppose we replace a monkey with a Python function. How long do you think it would take for a Python function to generate just one sentence of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”
# 
# You’re not going to want to run this one in the browser, so fire up your favorite Python IDE. The way we’ll simulate this is to write a function that generates a string that is 27 characters long by choosing random letters from the 26 letters in the alphabet plus the space. We’ll write another function that will score each generated string by comparing the randomly generated string to the goal.
# 
# A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. If the letters are not correct then we will generate a whole new string.To make it easier to follow your program’s progress this third function should print out the best string generated so far and its score every 1000 tries.


import random


def generate_sentence(slen):
    res = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzi "

    for i in range(slen + 1):
        res += alphabet[random.randrange(len(alphabet))]
    return res


def score_sentence(goal, gen_sentence):
    same_character = 0
    for i in range(len(goal)):
        if gen_sentence[i] == goal[i]:
            same_character += 1
    return float(same_character) / float(len(goal))


def main():
    goal_sentence = "methinks it is like a weasel"
    new_sentence = generate_sentence(len(goal_sentence))
    best_sentence = ""
    new_score = score_sentence(goal_sentence, new_sentence)
    best_score = 0
    iter_number = 0
    while best_score < 1:
        iter_number += 1
        if new_score > best_score:
            best_score = new_score
            best_sentence = new_sentence
        new_sentence = generate_sentence(len(goal_sentence))
        new_score = score_sentence(goal_sentence, new_sentence)
        if iter_number == 1000:
            iter_number = 0
            print "best sentence: %r" % best_sentence
            print "best score: %r" % best_score
            # break


main()

