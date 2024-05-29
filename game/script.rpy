# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
#Code for resize character.

#akemi character
image akemi = im.Scale("akemi_def.png", 679, 900)
image akemi 2 = im.Scale("akemi_2.png", 679, 900)
image akemi 3 = im.Scale("akemi_3.png", 679, 900)
image akemi 4 = im.Scale("akemi_4.png", 679, 900)
image akemi 5 = im.Scale("akemib.png", 679, 900)
image akemi 6 = im.Scale("akemibs.png", 679, 900)
image akemi 7 = im.Scale("akemi_5.png", 679, 900)
image akemi 8 = im.Scale("akemi_HURT.png", 679, 900)
image akemi 9 = im.Scale("akemi_HURTS.png", 679, 900)
image akemi 10 = im.Scale("akemi_3N.png", 679, 900)
image akemi 11 = im.Scale("akemi_defws.png", 679, 900)
image akemi 12 = im.Scale("akemi_2ws.png", 679, 900)
image akemi 13 = im.Scale("akemi_4ws.png", 679, 900)
image akemi 14 = im.Scale("akemi_5ws.png", 679, 900)
image akemi 15 = im.Scale("akemibh.png", 679, 900)
image akemi 16 = im.Scale("akemibsh.png", 679, 900)
image akemi 17 = im.Scale("akemi_HURTB.png", 679, 900)
image akemi 18 = im.Scale("akemi_HURTBS.png", 679, 900)
image akemi 19 = im.Scale("Akemi_HB.png", 679, 900)
image akemi 20 = im.Scale("Akemi_HBS.png", 679, 900)
# Princess aoi
image princess = im.Scale("princess_def.png", 679, 900)
image princess 1= im.Scale("princess_1.png", 679, 900)
image princess 2 = im.Scale("princess_2.png", 679, 900)
image princess 3 = im.Scale("princess_3.png", 679, 900)
image princess 4 = im.Scale("aoib.png", 679, 900)
image princess 5 = im.Scale("aoibs.png", 679, 900)
image princess 6 = im.Scale("princess_2s.png", 679, 900)
image princess 7 = im.Scale("princess_3s.png", 679, 900)
# Himiko
image himiko = im.Scale("himiko_def.png", 679, 900)
image himiko 1= im.Scale("himiko_1.png", 679, 900)
image himiko 2 = im.Scale("himiko_2.png", 679, 900)
image himiko 3 = im.Scale("himiko_3.png", 679, 900)
image himiko 3 = im.Scale("himiko_3.png", 679, 900)
image himiko 4 = im.Scale("himiko_4.png", 679, 900)
image himiko 5 = im.Scale("himiko_3s.png", 679, 900)
# Elder
image elder = im.Scale("Elder_Elf.png", 1602, 900)
# Elder
image snake = "snake.png"
# Durin
image durin = im.Scale("durin.png", 1602, 900)
# King Throin
image throin = im.Scale("king throin.png", 1602, 900)
# Minion
image minion = im.Scale("minion.png", 1602, 900)
image minion1 = im.Scale("Villain_1.png", 1602, 900)
# Dragon
# image dragon = im.Scale("dragon_def.png", 679, 900)
# Elf Guard
# image elfguard = im.Scale("elfguard_def.png", 679, 900)
# Elder Elf
# image elderelf = im.Scale("elderelf_def.png", 679, 900)
# Dwarf
# image dwarf = im.Scale("dwarf_def.png", 679, 900)
# Generl Ragnor
image ragnor = "General_Ragnor.png"
# King Charles
image charles = "King_Charles.png"
#Necklace
image necklace ="Necklace.png"

#background
image bg forest1 = "forest1.png"
image bg forest1full = "forest1full.png"
image bg frontgateazure = "frontgateazure.png"
image bg deepforest = "deepforest.png"
image bg deepforestsword = "deepforestsword.png"
image bg cave1 = "caved.png"
image bg meetingelf ="meetingelf.png"
image bg incavegold ="incavegold.png"
image bg mountain = "mountain.png"
image bg dcave = "Deepcave.png"
image bg library1="library1.png"
image bg library2="library2 w door"
image bg outc = "outsidecastle.png"
image bg ruins = "ruin door.png"
image bg throne2 = "throne 2.png"
image bg throne1 = "king chair.png"
image bg smith = "blacksmith.png"
image bg cc = "crystalcave.png"
image bg ctr = "crystalnobg.png"
image bg dayelf= "dayelfvillage.png"
image bg nightelf= "nightelfvillage.png"
image bg fgdwarf = "frontgatedwarf.png"
image bg gatedwarf= "gatedwarf.png"
image bg outsidek = "outcastle.png"
image bg cavepurple = "incavegoldpurplesmoke.png"
image bg gcave ="incavegold.png"


init:
    transform flip:
        xzoom -1.0
init:
    transform unflip:
        xzoom 1.0
init:
    transform notspeaking:
        alpha .63
init:
    transform speaking:
        alpha 1
init:
    transform rightish:
        xalign +0.2
init:
    transform shaking:
        linear 0.1 xoffset -2 yoffset 2 
        linear 0.1 xoffset 3 yoffset -3 
        linear 0.1 xoffset 2 yoffset -2
        linear 0.1 xoffset -3 yoffset 3
        linear 0.1 xoffset 0 yoffset 0

#asset
image bg ring = "ring_final.png"
image bg sword = "sword.png"

define a = Character("Akemi",color="546569") 

define pra = Character("Princess Aoi",color="d8aec5") 

define h = Character("Himiko",color="546569") 

define n = Character("Narrator") 

define k = Character("King Throin") 

define s = Character("Snake") 

define g = Character("General Ragnor") 

define grdelf = Character("Elf Guard") 

define elder  = Character("Elfe Elder")

define dwarfgrd=Character("Dwarf Guard")

define durin=Character("Durin", color="#93502A")

define k = Character("King Throin" )

define min1 = Character("Minion 1")

define min2 = Character("Minion 2")

define c = Character("King Charles")

define dra =Character ("Draythorn")

define dragon =Character("Dragon")


# The game starts here.

label start:
    play music "library.mp3" loop
    scene black
    with None
    n"Summer has passed, and another school year is approaching. Students are excited as the new year will embrace them." 
    n"Everyone’s busy with their requirements. And there’s one student who made the room a bit odd as she walks on." 
    show akemi
    with Fade(.5,.5,.5)
    n"Akemi is an ordinary student. She always wears her jolliest smile." 
    scene black
    with Dissolve(.5)
    pause .5
    scene black
    with Dissolve(.5)
    scene bg library1
    with None
    n"School Day is done as she makes her way to her favorite spot, which is at the library, then she saw an old book." 
    n"Akemi picked it up and tried to read it but there is nothing from the book, there’s only a riddle." 
    show akemi 4 at left, flip 
    with dissolve
    a"Hmmm there's a riddle (It lights sometimes; it’s dark sometimes everyone wants to walk all over me. What am I?)" 
    hide akemi
    n"As Akemi read the riddle, she tries to answer it." 
    show akemi 3 at left, flip
    a"Hmmmmm......Moon?" 
    #Stop Music library.mp3
    stop music
    #Play Music branch1.mp3
    play music "branch1.mp3" loop 
    scene white 
    with Fade(.5,.5,.5)
    n"The book glows a bright light and Akemi closed her eyes" 
    n"Akemi heard that someone is calling her and as she slowly opens her eyes, she saw this mysterious woman." 
    #MUSIC STOP
    stop music 
    #MUSIC START
    play music "branch1.mp3" loop 
    scene bg ruins
    with Fade(.5,.5,.5)
    show princess 3
    "Mysterious" "Hero, please wake up..." 
    show akemi 3 at left, flip
    show princess 3 at right
    with move
    show princess 3 at notspeaking
    a"Huh? What happened... and who are you?" 
    show akemi at notspeaking
    show princess 1 at speaking
    "Mysterious" "Thanked God, you’re alright.... My name is Aoi, I am the daughter of King Charles and from the kingdom of Azurevale" 
    show princess 2
    pra"May i ask your name Hero"
    show akemi 2 at speaking
    show princess at notspeaking
    a"Hi, my name is Akemi.... Where am I?" 
    show akemi at notspeaking
    show princess 2 at speaking
    pra"Hero Akemi then... you are in the ruins forest"
    pra"This place is used to summon a hero from another world" 
    show akemi 3 at speaking
    show princess at notspeaking
    a"Huh? I am not a hero"
    a"I am just a regular student." 
    show akemi at notspeaking
    show princess 2 at speaking
    n"As Akemi seems confused, Princess Aoi tries to explain everything as she gradually understands the situation and Akemi asks another question." 
    show akemi 3 at speaking
    show princess at notspeaking
    a"I see, so that's what happened.... then why did you summon me here?" 
    show akemi at notspeaking
    show princess 3 at speaking
    pra"Please help me on my quest to defeat an evil magician that has been terrorizing my kingdom and my father..." 

    pra"Please help me..." 
    show princess at offscreenright
    show akemi at center, speaking
    with move
    n"Akemi has been too honest and always helping someone who needs her help even if she puts herself in danger." 
    show akemi at left
    with move
    show akemi 3
    a"...Okay, I'll help you Princess Aoi" 
    show akemi at notspeaking
    show princess 2 at right, speaking
    with move
    pra"Really? Thank you so much, hero Akemi." 
    show akemi 3 at speaking
    show princess at notspeaking
    a"It's fine.... and please stop calling me Hero Akemi. It's kind of embarrassing." 
    show akemi 2
    a"Just call me Akemi... " 
    show akemi at notspeaking
    show princess 2 at speaking
    pra"Okay.... Then you can call me Aoi, it’s so nice to meet you!" 
    show akemi 2 at speaking
    show princess at notspeaking
    a"Yeah, nice to meet you too." 
    hide akemi
    hide princess
    with dissolve
    #Stop Music branch1
    stop music fadeout 0.5
label branch_2:
    #BG MUSIC
    play music "forest2.mp3" loop
    play audio "bird.mp3" loop
    scene bg forest1
    with None
    n"As Akemi and Princess Aoi have decided to start their adventure journey…"
    show princess 2
    pra"Thank you for helping me Akemi."
    show princess -2 at right
    with move
    show princess at notspeaking, unflip
    show akemi 3 at left, flip
    a"It’s nothing, you are welcome.... So, are we going straight to kingdom of Azurevale? "
    show akemi -3 at notspeaking
    show princess 3 at speaking
    pra"No, Himiko is a powerful magician. A simple physical and magical attack won't hurt her."
    show akemi 3 at speaking
    show princess 3 at notspeaking
    a"So, how will I be able to beat Himiko then??"
    show akemi at notspeaking
    show princess 2 at speaking
    pra"We need to get the 3 legendary items that can only be wielded by a hero who came far from our world and that is you."
    show akemi 3 at speaking
    show princess at notspeaking
    a"So, what are those 3 legendary items?"
    show akemi at notspeaking
    show princess 2 at speaking
    pra"The first is the blade of Ethereal Fang; legend tells that it has been forged and blessed by the Ancient Gods and imbued with the power to pierce through darkness itself."
    pra"The second item is the Necklace of Valor; it is made by the most skilled dwarf and can increase physical and magical power to its full potential."
    show akemi 3 at speaking
    show princess  at notspeaking
    a"What about the third item?"
    show akemi at notspeaking
    show princess 3 at speaking
    pra" I can't tell you yet, because to get the last item. You must get the first two items."
    show akemi 3 at speaking
    show princess 3 at notspeaking
    a"I see..."
    show akemi at notspeaking
    show princess 1 at speaking
    pra"So, which of the two items do you want to get first?"
    hide princess
    hide akemi
    stop audio
    menu:
        "Blades of Ethernal Fang":
            $ menu_flag = True
            jump branch_3

        "Necklace of Valor":
            $ menu_flag = False
            jump branch_4
