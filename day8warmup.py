#!/usr/bin/env python3

def main():    
    usr_name = input("Please enter your name:\n>").title()
    year_mod = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>")) % 12

    zodiac_signs = [
        {'sign': 'Monkey', 'adjectives': 'sharp, smart, curious, and mischievious.'},
        {'sign': 'Rooser', 'adjectives': 'hardworking, resourceful, courageous, and talented'},
        {'sign': 'Dog', 'adjectives': 'loyal, honest, cautious, and kind'},
        {'sign': 'Pig', 'adjectives': 'wealth, honesty, and practicality'},
        {'sign': 'Rat', 'adjectives': 'artistic, sociable, industrious, charming, and intelligent'},
        {'sign': 'Ox', 'adjectives': 'strong, thorough, determined, loyal, and reliable'},
        {'sign': 'Tiger', 'adjectives': 'courageous, enthusiastic, confident, charismatic, and a leader'},
        {'sign': 'Rabbit', 'adjectives': 'vigilant, witty, quick-minded, and ingenious'},
        {'sign': 'Dragon', 'adjectives': 'talented, powerful, lucky, and successfull'},
        {'sign': 'Snake', 'adjectives': 'wise, like to work alone, and determined'},
        {'sign': 'Horse', 'adjectives': 'animated, active, and energetic'},
        {'sign': 'Sheep', 'adjectives': 'creative, resilient, gentle, mild-mannered, and shy'}
    ]

    zodiac = zodiac_signs[year_mod]

    print(f"{usr_name} your zodiac sign is {zodiac['sign']}, you are {zodiac['adjectives']}")


main()