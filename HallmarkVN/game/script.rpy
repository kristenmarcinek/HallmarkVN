# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[player]", image="mc")
define c = Character("Charlie")
define m = Character("Monica")
define b = Character("Bailey")

define n_nvl = Character("Nighten", kind=nvl, image="nighten", callback=Phone_SendSound)
define e_nvl = Character("Eileen", kind=nvl, callback=Phone_ReceiveSound)

#---BACKGROUNDS---
image office = "/bg/office.jpg"
image markhall day = "/bg/markhall day.jpg"
image bakery = "/bg/bakery.jpg"
image airport = "/bg/airport.jpg"

#---MONICA---
image m angry = "/monica/m angry.png"
image m angry b = "/monica/m angry b.png"
image m neutral = "/monica/m neutral.png"
image m neutral b = "/monica/m neutral b.png"
image m sigh = "/monica/m sigh.png"
image m sigh b = "/monica/m sigh b.png"
image m smirk = "/monica/m smirk.png"
image m smirk b = "/monica/m smirk b.png"
image m surprise = "/monica/m surprise.png"
image m surprise b = "/monica/m surprise b.png"

#---CHARLIE---
image c angry = "/charlie/c angry.png"
image c angry b = "/charlie/c angry b.png"
image c neutral = "/charlie/c neutral.png"
image c neutral b = "/charlie/c neutral b.png"
image c sad = "/charlie/c sad.png"
image c sad b = "/charlie/c sad b.png"
image c smile = "/charlie/c smile.png"
image c smile b = "/charlie/c smile b.png"
image c surprise = "/charlie/c surprise.png"
image c surprise b = "/charlie/c surprise b.png"
image c wink = "/charlie/c wink.png"
image c wink b = "/charlie/c wink b.png"

# ---MC SPRITE---

# when we add the male sprite in later we're probably gonna have to put this under an if statement somehow

# if chosen appearance is feminine
if appearance is "fem" or appearance == "fem":
    # side images
    image side mc angry = "/mc/mc angry.png"
    image side mc angry b = "/mc/mc angry b.png"
    image side mc confused = "/mc/mc confused.png"
    image side mc confused b = "/mc/mc confused b.png"
    image side mc done = "/mc/mc done.png"
    image side mc done b = "/mc/mc done b.png"
    image side mc neutral = "/mc/mc neutral.png"
    image side mc neutral b = "/mc/mc neutral b.png"
    image side mc open = "/mc/mc open.png"
    image side mc open b = "/mc/mc open b.png"
    image side mc sad = "/mc/mc sad.png"
    image side mc sad b = "/mc/mc sad b.png"
    image side mc surprise = "/mc/mc surprise.png"
    image side mc surprise b = "/mc/mc surprise b.png"

    # mc half images
    image mc angry = "/mc/mc angry full.png"
    image mc confused = "/mc/mc confused full.png"
    image mc done = "/mc/mc done full.png"
    image mc neutral = "/mc/mc neutral full.png"
    image mc open = "/mc/mc open full.png"
    image mc sad = "/mc/mc sad full.png"
    image mc surprise = "/mc/mc surprise full.png"

# if chose appearance is masculine
elif appearance is "masc" or appearance == "masc":
    return

# if nothing is chosen/it breaks
else:
    return

# ---COSMETIC STUFF---

# changing left and right positions
define right = Position(xalign=0.8)
define left = Position(xalign=0.2)

# in and out transitions for smooth sailing
define easeoutleft = ComposeTransition(dissolve, before=easeoutleft)
define easeinleft = ComposeTransition(dissolve, after=easeinleft)
define easeoutright = ComposeTransition(dissolve, before=easeoutright)
define easeinright = ComposeTransition(dissolve, after=easeinright)
define easeoutbottom = ComposeTransition(dissolve, before=easeoutbottom)
define easeinbottom = ComposeTransition(dissolve, after=easeinbottom)

# changing speed of dissolve transitions
define dissolve = Dissolve(.3)
define quickdissolve= Dissolve(.2)

# default affection variables
init python:
    monica_affection = 0
    charlie_affection = 0

# The game starts here.

label start:

    # default pronouns
    $ proSingle = "they"
    $ proAdjective = "them"
    $ proPossessive = "theirs"
    $ proReflexive = "themselves"
    $ toBe = "are"

    # default appearance
    $ appearance = "fem"


# side image code shit

    init python:
        config.side_image_tag = "mc"
        config.default_show_empty_window = True
        config.nvl_paged_rollback = True
        config.window_hide_transition = dissolve
        config.window_show_transition = dissolve
        style.nvl_window.xpadding = 55
        style.nvl_window.ypadding = 55
        style.nvl_vbox.box_spacing = 20
        config.side_image_only_not_showing = True
        config.side_image_same_transform = None
        renpy.save_persistent()

    transform change_transform(old, new):
        contains:
            old
            alpha 1.0 xalign 0.0 yalign 1.0
            linear 0.5 alpha 0.0 xalign 0.0 yalign 1.0
        contains:
            new
            alpha 0.0 xalign 0.0 yalign 1.0
            linear 0.5 alpha 1.0 xalign 0.0 yalign 1.0

    define config.side_image_change_transform = change_transform

    # flash transition if we need it ig
    $ flash = Fade(.25, 0, .35, color="#fff")