stop music fadeout 0.5
with dissolve
#Blade of Ethernal Fang
label branch_3:
    play music "yume1.mp3" loop 
    play audio "bird.mp3" loop
    scene bg forest1
    with None
    n "Ethereal Fang legend speaks that it is resting place deep within the heart of mystical forest known as the Whispering Woods and the location of the forest is only known by the elder elf which is located at Faewood."
    show princess 2 at left, flip
    pra"We must travel deep and explore here in Whispering Woods to meet the elder elf."
    hide princess
    with dissolve
    n "Upon reaching the guard gates of the Faewood, they met a vigilant sentry, wary of outsiders."
    scene bg dayelf
    with dissolve
    grdelf "Stop right there, who are you and state your business?"
    show princess 2 at left, flip
    n "As Aoi present herself with regal presence lending credibility and royal etiquette."

    pra"Good day to you Sir, I am Princess Aoi from the kingdom of Azurevale, we humbly request to meet and ask for guidance from the elder elf."

    grdelf "Wait here, I will ask for the chief of the village."

    n "As the time passed, Akemi and Princess Aoi have the approval of the village chief."

    grdelf "You may now enter and be careful."
    hide princess
    with dissolve
    n "As they entered the elf village, Akemi was amazed at the scenery of the elf village, especially with the giant tree in the center."
    show akemi 2 at left, flip
    a "Wow! Look at that tree, it looks bigger than the biggest building in my hometown."
    show akemi at notspeaking
    show princess 2 at right
    pra"Really? It was said that the tree has been here for thousands of years, and my father told me that it became the guardian of this forest."
    show akemi 2 at speaking
    show princess at notspeaking
    a "Amazing!"
    hide akemi
    hide princess
    with dissolve
    n "As they enter inside the giant tree, they are greeted by the elder of the elf village."
    scene bg meetingelf
    show elder
    elder "Greetings! Princess Aoi, you have grown much."
    show princess 2 at left, flip
    show elder:
        xalign 2.0 yalign 1.0
    with move
    show elder at notspeaking
    pra"It's nice to see you again!"
    show princess at notspeaking
    show elder at speaking
    elder "Hmm... Princess Aoi, are you doing okay? I heard what happened to your father and your kingdom."

    elder "You know that we have a great friendship with your ancestor and your father. I’m sorry to hear it."
    show princess 2 at speaking
    show elder at notspeaking
    pra"Thank you for your concern. Please allow me to introduce you to Akemi, the hero I brought to this world to defeat Himiko."
    hide princess
    show akemi 2 at left, flip
    a "Hello, it's so nice to meet you."
    show akemi at notspeaking
    show elder at speaking
    elder "Hmmm... I guess that you are here to ask us the location of the Blade of Ethereal Fang."
    hide akemi
    show princess 2 at left, flip
    pra"Yes, we would like to use it on defeating Himiko."
    show princess at notspeaking
    show elder at speaking
    elder "I will tell you the location, but it's very dangerous in the forest, and up until now many monsters have been wandering there."
    elder "Do you know how to fight them?"
    show princess 2 at speaking
    show elder at notspeaking
    pra"Yes"
    show princess at notspeaking
    show elder at speaking
    elder "And how about you, are you prepared to fight such a monster?"
    show elder at speaking
    show princess:
        xalign 1.15 yalign 1.0
    with MoveTransition(0.5)
    show princess at speaking
    show princess at unflip
    with None
    show akemi at left, flip
    n "They both looked at Akemi waiting for her response."
    show akemi 2 at speaking
    show princess at notspeaking
    show elder at notspeaking
    a "Yes, because I made a promise to Princess Aoi to help her."
    hide princess
    with dissolve
    show akemi at notspeaking
    show elder at speaking
    elder "Very well then, the location of the sword is located at the center of Whispering Woods..."

    elder "It is west from here, but recently there's a giant snake wandering, and we tried everything we could, but the monster can heal itself easily."

    elder "Princess Aoi, please be careful and look for each other and one more thing always go the center part of the forest because the monster won't go near that location of the sword." 
    show akemi 2 at speaking
    show elder at notspeaking
    a "Yes."
    hide akemi
    show princess 2 at left, flip
    pra"Okay, thank you so much! Yes, we will be more careful." 
    scene bg meetingelf
    n "As they started their quest on getting the sword, Akemi asked Princess Aoi..."
    show akemi 3 at left, flip
    a "Aoi, why did Himiko attack and want to claim your kingdom?"
    show akemi at notspeaking
    show princess 2 at right
    pra"Himiko is also a magic caster like me but instead of helping others, she used it for her personal gain, and became obsessed with gaining more power then, later fell into the darkness and wanted to control others through fear and power."
    show akemi 3 at speaking
    show princess at notspeaking
    a "So, she really is obsessed with gaining more power huh."
    stop audio
    stop music
    scene bg deepforest
    with dissolve
    play music"cbattle.mp3" loop
    show akemi at offscreenleft, flip
    show princess behind akemi at offscreenleft, flip
    with None
    show akemi at left
    show princess:
        xalign -0.2 yalign 1.0
    with move
    show snake at offscreenright
    with None
    show snake:
        xcenter 0.75 ycenter 0.52
    with move
    show akemi 4
    show princess 6
    with None
    n "As Akemi and Princess Aoi got closer to their destination, suddenly an angry giant snake attacked them..." 
    show akemi 4 at notspeaking
    show princess 6 at notspeaking
    s "(sssSSsss)"
    show snake at notspeaking
    show akemi 7 at speaking
    a "Ahh!"
    show akemi 7 at notspeaking
    show princess 6 at speaking
    pra"Ahh!"
    show akemi 7 at speaking
    show princess at notspeaking
    a "Are you okay, Aoi?!"
    show snake at offscreenright
    show princess at right
    with move
    show princess 2 at unflip
    show princess 6 at speaking
    show akemi 4 at notspeaking
    pra"Yes, I am fine."
    hide princess
    with dissolve
    show princess 6 behind akemi:
        xalign -0.2 yalign 1.0
        xzoom -1.0
        alpha 0.63
    with dissolve
    show snake at speaking
    show snake:
        xcenter 0.75 ycenter 0.52
    with move
    s "(sssSHAAaa)"
    show akemi at speaking
    show princess at speaking
    show akemi:
        linear 0.3 xalign -0.2 yalign 1.0
        "akemi 7"
        linear 0.2 xalign 0.0 yalign 1.0
    show princess 6:
        linear 0.2 xalign -0.75 yalign 1.0
    n "As they dodged from the attack of the giant snake, Akemi suddenly stumbled by a tree."
    show snake at notspeaking
    a "Ahh!"
    show snake at speaking
    show akemi 8
    n "Then the snake suddenly releases a purple smoke and let it out to Akemi"
    show akemi 8 at notspeaking
    s "(sssSSsss)"
    show akemi 8 at speaking
    show snake at speaking
    n "Akemi suddenly felt dizzy and weak with the smoke and the giant snake saw Akemi lie down on the ground"

    n "The giant snake tries to attack again as Akemi looked weak"
    show akemi 8 at notspeaking
    s "(sssSSHAAaa)"
    show princess 5:
        xalign -0.2 yalign 1.0
    pra"Akemi, Look out!!"
    show akemi 8 at offscreenleft
    with move
    show princess 4 at left
    with move
    n "As Princess Aoi saw Akemi can't move, she used her magic and attack the snake with fire"
    play audio "mstrike.mp3"
    show princess 5
    pra"Fireball!"
    play audio "fireact.mp3"
    show princess 4
    show snake at shaking
    n "As the giant snake got fired, it got distracted and Princess Aoi used the chance to see and help Akemi"
    show princess 4 at notspeaking
    s "(sssSSsss)"
    show princess 4 at speaking
    show snake at offscreenright
    show princess 4 at right
    with move
    show princess 5 at unflip
    pra"Are you alright, Akemi?"
    show akemi 9 at left, speaking
    with move
    show princess 4 at notspeaking
    a "Yeah, I am fine... I just feel a little dizzy."
    show akemi 8 at notspeaking
    show princess 5 at speaking
    pra"Let's retreat for now."
    show akemi 9 at speaking
    show princess 4 at notspeaking
    a "Yeah, you're right."
    show princess 4 at speaking
    with None
    show princess 4 at offscreenleft
    show akemi 8 at offscreenleft, unflip
    with move
    stop music
    show princess 3 
    play music "branch1.mp3" loop
    n "As they retreat far away from the monster for now, they rest for a bit."
    show princess 7 at center
    with dissolve
    pra"Are you okay, Akemi?"
    show princess 3
    n "As Princess Aoi asked Akemi if she is okay, she didn't get a respond."
    show princess 7
    pra"Akemi, Akemi hey are you okay?"
    show princess 3
    n "Princess Aoi shake Akemi and noticed something is strange on Akemi…"
    show princess 6
    pra"Huh!? Poison?"
    show princess 7
    pra"That is the content of the purple smoke that the snake released earlier."
    show princess 5
    pra"I must do something."
    show princess 4
    n "As soon as Princess Aoi knows that it is a poison, she began to sight an incantation for magic."
    show princess 5
    play audio "mstrike.mp3" fadein 0.5 fadein 0.5
    pra"Heal!"
    play sound "mheal.mp3" fadein 0.5 loop
    show princess 7
    pra"Yes, its working, are you okay now Akemi?"
    show princess 3
    with None
    stop sound fadeout 0.5
    show akemi 10 at left, flip
    with dissolve
    n "Suddenly Akemi began to open her eyes and see Princess Aoi was about to cry."
    show akemi 3
    show princess 3 at right
    with move
    show princess 3 at notspeaking
    a "Aoi, what happened?"
    show akemi 10 at notspeaking
    show princess 7 at speaking
    pra"Thank goodness you're okay... are you still injured?"
    show akemi 3 at speaking
    show princess 3 at notspeaking
    a "No, I think I am fine... What happened anyway?"
    show akemi 4 at notspeaking
    show princess 5 at speaking
    pra"You got poisoned!"
    show akemi 7 at speaking
    show princess 3 at notspeaking
    a "Oh, I see! Thank you for helping me."
    show akemi 4 at notspeaking
    show princess 7 at speaking
    pra"It’s okay, don't mention it."
    show akemi 4 at speaking
    show princess 4 at speaking
    play music "cbattle.mp3" loop

    n "As they rested for a bit, Akemi heard something rustling in the forest, and the giant snake appeared again."
    show princess 4 at center
    show snake:
        xcenter 1.0 ycenter 0.52
    with move
    s "(sssSSHAAaa)"
    show princess 4 at notspeaking
    show akemi 7 at speaking
    a "Aoi, look out!"
    show princess 6 at speaking
    show princess 6 at flip
    show akemi 4 at notspeaking
    pra"Ahh!"
    show princess 4 at unflip
    show akemi 4 at speaking
    show akemi 4 at unflip
    with None
    show princess 4 at offscreenleft
    show akemi 4 at offscreenleft
    show snake:
        xcenter 0.1 ycenter 0.52
        linear 0.3 xcenter 1.0 ycenter 0.52
    with move
    show akemi 5 at flip
    with None
    show akemi 5 at left, speaking
    with move
    n "Princess Aoi and Akemi were able to dodge from the snake attack."
    show princess 5 at flip
    with None
    show princess 5:
        xalign -0.2
    with move
    show akemi 5 at notspeaking
    pra"Be careful, Akemi!"
    show akemi 5 at center
    show princess 5 at left
    show snake at offscreenright
    with move
    show akemi 5 at unflip
    pra"Aoi we need to run deep in the forest. "
    show akemi 6 at right, speaking
    with move
    show princess 4 at notspeaking
    a "Yeah, you're right! The monster won't go near the location of the sword, we just need to make a diversion."
    show akemi 5 at notspeaking
    show princess 5 at speaking
    pra"I will cast support magic on you, to boost your agility and i will try to use my magic to make a diversion but it will take some time"
    play sound "mheal.mp3" fadein 0.5 fadein 0.5 loop
    pra"Akemi, I will cast a support magic on you, but I need some time."
    show akemi 6 at speaking
    show princess 4 at notspeaking
    a "Okay, got it, I’ll distract it to buy you sometime"
    show akemi 5 at left
    show princess 4 at notspeaking:
        xalign -0.2
    show snake:
        xcenter 0.75 ycenter 0.52
    with move
    show akemi 5 at flip
    show akemi 5 at notspeaking,
    s "(sssSSsss)"
    show akemi 5 at speaking,
    with None
    show princess at offscreenleft
    with move
    show akemi 5:
        linear 0.5 xoffset -200
        linear 0.5 xoffset 100
        linear 0.5 xoffset -250
        linear 0.5 xoffset 0 yoffset 0
        repeat
    n "As Akemi tries to distract the giant snake, Princess Aoi is preparing her magic on the side."
    hide akemi 5
    with dissolve
    show princess 5 at left, speaking
    with dissolve
    pra"I am ready, Akemi."
    show akemi 6 at left, flip
    hide princess 5
    a "Okay!"
    hide akemi 5
    show princess 5 at left, flip
    stop sound
    play sound "mstrike.mp3" 
    pra"Mega Flare!!"
    stop sound
    play sound "fattack.mp3"
    show snake at shaking
    show princess 4 at notspeaking
    s "(sssSSHAAaa)"
    show akemi 5 at offscreenleft, flip
    with None
    show akemi 5:
        xalign -0.2 yalign 1.0
    with move
    show princess 4 at speaking
    n "As the snake got attacked again by fire, Akemi rushed towards Princess Aoi."
    show akemi 6
    show princess 4 at notspeaking
    a "We did it! Let’s go."
    show snake at offscreenright
    stop sound fadeout 1.0
    show princess 4 at right
    show akemi 6 at left
    with move
    show princess 5 at speaking
    show princess 5 at unflip
    show akemi 5 at notspeaking
    pra"Yeah, but I can’t run that fast because I don’t have much energy left,  I’ve used all my magic power on that attack."
    show princess 4 at notspeaking
    show akemi 6 at speaking
    a "Okay then, I'll carry you. Let’s go."
    show princess 5 at speaking
    show akemi 5 at notspeaking
    pra"Thank you Akemi."
    show princess 4 at notspeaking
    show akemi 6 at speaking
    a "No worries."
    hide princess
    show princess 4 at right
    show akemi 5:
        linear 0.5 xalign 0.7 yalign 1.0
        xzoom 1,0
        pause (0.5)
    show princess 4:
        pause (0.5)
        linear 0.1 xoffset -2 yoffset 2 
        linear 0.1 xoffset 3 yoffset -3 
        linear 0.1 xoffset 2 yoffset -2
        linear 0.1 xoffset -3 yoffset 3
        linear 0.1 xoffset 0 yoffset 0
    pause (1)
    show akemi 5:
        linear 1 xalign -1.0 yalign 1.0
    show princess 4:
        linear 1 xalign -0.7 yalign 1.0
    n "Akemi carries Princess Aoi and ran fast at the center of the forest as much as they could."
    scene bg deepforestsword
    with dissolve
    stop music
    play music "branch1.mp3" loop
    pause (1)
    show akemi 2:
        xzoom -1.0
        xalign -1.0 yalign 1.0
        linear 1 xalign 0.0 yalign 1.0
    show princess behind akemi:
        xzoom -1.0
        xalign -1.2 yalign 1.0
        linear 1 xalign -0.2 yalign 1.0
    a "AAHHH! We made it!"
    show akemi:
        xzoom -1.0
        xalign 0.0 yalign 1.0
        linear 1 xalign 1.0 yalign 1.0
        xzoom 1.0
        alpha 0.63
    show princess 2 behind akemi:
        xzoom -1.0
        xalign -0.2 yalign 1.0
        linear 1 xalign 0.0 yalign 1.0
    pra"Yeah!"
    show akemi at speaking
    show princess at speaking
    n "As they got in the center of the forest, Akemi look at the sword"
    show akemi 3 at speaking
    show princess at notspeaking
    a "So, that is the Blade of Ethereal Fang"
    show akemi at notspeaking
    show princess 2 at speaking
    pra"Yes, go on Akemi, try to pull it."
    show akemi 2 at speaking
    show princess at notspeaking
    a "Yeah okay, let’s do this."
    hide princess
    with dissolve
    show akemi:
        linear 0.5 xalign 0.8
    n "As Akemi approaches to the sword, she can already feel the power and wonders if this is the reason why the monster can’t go near it,"
    show akemi 7
    n "As Akemi holds the sword, she felt warm feelings all over her body."
    show akemi 3
    a "Here’s go nothing on trying."
    show akemi:
        pause(0.2)
        "akemi 4"
        linear 0.3 xalign 1.0
    pause(0.6)
    scene bg sword
    show akemi 4 at right
    with dissolve
    n "As soon as Akemi tried to pull the sword, she felt it was too light."
    show akemi 7
    a "Yes! Look Aoi, I did it! I pulled the sword."
    show akemi
    show princess at offscreenleft, flip
    with None
    show princess 1 at left
    with move
    n "Princess Aoi looked at Akemi and smiled."
    show princess 2
    show akemi at notspeaking
    pra"Yes, you did it!"
    show princess at notspeaking
    show akemi 2 at speaking
    a "Let's rest here for a while, are you still tired?"
    show princess 2 at speaking
    show akemi at notspeaking
    pra"Yes, thank you for asking."
    scene black
    with Dissolve(1.0)
    n "Akemi and Princess Aoi finally rested for a bit. They are now trying to go back to the elf village once again."
    scene bg deepforest
    with dissolve
    show akemi 12:
        xzoom -1
        xalign -0.5 yalign 1.0
        linear 1.0 xalign 0.0 yalign 1.0
    a "Finally, we got the Blade of Ethereal Fang. We’re close in saving your Kingdom, Aoi."
    show akemi 11:
        xalign 0.0 yalign 1.0
        linear 1.0 xalign 1.0 yalign 1.0
        xzoom 1
    show princess 2:
        xzoom -1
        xalign -0.5 yalign 1.0
        linear 1.0 xalign 0.0 yalign 1.0
    
    pra"Yes."

    stop music
    #SNAKE
    show akemi 11:
        xalign 1.0 yalign 1.0
        linear 0.7 xalign 0.4 yalign 1.0
        alpha 0.63
    show princess 2:
        alpha 0.63
    show snake:
        xcenter 2.0 ycenter 0.52
        linear 1.0 xcenter 1.0 ycenter 0.52
    play music "cbattle.mp3" loop
    s "(sssSSsss)"
    show akemi 11:
        alpha 1.0
        xalign 0.4 yalign 1.0
        linear 0.5 xalign 0.0 yalign 1.0
        xzoom -1
        "akemi 5"
    show princess 2 behind akemi:
        linear 0.5 xalign -0.2 yalign 1.0
        alpha 1.0
        "princess 4"
    show snake:
        xcenter 1.0 ycenter 0.52
        linear 0.5 xcenter 0.75 ycenter 0.52
    n "Akemi and Princess Aoi chatting, the snake appears again on their way."
    show akemi 6
    show princess 4 at notspeaking, offscreenleft
    show snake at notspeaking
    with move
    a "Aoi, be careful. Let's defeat this giant snake for real this time."
    show princess 5 at speaking, left
    hide akemi
    pra"Right!"
    show akemi 6 at offscreenleft, flip
    with None
    show akemi 5 at left
    show snake at speaking, offscreenright
    show princess 4 at right
    with move
    show princess 4 at unflip
    n "Akemi proposes a plan on how to fight the giant snake…"
    show akemi 6
    show princess 4 at notspeaking
    a "Use your magic and support me as I will draw its attention. Try to use fire magic only."
    show akemi 5 at notspeaking
    show princess 5 at speaking
    pra"Okay"
    show akemi 5:
        alpha 1
    show princess 4 behind akemi:
        linear 0.8 xalign -0.7 yalign 1.0
        xzoom -1
    show snake:
        alpha 1
        xcenter 2.0 ycenter 0.52
        linear 1.0 xcenter 0.75 ycenter 0.52
    s "(sssSSsss)"
    show akemi 5:
        linear 0.5 xoffset -200
        linear 0.5 xoffset 100
        linear 0.5 xoffset -250
        linear 0.5 xoffset 0 yoffset 0
        repeat
    n "Akemi draws the attention of the snake and Princess Aoi used fire magic to make the giant snake more confused."
    n "Because of this, the giant snake tries to use the purple smoke and Princess Aoi used her support magic for Akemi resists to be poised just a short of time"
    play sound "fattack.mp3"
    hide akemi
    show princess 5 at left:
        linear 0.0 xoffset 0 yoffset 0
    pra"Now is your chance, Akemi."
    hide princess
    show akemi 6 at flip:
        xalign 0.0 yalign 1.0
        linear 0.2 xalign 0.25 yalign 0.5
        linear 0.2 xalign 0.5 yalign 1.0
        linear 0.2 xalign 0.0 yalign 1.0
    a "Right, HYAAAA!"
    show akemi 5:
        alpha 0.63
        xzoom -1
    s "(sssSSHAAaa)"
    show akemi 5 at speaking
    hide snake
    with Dissolve(1.0)
    stop sound
    stop music
    play music "forest2.mp3" loop
    n "Akemi jumps high and goes directly to attack the head of the snake. As she swings her sword to the head, it lands on the giant snake's head."
    show akemi 12 at speaking
    a "Wow, this sword cut it like paper... we did it Aoi!"
    show akemi 11 at notspeaking
    show princess 2 at right
    pra"Yeah... that was amazing Akemi!"
    show akemi 12 at speaking
    show princess at notspeaking
    a "Let's go back to the elf village now."
    show akemi 11 at notspeaking
    show princess 2 at speaking
    pra"Yeah."
    scene bg dayelf
    with dissolve
    show akemi 11:
        xzoom -1
        xalign -0.5 yalign 1.0
        linear 1.0 xalign 0.2 yalign 1.0
    show princess behind akemi:
        xzoom -1
        xalign -0.7 yalign 1.0
        linear 1.0 xalign 0.0 yalign 1.0
    n "Akemi and Princess Aoi got in front of the elf village. The elves were surprised to see that Akemi is holding the Blade of Ethereal Fang"
    show elder:
        xalign 2.0 yalign 1.0
    with dissolve
    elder "I am so glad that you are safe Princess Aoi and Akemi."
    hide akemi
    with dissolve
    show princess 2
    show elder at notspeaking
    pra"Thank you."

    n "Princess Aoi explained what happened, they are relieved and surprised because they were able to slay the giant snake."
    show princess at notspeaking
    show elder at speaking
    elder "I have been trying to find out for a long time how did that snake appeared out of nowhere and how it releases purple smoke."
    show princess 6 at speaking
    show elder at notspeaking
    pra"Himiko must be the one behind it. She must be trying to stop someone who will search for the sword."
    show princess at notspeaking
    show elder at speaking
    elder "It must be.... but the sword can’t be pulled by a normal person, Akemi."
    hide princess
    show akemi 3 at left, flip
    show elder at notspeaking
    a "Yes."
    show akemi at notspeaking
    show elder at speaking
    elder "The sword chooses you to be its user. Please use it only for good."
    show akemi 2 at speaking
    show elder at notspeaking
    a "I will."
    show akemi at notspeaking
    show elder at speaking
    elder "I assumed that the two of you will continue your journey, we will all pray for your success and safety, good luck Akemi and Princess Aoi."
    show akemi 2 at speaking
    show elder at notspeaking
    a "Thank you!"
    hide akemi
    show princess 2 at left, flip
    pra"Thank you!"
    show elder at speaking
    show akemi behind princess:
        xzoom -1
        xalign -0.2 yalign 1.0
    with dissolve
    pause(0.5)
    show princess behind akemi:
        xzoom 1
        xalign 0.0 yalign 1.0
        linear 1.0 xalign -0.8 yalign 1.0
    show akemi:
        xzoom 1
        xalign -0.2 yalign 1.0
        linear 1.0 xalign -1.0 yalign 1.0
    n "Akemi and Princess Aoi say goodbye to the elf village as they take off on their next journey."
    if menu_flag == False:
        jump branch_5
    elif menu_flag == True:
        jump branch_4
