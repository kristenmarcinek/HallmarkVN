label choice1_monica:
    show c neutral at left
    show m neutral coat at right

    mc neutral coat "Oh, that’s okay, Charlie. We can just put it on the company card."

    show c sad at left
    show m smirk coat at right

    m "Exactly! The good ol’ company card. So thanks anyway, Charlie!"

    c "Well, if you’re sure… But, hey, let me give you my number in case you need anything while you’re in town."

    "You exchange numbers with Charlie."

    mc neutral coat b "Got it. Thanks, Charlie."

    show m neutral coat

    m "Don’t worry about us, Charlie! Us city girls can take care of ourselves, right, [player]? Oh look - there’s our SuperLift! C’mon!"

    "You and Monica pile into the back of the SuperLift and head back to the hotel."

    scene hotel outside with fade

    "Back outside the hotel…"

    show m neutral coat with dissolve

    m "Alright. [player], you grab the bags and I’ll see if we can get our room back for a couple more nights."

    hide m with dissolve

    "You unload the bags out of the back of the SuperLift and bring them into the lobby."

    jump prologue_2

label choice2_monica:
    scene hotel outside with dissolve

    "You decide to take Monica up on her offer. After all, you’re traveling together, and she is your coworker. It makes more sense to have dinner with her than it does to reconnect with some rando from grade school…"

    show m neutral with dissolve

    mc neutral "Take out sounds great! You wanna call it in and I’ll run out and grab it?"

    show m smirk

    m "Sounds like a plan. Hurry back! I’m starving."

    jump chapter1

label chapter1_monica:
    scene hotel with dissolve

    "Evening."

    "You order take-out from the only Chinese restaurant in town: Panda Cafe. Luckily, it just so happens to be right around the corner so it’s a quick walk there and back."

    "Not only does it get you out of the cold quicker but the chances of you running into anyone else from high school today are slim to none. A win-win."

    "When you get back to the hotel room Monica is sitting cross-legged on the bed, clicking through TV channels."

    show m neutral with dissolve

    m "What the fuck is wrong with your hometown, [player]?!"

    mc confused b "What, you mean besides the fact that it’s a small town in the middle of nowhere?"

    m "Don’t get me wrong, it’s still a snoozefest but I’m past that. I’m talking about the {b}TV!{/b}"

    mc confused "What about it?"

    show m angry

    m "There’s {b}nothing but shitty Christmas movies on! Look!{/b}"

    "Sure enough, as Monica clicks through the channels your senses are bombarded by the gaudy, cheerful, tell-tell staples of the Christmas movie genre."

    "You see ugly sweater after ugly sweater, plaid, tinsel, wrapping paper, kisses under the mistletoe. Monica flips through 10 channels, just to get her point across - a different movie on each of them."

    mc neutral "Oh. Yeah."

    show m sigh

    m "You mean you {b}knew{/b} about this?"

    mc "I mean... yeah. They do it every year. You get the news in the morning and at night, but otherwise pretty much every channel is just… that crap."

    show m surprise

    m "But… why?!"

    mc neutral "I told you. They really, {b}really{/b} like Christmas here."

    m "Christ. No wonder you got out when you could…"

    show m neutral

    m "Pass me the wontons, would you?"

    "You and Monica begin divvying up your feast of Chinese takeout."

    mc confused "Wait - so if you hate Christmas so much… why are we writing this article? Wasn’t it your idea?"
    
    "Monica answers between chowing down bites of Chow mein."

    show m sigh

    m "I don’t hate Christmas. I hate fake Christmas."

    mc confused "Fake Christmas?"

    m "Yeah. It’s a bullshit time of year where you have to see family you hate and pretend to like them. It’s the small talk at holiday parties. It’s pretending to like hearing the same four Christmas carols on the radio."

    m "It’s exactly that kind of crap you see in Christmas movies. Where the protagonist leaves her awesome, wonderful, well paying job in the big city and decides to go live in some shithole town because some {b}guy{/b} smiled at her and gave her a cookie and suddenly she thinks she’s in love."

    m "Love doesn’t work that way. Life isn’t like that."

    show m angry

    "Monica stabs heatedly at a piece of chicken with her plastic fork."

    mc surprise b "Wow. I didn’t realize you felt that strongly about it."

    show m sigh

    "That’s because we only ever talk about work stuff."

    "You blink, stunned. She’s harsh, but she has a point. An awkward silence passes."

    menu:
        "You’re right. I’m sorry. This trip has kind of been all about my past. We haven’t really talked about you.":
            $ mSappy = True
            $ monica_affection -= 5
        "Stay silent.":
            $ mSappy = False
            $ monica_affection += 5
    if mSappy:
        jump chapter1_monica_A
    else:
        jump chapter1_monica_B

