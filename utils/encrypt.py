import hashlib

def hash_answer(answer):
    answer = answer.lower()
    hash_obj = hashlib.sha256()
    hash_obj.update(answer.encode('utf-8'))
    hashed_answer = hash_obj.hexdigest()

    # print(f"User Answer: {answer}")
    # print(f"Hashed Answer: {hashed_answer}")

    return hashed_answer

if __name__ == "__main__":
    questions = {
        'Larry': ['What is Larry\'s first name?', 'What is Larry\'s last name?', 'What city was Larry born?'],
        'Nikki': ['What is my go-to Starbucks order? (Hint: 4 words)', 'What restaurant did we eat at on February 13, 2022?', 'Common phrase we text each other: brush my ____', 'Our shared Netflix password referenced this stuffed animal: ____'],
        'Xixi': ['What is the company that makes the ammonia test kit you gave me? Hint: look at your Amazon order history!', 'My favorite Chinese song (Hint: 2 characters in pinyin w/o accents, ___ ___', 'How many yellow spines on the back of the woobles dinosaur? (Hint: Enter as a number)'],
        'Avery': ['What was the name of the series of surprise attacks launched by the Viet Cong and North Vietnamese forces during the Vietnamese New Year holiday in 1968? (Hint: two words)', 'Wikipedia tells me that the Spokane Valley Mall has a Regal Cinemas movie theater. How many movie screens does it have? (Hint: Enter as a number)', 'What day did you randomly decide to create a GitHub account? (Hint: Enter in MM/DD/YYYY format)'],
        'Trinity': ['Your research involved evaluating structural differences between SARS-CoV-2 and this predicted progenitor bat coronavirus: ______', 'Your Dawg Dash 5k race number (Hint: enter as a number)', 'What is the genus of the plant clipping you gave me?', 'There are three animal stickers on the bottom left corner of your refrigerator\'s upper door. What is the third animal?', 'This question is mostly so Nikki doesn\'t try to hack into the system since she probably can figure out most of the other answers. What are the contents of the first text message I sent at 1:37 PM PST on Friday, April 28th, 2023?'],
        'Ashley': ['Who scored the goal for OL Reign on the second game we went to? (Hint: First & Last Name)', 'How many years has your dad worked at Microsoft? (Hint: enter as a number)', 'What is my current chapter in Survivor.io?', 'What is the genus of the small bird you had to study for your animal behavior class?'],
        'Michelle': ['What is the date of the recent Lavin Spring BBQ (which I did not attend)? (Hint: Enter in MM/DD/YYYY format)', 'The odd-looking wooden structure outside of the architecture building I sent you a picture of is a _________ ____', 'What was the extra fancy product you theorized for your Lavin final project? (Hint: Appliance, one word)'],
        'Amelia': ['What is the name of the song by Paul Simon which has a lullaby-like quality to it?', 'What funky word did we encounter during a game of Balderdash early last year?', 'What is Zucc\'s favorite sauce for smoking a brisket and some ribs?', 'This ceramic artist\'s exasperating pottery line features simple, one-word labels in a hand-drawn script.'],
        'Jared': ['One day during my office hours at Mary Gates, you spontaneously appeared in the window. What day was this? (Hint: Enter in MM/DD/YYYY format)', 'What is the name of the beverage we got at Trinity Market and enjoyed together at Ashley\'s place?', 'What is the brand of your sling bag?'],
        'Benjamin': ['What is the maximum value that can be represented by a 32-bit signed integer in two\'s complement form?', 'We toured two apartment units together when seeking housing last year. What was the first one we toured? (Hint: 5/18/22, one word)', 'What is the name of the popular outdoor shopping and entertainment center located in Rancho Cucamonga?']
    }
    
    answers = []
    for friend in questions:
        qlist = questions[friend]
        answer = []
        for question in qlist:
            val = input(f"{friend}: {question} ")
            answer.append(f"'{hash_answer(val)}'")
        answerStr = ", ".join(answer)
        answers.append(f"'{friend}': [{answerStr}]")
    
    for string in answers:
        print(string + ",")
            
    