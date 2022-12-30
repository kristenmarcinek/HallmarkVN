label choice1_charlie:
    mc neutral coat "I mean, if he’s going that way anyway we might as well… And we can save the company a few bucks, right?"

    show c smile b at left
    show m angry coat at right

    c "That’s what I’m sayin’! C’mon! That’s my truck right over there. We can throw your bags in the bed. One of you will have to sit in the back with Bailey though."

    hide c smile b
    hide m
    with dissolve
    # show b happy
    # with dissolve
    # commenting this out until we have a bailey

    b "WOOF!!"

    # hide b happy with dissolve
    show m angry coat with dissolve

    mc open coat "I’ll sit in the back."

    scene airport with dissolve

    "You all pile into Charlie’s pickup truck and take off back towards the hotel. You manage to make small talk with Charlie and catch up while giving Bailey the requisite amount of headpats."

    scene hotel outside with fade

    "In front of the hotel…"

    show m neutral coat with dissolve

    m "Alright. [player], you and Charlie grab the bags. I’ll go see if we can get our room back for a couple nights."

    hide m neutral with dissolve
    show c neutral with dissolve

    "You begin to help Charlie unload the bags."

    show c smile

    c "Man, [player], it was so great catching up. I know you’re only in town for a couple days but… if you need anything, don’t hesitate to reach out. Here’s my number…"

    "You exchange numbers with Charlie."

    mc open coat b "Got it. Thanks, Charlie. I’ll see you later!"

    hide c smile with dissolve

    "You take the bags into the lobby and meet back up with Monica."

    jump prologue_2

label choice2_charlieA:
    "You decide to take Charlie up on his offer. It was really good to catch up with him in the car, and he was so nice to offer to drive you and Monica all the way back from the airport. Besides… that pie looked {b}really{/b} good."

    mc open "I um… actually got an invite from Charlie to have dinner at his place. You could probably come if you want? Consider it research! Finding out how the people in Harkmall live."

    show m angry

    m "Uh, I think I got a clear enough idea during the hour-long car ride where he wouldn’t stop talking about gingerbread. I’ll pass. You go ahead though."

    jump chapter1

label choice2_charlieB:
    "You decide to take Charlie up on his offer. It could be good to catch up with an old friend from high school. Besides… that pie looks {b}really{/b} good."

    mc open "I um… actually got an invite from Charlie to have dinner at his place. You could probably come if you want? Consider it research! Finding out how the people in Harkmall live."

    show m angry

    m "I’ll pass. You go ahead though."

    jump chapter1

label chapter1_charlie:
    