label chapter1_monica_A:
    mc sigh "You’re right. I’m sorry. This trip has kind of been all about my past. We haven’t really talked about you."

    show m angry b

    m "Don’t get all sappy on me now. I didn’t say that was a bad thing. I’m just saying it’s true. We’ve never really hung out for an extended period of time like this before."

    jump chapter1_monica_pt_2

label chapter1_monica_B:
    "You fall silent, unsure of what to say, so you decide to pick at a piece of chicken instead."

    show m sigh b

    m "...That came out bitchier than I meant it. Sorry."

    mc surprise b "Oh! That’s… That’s okay."

    m "I didn’t mean it in a bad way. I just mean we’ve never really hung out for an extended period of time like this before, you know?"

    jump chapter1_monica_pt_2

label chapter1_monica_pt_2:
    mc confused b "You’re right."

    show m smirk

    m "I usually am."

    mc neutral "Well, why don’t we fix that?"

    show m surprise

    m "Isn’t that what we’re doing right now?"

    mc "Well, yeah. But I mean tomorrow! All flights to New York are grounded so we have another day in town. Let’s spend it together and make a deal. No work talk"

    show m neutral

    m "Yeah, okay, I think I can agree to that."

    mc neutral "Tomorrow is the townwide snowball fight! We can go to that if you want!"

    show m angry

    m "Ugh. Isn’t there anything else to do in this town?"

    mc "Nope. It’s either snowballs or stay in and watch shitty Christmas movies."

    show m sigh

    m "Alright. Snowballs it is."

    mc "C’mon. It’ll be fine! First one to get hit in the face buys the hot chocolate?"

    show m smirk

    m "Oh you’re going down."

    scene hotel

    "The two of you pass the right of the night in peace, chatting about life, love, and anything except work."

    "At the end of the night, Monica insists you take the bed and decides to sleep on the floor."

    mc confused "Are you sure…? There’s plenty of room!"

    show m smirk with dissolve

    m "Yeah, it’s fine, trust me. I’m technically your supervisor right now. Sleeping in the same bed would be like an HR violation just waiting to happen. And what kind of boss makes their subordinate sleep on the floor? A bad one, that’s who."

    mc "Yeah, but…"

    show m neutral

    m "Shhh. Go to sleep. I’ll get payback when I deck you in the face with a snowball tomorrow."

    "With that, Monica flips off the lights and settles into the nest she made herself on the floor."

    mc neutral "Night, Monica…"

    m "Night, [player]"

    jump chapter2

label chapter2_monica:
    scene markhall days

    "You decide to look for Monica. It isn’t too hard to spot her. She seems to have shaken off the despair of losing her coffee in the heat of battle. She’s in the middle of the fray, laughing maniacally."

    mc smile coat b "“Monica!"

    show m smile coat b with dissolve

    "She grins at you."

    m "[player]! You were right! This was a blast."

    mc surprise coat "Yeah, it was a great time! I was just going to ask if- whoah!"

    show m surprise coat

    "Your foot skids on a slippery patch of ice. Everything moves in slow motion for an instant as you fall towards Charlie. He reaches out his arms to catch you."

    "It would almost be romantic…"

    "…If he wasn’t a moment too late."

    "You fall face first onto a patch of ice like a klutz."

    scene black with fade

    "BONK!"

    "And go out like a light."

    jump chapter3_monica

