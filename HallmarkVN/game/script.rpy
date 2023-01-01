# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[player]", color="#dead71", image="mc")
define c = Character("Charlie", color="#b55151")
define m = Character("Monica", color="#5ba84c")
define b = Character("Bailey")
define k = Character("Kid")

define n_nvl = Character("Nighten", kind=nvl, image="nighten", callback=Phone_SendSound)
define e_nvl = Character("Eileen", kind=nvl, callback=Phone_ReceiveSound)

#---BACKGROUNDS---
image office = "/bg/office.png"
image markhall day = "/bg/markhall day.png"
image bakery = "/bg/bakery.png"
image airport = "/bg/airport.png"
image hotel = "/bg/hotel.png"
image hotel outside = "/bg/hotel outside.png"
image charlie cg 2 = /cg/charlie cg 2.png
image monica cg 2 = /cg/monica cg 2.png

image credits = "/gui/menus/plain bg.png"

#---CG---
image monica cg 1 = "/cg/monica cg 1.png"
image charlie cg 1 = "/cg/charlie cg 1.png"
image monica cg 2 = "/cg/monica cg 2.png"
image charlie cg 2 = "/cg/charlie cg 2.png"

#---MONICA---
image m angry = "/monica/m angry.png"
image m angry b = "/monica/m angry b.png"
image m angry coat = "/monica/m angry coat.png"
image m angry coat b = "/monica/m angry coat b.png"

image m neutral = "/monica/m neutral.png"
image m neutral b = "/monica/m neutral b.png"
image m neutral coat = "/monica/m neutral coat.png"
image m neutral coat b = "/monica/m neutral coat b.png"

image m sigh = "/monica/m sigh.png"
image m sigh b = "/monica/m sigh b.png"
image m sigh coat = "/monica/m sigh coat.png"
image m sigh coat b = "/monica/m sigh coat b.png"

image m smirk = "/monica/m smirk.png"
image m smirk b = "/monica/m smirk b.png"
image m smirk coat = "/monica/m smirk coat.png"
image m smirk coat b = "/monica/m smirk coat b.png"

image m surprise = "/monica/m surprise.png"
image m surprise b = "/monica/m surprise b.png"
image m surprise coat = "/monica/m surprise coat.png"
image m surprise coat b = "/monica/m surprise coat b.png"

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

#charlie apron

image c angry apron = "/charlie/c angry apron.png"
image c angry apron b = "/charlie/c angry apron b.png"
image c neutral apron= "/charlie/c neutral apron.png"
image c neutral apron b = "/charlie/c neutral apron b.png"
image c sad apron = "/charlie/c sad apron.png"
image c sad apron b = "/charlie/c sad apron b.png"
image c smile apron = "/charlie/c smile apron.png"
image c smile apron b = "/charlie/c smile apron b.png"
image c surprise apron = "/charlie/c surprise apron.png"
image c surprise apron b = "/charlie/c surprise apron b.png"
image c wink apron = "/charlie/c wink apron.png"
image c wink apron b = "/charlie/c wink apron b.png"

# ---MC SPRITE---

#angry expression
image side mc angry = ConditionSwitch(
"appearance == 'fem'", "/mc/mc angry.png",
"appearance == 'masc'", "/mc male/mc mangry.png",
)

image side mc angry b = ConditionSwitch(
"appearance == 'fem'", "/mc/mc angry b.png",
"appearance == 'masc'", "/mc male/mc mangry b.png",
)

image side mc angry coat = ConditionSwitch(
"appearance == 'fem'", "/mc/mc angry coat.png",
"appearance == 'masc'", "/mc male/mc mangry coat.png",
)

image side mc angry coat b = ConditionSwitch(
"appearance == 'fem'", "/mc/mc angry coat b.png",
"appearance == 'masc'", "/mc male/mc mangry coat b.png",
)

#confused expression

image side mc confused = ConditionSwitch(
"appearance == 'fem'", "/mc/mc confused.png",
"appearance == 'masc'", "/mc male/mc mconfused.png",
)

image side mc confused b = ConditionSwitch(
"appearance == 'fem'", "/mc/mc confused b.png",
"appearance == 'masc'", "/mc male/mc mconfused b.png",
)

image side mc confused coat = ConditionSwitch(
"appearance == 'fem'", "/mc/mc confused coat.png",
"appearance == 'masc'", "/mc male/mc mconfused coat.png",
)

image side mc confused coat b = ConditionSwitch(
"appearance == 'fem'", "/mc/mc confused coat b.png",
"appearance == 'masc'", "/mc male/mc mconfused coat b.png",
)