# ---START---

    #note to kayla (aka me): make this an imagemap or some shit in the future
    #note to kristen: i commented this out bc i figured for mike's demo we aren't using this feature, at least for now

    # "Choose your appearance!"

    # show mc neutral
    #
    # menu:
    #     "masculine":
    #         $ appearance = "masc"
    #
    #     "feminine":
    #         $ appearance = "fem"
    #
    # hide mc neutral

    "Choose your pronouns!"

    menu:
        "she/her":
            $ proSingle = "she"
            $ proAdjective = "her"
            $ proPossessive = "her"
            $ proReflexive = "herself"
            $ toBe = "is"

        "he/him":
            $ proSingle = "he"
            $ proAdjective = "him"
            $ proPossessive = "his"
            $ proReflexive = "himself"
            $ toBe = "is"

        "they/them":
            $ proSingle = "they"
            $ proAdjective = "them"
            $ proPossessive = "theirs"
            $ proReflexive = "themselves"
            $ toBe = "are"

    window show
    scene office


    show mc neutral with dissolve


    label name:
        $ player = renpy.input("What is your name?", "Rowan", length = 12)
        $ player = player.strip()
        $ player = player.title()
        if player == "":
            $ player = "Rowan"
        if player == "Charlie" or player == "Monica":
            "Please choose a different name."
            jump name


    play music "Office SFX.mp3" fadein 1 fadeout 1

    "You, [player], are a junior reporter for Buzzread - the internet’s most popular news outlet specializing in 60-second viral news videos and hard hitting, investigative listicle journalism."

    "Your last listicle, {i}10 Starcups {b}Lattes Better{/b} Than Pumpkin Spice{/i} was a total flop. It turns out people {b}really{/b} like their PSL and aren’t ready to move on."

    show mc sad

    "To make up for the dumpster fire that was your last listicle, your boss assigned you to work with Monica, a senior journalist at Buzzread."

    hide mc with dissolve

    show m neutral with dissolve

    "Monica’s next big project was practically guaranteed to go viral: {i}The Top 10 Small Town Getaways That Will Have You Living Your Best “Christmas Movie Protagonist” LIFE. {/i}"

    show m smirk

    m "Bitches love Christmas movies. Don't ask me why - I can't stand 'em - but this shit's bound to go viral!"

    show m neutral

    "The two of you have spent the last month and a half traveling to every quaint town in New England, picking out the best bed and breakfasts."

    "The final stop on your little road trip just happens to be your hometown."

    scene markhall day with fade
    play music "Almost Christmas.mp3" fadein 1 fadeout 1

    "Harkmall, Massachusetts"

    "It’s a quiet, sleepy, little town with just one traffic light, nothing to do, and no reason for you to stay."

    "Your parents moved to Florida years ago to escape the cold winters and Seasonal Depression, and you hadn’t been back in years."

    "{i}Until today...{/i}"

    #scene showing_monica_around - kayla
    #do you want this to be a CG???

    show m neutral with dissolve

    #if i have time i can make special cut in images for this. IF I HAVE TIME. - kayla

    "You spend the day showing Monica around town. You’re on a tight schedule because your plane back to the city is that afternoon, but you manage to hit the biggest attractions:"
    "The giant Christmas tree in town square, the life-sized gingerbread house that gets fresh-baked every year, and..."

    "Most depressingly, the lake you used to go ice skating on that now doesn’t even freeze over half the time because global warming’s impending heat death of our planet."

    show m smile

    m "Holy shit, [player]. This place has everything. A snowman building contest? Sledding races? A town-wide snowball fight extravaganza? [player], you practically grew up in the {i}North Pole{/i}."

    #whenever you want the mc to show as a side image, use the speaker tag followed by the regular sprite image, in this case:
    #mc surprise "(dialogue)"

    #it's coded so that this sprite will not go away even when mc isn't speaking, but to clear it you can cheese it by using the scene function, bc that makes it disappear

    mc confused "Yeah. You take one too many snowballs to the face and the joy’s kind of lost on you."

    m "Yeah, no shit. I see why you got out of this hell hole. There isn’t even a Starcups. No wonder your last article sucked."

    mc angry "It wasn’t that bad…"

    show m smirk

    m "Yeah, it was. But don’t worry. Once we blow the lid off this sleepy, little snoozefest of a town, all the basic bitches will be crawling out of the woodwork to take their Christmas photos here and then there’ll be a Starcups on every block."
    m "And, you’ll be back on the boss’s good side!"

    mc neutral "Right. Let’s just get going. Our SuperLift is downstairs."

    scene markhall day
    show m neutral
    with dissolve

    "The drive to the airport is a little over an hour. You and Monica get stuffed into the back of the SuperLift, during which the driver insists on blasting the latest Christmas album by Mike Bubbles."

    scene airport

    "By the time you finally get to the airport, a light flurry has started. Monica clutches her well-tailored suit jacket a little tighter to her."

    show m sigh with dissolve

    m "Fuck, it’s freezing. I’ll go check our bags. Will you get me a coffee? We should still have a little money on the company card…"

    hide m with dissolve

    "You turn and head towards the airport’s Starcups when you hear a deep, booming voice ring out behind you."

    c "[player]!? [player], is that you!?"

    show c smile with dissolve

    c "Holy smokes, it is you! [player]! How’ve you been?"

    mc confused b "Uhhh… do I know you?"

    show c surprise

    c "It’s me! Charlie! Charlie Baker from school!"

    "Holy crap! You used to play with a kid named Chucky when you were little. Looks like little Chucky Baker got BIG!"

    mc surprise "Chuck - I mean - Cha- Charlie?! You look… different!"

    show c smile

    c "You haven’t aged a day! You look fantastic! How have you been?!"

    mc neutral b "Oh, you know. Good. Life’s good. Work is… work. You?"

    c "Oh, I hear that. My dad and I have been working overtime at the bakery now that it’s just the two of us. Say-! If you’re in town visiting you’ve totally gotta stop by. He would love to see you!"

    mc surprise "Oh-! No. I’m not staying. In fact, we were actually just leaving."

    show c sad

    c "Leaving? Ah jeez. You mean you haven’t heard?"

    mc confused "Heard what…?"

    c "A major blizzard blew through New York. Every flight headed that way has been-"

    scene airport with fade

    show c surprise

    m "CANCELED?! WHAT DO YOU MEAN CANCELED?!"

    show c surprise at left with dissolve
    show m angry at right with dissolve

    m "Unbelievable! The forecast called for clear skies! How’s a blizzard just appear out of thin air?!"

    show c smile at left

    c "It’s a Christmas miracle! The first white Christmas we’ve had in years! Maybe the lake will freeze thick enough to go skating."

    m "[player], who’s this?"

    mc open "Oh, this is Charlie. We went to school together. Charlie, this is Monica."

    c "Hiya, Monica!"

    show m neutral at right

    m "Pleasure to meet you, Charlie"

    "She doesn’t look too pleased."

    show m sigh at right

    m "[player], I guess we’re grounded for a couple more days. We should get a SuperLift back to the hotel."

    c "Oh, don’t worry about that! I can give you both a ride back in my truck!"

    m "Oh, that’s okay, we wouldn’t want to {i}impose{/i} right, [player]?"

    c "Aw, it’s no big deal! Right, [player]?"

    menu:
        "Who should you go with?"

        "Call the SuperLift":
            $ called_superlift = True
            $ monica_affection += 5
            $ charlie_affection -= 5

        "Accept the ride from Charlie":
            $ called_superlift = False
            $ monica_affection -= 5
            $ charlie_affection += 5

    if called_superlift:
        jump choice1_monica
    else:
        jump choice1_charlie

    label prologue_2:
        show m neutral with dissolve

        m "Soooo… good news and bad news. Good news is, I got us a room. Bad news is, they already turned our old room over to some couple on their honeymoon."

        mc surprise "Okay… But we got a room, right? What’s the bad news?"

        m "Well, our old room was the last double. This room only has one bed. But, whatever. It’s fine, we’ll make it work. I’ll sleep on the floor."

        "You and Monica lug your bags up to the room and sure enough, there’s only one bed."

        show m sigh

        m "I’m gonna shower, then we can talk dinner plans."

        hide m sigh with dissolve

        scene hotel

        "You lay on your bed, doomscrolling through InstantPic, while Monica takes over the bathroom.  Mid-scroll, you get a text from Charlie. It’s a picture of an apple pie cooling on a kitchen counter."

        c "By the way, in case you don’t have dinner plans…"

        "An hour later, Monica comes out of the bathroom looking refreshed… and wearing a pantsuit nearly identical to the one she was wearing earlier that day."

        show m neutral with dissolve

        m "Christ, I needed that… Okay. You hungry?"

        mc done "Starving…"

        m "M’kay… let’s see what’s open. We don’t actually have a ton of money left on the company card… I used a lot of it to book this room for the next couple nights. But we could get some cheap take out if you want? My treat?"

        menu:
            "Who do you get dinner with?"

            "Get take out with Monica.":
                $ takeout = True
                $ monica_affection += 10
                $ charlie_affection -= 10

            "Take Charlie up on his offer.":
                $ takeout = False
                $ monica_affection -= 10
                $ charlie_affection += 10

        if takeout:
            jump choice2_monica
        else:
            jump choice2_charlie

    label chapter1:



    # This ends the game.

    return