label chapter3_monica:
    scene hotel with fade

    "The sound of an angry phone call stirs you from unconsciousness. "

    m "Look, just get someone down here as soon as you can, okay?!"

    show m angry 

    "As your eyes flutter open you feel a dull pang in your forehead, followed by a cold sensation trickling down your temple."

    "You reach up and feel a washcloth clumsily tied into a little pouch with some loose ice inside set upon your forehead."

    mc confused b "Monica…?"

    m "Oh shit - ! [proSingle] [toBe] awake. Look, please just send someone when you can, okay? I gotta go…"

    "Monica ends the call abruptly and turns towards you."

    show m smirk b

    m "[player]! You’re awake! Are you feeling okay?"

    mc sigh "My head feels like it split open but otherwise fine…"

    m "Yeah, you took a rough fall there…"

    show m surprise b 

    "You look up and see Monica’s face suddenly filled with concern."

    mc "Don’t tell me… you were {b}worried{/b} about me, Monica?"

    show m angry b

    m "Don’t get ahead of yourself, mc. I was just… you know, you can’t fly if you have a concussion - which means if your dumbass concussed yourself that means we’re going to be stuck here even longer!"

    mc neutral b "Is that why you called the doctor…?"

    m "Obviously! I’ve gotta get us out of here pronto!"

    show m sigh b

    m "Okay, and yes, maybe I was a little worried about you. They said they don’t even do house calls anymore, but I yelled at them until they agreed to come down here. This crappy hotel doesn’t even have any ice packs. I had to improvise."

    mc "Wow… that’s… really sweet of you. Thanks, Monica."

    show m sigh 

    m "I know. I’m a goddamn delight."

    mc "Did you at least have fun today…?"

    m "Well, we’re not gonna talk about the coffee tragedy… but yeah, I guess I did have fun."

    show m neutral 

    m "This town isn’t as sleepy as I thought it was."

    mc neutral b "See! I knew you’d like the snowball fight!"

    show m smirk 

    m "Look, I just needed to let off a little steam from all the travel stress, okay? It’s not like I’m about to drop everything and move out here and become a… Harkmallian… Harkmaller… Whatever you call you freaks from this dumb town-!"

    mc done "I didn’t think you were, jeez…"

    m "Besides, this trip has been fun the entire time, not just in Harkmall."

    mc open "Yeah, I guess the other towns were pretty fun too…"

    show m angry b

    m "I’m talking about you, dummy-!"

    mc surprise b "Me…?"

    m "Yes, you!"

    show m sigh 

    m "Look. I don’t fucking like the holidays. At best they’re a capitalist cash grab and at their worst they’re just depressing reminders for anyone who doesn’t have anyone to spend them with."

    m "...I thought I was going to be alone this year since my ex and I got divorced. That’s why I took this stupid assignment in the first place. I was hoping it would distract me. But… then you got assigned to it as well…"

    mc sad "Monica…"

    show m sigh b 

    m "Look, don’t get all sentimental on me or anything. I’m just saying… I’ve had a lot of fun hanging out and getting to know you. You’re… you’re alright, [player]."

    mc open b "You’re… you’re alright too, Monica."

    show m smirk 

    m "I know, right? Alright, now lie back down and I’ll fill the rag with more ice from the bin down the hall… I want that noggin shrunk by the time the doctor gets here. We gotta clear you to fly, baby!"

    "Monica grabs the ice pack off your head, turns on her heel, and marches out the door."

    jump chapter4