#done expression
image side mc done = ConditionSwitch(
"appearance == 'fem'", "/mc/mc done.png",
"appearance == 'masc'", "/mc male/mc mdone.png",
)

image side mc done b = ConditionSwitch(
"appearance == 'fem'", "/mc/mc done b.png",
"appearance == 'masc'", "/mc male/mc mdone b.png",
)

image side mc done coat = ConditionSwitch(
"appearance == 'fem'", "/mc/mc done coat.png",
"appearance == 'masc'", "/mc male/mc mdone coat.png",
)

image side mc done coat b = ConditionSwitch(
"appearance == 'fem'", "/mc/mc done coat b.png",
"appearance == 'masc'", "/mc male/mc mdone coat b.png",
)

#neutral expression
image side mc neutral = ConditionSwitch(
"appearance == 'fem'", "/mc/mc neutral.png",
"appearance == 'masc'", "/mc male/mc mneutral.png",
)

image side mc neutral b = ConditionSwitch(
"appearance == 'fem'", "/mc/mc neutral b.png",
"appearance == 'masc'", "/mc male/mc mneutral b.png",
)

image side mc neutral coat = ConditionSwitch(
"appearance == 'fem'", "/mc/mc neutral coat.png",
"appearance == 'masc'", "/mc male/mc mneutral coat.png",
)

image side mc neutral coat b = ConditionSwitch(
"appearance == 'fem'", "/mc/mc neutral coat b.png",
"appearance == 'masc'", "/mc male/mc mneutral coat b.png",
)

#open expression

image side mc open = ConditionSwitch(
"appearance == 'fem'", "/mc/mc open.png",
"appearance == 'masc'", "/mc male/mc mopen.png",
)

image side mc open b = ConditionSwitch(
"appearance == 'fem'", "/mc/mc open b.png",
"appearance == 'masc'", "/mc male/mc mopen b.png",
)

image side mc open coat = ConditionSwitch(
"appearance == 'fem'", "/mc/mc open coat.png",
"appearance == 'masc'", "/mc male/mc mopen coat.png",
)

image side mc open coat b = ConditionSwitch(
"appearance == 'fem'", "/mc/mc open coat b.png",
"appearance == 'masc'", "/mc male/mc mopen coat b.png",
)

#sad expression

image side mc sad = ConditionSwitch(
"appearance == 'fem'", "/mc/mc sad.png",
"appearance == 'masc'", "/mc male/mc msad.png",
)

image side mc sad b = ConditionSwitch(
"appearance == 'fem'", "/mc/mc sad b.png",
"appearance == 'masc'", "/mc male/mc msad b.png",
)

image side mc sad coat = ConditionSwitch(
"appearance == 'fem'", "/mc/mc sad coat.png",
"appearance == 'masc'", "/mc male/mc msad coat.png",
)

image side mc sad coat b = ConditionSwitch(
"appearance == 'fem'", "/mc/mc sad coat b.png",
"appearance == 'masc'", "/mc male/mc msad coat b.png",
)

#surprise expression

image side mc surprise = ConditionSwitch(
"appearance == 'fem'", "/mc/mc surprise.png",
"appearance == 'masc'", "/mc male/mc msurprise.png",
)

image side mc surprise b = ConditionSwitch(
"appearance == 'fem'", "/mc/mc surprise b.png",
"appearance == 'masc'", "/mc male/mc msurprise b.png",
)

image side mc surprise coat = ConditionSwitch(
"appearance == 'fem'", "/mc/mc surprise coat.png",
"appearance == 'masc'", "/mc male/mc msurprise coat.png",
)

image side mc surprise coat b = ConditionSwitch(
"appearance == 'fem'", "/mc/mc surprise coat b.png",
"appearance == 'masc'", "/mc male/mc msurprise coat b.png",
)

#all half images

image mc angry = ConditionSwitch(
"appearance == 'fem'", "/mc/mc angry full.png",
"appearance == 'masc'", "/mc male/mc mangry full.png",
)

image mc confused = ConditionSwitch(
"appearance == 'fem'", "/mc/mc confused full.png",
"appearance == 'masc'", "/mc male/mc mconfused full.png",
)

image mc done = ConditionSwitch(
"appearance == 'fem'", "/mc/mc done full.png",
"appearance == 'masc'", "/mc male/mc mdone full.png",
)

