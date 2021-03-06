﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Akari")

define q = Character("?????")

define mcf = Character("McFonalds Manager")

define am = Character("Akari's Mom")

define ph = Character("Phone")

define ca = ("Cashier")

transform slightleft:
    xalign 0.25
    yalign 1.0

transform slightright:
    xalign 0.75
    yalign 1.0

transform center:
    xalign 0.5
    yalign 1.0

transform left:
    xalign 0.0
    yalign 1.0

transform right:
    xalign 1.0
    yalign 1.0

# The game starts here.

label start:

    scene bg black

    a "No... you can't go... please..."

    # show secretchar silhouette

    q "*sigh*"

    q "It was inevitable..."

    q "You all knew about it..."

    "  "

    scene bg mcoffice

    # show mcmanager normal

    mcf "I'm sorry, we can't accept you right now. Try applying next time."

    a "I see. Thanks anyways."

    # hide mcmanager normal

    "I left the restaurant manager’s office and decided to go home for the day."

    "There wasn’t really much to do since I just grabbed a quick bite before I got to this stupid interview."

    scene bg road sunset

    a "Man, this sucks..."

    scene bg icafe sunset

    "As I head home I spot an internet café, hesitating as to whether I should have a go or not."

    "Ah, screw it."

    a "Hm... it may not be a bad idea to play a game or two."

    "I wonder what kind of updates they made in RiFT."

    a "Let's see if I still got it. Fufu…"

    scene bg black

    " "

    scene bg icafe night

    "I left the internet café feeling confident after a couple hours of playing. not to mention a couple of wins."

    "I used to win all the time, but I’ve gotten rustier overtime since the last time I played."

    "I totally blame it on the new updates. Hmph."

    "But overall, I think my win-lose ratio is still god-tier, nevertheless~"

    a "Heh. Looks like I've still got it."

    "I walked my way from the internet café and back to my typical route home."

    scene bg road night

    "Honestly, I would be spending more time in there if I'd gotten a freaking job. Ughhhh."

    ph "*zzzzzzzz*"

    "My phone rang and I saw that it was my mother calling. I’ll bet a thousand yen my sister’s sick again."

    a "Oh, hi mom. Something the matter?"

    am "Akari, your sister needs medicine. Would you be so kindly to go get some for her?"

    "Ah."

    a "Itsuko’s sick again? Alright then, I’ll pass by the pharmacy ASAP."

    am "Thank you, dear."

    ph "*beep*"

    "The call ended, I immediately head to the pharmacy to buy medicine for Itsuko."

    scene bg pharmacy

    a "One pack of SoloFlu please."

    ca "Sure thing ma'am, one second..."

    "I wait for a couple of minutes as the cashier gets some medicine from the shelves."

    "I find myself jumbling through thoughts as my impatience bores me to death."

    "I can't help but think about everything."

    "What am I supposed to be doing right now? Is this where I'm supposed to be?"

    "Hm… Should I return to THAT scene? The pro sce-"

    ca "Here you go, Miss."

    "...and the cashier finally got the medicine."

    a "Thank you."

    scene bg road night

    "I paid the cashier and went on ahead to my mother's house to deliver Itsuko's medicine."

    scene bg moms house outside

    "I wonder how Itsuko's doing right now, though..."

    scene bg moms house inside

    a "Mom, I'm here."

    show akarismom

    am "Hi Akari. Thanks for coming so quickly."

    show akarismom at slightleft
    with move

    show akari at slightright
    with Dissolve(.25)

    a "How is she?"

    am "Your sister is fine for now. It’s just a simple flu. She will get better soon. You know how it is."

    a "Here you go."

    "I hand over the small paper bag with the medicines inside, and I was expecting her to take it, but..."

    am "You know, you should visit your sister and give these to her personally. She misses you a lot."

    a "I would, but I need to get home quickly, it's late now and all. And I have to get back to finding work too."

    am "*sigh* Next time, okay? It wouldn't hurt to talk to your sister a little."

    a "I know."

    hide akarismom
    with Dissolve(.25)

    show akari at center
    with move

    "I love my sister, but, to face her like this with what I am right now? I just wish I could be a better older sister to her right now."

    show akari at slightright
    with move

    show akarismom at slightleft
    with Dissolve(.25)

    a "Bye then. I'll be going home now."

    am "Be careful on your way. I love you, dear."

    a "Thanks, same here."

    scene bg moms house outside

    "I briskly walked away from my mom's house. Or rather, I should say, my old house. I thought it was an okay place to live, but it's the nostalgia from that place that really mattered."

    "Still, I made my choice to live on my own. I'm not really sure, I just felt like it."

    scene bg road night

    "Walking on the road home, I passed by that internet café once more."

    "Reeeeaaaally tempting to come back and play another round, but nah, I'll pass. I've gotten some more self-control getting older."

    "I made my way home to finally get some rest."

    scene bg akaris house bedroom night

    a "*sigh*"

    a "Haaaaaa~"

    "I’m glad this day is done and over with."

    "Maybe my luck will be better tomorrow..."

    "After I thought about that, I immediately fell asleep."

    scene bg akaris house bedroom morning

    "*ding-dong*"

    "I wake up to the sound of a doorbell ringing. What time is it?"

    "8 AM?! Who the hell gets up this early??"

    "I walk down the steps to get the door. Hmm... who could it be? I wasn't expecting anyone to be up nor be here this early. Very suspicious."

    "Opening the door, I find a guy rather sharply dressed but somewhat laidback too. You know, the type you'd find to be a young millionaire or something."

    a "Who are you?"

    q "Well, hello Akira. How are you today?"

    "Wait what?!"

    a "...h-how do you know that name?!"

    q "Who wouldn't know the number 1 RiFT player in all of Japan? The Legendary Akira!"

    a "Hold on there, I'm not this Akira lady you speak of..."

    q "Well, I'm pretty sure Akira is Akari Tsuki. And I'm pretty sure you came along to a bunch of our events back when we were sponsoring some RiFT events."

    q "And I'm pretty sure you did share your identity with some of the higher-ups for legal reasons. Which is why I know you."

    a "E-eh? Alright, a-anyways... come in. I'm assuming you wanna talk about something?"





    # show eileen happy
    return