label monica_ending:
    scene hotel outside with fade 

    "Luckily, that evening, Doctor Klaus from the county hospital, St. Nicholas’s, came by and cleared you for flying."

    "It was a miracle you weren’t concussed, but little miracles like that happen all the time in Harkmall, Massachusetts."

    "The next morning, Charlie is kind enough to drive you and Monica to the airport. "

    show c smile

    c "Mornin’ folks!"

    mc neutral coat "Hey Charlie, thanks so much for picking us up."

    c "My pleasure! Where’s Monica…?"

    mc "She’s just paying the bill, she should be out in a second."

    "You and Charlie load the bags up into the bed of his truck and a couple minutes later Monica walks out."

    show m angry coat

    m "You’d think at the rates we pay the least they could do is give us a decent fucking cup of coffee in the morning…"

    c "Oh, right, that reminds me-!"

    "Charlie opens the passenger’s side door and leans down to pick something up off the floor. When he turns around, he’s holding a drink tray with two piping hot cups of coffee."

    c "I brought ‘em over from the bakery!"

    show m surprise coat b

    m "For… us?"

    c "Of course! Dark blend and everything!"

    show m sigh b 

    m "Charlie. I owe you my life.."

    c "Aw don’t mention it."

    mc "Alright, are we ready to head out?"

    m "I think so!"

    c "Let’s roll. Though, someone’s going to need to sit in the back with Bailey…"

    b "WOOF~!"

    mc done coat "I got it…"

    show m smirk coat

    m "That’s okay, mc. You got shotgun last time. I’ll take a turn in the back."

    mc surprise coat b "Wait, really?"

    show m sigh coat

    "Anything is possible with a good dark roast."

    "The three of you load up into Charlie’s truck and begin the hour long trek out to the airport. The trip out there flies by much quicker than the one into town, and soon you’re pulling up to the Departure terminal after what feels like much too quick of a drive. "

    scene airport with fade

    show c smile at left

    show m neutral coat at right

    c "Welp! Here you go, folks! Safely delivered and ready to ship back to the big city."

    mc neutral coat "Thanks again, Charlie. I really appreciate it."

    m "Charlie, it has been a pleasure. Thanks for everything. Especially the coffee."

    c "Of course! Have a safe flight back, you two. And good luck with your article! If you’re ever back in town, don’t hesitate to call me up, okay?"

    mc "Will do!"

    c "Say bye, Bailey!"

    b "WOOF~!"

    "You and Monica make sure to give Bailey the requisite number of head pats before grabbing your bags out of the bed of the truck. With everything you need, Charlie gives you a thumbs up and pulls away."

    hide c smile at left

    mc "Alright, let’s head home, yeah?"

    show m surprise coat b

    m "Hang on a minute, [player]"

    mc open coat b "What's up?"

    show m sigh coat b

    m "I meant what I said yesterday. About how much fun I’ve had hanging out with you. Would you… I mean, do you want to keep hanging out when we’re back in the city…"

    mc surprise coat b "Hanging out…?"

    show m neutral coat b

    m "Yeah… Like… Not just coworkers."

    mc "Like… friends or…?"

    show m smirk coat b 

    m "Maybe like more than friends, if you wanted? I’d… I’d like to take you out on a real date. You know. We’ll go somewhere nice. Get some good noodles. Keep talking, is all."

    mc neutral b "...Yeah. Yeah, I’d like that a lot."

    m "Great! It’s a date"

    "Together, you and Monica head inside and catch your flight home."

    "The trip is a success and the article that came of it is a viral hit, just as promised. It doesn’t lead to quite the booming tourism economy for Harkmall that Monica envisioned… but it does bring the town its first Starcups. "

    "Your bosses at BuzzRead give you and Monica both big time bonuses. The first thing Monica does is take you out for a nice dinner at a world-class noodle joint."

    scene monica cg 2

    "The next year, the two of you spend Christmas together again. This time on a sunny beach in Puerto Rico, far, far away from snow."

    return