stop music
with dissolve

#Necklace of Valor
label branch_4:
    stop music
    # play music "Arrraivesound.mp3" loop 
    scene black
    with dissolve
    n"As Akemi and Princess Aoi set their journey to get the Necklace of Valor from the dwarf kingdom which is from the Ironforge mountain."
    scene bg fgdwarf
    show princess 2
    with dissolve
    pra"We need to travel to the Ironforge mountain then go to their kingdom to meet their King Throin."
    pra"We can easily go inside and meet King Throin because he and my father are friends."
    show akemi 2 at left, flip
    show princess 2 at right
    with move
    show princess at notspeaking, unflip
    a"I am excited to enter the dwarf kingdom, it's like a real fantasy."
    show akemi at notspeaking
    show princess 2 at speaking
    pra"Yes, and I also have a friend in the kingdom."
    show akemi at speaking
    with dissolve
    n"Akemi and Princess Aoi got closer to the entrance of the the dwarf kingdom."
    with dissolve
    scene bg gatedwarf
    show princess 2
    with fade
    pra"Here we are, at the Ironforge Kingdom."
    show  princess at right, notspeaking
    with move
    show akemi 2 at left,flip
    a"Wow! look at the size of the wall and the gate is so huge."
    show princess at offscreenleft, speaking
    show akemi at offscreenleft
    with dissolve
    show akemi behind princess:
        xalign -0.3
    show princess at left, flip
    with move
    n"As Akemi and Princess Aoi got closer. One of the guards recognized Princess Aoi."
    show princess at notspeaking
    show durin:
        xalign 2.0
        yalign 1.0
    hide akemi
    with dissolve
    dwarfgrd"Princess Aoi, is that you? Thanked God, you are safe. It’s been too long." 
    show durin at notspeaking
    show princess 1 at speaking
    n"Princess Aoi returns to the dwarf with a smile, her relief evident as she explains their quest to retrieve the Necklace of Valor to save her kingdom from the encroaching darkness by Himiko."
    pra"It has been too long indeed, Durin."
    show durin at speaking
    show princess at notspeaking
    durin"What brings you here to Ironforge, ts she your companion?"
    show durin at notspeaking
    show princess 2 at speaking
    pra"Yes, she is also my friend, and the hero who’s summoned."
    hide princess
    show akemi 2 at left, flip
    a"Hello, nice to meet you Durin."
    show akemi at notspeaking
    show durin at speaking
    durin"Nice to meet you too."
    hide akemi
    show durin at notspeaking
    show princess 2 at speaking, left, flip
    pra"We came hoping to meet King Throin and ask for the Necklace of Valor to help me and the hero to defeat Himiko that invaded our Kingdom."
    show durin at speaking
    show princess at notspeaking
    n"Durin nods and promise to Princess Aoi"
    
    durin"Fear not, Princess Aoi. As your friend and ally, I shall see to it that you and your companion are granted an audience with King Throin."
    show durin at notspeaking
    show princess 2 at speaking
    pra"Thank you, Durin."
    scene bg outsidek
    with fade
    n"With Durin’s guidance, Akemi and Princess Aoi are escorted through the bustling street of Ironforge."
    show akemi 2 at flip, center
    a"Look at the busy street Aoi, there are a lot of weapons displays, beautiful jewelries and shining armors. It’s really like a fantasy."
    show akemi at left, notspeaking
    with move
    show princess 2 at right
    with dissolve
    pra"Yes, there's a lot of people than the last time I visited here."
    scene bg throne1
    with fade
    n"As they approached the imposing gate of the royal castle, Akemi and Princess Aoi were able to meet King Throin."
    show throin
    k"Welcome, it is an honor to meet you once more and to meet your esteemed companion."
    show throin at notspeaking:
        xalign 2.0
    with move
    show princess at left, flip
    pra"It's an honor to meet you too King Throin, allow me to introduce my companion, her name is Akemi, and she is the summoned hero."
    hide princess
    show akemi at speaking, left, flip
    a"It's a pleasure to meet you, King Throin."
    show throin at speaking
    show akemi at notspeaking
    n"King Throin regarded Akemi with a solemn gaze, acknowledging the hero's presence with a hint of respect."
    show throin
    show akemi at notspeaking
    k"Akemi, it's an honor to meet you."
    show throin at notspeaking
    hide akemi
    show princess at left, flip
    n"Princess Aoi continued her tone urgently."
    pra" Your Majesty, we seek your aid in offering us the Necklace of Valor."
    stop music
    show throin at speaking 
    show princess at notspeaking
    play music "falls.mp3" loop
    k"I fear I must deliver grim tidings."
    
    n"The king tells them with heavy sorrow."
    
    k"The Necklace of Valor was stolen and destroyed from us by one of Himiko’s men in the past few months by General Ragnor, a cunning and ruthless adversary."
    show princess 3 at speaking
    n"Princess Aoi’s heart sank at the news, but before she could despair, King Throin spoke again, his tine resolute."
    show princess 3 at notspeaking
    stop music
    play music "goodnews.mp3" fadein 0.5 fadeout 0.5 loop
    k"However, there’s another way. We can forge a new necklace, one that is more powerful than its predecessor."
    show princess 2 at speaking
    n"A glimmer of hopes sparked within Princess Aoi’s heart at the King's words, but their joy was short-lived as the ground tremble beneath their feet a harbinger of impending danger."
    stop music
    hide princess
    hide throin
    show durin
    play music "fighsoundef2.mp3" fadein 0.5 fadeout 0.5 loop
    durin"We are under attack!"
    show akemi 5 at offscreenleft, flip
    show princess 4:
        xalign -1.3
        yalign 1.0
        xzoom -1
    with None
    show durin at offscreenright, flip
    show akemi 5:
        xalign 2.0
        yalign 1.0
    show princess 4 at offscreenright
    with MoveTransition(1)
    n"One of the guards shouted, with resolved in their hearts Akemi and Princess Aoi rushed to defend Ironforge with their swords drawn and their magic ablaze"
    scene bg gatedwarf
    show minion as minion1:
        xalign 2.0
        yalign 1.0
    show minion as minion2:
        xalign 3.5
        yalign 1.0
    show akemi 5 at offscreenleft, flip
    show princess 4 at offscreenleft, flip
    show durin at offscreenleft, flip
    with None
    show akemi 5:
        xalign 0.2
        yalign 1.0
    show princess 4 behind akemi:
        xalign 0.1
        yalign 1.0
    show durin behind akemi, princess:
        xalign -2.0
        yalign 1.0
    with move
    n"Outside the castle walls, they were met with a horde of monstrous creatures, their eyes filled with malice and hunger for battle."
    show akemi 5:
        xalign 0.15
        yalign 1.0
    show princess 4 behind akemi:
        xalign 0.0
        yalign 1.0
    with move
    hide durin
    with dissolve
    pause(0.5)
    hide minion1
    with dissolve
    pause(0.5)
    hide minion2
    with dissolve
    n"As Akemi and Princess Aoi fought bravely against the onslaught, King Throin approached them with a grim expression." 
    show throin at offscreenright:
        yalign 1.0
    with move
    show throin:
        xalign 2.0
        yalign 1.0
    with move
    
    k"Our enemies seek the gemstone needed to forge for the new necklace."
    
    k"It lies deep within the mining caves, but the entrance is heavily guarded by General Ragnor's minions."
    scene bg dcave
    show princess at offscreenleft, flip
    pause(0.2)
    show princess at right
    with MoveTransition(1.5)
    show akemi at offscreenleft
    pause(0.2)
    show akemi at left, flip
    with move
    pause(0.2)
    show princess at unflip
    n"Princess Aoi's determination burned brighter than ever as she turned to Akemi, her eyes shining with resolve."
    show akemi at notspeaking
    show princess 2 
    pra"We must retrieve the gemstone, no matter the cost." 
    show akemi at offscreenright, speaking
    show princess at flip, offscreenright
    with MoveTransition(0.8)
    n"Her voice echoed with determination. With the king's blessing and the support of the dwarven warriors, Akemi and Princess Aoi ventured into the mining caves, their hearts ablaze with courage and hope."
    show akemi at offscreenleft
    show princess:
        xalign -1.0
        yalign 1.0
        xzoom -1.0
    with None
    show akemi:
        xalign 2.0
        yalign 1.0
        xzoom -1.0
    show princess at offscreenright
    with MoveTransition(1.5)
    n"Akemi and Princess Aoi set forth into the depths of the mining caves"
    hide princess
    show akemi at left
    with dissolve
    show akemi 2
    a"We have faced greater dangers before, Princess. Together, we can overcome any obstacle."
    show akemi at notspeaking
    with None
    show princess 2 at right
    with dissolve
    pra"You're right, Akemi. With the strength of our friendship and the bravery of the dwarves, we will prevail."
    show akemi at offscreenright, speaking
    show princess at flip, offscreenright
    with MoveTransition(0.8)
    n"The resolve in their voices strengthened as they ventured deeper into the darkness"
    show minion at left
    show minion1 at right
    with Dissolve(1)
    stop music
    play music "ragnorbg.mp3" fadein 0.5 fadeout 0.5 loop
    n"Suddenly, shadows moved in the darkness ahead, revealing General Ragnor's minions ready to attack."
    g"Foolish mortals! You will go no further!"
    show minion:
        xcenter 0.9
        yalign 1.0
    show minion1:
        xcenter 0.75
        yalign 1.0
    with move
    pause(0.2)
    show princess 4 behind akemi at offscreenleft, flip
    with None
    show princess 4:
        xalign -0.2
    with move
    pause(0.5)
    show akemi 5 at offscreenleft, flip
    with None
    show akemi 5:
        xalign 0.0
    with move
    pra"Stand your ground, Akemi! We can do this!"
    hide princess
    with dissolve
    show akemi 6
    with None
    a"For the dwarves! For our people!"