image mc neutral = ConditionSwitch(
"appearance == 'fem'", "/mc/mc neutral full.png",
"appearance == 'masc'", "/mc male/mc mneutral full.png",
)

image mc open = ConditionSwitch(
"appearance == 'fem'", "/mc/mc open full.png",
"appearance == 'masc'", "/mc male/mc mopen full.png",
)

image mc sad = ConditionSwitch(
"appearance == 'fem'", "/mc/mc sad full.png",
"appearance == 'masc'", "/mc male/mc msad full.png",
)

image mc surprise = ConditionSwitch(
"appearance == 'fem'", "/mc/mc surprise full.png",
"appearance == 'masc'", "/mc male/mc msurprise full.png",
)

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

    "Choose your appearance!"

    menu:
        "masculine":
            $ appearance = "masc"

        "feminine":
            $ appearance = "fem"

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

    scene office


    show mc neutral
    with fade
    window show


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

    scene monica cg 1 with fade

    "Monica’s next big project was practically guaranteed to go viral: {i}The Top 10 Small Town Getaways That Will Have You Living Your Best “Christmas Movie Protagonist” LIFE. {/i}"

    m "Bitches love Christmas movies. Don't ask me why - I can't stand 'em - but this shit's bound to go viral!"


    "The two of you have spent the last month and a half traveling to every quaint town in New England, picking out the best bed and breakfasts."

    "The final stop on your little road trip just happens to be your hometown."
    $persistent.monica1=True

    scene markhall day with fade
    play music "Almost Christmas.mp3" fadein 1 fadeout 1

    "Harkmall, Massachusetts"

    "It’s a quiet, sleepy, little town with just one traffic light, nothing to do, and no reason for you to stay."

    "Your parents moved to Florida years ago to escape the cold winters and Seasonal Depression, and you hadn’t been back in years."

    "{i}Until today...{/i}"

    #scene showing_monica_around - kayla
    #do you want this to be a CG???

    show m neutral coat with dissolve

    #if i have time i can make special cut in images for this. IF I HAVE TIME. - kayla

    "You spend the day showing Monica around town. You’re on a tight schedule because your plane back to the city is that afternoon, but you manage to hit the biggest attractions:"
    "The giant Christmas tree in town square, the life-sized gingerbread house that gets fresh-baked every year, and..."

    "Most depressingly, the lake you used to go ice skating on that now doesn’t even freeze over half the time because global warming’s impending heat death of our planet."

    show m smile coat

    m "Holy shit, [player]. This place has everything. A snowman building contest? Sledding races? A town-wide snowball fight extravaganza? [player], you practically grew up in the {i}North Pole{/i}."

    #whenever you want the mc to show as a side image, use the speaker tag followed by the regular sprite image, in this case:
    #mc surprise "(dialogue)"

    #it's coded so that this sprite will not go away even when mc isn't speaking, but to clear it you can cheese it by using the scene function, bc that makes it disappear

    mc confused coat "Yeah. You take one too many snowballs to the face and the joy’s kind of lost on you."

    m "Yeah, no shit. I see why you got out of this hell hole. There isn’t even a Starcups. No wonder your last article sucked."

    mc angry coat "It wasn’t that bad…"

    show m smirk coat

    m "Yeah, it was. But don’t worry. Once we blow the lid off this sleepy, little snoozefest of a town, all the basic bitches will be crawling out of the woodwork to take their Christmas photos here and then there’ll be a Starcups on every block."
    m "And, you’ll be back on the boss’s good side!"

    mc neutral coat "Right. Let’s just get going. Our SuperLift is downstairs."

    scene airport with fade

    "The drive to the airport is a little over an hour. You and Monica get stuffed into the back of the SuperLift, during which the driver insists on blasting the latest Christmas album by Mike Bubbles."


    "By the time you finally get to the airport, a light flurry has started. Monica clutches her well-tailored suit jacket a little tighter to her."

    show m sigh coat with dissolve

    m "Fuck, it’s freezing. I’ll go check our bags. Will you get me a coffee? We should still have a little money on the company card…"

    hide m with dissolve

    "You turn and head towards the airport’s Starcups when you hear a deep, booming voice ring out behind you."

    c "[player]!? [player], is that you!?"

    scene charlie cg 1 with fade

    c "Holy smokes, it is you! [player]! How’ve you been?"

    mc coat "Uhhh… do I know you?"

    c "It’s me! Charlie! Charlie Baker from school!"

    "Holy crap! You used to play with a kid named Chucky when you were little. Looks like little Chucky Baker got BIG!"

    $persistent.charlie1=True

    scene airport with fade

    mc surprise coat "Chuck - I mean - Cha- Charlie?! You look… different!"

    show c smile with dissolve

    c "You haven’t aged a day! You look fantastic! How have you been?!"

    mc neutral coat b "Oh, you know. Good. Life’s good. Work is… work. You?"

    c "Oh, I hear that. My dad and I have been working overtime at the bakery now that it’s just the two of us. Say-! If you’re in town visiting you’ve totally gotta stop by. He would love to see you!"

    mc surprise coat "Oh-! No. I’m not staying. In fact, we were actually just leaving."

    show c sad

    c "Leaving? Ah jeez. You mean you haven’t heard?"

    mc confused coat "Heard what…?"

    c "A major blizzard blew through New York. Every flight headed that way has been-"

    scene airport
    show c sad
    with dissolve

    m "CANCELED?! WHAT DO YOU MEAN CANCELED?!"
    show c surprise

    show c surprise at left with ease
    show m angry coat at right with dissolve

    m "Unbelievable! The forecast called for clear skies! How’s a blizzard just appear out of thin air?!"

    show c smile at left

    c "It’s a Christmas miracle! The first white Christmas we’ve had in years! Maybe the lake will freeze thick enough to go skating."

    m "[player], who’s this?"

    mc open coat "Oh, this is Charlie. We went to school together. Charlie, this is Monica."

    c "Hiya, Monica!"

    show m neutral coat at right

    m "Pleasure to meet you, Charlie."

    "She doesn’t look too pleased."

    show m sigh coat at right

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
        show m neutral coat with dissolve

        m "Soooo… good news and bad news. Good news is, I got us a room. Bad news is, they already turned our old room over to some couple on their honeymoon."

        mc surprise coat "Okay… But we got a room, right? What’s the bad news?"

        m "Well, our old room was the last double. This room only has one bed. But, whatever. It’s fine, we’ll make it work. I’ll sleep on the floor."

        scene hotel with fade

        "You and Monica lug your bags up to the room and sure enough, there’s only one bed."

        show m sigh with dissolve

        m "I’m gonna shower, then we can talk dinner plans."

        hide m sigh with dissolve

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
        elif not called_superlift and not takeout:
            jump choice2_charlieA
        else:
            jump choice2_charlieB

    label chapter1:
        $ rng = renpy.random.randint(1, 2)
        if monica_affection > charlie_affection:
            jump chapter1_monica
        elif charlie_affection > monica_affection:
            jump chapter1_charlie
        else:
            if rng == 1:
                jump chapter1_monica
            if rng == 2:
                jump chapter1_charlie

    label chapter2:
        scene hotel with fade

        "The next morning."

        "Monica’s snoring rouses you. The woman seems to be as loud and brash asleep as she is awake."

        "You consider waking her up, but given the fact that you’re dragging her into a massive snowball fight in a town that’s a little too obsessed with Christmas, you decide to let her enjoy her peace for a little while longer."

        "Instead, you decide to hop up, get dressed, and stroll around town for a bit."

        scene markhall day with fade

        show mc neutral coat

        "It’s a nice walk. Quiet. You can’t remember the last time you experienced a morning this quiet. It’s nothing like the city."

        "As eager as you were to get out of the sleepy, little town, you have to admit it’s got its perks."

        "After about an hour of walking, which includes stopping into a local Mom and Pop shop for a cup of coffee and a bagel, you hear some commotion beginning a block over."

        "Just then, a little kid dragging a sled loaded up with pre-packed snowballs sprints past you."

        show mc surprise coat

        k "CHAAAAAARGE!"

        "Sounds like the Snowball Extravaganza is popping off."

        show mc neutral coat

        "When you arrive at the park a small crowd has already begun to gather. An assortment of people have turned up - from eager, excitable kids, to rowdy teenagers, and even small families."

        "The park has been turned into a veritable battle field of epic, snowy proportions."

        "It looks like some of the more overeager contenders have arrived early to set up fortifications - some have built small walls to duck behind, or trenches to get in."

        "It looks like someone even built a makeshift igloo in one corner - whoever it was must have gotten here at like 6:00 AM-!"

        scene markhall day

        c "Yo, [player], you made it!!"

        show c smile b

        "Suddenly, Charlie popped out of the hole in the top of the igloo, beaming brightly at you with a snowball in each hand."

        mc surprise coat b "Charlie?!"

        c "Look alive, [player]! Fire in the hole!"

        "Charlie suddenly lobbed one of the snowballs high into the air, clearly not caring where it may land."

        mc "Charlie, you- you built an {b}igloo{/b}?"

        show c wink b

        c "Well, yeah! Why not?"

        mc "This must have taken hours!"

        c "Ehhh a couple. But I had to wake up to take the early shift at the bakery anyway. Gotta get the buns in the oven at, like, 4:00 AM if we want them all ready in time for opening. I just skedaddled after they were done!"

        "Charlie chucks another snowball mid sentence that narrowly misses a middle-aged man running by."

        mc open coat b "This is insane! I don’t remember it being this popular when we were kids"

        show c smile

        c "“Well, yeah, that’s how holiday traditions work, right? You start one and then you teach your friends or kids, and then soon enough everyone’s doing it!"

        mc "I guess so."

        c "Hey- Where’s your friend?"

        "As if on cue you hear a scream from the edge of the park."

        m "MY COFFEE!!!"

        show m angry coat

        show c surprise

        mc surprise coat "Uh oh-"

        "You look over and see Monica scrambling in the snow, fumbling to retrieve a paper coffee cup whose contents have splattered all over the ground, turning a patch of snow dark brown and melting it quickly."

        "It looks like a stray snowball caught Monica in the arm and sent the cup flying."

        m "WHO THREW THAT?!"

        "You book it over to Monica, who has failed to salvage her cup of coffee… and looks to be seething hotter than the now-steaming patch of snow."

        mc neutral coat "Heyyyyy Monica… You made it!"

        "Monica looks up from the remnants of her ruined cup of coffee, clearly in distress."

        show m sigh coat b

        m "[player]! My coffee! It took half an hour for the hotel’s shitty coffee maker to brew a single cup! It’s not even a french press or anything. It’s just {b}drip{/b}! I {b}hate{/b} this place!"

        mc "Aww, Monica… I think it’s a little harsh to judge a whole town just for one shitty coffee maker, don’t you…?. Why don’t we get you out of the way. Last thing you need right now is a snowball to the face. C’mon. Charlie built an igloo…"

        m "You know I’m no good without my coffee, mc… I’d better just sit and watch."

        mc "Oh, come on. Just throw one snowball. It’ll make you feel better."

        m "I don’t know about that…"

        "You help Monica up and guide her back towards the igloo where Charlie is chucking snowballs with abandon."

        show c smile b

        c "Hey, Mon-! C’mon! Join the fun!"\

        show m surprise coat

        m "You built an entire igloo for just one snowball fight…?"

        c "Sure! Why not? There’s plenty of snow to go around!"

        m "It’s not the snow I was worried about. It just seems a tad… excessive."

        show m angry coat

        "You see Monica’s eyebrow twitch in anger but Charlie continues before she can go off on him."

        c "Sorry about that. Stop by the bakery next time, I always keep a fresh pot going!"

        m "Yeah, I’ll be sure to do that…"

        c "Anyway, you wanna toss a snowball?"

        m "I’ll pass."

        c "Aww c’mon. It’ll make you feel better. Avenge your shitty coffee!"

        "Monica stares at the snowball in Charlie’s hand for a long moment before finally taking it with a sigh."

        m "Fine."

        "She turns and lobs the snowball as hard as she can, pegging a teenager right in the face!"

        show m surprise coat b

        show c surprise

        m "Oops-"

        "But before she can apologize, the teenager lets out a battle cry and he and his friends start lobbing a volley of snowballs at you!"

        c "FIGHT FOR YOUR LIVES!"

        "Suddenly, you, Monica, and Charlie are thrust into the snow-slinging free for all."

        scene markhall day

        "The Snowball Extravaganza rages on as more and more people show up. Before you know it, you’ve passed half an hour of snow-slinging fun with your friends."

        "As more people show up, the park starts to get crowded. Eventually, you become separated from Monica and Charlie."

        "As the fun starts to wind down you decide it’s time to find your friends."

        menu:
            "Look for Charlie":
                $ findCharlie = True
                $ charlie_affection += 5
            "Look for Monica":
                $ findCharlie = False
                $ monica_affection += 5

        if findCharlie:
            jump chapter2_charlie
        else:
            jump chapter2_monica

    label chapter4:
        $ rng = renpy.random.randint(1, 2)
        if monica_affection > charlie_affection:
            jump monica_ending
        elif charlie_affection > monica_affection:
            jump charlie_ending
        else:
            if rng == 1:
                jump monica_ending
            if rng == 2:
                jump charlie_ending


    # This ends the game.

    return
