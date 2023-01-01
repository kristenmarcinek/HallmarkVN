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
    scene hotel with fade

    "Evening"

    "When Charlie texts you the address you recognize it immediately. It’s just a couple of blocks from your hotel - the house he grew up in. You used to play there every now and then. It had a great backyard and a tire swing."

    scene bakery with fade

    "It’s a charming little place on the corner of Main Street tastefully decorated for Christmas with a wreath on the front door and a little candle in every window. You immediately know you have the right place when you hear Charlie’s dog Bailey barking as you walk up the front steps."

    "Before you can even knock the door swings open, revealing a beaming Charlie who is holding Bailey back by the collar."

    show c smile with dissolve

    c "Hey, [player]! Thanks for coming! C’mon in!"

    mc neutral coat "Hey, thanks for having me! Hi, Bailey."

    b "WOOF!"

    show c smile

    c "Here. Lemme take your coat. We’re gonna be right in through there."

    mc neutral "So it’s just us then?"

    show c neutral

    c "Yup! Dad went out with some buddies so we’ve got the run of the place. I hope spaghetti’s okay?"

    mc "Spaghetti’s great!"
    
    "Charlie leads you towards the dining room table where a generous helping of noodles has already been served onto your plate. In the middle of the table sits the delicious looking apple pie that he used to entice you over in the first place."

    mc surprise "That’s quite the pie, Charlie… You work at the bakery with your dad, right?"

    c "Yeah! I just started last year. My bread still needs work but pie’s become something of my speciality"

    show c smile

    "Charlie puffs out his chest, clearly looking more than a little pleased with himself."

    mc neutral "Just last year? What were you doing before then?"

    show c neutral

    c "Ahh, I was living in Boston…"

    mc surprise "Really? I can’t really see you in a big city!"

    c "Yeah! I was actually really liking it. I moved out there with a buddy of mine. I was working as a barista and going to law school at night. It was nice."

    mc "Law school! That’s awesome, Charlie! What happened? How’d you wind up back here? I didn’t realize you tried to get out like me!"

    show c sad

    c "My uh… My mom got sick. She declined pretty rapidly. It was really hard on my dad, so I decided to move back to be with him. It’ll actually be one year on Christmas Eve…"

    mc "Oh, jeez… Charlie… I’m sorry, I had no idea…"

    show c neutral

    c "Ahh it’s okay. We’re making it work. And besides, I actually really like working at the bakery. It’s nice being able to finish a day’s work, working with my hands, and say ‘Yeah. I made that thing!’ and have people enjoy it, y’know?"

    mc done "“I guess so. The last thing I did at work was kind of a huge flop."

    c "Whadja do? Where do you work now?"

    mc "I work at BuzzRead, with that girl Monica you met at the airport. My last listicle bombed so my boss is having me work with her on the next one."

    show c smile

    c "Oh! That’s so cool! What’s the article about?"

    mc neutral "It’s Monica’s idea. She had this big idea to make it go viral by appealing to people’s love for Christmas. Says it’ll drive tourism here and be good for town. She’s made it her personal mission to make sure Harkmall gets its first Starcups"

    show c surprise
    
    c "That’s… awful!"

    mc confused "What? Why?"

    show c sad

    c "The bakery… it’s not doing so well. I mean, I’m helping out as much as I can but I’m nowhere near as good at baking as my mom was. If a Starcups moves in across the street or something… that could put us out of business for good"

    menu:
        "That’s terrible! I didn’t realize. I’ll see what I can do.":
            $ noStarcups = True
            $ charlie_affection += 5
        "“I’m sure it won’t be that bad! Don’t you think that’s a little overdramatic?"
            $ noStarcups = False
            $ charlie_affection -= 5
    
    show c neutral
    
    c "Don’t get me wrong, I don’t want to tell you how to do your job. Just… think about it. Maybe you can just undersell Harkmall so it stays off the radar…?"

    mc neutral "Well, it’s really Monica’s article so I’ll have to talk to her…"

    c "Ah jeez… Look, maybe don’t mention it after all. I don’t want to end up on her bad side."

    mc neutral "She’s really not that bad once you get to know her."

    show c smile

    c "I’ll take your word for it."

    scene bakery

    "You two continue to chat through dinner. You catch up on life, trade cooking recipes, and reminisce about growing up in Harkmall together. Finally, it’s time for dessert!"

    show c smile

    c "Alriiiiiighty… here you go! One slice of apple pie a la mode…"

    mc neutral b "Charlie-! This is amazing!"

    show c smile b 

    c "You really like it?"

    mc "You really like it?"

    c "Well shucks, thank you [player]! There’s plenty more where that came from, I promise! D’you wanna take the rest of it with you? Give some to Monica?"

    mc neutral "Sure, that sounds like a good idea. She’s bound to be a little grumpy when I get back. I left her in the hotel room and didn’t tell her the only thing on TV tonight was a Christmas movie marathon…"

    show c smile

    c "Oh yeah. You’ll need all the help you can get. Say, if you’re looking for something to do tomorrow while you’re in town… do you two want to hang out at the park tomorrow…?"

    mc confused "“Isn’t tomorrow the big, town-wide snowball fight?"

    c "Well, yeah-! But we wouldn’t have to participate! We could just watch.! Just thought it might be better than hanging out in your hotel room all day…"

    mc "Uh huh… when have you ever {b}just watched{/b} a snowball fight and not gotten involved Charlie?"

    show c smile b 

    c "“Okay, okay you got me. I’m definitely joining in. But you totally don’t have to! It’ll be a fun time either way. And besides… I’ll be bringing Bailey!"

    b "WOOF!"

    mc smile b "Alright, alright. I’ll talk to Monica and see if she wants to come. I’m sure she’ll be happy to get out of the hotel room at least."

    c "Definitely! It’ll be fun."

    scene bakery

    "After you finish your apple pie, you thank Charlie for the dinner and he leads you back towards the front door."

    show c smile

    c "Thanks again for coming, [player]. I had a really great time catching up!"

    mc neutral "Thank you again for having me! The food was excellent, and I enjoyed catching up too. And of course seeing you again, Bailey!"

    b "WOOF!"

    mc "Thanks, Bailey. I’ll see you both tomorrow at the park!"

    jump chapter2