#fight DIALOG
    # play music "bgground.mp3" fadein 0.5 fadeout 0.5 loop 
    scene bg dcave
    show minion
    with fade
    min1"You won't leave here alive!"
    show akemi 5 at offscreenleft, flip
    with None
    show minion:
        xalign 2.0
    with move
    show akemi 5 at left
    with move
    show akemi 6
    a"We'll see about that!"
    play audio "swordfight.mp3"
    show akemi 6 at left
    show minion:
        xalign 2.0 yalign 1.0
        linear 0.2 xalign 1.7 yalign 1.0
        linear 0.4 xalign 2.0 yalign 1.0
        pause(0.5)
        repeat 2
    show akemi 6:
        xalign 0.0 yalign 1.0
        linear 0.2 xalign 0.3 yalign 1.0
        linear 0.4 xalign 0.0 yalign 1.0
        pause(0.5)
        repeat 2
    a"*Clashes swords with Minion 1*"
    hide akemi
    hide minion
    show princess 4 at left, flip
    pra"Your reign of terror ends here!"
    show princess 4 at notspeaking
    show minion1:
        xalign 2.0 yalign 1.0
    with dissolve
    min2"*Charging at Aoi* You'll regret those words!"
    hide princess
    hide minion1
    play audio "<from 0.0 to 1>swordfight.mp3"
    show minion:
        xalign 2.0 yalign 1.0
        linear 0.2 xalign 1.7 yalign 1.0
    show akemi 6 at left, flip:
        xalign 0.0 yalign 1.0
        linear 0.2 xalign 0.3 yalign 1.0
        linear 0.4 xalign 0.0 yalign 1.0
        pause(0.7)
    pause(0.5)
    hide minion
    with dissolve
    a"*Defeating Minion 1* Aoi, stay behind me!"
    hide akemi
    show princess 4 at left, flip
    show minion1:
        xalign 2.0 yalign 1.0
        pause(0.5)
        linear 0.3 xalign 0.4 yalign 1.0
        linear 0.2 xalign 2.0 yalign 1.0
    pause(0.6)
    play audio "<from 0.0 to 1>swordfight.mp3"
    pra"*Swiftly blocking Minion 2's attack and providing a shield* I’ve got your back, Akemi!"
    show princess 4:
        linear 0.2 xalign -0.2 yalign 1.0
    show akemi 5 at left, flip:
        xalign -1.0 yalign 1.0
        linear 0.4 xalign 0.7 yalign 1.0
        linear 0.4 xalign 0.0 yalign 1.0
    play audio "<from 0.0 to 1>swordfight.mp3"
    pause(0.7)
    hide minion1
    with dissolve
    pause(0.7)
    show ragnor:
        xcenter 0.75
        yalign 1.0
    with Dissolve(2.0)
    n"As they defeated the minions, a menacing figure stepped out from the shadows... General Ragnor himself."
    stop audio
    show akemi 5 at flip
    show akemi 5 at notspeaking
    show princess 4 at notspeaking
    g"Impressive, but now you face me!"
    show akemi 5 at speaking
    show princess 4 at notspeaking
    show ragnor at notspeaking
    a"The real challenge begins. Ready, Princess?"
    show akemi 5 behind princess at notspeaking
    show princess 4 at speaking
    pra"I’ll support you, Akemi. Let’s end this!"
    show akemi 5 at notspeaking
    show princess 4 behind akemi at notspeaking
    show ragnor at speaking
    g"You have courage, but it will not save you from my wrath!"
    show akemi 5 at speaking
    show princess 4 at notspeaking
    show ragnor at notspeaking
    a"We have more than courage... We have each other!"
    show akemi 5 behind princess at notspeaking
    show princess 4 at speaking
    pra"And we fight for a just cause! (Casts a attack spell on General Ragnor)"
    show ragnor at speaking
    play audio "<from 0.0 to 1>swordfight.mp3"
    g"(Deflects Aoi's attack with a powerful swing) Foolish girl!"
    hide princess
    show akemi 6 at speaking
    show ragnor at notspeaking
    a"(Flanking Ragnor) Over here, brute! (Strikes at Ragnor's side)"
    show akemi 5 at notspeaking
    show ragnor at speaking
    g"(Roars in anger) You will pay for that! (Swings his massive axe at Akemi)"
    show akemi 5 at speaking
    show princess 6:
        xzoom -1
        xalign -0.7 yalign 1.0
        linear 0.1 xalign -0.2 yalign 1.0
    show ragnor:
        linear 0.2 xcenter 0.5 yalign 1.0
        linear 0.2 xcenter 0.75 yalign 1.0
    pause(0.2)
    play audio "<from 0.0 to 1>swordfight.mp3"
    pra"Akemi, look out! (Uses her magic shield to block the sword)"
    show princess 5
    n"The battle intensifies, with Akemi and Aoi coordinating their attacks, wearing Ragnor down"
    show akemi 5 at notspeaking
    show princess 4 behind akemi at notspeaking
    g"(Breathing heavily) This... this cannot be!"
    show akemi 6 at speaking
    show ragnor at notspeaking
    a"It's over, Ragnor. Surrender!"
    show akemi 5 at speaking
    show ragnor:
        alpha 1
        linear 0.2 xcenter 0.5 yalign 1.0
        linear 0.2 xcenter 0.75 yalign 1.0
    pause(0.2)
    play audio "<from 0.0 to 1>swordfight.mp3"
    g"Never! (Lunges desperately)"
    show akemi 5 behind princess at notspeaking
    show princess 5 at speaking
    pra"(Providing a final spell boost to Akemi) Now, Akemi!"
    hide princess
    show akemi 5:
        alpha 1
        xalign 0.0 yalign 1.0
        pause(0.5)
        "akemi 6"
        linear 0.2 xalign 0.5 yalign 1.0
        linear 0.4 xalign 0.0 yalign 1.0
        "akemi 5"
    pause(0.5)
    play audio "<from 0.0 to 1>swordfight.mp3"
    a"(With a final, powerful strike) This is for the dwarves!"
    stop music
    hide ragnor
    with Dissolve(1)
    scene black
    with fade
    n"With a final, resounding clash, General Ragnor fell to the ground, defeated. The cavern echoed with the silence of their victory."
    n"With the gem safely in their possession, Akemi and Princess Aoi return to the dwarven kingdom, their hearts buoyed by the success of their mission."
    hide akemi
    with dissolve
    play music "goodnews.mp3" fadein 0.5 fadeout 1.0 loop
    scene bg cc
    with dissolve
    show princess 2 at left, flip
    pra"Akemi, look! Over there, deep in the mining cave. It's the Mystic Lunar, shimmering in a radiant sky blue. It's truly breathtaking..."
    pra"Our journey was not in vain, this gem holds the key to our kingdom's salvation."
    show akemi 2 at offscreenleft, flip
    with None
    show princess at right
    show akemi 2 at left, flip
    with move
    show princess at unflip
    show princess at  notspeaking
    a"Princess Aoi, I've never seen anything so beautiful. It's like the heavens themselves have descended into this cave."
    scene black
    show bg ctr 
    with fade
    a"With this gem, we can forge the Necklace of Valor and bring hope back to your people."
    scene bg throne1
    with fade
    n"As Akemi and Princess Aoi return, King Throin greeted them with gratitude. He thanked both for their bravery."
    show throin
    k"You have defeated General Ragnor and I congratulate you on your victory. It seems the victory has weakened our enemy's forces."
    show akemi at offscreenleft, flip
    with None
    show throin:
        xalign 2.0
    show akemi at left, flip
    with move
    show akemi 2
    show throin at notspeaking
    a"Thank you, King Throin. We're honored to have helped. Our encounter with General Ragnor was challenging, but with Princess Aoi's leadership, we prevailed."
    show akemi at notspeaking
    show throin at speaking
    k"Your bravery has brought light to our kingdom in these dark times. With the Mystic Lunar in our possession, we can now forge a necklace stronger than ever before. Guards, prepare the forge and summon our most skilled smith. The Necklace of Valor shall rise again!"
    hide throin
    show princess 2 at right
    pra"Akemi, our journey together has been filled with danger and uncertainty, but seeing the Mystic Lunar fills me with hope. We've faced adversity and triumphed, and now our kingdom can rebuild."
    show akemi 2 at speaking
    show princess at notspeaking
    a"Princess Aoi, it's been an honor to fight by your side. Your courage and determination inspire me. Together, we've overcome every obstacle, and I have no doubt that we'll continue to do so."
    show akemi at notspeaking
    show princess 2 at speaking
    pra"Thank you, Akemi. Your strength and loyalty have been invaluable to our cause. Let us go forth and ensure that the Necklace of Valor is forged with the same determination that brought us here!"
    pra"But for now we must rest up I am tired!"
    scene black
    with fade
    n"After all was said and done everyone rested up for a few days waiting for the smith to finish forging the Necklace of Valor"
    n"While resting, Akemi notice something is worrying Princess Aoi."

    play music "falls.mp3" fadein 0.5 fadeout 1.0 loop
    show akemi 3 at left, flip
    a"Aoi are you okay? I can see the worry in your eyes."
    show akemi 10 at notspeaking
    show princess 7 at right
    pra"Thank you Akemi, I am just worry about my father and the people of Azurevale"
    show akemi 3 at speaking
    show princess 3 at notspeaking
    a"I see... Don't worry we will save your father and your people, but for now, let us focus on the task at hand. We have the gem, and soon we will have the necklace. With its power, we will be better equipped to face whatever challenges lie ahead."
    show akemi 10 at notspeaking
    show princess 7 at speaking
    pra"You're right, Akemi. We must stay focused on our mission. But I cannot shake the worry for my father and my people. They need us now more than ever."
    show akemi 2 at speaking
    show princess 3 at notspeaking
    a"We'll do everything we can to protect them, Princess. But for now, let's trust in the dwarven craftsmanship and the magic of the necklace."
    show akemi at notspeaking
    show princess 2 at speaking
    pra"Yes, you're right, Akemi. Thank you for your support. Let's assist wherever we can in the dwarven kingdom while we await the completion of the necklace."
    scene black
    with fade
    n"As they awaited the necklace's completion, Akemi and Princess Aoi spent their days in the dwarven kingdom, assisting those in need. Though outwardly brave, the weight of their responsibilities grew heavier, intensifying their sense of urgency."
    stop music fadeout 0.5
    play music "goodnews.mp3" fadein 0.5 fadeout 1.0 loop
    n"On the day of completion, King Throin presented the finished necklace to Akemi and Princess Aoi."
    scene bg throne1
    show throin
    with fade
    k"This necklace is a testament to your bravery and determination. May it serve you well in your quest to bring peace to your kingdom."
    show black:
        alpha 0.5
    show necklace
    with dissolve
    pause(2)
    hide necklace
    hide black
    with dissolve
    show princess at offscreenleft, flip
    with None
    show throin:
        xalign 2.0

    show princess at left, flip
    with move
    show princess 2
    pra"Thank you King Throin"
    hide princess
    show akemi 2 at left, flip 
    a"Thank you"
    scene black
    with fade
    n"As they set their next journey, the grand halls of the royal palace, they were greeted with cheers and applause from the dwarven citizens, who hailed them as heroes."

    if menu_flag == False:
        jump branch_3
    elif menu_flag == True:
        jump branch_5

