#Breach Bot Starter Code
breachYear = 2017

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts years of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the Hong Kong Registration and Electoral Office data breach!")

#Introduces breach
print("Would you like to learn about the Hong Kong Registration and Electoral Office 2017 data breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
    print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organizations response, (c) I would like to hear your reflection")
    topic = input()
    
    if topic.lower() == "a":
        print("The REO, which stands for Registration and Electoral Office, in Hong Kong was involved.")
        print("Two laptops were stolen. One laptop had voter registration like ID card numbers, addresses and phone numbers and the other laptop had names of the 1194 members of the Election Committee.")
        print("It’s not entirely known how it happened. The door to the locked room needs a passcode and access card for entry and the door appeared to not be forced open. Only the bags that the laptops were in were left behind two days after they were placed there. ")
    
    elif topic.lower() == "b":
        print("While Hong Kong did have data privacy regulations, enforcement lagged until a direct marketing scandal in 2010. Hong Kong’s commissioner for personal data became more active and fines were increased for mishandling personal data.")
        print("The article does not specify any actions they recommended affected users to do.")
    
    elif topic.lower() == "c":
        break
    
    else:
        print("Sorry, I didn't catch that. Choose one of the options listed.")
    
    input("Press enter to continue\n")

#Introduces my take
print("I'm excited to share my perspective with you! Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")
    
#shares my take
while giveInfo.lower() == "yes":
    print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to the CIA triad, (b) my reaction, (c) my advice, (d) none")
    topic = input()
    
    if topic.lower() == "a":
        print("Hong Kong Registration and Electoral Office data breach in 2017 connects to confidentiality in the CIA triad because it released information to the public that was supposed to be private.")
    
    elif topic.lower() == "b":
        print("We agree and disagree with the organization's response because… it did step in to regulate it a little bit, however, it could have done more and not waited until another scandal happened to start implementing these laws.")
    
    elif topic.lower() == "c":
        print("I would convince victims to take action by letting them know that private information was released to the public and could be used against them. \n My advice would be to not be shy. Speak out and let them know you care that your data was breached.")
    
    elif topic.lower() == "d":
        break
    
    else:
        print("Sorry, I didn't catch that. Choose one of the options listed.")
    
    input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")
