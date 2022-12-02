# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define u = Character("[player]", color="#b2315c", image="mc")
define c = Character("Charlie")
define m = Character("Monica")

# ---MC SPRITE---

# when we add the male sprite in later we're probably gonna have to put this under an if statement somehow

if appearance is 'fem' or appearance == 'fem':
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

elif appearance is 'masc' or appearance == 'masc':
    return

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

# The game starts here.

label start:

    $ proSingle = "they"
    $ proAdjective = "them"
    $ proPossessive = "theirs"
    $ proReflexive = "themselves"
    $ toBe = "are"

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
            alpha 1.0 xalign -.01 yalign 1.0
            linear 0.5 alpha 0.0 xalign -.01 yalign 1.0
        contains:
            new
            alpha 0.0 xalign -.01 yalign 1.0
            linear 0.5 alpha 1.0 xalign -.01 yalign 1.0

    define config.side_image_change_transform = change_transform

    # flash transition if we need it ig
    $ flash = Fade(.25, 0, .35, color="#fff")

# ---START---
    "Choose your appearance!"
    show mc neutral

    menu:
        "masculine":
            $ appearance = 'masc'
        
        "feminine":
            $ appearance = 'fem'

    hide mc neutral

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
    scene bg room


    show mc neutral with dissolve


    label name:
        $ player = renpy.input("What is your name?", "Rowan", length = 12)
        $ player = player.strip()
        $ player = player.title()
        if player == "":
            $ player = "Rowan"
    

    "You, [player], are a junior reporter for Buzzread - the internet’s most popular news outlet specializing in 60-second viral news videos and hard hitting, investigative listicle journalism."

    "Your last listicle, {i}10 Starcups {b}Lattes Better{/b} Than Pumpkin Spice{/i} was a total flop. It turns out people {b}really{/b} like their PSL and aren’t ready to move on."

    show mc sad

    "To make up for the dumpster fire that was your last listicle, your boss assigned you to work with Monica, a senior journalist at Buzzread."

    hide mc sad

    show m neutral with dissolve

    "Monica’s next big project was practically guaranteed to go viral: {i}The Top 10 Small Town Getaways That Will Have You Living Your Best “Christmas Movie Protagonist” LIFE. {/i}"

    show m_happy

    m "Bitches love Christmas movies. Don't ask me why - I can't stand 'em - but this shit's bound to go viral!"

    show m_neutral

    "The two of you have spent the last month and a half traveling to every quaint town in New England, picking out the best bed and breakfasts."

    "The final stop on your little road trip just happens to be your hometown."

    scene harkmall_landscape

    "Harkmall, Massachusetts"

    "It’s a quiet, sleepy, little town with just one traffic light, nothing to do, and no reason for you to stay."

    "Your parents moved to Florida years ago to escape the cold winters and Seasonal Depression, and you hadn’t been back in years."

    "{i}Until today...{/i}"



    # This ends the game.

    return