label branch_5:
     play music "branch5.mp3"
    scene black
    n"Akemi and Princess Aoi continue and prepare their journey."
    n"Princess Aoi turned to Akemi with a determined look in her eyes"
    with fade
    scene bg deepforest
    show princess 5 at center, speaking 
    show akemi 4 at left, flip, notspeaking
    pra"Akemi, there is one final item that we need to retrieve on defeating Himiko once and for all. "
    n"She explained, her voice filled with resolve."
    pra"It is the Crimson Radiance Ring, said to protect its wearer from even the most powerful of attacks."
    pra"However, it is in the realm of one of the Heavenly Dragons, guarded for millennia, awaiting the true and worthy hero to retrieve it"
    hide princess
    show akemi 2 at left, flip, speaking
    show princess 5 at center, notspeaking
    n"Akemi nodded, understanding the gravity of their task." 
    show akemi 2 at left, speaking
    show princess 2 at center, notspeaking 
    a "Then we must start our journey to the realm of the Heavenly Dragon and prove ourselves worthy of the Crimson Radiance Ring."
    n"She replied, her voice steady with determination"
    a"Together, we will face whatever challenges lie ahead and emerge victorious."
    show akemi at left, flip,speaking
    show princess at center, flip ,speaking
    n"With their hearts set on their next quest, Akemi and Princess Aoi, their minds filled with thoughts of the trials and tribulations that awaited them."
    with dissolve
    scene black 
    #black screen
    n"As one of the minions of General Ragnor escaped from the kingdom of the dwarves."
    n"He wasted no time in delivering his message to Himiko. Rage consumed her as she learned of Princess Aoi and Akemi's involvement.."
    with fade
    scene bg throne2
    show himiko  at left, flip, notspeaking
    show minion :
        xalign 2.0 yalign 1.0
    min1"Your Majesty, General Ragnor was defeated by Princess Aoi and a girl named Akemi."
    show minion at left, notspeaking:
        xalign 2.0 yalign 1.0
    show himiko 1 at left, flip, speaking
    h"What?....They defeated Ragnor? He is so strong, and yet he was defeated."
    show himiko 3 at left, flip, notspeaking 
    show minion at left, speaking:
        xalign 2.0 yalign 1.0
    min1"What should we do, your Majesty?"
    show himiko 3 at left, flip,speaking
    show minion at left, notspeaking:
        xalign 2.0 yalign 1.0
    h"Bring me King Charles (king of Azurevale) from his cell now!"
    show minion at left, speaking:
        xalign 2.0 yalign 1.0
    show himiko 3 at left, notspeaking
    min1"Yes, your Majesty."
    show kc at center
    n"The Minion brings King Charles to Himiko and asks him the location of the Crimson Radiance Ring. "
    #slide King and minion from rigth to left
    show kc at center, notspeaking
    show himiko 1 at left, flip, speaking
    show minion at right, notspeaking:
        xalign 2.0 yalign 1.0
    h" Hmmm... I want you to tell me something and don't you think of lying to me!"
    show kc at center, speaking
    show himiko 1 at left, notspeaking
    show minion at right, notspeaking:
        xalign 2.0 yalign 1.0
    c"Ahhh...Hmmm... "
    show minion at right, notspeaking:
        xalign 2.0 yalign 1.0
    show kc at center, notspeaking
    show himiko 1 at left, flip, speaking 
    h"Tell me the location of where the Crimson Radiance Ring is."
    show kc at center, speaking 
    show himiko 1 at left, flip, notspeaking 
    show minion at right, notspeaking:
        xalign 2.0 yalign 1.0
    c"Hmmm... I won't tell you even if you threaten to kill me."
    show himiko 3 at left, flip, speaking
    show kc at center, notspeaking 
    show minion at right, notspeaking:
        xalign 2.0 yalign 1.0
    h"Hmm... If you won’t tell me the location of the ring, I will kill your people in this castle HAHAHHAHAH!"
    h"And that's not all, I will also kill your beloved daughter."
    
    show kc at center, speaking 
    show himiko 1 at left, flip, notspeaking 
    show minion at right, notspeaking:
        xalign 2.0 yalign 1.0
    c"You monster! Don't you dare to hurt her... or-"
    
    show himiko 4 at left, flip, speaking
    show kc at center, notspeaking 
    show minion at right, notspeaking:
        xalign 2.0 yalign 1.0
    h"HAHAHAHAH! Or what?......What can you possibly do in your current state?"
    h"I will make you a deal, I will order my servant to only capture Princess Aoi and return her to you safe and sound, if you tell me the location of the ring."
    
    show kc at center, speaking 
    show himiko 1 at left, flip, notspeaking 
    show minion at right, notspeaking:
        xalign 2.0 yalign 1.0
    c"Hmmm....I want you to give me your word that you won't hurt my daughter and my people."

    show himiko 4 at left, flip, speaking
    show kc at center, notspeaking 
    show minion at right, notspeaking:
        xalign 2.0 yalign 1.0
    h"Hehe, fine, I give you my word."

    show kc at center, speaking 
    show himiko 1 at left, flip, notspeaking 
    show minion at right, notspeaking:
        xalign 2.0 yalign 1.0    
    c"The location of the Crimson Radiance Ring is in the Heavenly Dragon Mountain."
    
    show himiko 4 at left, flip, speaking
    show kc at center, notspeaking 
    show minion at right, notspeaking:
        xalign 2.0 yalign 1.0
    h"Was that hard to say? Take him back to his cell!"
    n"As King Charles returns to his cell, his heart heavy with guilt and despair, he hopes to protect his people and Princess Aoi from her wrath."
    hide minion
    hide kc
    show himiko 4 at center, speaking 
    n"But as soon as the information was in her grasp, Himiko's true intentions were revealed."
    n"With a wicked grin, she ordered her minion to return the king to his cell and his fate sealed for daring to defy her."
    h"Heavenly Dragons Mountain huh.... Let's see if this time they will survive HAHAHAAHAH!"
    n"Himiko concocted a sinister plan to ensure Akemi and Princess Aoi's demise. Harnessing her dark powers, she formed a purple orb infused with her malevolent energy. "
    
    show himiko 4 at left, flip, speaking 
    show minion at right, notspeaking:
        xalign 2.0 yalign 1.0
    h"Come my servant, I want to give you a special quest right now. You are my general, I need you to deliver this in the Heavenly Dragons Mountain now."
    show himiko 4 at left, flip, notspeaking 
    show minion at right, speaking:
        xalign 2.0 yalign 1.0
    min1" It’s an honor, Your Majesty. "
    n"The orb contains some of Himiko’s power and it will release a purple smoke that will make any living creature go berserk and becomes Himiko’s pawn."
    hide himiko
    with dissolve
    scene black
    show himiko 4 at center, speaking  
    h"HAHAHAHAHAHAHHA!"
    with dissolve
    #Next Scene for akemi and aio  ot heavenly dragon mountain
    scene bg mountain
    #show akemi 4 at center, speaking 
    show akemi 4 at center, flip, speaking   
    show princess at left, flip, notspeaking
    a" So, that’s the Heavenly Dragons Mountain."
    
    show princess 2 at left, flip, speaking
    show akemi at center, flip, notspeaking
    pra"Yes, there’s a dragon living there."
    
    show akemi 7  at center, flip, speaking
    show princess 2 at left, flip, notspeaking
    a"Really, that’s amazing! Wait, if there is a dragon living there then we will get attacked by it."

    show princess at left, flip, speaking
    show akemi 2 at center, flip,notspeaking
    pra"No, it’s okay. The dragon living there is a kind of dragon that never attacks humans especially if it doesn’t bother him."

    show akemi 2 at center, flip, speaking
    show princess 2 at left, flip, notspeaking
    a"Really, we are safe then. That’s easy."
    show akemi 4 at center, notspeaking
    show princess at left, flip, speaking
    pra"Yes"
    
    #hurt
    show akemi 7 at center, unflip ,speaking
    show princess 7 at left, flip, notspeaking

    n"As Akemi and Princess Aoi continue their walk, a violent wind suddenly whipped around them."
    show akemi 3 at right, unflip ,speaking
    show princess at left, flip, notspeaking
    a"Aoi, AAHHHH!"
    show akemi 3 at right, unflip ,notspeaking
    show princess 7 at left, flip, speaking
    pra"Akemi, AAHHHH!"
    n"They senses heightened, they looked up to see a massive dragon" 
    n"descending from the sky, its eyes ablaze with malice and ready to attack."
    show akemi 3 at right, unflip ,notspeaking
    show princess at left, flip, notspeaking
    show drag at center, speaking
    dragon"(Roar)RAWWWWWWW!!!!"
    #slide Effect fight
    show drag at center, notspeaking
    show akemi 7 at right, unflip ,speaking
    show princess at left, flip, notspeaking
    a"Aoi, look out!!"
    show akemi 3 at right, unflip ,notspeaking
    show princess 7 at left, flip, speaking
    pra"AHH!!"
    show akemi 6 at right, unflip ,speaking
    show princess 7 at left, flip, notspeaking
    show drag at center, speaking
    a"Why you!!"
    n"As the dragon ready itself for another strike, Akemi leaped high into the air, carrying Princess Aoi to safety."
    show akemi 6 at center, notspeaking
    show princess 7 at left, flip, notspeaking
    show drag at right, speaking
    dragon"(RrrrrrrRrrrr)"

    #allignment Needed
    show akemi 3 at center, unflip ,speaking
    show princess at left, flip, notspeaking
    show drag at right, notspeaking
    a"Are you okey Aoi. "
    show akemi 3 at center, unflip ,notspeaking
    show princess at left, flip, speaking
    pra"Yes, I am fine. Thank you."

    #Need Transition
    show akemi 6 at center, flip, speaking
    show princess 7 at left, flip, notspeaking
    show drag at right, notspeaking
    a"Stay here, I will deal with the dragon."
    n"Akemi drew her sword, ready to face the formidable foe. With a swift and precise strike, she lunged at the dragon, but to her astonishment, her blade had no effect."
    
    show akemi 7 at center,speaking
    show princess 7 at left, flip, notspeaking
    show drag at right, notspeaking
    a" What?....It didn’t work, what's going on? "
    show akemi 3 at center,notspeaking
    show princess 5 at left, flip, speaking
    show drag at right, notspeaking
    n"Princess Aoi uses her magic to strike the dragon's wing and Akemi is surprised that the magic is working. She then also tried to use it."
    pra"Fireball"
    show akemi 3 at center,speaking
    show princess at left, flip, notspeaking
    show drag at right, notspeaking
    a"So magic works huh. Then, let's see if you try to take this."

    show akemi 3 at center,notspeaking
    show princess at left, flip, notspeaking
    show drag at right, speaking
    dragon"(RrrrrrrRrrrr)"
    n"The sword lights fire and Akemi tries to slash the dragon but as soon as Akemi is about to attack, Princess Aoi stops her."
    
    show akemi 3 at center,notspeaking
    show princess 6 at left, flip, speaking
    show drag at right, notspeaking
    pra"Wait Akemi!!"

    show akemi 3 at center,speaking
    show princess at left, flip, notspeaking
    show drag at right, notspeaking
    a"Huh? Why, what’s wrong?"
    n"As soon as Akemi got stopped by princess Aoi, the dragon raised up and started to fire a multiple fireball"
    show akemi 3 at center,notspeaking
    show princess at left, flip, notspeaking
    show drag at right, speaking
    dragon"(grrrooooowl)"

    show akemi 7 at center,speaking
    show princess at left, flip, notspeaking
    show drag at right, notspeaking
    a"Whooo! That was close."

    show akemi 3 at center,notspeaking
    show princess 5 at left, flip, speaking
    show drag at right, notspeaking
    pra"Akemi, let’s hide for now. Trust me."

    show akemi 3 at center, speaking
    show princess at left, flip, notspeaking
    show drag at right, notspeaking
    a"Really, okay if you say so."
    with dissolve
    scene bg deepforest
    n"Akemi and Princess Aoi ran deep into the forest then they stumbled into a lake and Princess Aoi explained to Akemi what she had noticed."
    
    show akemi 3 at center, unflip ,speaking
    show princess 7 at left, flip, notspeaking
    a"What, why did you stop me?"
    show akemi 3 at center,notspeaking
    show princess 7 at left, flip, speaking
    pra"That dragon seems in pain and under the influence of something like there’s controlling it against its will."
    hide princess
    hide akemi
    show drag at center, speaking
    dragon"(prrrr prrrr) (sighing)"
    hide drag
    show akemi 3 at center,speaking
    show princess at left, flip, notspeaking
    a"Then, what should we do?"

    show akemi 3 at center,notspeaking
    show princess 7 at left, flip, speaking
    pra" I know that I am asking too much, but we can help it."


    show akemi 2 at center, speaking
    show princess at left, flip, notspeaking
    a"Okay, if that's what you want. So, how will we help it?"
   
    show akemi 3 at center,notspeaking
    show princess 2 at left, flip, speaking
    pra"Hmm... how about we investigate his lair? Maybe we can find something there or."
    pra"We can try to make it unconscious and see what is going on to him Whats your choice?"
