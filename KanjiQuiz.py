question_answer_dict = {"What is the kanji for 'Go'?": '行く', "What is the kanji for 'snow'? ": '雪', "What is the Kanji for 'Now'?": '今'}

while True:
    name = input("Hello, to exit enter 'q' or Please enter your name: ")    
    if name == 'q':
        break
    
    for question,answer in question_answer_dict.items():
        tries = 3
        while tries != 0:
            try:
                print (question)
                response = input("Answer: ")

                if response != answer:
                    print("That's incorrect {}, Try again you have {} tries left".format(name, tries))
                    tries -= 1
                    
                else:
                    response == answer
                    print("This is right!, {} good job!".format(name))
                    
                
            except ValueError:
                continue


print("{} thank you for taking the quiz!".format(name))
                
                
