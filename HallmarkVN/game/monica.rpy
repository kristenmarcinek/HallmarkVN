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