menu:
        "Investiagte the cause":
            $ menu_flag = True
            jump invest_dragon

        "Fight the dragon":
            $ menu_flag = False
            jump fight_dragon
            with dissolve
label invest_dragon:
    show akemi 3 at center,speaking
    show princess at left, flip, notspeaking
    a"We should investigate it then." 
    show akemi 3 at center,notspeaking
    show princess at left, flip, speaking
    pra"Okay. "
    with dissolve
    show akemi 3 at center,notspeaking
    show princess at left, flip, notspeaking
    n"As they tried to hide from the trees to go look for the dragon’s lair, Princess Aoi saw something."
    scene bg cave1 
    show akemi 3 at right, unflip,notspeaking
    show princess at left, flip, speaking
    pra"Hmm what’s that? Akemi come over here."
   
    show akemi 3 at center, speaking
    show princess at left, flip, notspeaking
    a"What did you see?"
    
    show akemi 3 at center,notspeaking
    show princess at left, flip, speaking
    pra"There's seemed to be a cave over there and seem there’s a purple fog inside it."

    show akemi 3 at center, speaking
    show princess at left, flip, notspeaking
    a"We should go and see it."

    show akemi 3 at center,notspeaking
    show princess at left, flip, speaking
    pra" Okay but first, I will cast a spell to protect us from that purple smoke."
    with dissolve
    scene bg cavepurple
    show akemi 3 at right, speaking
    show princess at left, flip, speaking
    n"Akemi and Princess Aoi enter the cave the saw a purple orb that is releasing purple smoke."

    show akemi 3 at right, speaking
    show princess at left, flip, notspeaking
    a"What is that should we go and see it."

    show akemi 3 at right,notspeaking
    show princess at left, flip, speaking
    pra"Okay, but let’s be careful."
    n"They got closer to the purple orb as Princess Aoi looked at it and realized that was Himiko’s doing. "
    
    show akemi 3 at right,notspeaking
    show princess 5 at left, flip, speaking
    pra"I see, Himiko must have used this purple orb to control the dragon. "

    show akemi 3 at right, speaking
    show princess at left, flip, notspeaking
    a"Should we destroy it then?"
    show akemi 3 at right, notspeaking
    show princess 5 at left, flip, speaking
    pra"Wait, if we just destroy it, the smoke will get more powerful."

    show akemi 3 at right,speaking
    show princess at left, flip, notspeaking
    a"So What should we do?"
    
    show akemi 3 at right,notspeaking
    show princess 3 at left, flip, speaking
    pra"We need to purify it by channeling light magic into it. Maybe it will stop the smoke, but my magic is not enough to purify it."
    pra"But I think you can do it Akemi, your Blade of Ethereal Fang to cast the light magic and the Necklace of Valor to boost your magic."
    
    show akemi 3 at right, unflip, speaking
    show princess at left, flip, notspeaking
    a"Okey, i will try"
    
    n"Akemi tries to focus with the help of the elder elf. Akemi was able to cast magic into the sword and as the sword lit, the smoke slowly vanishes, and the purple orb suddenly turns gray."
    
    show akemi 5 at right, unflip, speaking
    show princess at left, flip, notspeaking
    a"HMMMM!!!!MMMMMM!!!"
    hide akemi
    scene bg cavepurple
    with fade
    scene bg gcave
    show akemi 5 at right, unflip, speaking
    show princess 2 at left, flip, speaking
    n"Princess Aoi notice that the purple smoke gradually fading and the orb is turning into a gray orb"

    show akemi 3 at right, unflip, notspeaking
    show princess 2 at left, flip, speaking
    pra"Yes, that’s it Akemi. You did it! We should see what’s the condition of the dragon."
    n"Akemi saw the dragon fall asleep nearby when the purple smoke was gone. "
    with fade
    jump outcome

