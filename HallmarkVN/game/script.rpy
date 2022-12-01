# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("Rowan")
define c = Character("Charlie")
define m = Character("Monica")


# The game starts here.

label start:

    $ proSingle = "they"
    $ proAdjective = "them"
    $ proPossessive = "theirs"
    $ proReflexive = "themselves"
    $ toBe = "are"

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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mc_neutral with dissolve

    label name:
        $ mc = renpy.input("What is your name?", "Rowan", length = 12)
        $ mc = mc.strip()
        $ mc = mc.title()
        if mc == "":
            $ mc = "Rowan"

    "You, [mc], are a junior reporter for Buzzread - the internet’s most popular news outlet specializing in 60-second viral news videos and hard hitting, investigative listicle journalism."
    
    "Your last listicle, {i}10 Starcups {b}Lattes Better{/b} Than Pumpkin Spice{/i} was a total flop. It turns out people {b}really{/b} like their PSL and aren’t ready to move on."

    show mc_sad

    "To make up for the dumpster fire that was your last listicle, your boss assigned you to work with Monica, a senior journalist at Buzzread."

    show m_neutral with dissolve

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