label chapter2_charlie:
    scene markhall days
    
    "You decide to look for Charlie. It isn’t too hard to spot him, after all. He stands about a foot above everyone else. He’s laughing and slowly trudging his way back towards his igloo. You run off towards him."

    mc neutral coat b "Charlie!"

    show c smile b with dissolve

    "He beams at you."

    c "Hey, [player]! Having fun?"

    mc surprise coat "Yeah, it was a great time! I was just going to ask if- whoah!"

    show c surprise 

    "Your foot skids on a slippery patch of ice. Everything moves in slow motion for an instant as you fall towards Charlie. He reaches out his arms to catch you."

    "It would almost be romantic…"

    "…If he wasn’t a moment too late."

    "You fall face first onto a patch of ice like a klutz."

    scene black with fade

    "BONK!"

    "And go out like a light."

    jump chapter3_charlie

label chapter3_charlie:
    scene bakery with fade

    "The first thing you notice as you come to is something warm and wet against the side of your cheek."

    "Is… someone licking you?"

    "Then, a deep bark snaps you out of your semi-conscious state."

    b "WOOF~!"

    show c surprise with dissolve 

    c "Whoah! Whoah! Bailey, down girl! Cool it!"

    "Your eyes slowly blink open and when you look up Charlie is walking towards you with an ice pack in his hand."

    show c sad 

    c "“Oh! [player]. You’re awake…"

    "You try to sit up but a dull, painful {b}throb{/b} makes you wince."

    "Charlie rushes to your side and gently placed the ice pack against your bruised noggin."

    c "Whoah, whoah, hey, hold on there. You’ve got quite the bump there…"

    mc confused "What… happened…?"

    c "You, uh… slipped on some ice and kinda face planted…"

    show c neutral

    "You see the faintest twitch at the corner of his mouth. Is he holding back a laugh?"

    mc angry b "It’s nice to see you so concerned."

    show c neutral b

    c "Ah, don’t be mad. It was kinda cute until you hit the ground…"

    "You look into Charlie’s eyes and they twinkle with affection as he stares down at you."

    mc sigh b "Easy for you to say. You’re not the one who hit your head.."

    c "“I mean, if it makes you feel better, I’ve hit my head plenty of times."

    mc "You know, somehow, that doesn’t make it any better…"

    c "Yeah, yeah. I’m just glad you’re doing okay now. I would hate to be another reason you hate home…"

    mc confused b "“I don’t… hate Harkmall, Charlie."

    show c sad b

    c "Nah, I know. That… was a little harsh. I just.. I gotta say… You had fun today right? I mean, before the tumble"

    mc "Well, yeah, it was the most fun I’ve had in a long time."

    c "Then maybe you’ll start to remember what makes this town so great, [player]. It’s not… some tourist trap with cheesy attractions…"

    mc neutral b "I know that, Charlie-"

    c "Hold on, just - lemme finish. Harkmall… sure it’s only got one traffic light and maybe a slight obsession with Christmas… but the traditions we’ve got… they’re what make it special."

    c "We don’t need a big tourism buzz or a Starcups on every block. It’s the people here that make the town special. I… I really hope you, especially, can see that."

    mc sad b "Charlie…"

    c "“I mean, sure, you still live in the city. I’m not… trying to get you to move back home or anything - that’d be crazy - but I mean, maybe it wouldn’t be so bad if you came back to vi-"

    mc neutral "Charlie, the ice pack is leaking."

    show c surprise

    "Sure enough, a steady trickle of ice water had started to trickle down the back of your neck, sending shivers down your spine. "

    c "Oh! Jeez, I’m sorry, [player]. Here, lemme grab another."

    mc "No that’s okay, I… I should get going anyway. I’m sure Monica will be worried. If I have a concussion I won’t be able to catch the flight back with her. I should head to the doctor just to be safe."

    c "Oh- okay. Do you want me to give you a lift?"

    mc "No, that’s okay, you’ve done enough already, Charlie. Thanks a million. I…"

    mc open b "...I really appreciate it. Everything. You made this lame work trip a million times better. Honest."

    show c smile b 

    c "Glad I could help, [player]. Get back to your hotel safe, okay? Text me if you need anything."

    jump chapter4





    