label fight_dragon:
    scene bg deepforest
    show akemi 6 at left, flip, speaking
    show princess at center, notspeaking
    a"We should fight it. If we don’t try to stop, now the dragon might attack an innocent one."
    show akemi 6 at left, speaking
    show princess 5 at center, speaking
    pra"Okey, I understand."
    show akemi 6 at left, speaking
    show princess 5 at center, speaking
    pra"First, we need a plan, magic is the only thing to hurt him, and we must knock him down so I will be able to observe what is wrong with him."
    show akemi 2 at left, speaking
    show princess at center, notspeaking
    a"I have an idea, Aoi."
    show akemi at left, notspeaking
    show princess 2 at center, speaking
    pra"Okay, what’s your idea?"
    hide princess
    show akemi 2 at left, speaking
    show princess at center, notspeaking
    a"First, I will draw its attention and you try to attack him with magic and once he is down, I will try to use a bind magic, so he won’t be able to move."
    show akemi 2 at left, notspeaking
    show princess 2 at center, speaking  
    pra"Okey I,got it."
    n" As Akemi try to shout loudly to lure the dragon."
    hide princess
    show akemi 6 at left, speaking 
    show princess at center, speaking
    a"HYYAAAAAAAAAAA!!"
    n"As Akemi tries to shout to lure the dragon."
    n" A violent wind dash through Akemi as see observe where will it attack Akemi."
    show drag at right, speaking
    show akemi at left, notspeaking 
    show princess at center, notspeaking
    dragon"(grrrooooowl)"

    show drag at right, speaking
    show akemi at left, notspeaking 
    show princess at center, notspeaking
    dragon"(RrrrrrrRrrrr)"

    show drag at right, notspeaking
    show akemi 6 at left, speaking 
    show princess at center, notspeaking
    a"Hmmm,It's over there, aoi get ready."
    show drag at right, notspeaking
    show akemi 6 at left, notspeaking 
    show princess 5 at center, speaking
    pra"On it."

    n"As Akemi drew the attention of the dragon, Princess Aoi used this chance to fire at the dragon. "
    show drag at right, notspeaking
    show akemi 6 at left, notspeaking 
    show princess 5 at center, speaking
    pra"FireBall"
    n"As the dragon got hit Akemi used a binding magic to seal the movement of the dragon while Princess Aoi notice the purple aura raleasing n the body of the dragon"
    
    show drag at right, notspeaking
    show akemi 6 at left, notspeaking 
    show princess 5 at center, speaking
    pra"Akemi, I got it. We need to use light magic to remove the purple aura, but my magic is not enough."
    
    show drag at right, notspeaking
    show akemi 6 at left, speaking 
    show princess 5 at center, notspeaking
    a"I will do it i will used the Blade of Ethereal Fang to cast the light magic and necklace of valor to boost your magic"
    n"As Akemi concentrates in casting light magic, the sword lit and the necklace glows then the purple aura is slowly fading and making the dragon fall sleep. "
    jump outcome

#Same ending for branch 6
label outcome:
    scene bg deepforest
    show akemi  at left, speaking
    show princess  at center, speaking
    n"Exhausted Akemi and Princess Aoi shared a triumphant smile, knowing they had succeeded in freeing the dragon from Himiko's control. Minutes passed, the dragon stirred awake, its eyes filled with remorse for its actions. "
    
    show akemi 2 at left, notspeaking
    show princess 2 at center, notspeaking
    show drag at right, speaking
    dragon"(prrrr prrrr) (sighing)"
    show akemi 2 at left, speaking
    show princess 2 at center, notspeaking
    show drag at right, notspeaking
    a"Hi are you okey?"
    show akemi 2 at left, notspeaking
    show princess 2 at center, speaking
    show drag at right, notspeaking
    pra"How are you feeling?"

    show akemi at left, notspeaking
    show princess at center, notspeaking
    show drag at right, speaking
    dragon"Huh, ahh. I am sorry about what happened earlier."

    show akemi 2 at left, speaking
    show princess 2 at center, notspeaking
    show drag at right, notspeaking
    a"It’s okay, don’t mention it."
    show akemi at left, notspeaking
    show princess at center, speaking
    show drag at right, 
    pra"Yeah, no worries"

    show drag at right, speaking 
    show akemi at left, notspeaking
    show princess at center, notspeaking
    dragon"Thank you for saving me."

    show drag at right, speaking 
    show akemi at left, notspeaking
    show princess 2 at center, speaking
    pra"My name is Princess Aoi, and this is my companion Akemi."\

    show drag at right, notspeaking 
    show akemi 2 at left, speaking
    show princess at center,speaking
    a"Hi, what’s your name?"

    show drag at right, speaking 
    show akemi at left, notspeaking
    show princess at center, notspeaking
    dragon"My name is Draythorn. It’s nice to meet both of you." 

    n"As they are resting for a bit. Draythorn pops a question."
    
    show drag at right, speaking 
    show akemi at left, notspeaking
    show princess at center, notspeaking
    dra"Anyway, what are you doing here in Heavenly Dragons Mountain?"
   
    show drag at right, notspeaking 
    show akemi at left, notspeaking
    show princess 2 at center, speaking
    pra"We are looking for the Crimson Radiance Ring."

    show drag at right, speaking 
    show akemi at left, notspeaking
    show princess at center, notspeaking
    dra"So, you are also looking for it huh?" 
    
    show drag at right, notspeaking 
    show akemi 3 at left, speaking
    show princess at center, notspeaking
    a"What do you mean by that?"

    show drag at right, speaking 
    show akemi at left, notspeaking
    show princess at center, notspeaking
    dra"When I was under the influence of that purple smoke. I keep on hearing a female voice about destroying someone and brings her the ring."

    show drag at right, notspeaking 
    show akemi at left, notspeaking
    show princess 5 at center, speaking
    pra"It’s Himiko again."

    show drag at right, notspeaking 
    show akemi 3 at left, speaking
    show princess at center, notspeaking
    a"Yeah, Himiko probably trying to get the ring for herself."

    show drag at right, speaking 
    show akemi at left, notspeaking
    show princess at center, notspeaking
    dra" So that's her name huh? It's true that I have the ring, but it won't work if I don't give my magic to power to it."

    show drag at right, speaking 
    show akemi at left, notspeaking
    show princess at center, notspeaking
    dra"I will give you the ring as a reward for helping me and promise me that you will defeat Himiko."

    show drag at right, notspeaking 
    show akemi 2 at left, speaking
    show princess 2 at center, notspeaking
    a" I Promise"

    show drag at right, speaking 
    show akemi at left, notspeaking
    show princess at center,speaking
    pra" I Promise"
    
    scene black
    n"Draythorn gave Crimson Radiance Ring. Akemi donned the ring, feeling its power course through her veins, and to their surprise, Draythorn blessed the ring, imbuing it with even greater strength. "
    n"With their mission accomplished, Draythorn offers Princes Aoi and Akemi a ride. As they soared towards the edge of the forest"
    n"they bid farewell to Draythorn, expressing their gratitude for his aid and the swift ride, With the Crimson Radiance Ring in their possession"
    n"and Draythorn's blessing, Akemi and Princess Aoi continued their quest with renewed determination"
with dissolve
#branch 6
label branch_6:
    stop music
    scene bg forest1
    show princess 2
    with fade
    pra"Now that we have gathered everything, we finally have all the necessary items needed to defeat Himiko!"
    show princess at right
    with move
    show princess at notspeaking
    show akemi 2 at left, flip
    a"Lead the way princess towards the Kingdom of Azurevale."
    show akemi at notspeaking
    show princess 2 at speaking
    pra"Draythorn dropped us off at the outskirts of the Kingdom, it will only take us half a day on foot to reach Azurevale, if we follow this path, we should be fine."
    show princess at notspeaking
    show akemi 2 at speaking
    a"Then, let’s get going then…"
    scene black
    with fade
    n"Akemi and Aoi set off to the kingdom of Azurevale."
    n"As they follow the path towards the kingdom their surroundings are filled with destruction and despair as they see villages nearby abandoned, natural resources destroyed, and dead bodies scattered in the area."
    n"Fear soon filled the air as the duo witnessed the results of their evil thinking how bad it is at the center of it all."
    show princess 7 at left,flip
    pra"This is one of the villages that are outside of the Azurevale. I know Himiko is evil, but it is worse than I thought."

    pra"All villagers that met their untimely demise, the houses are in ruins, even the farms and surrounding forest are reduced to ashes."

    pra"Can we really win this fight against Himiko? "

    pra"Was calling you from the other world was a big mistake?"

    pra"If this is what happened to the outskirts of the kingdom then how bad is it at the castle?"

    pra"I am afraid we are too late to take action?"

    pra"What do you think we should do?"
    hide princess
    menu:
        "Akemi comforted Aoi ":
            jump option_1

        "Akemi made Aoi stay":
            jump option_2
    

    
label option_1:
    scene bg forest1
    show akemi 3 at left, flip
    with fade
    a"Aoi you are the Princess of Azurevale, the one who helped me through this journey to get the necessary equipment to defeat Himiko, and the one who will free your people from Himeko."
    a"We may not be able to save everyone but there are still people who are waiting to be save and if we don’t stop her then she will continue destroying everything"
    show akemi 10 at notspeaking
    show princess 7 at right
    pra"You are right, defeat is never an option. We must continue."
    pra"I will support you with all I got Akemi and together we will defeat Himiko!"
    scene black
    with fade
    scene bg frontgateazure
    with fade
    n"The duo continued its way towards the kingdom but as they get closer and closer to their destination the sound of minions screaming can be heard getting louder and louder"
    n"Then they saw it, outside of the kingdom a massive horde of minions scattered outside ravaging everything from houses to the land scape itself"
    scene black
    with fade
    n"The once beautiful kingdom was turn into a desolate place by the army"
    n"As both of them are shocked at what they saw Akemi filled with self-doubt asked Princess Aoi"
    scene bg forest1
    show akemi 7 at left, flip
    with fade
    a"With all these minions are we able to fight this head on?"
    show akemi 4 at notspeaking
    show princess 7 at right
    pra"Although the legendary equipments are powerful, they only protect you and an ambush from Himiko herself can easily be the death of both of us."
    pra"Our best bet is to avoid conflict against the whole army and sneak our way in!"
    show princess 3:
        linear 0.3 xalign 0.5
        "princess 6"
        pause(1)
        linear 0.3 xalign 1.5
    show himiko 2:
        xalign 1.5 yalign 1.0
        pause(0.3)
        linear 0.15 xalign 1.0
        pause(0.15)
        "himiko 4"
    h"That’s a brilliant idea princess! *Binds the princess*"
    show bg forest1full behind akemi, himiko
    show akemi 4 at speaking
    show himiko 2
    with fade
    show himiko 4
    h"You may have the legendary equipment (looks at Akemi) but the princess doesn’t have anything!"
    show himiko 2
    show akemi 4:
        alpha 1
        xalign 0.0 yalign 1.0
        "akemi 5"
        pause(0.5)
        "akemi 5"
        linear 0.2 xalign 0.5 yalign 1.0
        linear 0.4 xalign 0.0 yalign 1.0
        "akemi 13"
    pause(0.5)
    play audio "<from 0.0 to 1>swordfight.mp3"
    n"Akemi surprised of what happened angerly tried to attack Himiko but was swiftly blocked by Himiko’s minions."
    show akemi 13 at notspeaking
    show himiko 4
    h"What will you do now that you lost your partner? Are you really going to fight me and my army all on your own?"
    show akemi 14 at speaking
    show himiko 2 at notspeaking
    a"What should I do? Why is she here? Can I even defeat her with her army?"
    show akemi 13 at notspeaking
    show himiko 2 behind princess:
        alpha 0.63
        linear 0.3 xalign 0.8
        "himiko 3"
    show princess 3:
        xalign 1.5 yalign 1.0
        linear 0.3 xalign 1.0
        "princess 7"
    pra"Stop doubting yourself!"
    pra"We have come this far just to give up! We got everything we needed. You can do it, Akemi!"
    pra"You have all you need to defeat her!"
    hide princess
    with dissolve
    show akemi 6 at speaking
    show himiko 3:
        alpha 0.63
        linear 0.3 xalign 1.0
        "himiko 3"
    a"You are right princess!"

    a"Himiko! If you are really that powerful, then you can defeat me all by yourself! Stop hiding behind your minions like a coward and fight me in a duel! Just you and me!"
    show akemi 5 at notspeaking
    show himiko 5 at speaking
    h"And what makes you think I would accept that? You are the one who is surrounded here, and I can easily command my army to attack you all at once."

    h"What gave you the authority to challenge me in a duel?"
    show akemi 6 at speaking
    show himiko 3 at notspeaking
    a"If you truly are as powerful as you say then there’s nothing to fear about the duel. At the very least if I fail to defeat you, I can have an honorable departure."
    show akemi 5 at notspeaking
    show himiko 4 at speaking
    h"You amuse me. Your name is Akemi, correct?"
    show akemi 6 at speaking
    show himiko 2 at notspeaking
    a"Yes, I am Akemi the Outworlder that will defeat you once and for all!"
    show akemi 5 at notspeaking
    show himiko 4 at speaking
    h"You amuse me Akemi, I will accept your duel so that you will have a much more humiliating defeat! I want to see you beg as you wish you fought my army instead of me!"
    show himiko 1
    h"Take the princess to the dungeon with the rest of the people and do not interfere with our fight!"

    n"Himiko started chanting as she prepares to transport both herself and Akemi to the throne room."

    jump himiko_fight

    

label option_2: 
    scene bg forest1
    show akemi 3 at left, flip
    with fade
    a"I am afraid that something bad may happen to you princess, so I must fight her alone."
    show princess 5 at right
    show akemi 10 at notspeaking
    pra"What are you saying? That’s suicide!"
    show akemi 3 at speaking
    show princess 4 at notspeaking
    a"I know it may be suicide but what will happen when we fail to defeat Himiko, and you didn’t survive?"

    a"What would happen if we won but at the cost of your life? Who will lead your people? Who will look for help from other kingdoms when things don’t go our way?"

    a"I will continue to take this path alone. Please go back or stay at a safe place."

    a"I will be back when everything is done and if I don’t come back ask the other kingdom for help."
    show akemi 5:
        xzoom 1
        linear 1.0 xalign -1.0
    show princess 3 at speaking
    pause(2.0)
    scene black
    with fade
    n"As Princess Aoi thought of everything Akemi has said. Akemi heads towards the Azurevale."

    n"As Akemi gets closer and closer to her destination the sound of minions screaming can be heard getting louder and louder"
    scene bg frontgateazure
    with fade
    n"Then she saw it, outside of the kingdom a massive horde of minions scattered outside ravaging everything from houses to the landscape itself"
    scene black
    with fade
    n"The once beautiful kingdom was turn into a desolate place"
    scene bg forest1
    show akemi 5 at left, flip
    with fade
    n"With determination in her heart, she continued her path and was met someone unfamiliar"
    show himiko 2:
        xalign 1.5 yalign 1.0
        pause(0.15)
        linear 0.3 xalign 1.0
        pause(0.15)
        "himiko 4"
    pause(0.6)
    show akemi 5 at notspeaking
    h"Are you the hero they keep on talking about? Where is the princess? Did she run away like the coward she is? Hahahahaha"
    show himiko 2 at notspeaking
    show akemi 6 at speaking
    a"So, you must be Himiko, the reason why the kingdom is in ruins."
    show himiko 4 at speaking
    show akemi 5 at notspeaking
    h"The one and only!"
    show akemi 6 at speaking
    show himiko 2 at notspeaking
    a"If you are really that powerful then you can defeat me all by yourself! I challenge you in a duel! Just you and me!"
    show akemi 5 at notspeaking
    show bg forest1full behind akemi, himiko
    with dissolve
    show himiko 5 at speaking
    h"And what makes you think I would accept that? You are the one who is outnumbered here, and I can easily command my army to attack you all at once."

    h"What gave you the authority to challenge me in a duel?"
    show akemi 6 at speaking
    show himiko 3 at notspeaking
    a"If you truly are as powerful as you say then there’s nothing to fear about the duel. At the very least if I fail to defeat you, I can have an honorable departure."
    show akemi 5 at notspeaking
    show himiko 4 at speaking
    h"You amuse me, what is your name?"
    show akemi 6 at speaking
    show himiko 2 at notspeaking
    a"I am Akemi the Outworlder that will defeat you once and for all!"
    show akemi 5 at notspeaking
    show himiko 4 at speaking
    h"You amuse me Akemi, I will accept your duel so that you will have a much more humiliating defeat! I want to see you beg as you wish you fought my army instead of me!"
    show himiko 1
    n"Himeko started chanting as she prepared to transport both herself and Akemi to the throne room."

    jump himiko_fight

label himiko_fight:
    scene bg throne2
    with fade
    show akemi 14 at left, flip
    a"What just happened? Where are we?"
    show akemi 13 at notspeaking
    show himiko 4 at right
    h"We are in the Throne Room of the castle where you will rest as the King watches you suffer."
    show akemi 5 at speaking
    show himiko 4 at notspeaking
    a"(Looks towards the throne and saw the king)"
    show charles:
        xcenter 0.75
        yalign 1.0
    show akemi 5 at speaking
    hide himiko
    c"..."
    hide akemi
    show charles:
        xcenter 0.5 yalign 1.0
    with move
    n"As the king stays silent, so does the castle where all of the guards and royalty are now gone and what was left was their echoes."
    hide charles
    show akemi 5 at flip, center
    with fade
    n"This will be Akemi’s final battle!"
    show akemi 5 at center
    show himiko 2 at offscreenright
    with None
    show akemi 5 at left
    show himiko 2 at right
    with move
    show akemi 5 at flip
    show akemi 5 at notspeaking
    show himiko 4
    h"Shall we commence this duel once and for all?"
    show akemi 6 at speaking
    show himiko 2 at notspeaking
    a "Im ready!"
    show akemi 5
    show himiko 2 at speaking
    pause(0.5)
    scene black
    with fade
    n"As Akemi was preparing and taking a stance. Himiko immediately launched an attack towards Akemi hitting her on her left side while a cloud of dust covered."
    show himiko 1
    h"Is it already over? And here I thought I would be able to torture her some…"
    scene bg throne2
    show akemi 15 at flip, left
    with Dissolve(1.0)
    n"As the dust settled, Himiko saw Akemi still standing."
    show himiko 4 at right
    h"So, you were able to be survive..."
    show himiko 3
    n"Himiko paused as she noticed that Akemi only received a scratch."
    show himiko 5
    h"That attack only scratched you? Just how powerful are these items!"
    show akemi 16
    show himiko 3 at notspeaking
    a"That didn’t really hurt too much! So, this must be the power of the ring and with this I have a chance to defeat you!"
    show akemi 15 at notspeaking
    show akemi 15 at flip
    show himiko 5 at speaking
    h"How powerful can these legendary items be? To think that attack will only leave a scratch!"
    show akemi 15:
        alpha 1
        linear 5 xalign 2.0
    hide himiko
    n"Akemi with her newfound confidence charged at Himiko preparing an attack."
    hide akemi
    show himiko 4 at right
    show akemi 15:
        xzoom -1
        xalign -1.0 yalign 1.0
        alpha 1
        linear 0.6 xalign 0.4 yalign 1.0
    h"That attack is nothing (waves hand to try deflecting the attack)"
    show himiko 4:
        pause (1)
        "himiko 3"
        pause (0.8)
        linear 0.5 xalign 1.75
    h"A magician defense must not be…(spell slowly breaks and forced Himeko to retreat)"
    hide akemi
    with dissolve
    show himiko 5 at right
    h"These items’ power holds is impressive if I don’t get serious, I may lose this battle."
    show himiko 1
    h"How are you able to get all 3 Legendary Items especially the necklace since it was broken?"
    show akemi 15 at left, flip
    n"Akemi didn’t respond as she is too focused on the fight as one wrong step may lead to her demise"
    show himiko 3:
        pause(1)
        linear 0.5 xalign 2.0
    show akemi 15
    h"So, you are going to be quiet about everything then so be it! (launches a volley of attacks with different elements)"
    show himiko 3:
        xalign 2.0
        pause(2)
        linear 3.5 xalign 1.0
    show akemi 15:
        linear 0.5 xoffset -200
        linear 0.5 xoffset 100
        linear 0.5 xoffset -250
        linear 0.5 xoffset 0 yoffset 0
        repeat
    n"Akemi although amazed at how powerful Himiko is, however she was unable to say anything as she is to focus on dodging while inching closer and closer towards Himeko waiting for the right opportunity to strike!"
    show akemi 16:
        xoffset 0 yoffset 0
        xalign 0.0
        pause(1)
        linear 0.2 xalign 0.25 yalign 0.5
        linear 0.2 xalign 0.5 yalign 1.0
    show himiko 3:
        linear 0.1 xalign 1.0
    a"I finally got close enough to you (lunges at her preparing for an attack)"
    show akemi 16:
        xalign 0.5 yalign 1.0
        pause(1)
        linear 0.2 xalign 0.0 yalign 1.0
        pause(0.2)
        "akemi 17"
    show himiko 4:
        linear 0.1 xalign 1.0
    h"A magician doesn’t only specialize in long range *As she says that a power spell that was prepared for the opportune moment was launched at Akemi hitting her directly*"
    show himiko 2
    n"The hit was so powerful it launched Akemi towards the wall!"
    show akemi 19
    n"Akemi visible hurt from the blast and impact was bleeding but still able to stand and fight."
    show himiko 5
    h"Still not giving up? Then you will suffer some more!"
    show himiko 3:
        linear 0.5 xalign 2.0
    show akemi 19:
        linear 0.5 xoffset -200
        linear 0.5 xoffset 100
        linear 0.5 xoffset -250
        linear 0.5 xoffset 0 yoffset 0
        repeat
    n"A barrage of spells continued to target Akemi as she tries to dodge and inch forward."
    show akemi 20:
        xoffset 0 yoffset 0
        linear 0.5 xoffset -200
        linear 0.5 xoffset 100
        linear 0.5 xoffset -250
        linear 0.5 xoffset 0 yoffset 0
        repeat
    a"What should I do? Getting closer to her is no problem but I am not fast enough to dodge the attack up close!"
    show akemi 19:
        xoffset 0 yoffset 0
        linear 0.5 xoffset -200
        linear 0.5 xoffset 100
        linear 0.5 xoffset -250
        linear 0.5 xoffset 0 yoffset 0
        repeat
    n"Akemi thinks of a way and wished she had a shield to block the spell to create an opening"
    n"An idea popped up in her head and gathered all her courage because she knew if she fails, she will meet death."
    hide akemi
    with dissolve  
    pause (0.5) 
    show himiko 4:
        linear 0.2 xalign 1.0
    h"You may be strong because of the items but in terms of experience you are no match for me! A simple girl with no sword training is nothing compared to me!"
    show himiko 2
    n"Himiko knows Akemi’s defense so strong, she prepared a spell with all her power and focusing it on one point, strong enough to piece anything. As she did that, she continued her volley of attack not letting Akemi gain any room to rest."
    show himiko 4
    h"With this spell, no matter how strong her defense is this spell will pierce through it!"
    show himiko 2
    show akemi 19:
        xzoom -1
        xoffset 0 yoffset 0
        xalign -1.0 yalign 1.0
        linear 0.5 xalign 0.0
    n"As Akemi is a meter away from Himiko, Himiko unleashed the magic circle where a huge spike burst through with a lot of speed"
    show akemi 19:
        xalign 0.0 yalign 1.0
        pause(0.5)
        linear 0.1 xalign 0.2
    n"This was the opportunity Akemi was waiting for as she clashed with the spell head on with the spell. Both attacks clashed to see which one is more powerful!"
    show himiko 4
    show akemi 19:
        alpha 0.63
        xalign 0.2 yalign 1.0
    h"Give it up Akemi! If you apologize and grovel now, I will let you live and be a part of my army or maybe even bring you back home."
    show himiko 2:
        alpha 0.63
    show akemi 20:
        alpha 1
    a"I don’t need your pity for I will be the victor here!"
    show himiko 2:
        alpha 1
        pause(1)
        "himiko 3"
    n"With all their might, the clashed continued until the spell broke surprising Himeko as the slash was able to connect to Himiko"
    show akemi 19
    show himiko:
        linear 1 matrixcolor SaturationMatrix(1)
        linear 1 matrixcolor SaturationMatrix(0)
        repeat
    n"Himiko collapsed as Akemi points her sword towards her."
    show akemi 20:
        linear 0.2 xalign 0.0
    a"You lose Himiko, surrender and get rid of all minions in the kingdom!"
    show akemi 19
    show himiko 1:
        linear 1 matrixcolor SaturationMatrix(1)
        linear 1 matrixcolor SaturationMatrix(0)
        repeat
    h"So, this is the power of the legendary items? With this power even if my army ambushed you, you will be able to wipe them out."
    show himiko 4:
        linear 1 matrixcolor SaturationMatrix(1)
        linear 1 matrixcolor SaturationMatrix(0)
        repeat
    h"I was supposed to let my minions ambush you, but it is too late now. I will honor our duel and let my army retreat. For I was defeated with honor."
    show himiko 1:
        linear 0.5 matrixcolor SaturationMatrix(0)
        "himiko"
        pause(0.5)
        linear 2 alpha 0
        repeat
    n"As she used her last bit of energy to order her army to retreat, Himiko has met her end."

    n"The battle was done, and Akemi was the Victor!"
    show charles:
        xcenter 0.75
        yalign 1.0
    with Dissolve(1)
    n"Akemi released the king and, with his help, freed all the prisoners."
    hide charles
    with dissolve
    show princess 3:
        xalign 2.0 yalign 1.0
        linear 0.5 xalign 1.0 yalign 1.0
        "princess"
    n"Aoi then reunites with Akemi."
    show princess 2
    pra"You did it, you won! You saved us all from Himiko! Our kingdom is once again free!"
    scene black
    with fade
return
