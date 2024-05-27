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
# Princess aoi
image princess = im.Scale("princess_def.png", 679, 900)
image princess 1= im.Scale("princess_1.png", 679, 900)
image princess 2 = im.Scale("princess_2.png", 679, 900)
image princess 3 = im.Scale("princess_3.png", 679, 900)
image princess 4 = im.Scale("aoib.png", 679, 900)
# Himiko
image himiko = im.Scale("himiko_def.png", 679, 900)
image himiko 1= im.Scale("himiko_1.png", 679, 900)
image himiko 2 = im.Scale("himiko_2.png", 679, 900)
image himiko 3 = im.Scale("himiko_3.png", 679, 900)
image himiko 3 = im.Scale("himiko_3.png", 679, 900)
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

#background
image bg forest1 = "forest1.png"
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
    a"Moon?" 
    scene white 
    with Fade(.5,.5,.5)
    n"The book glows a bright light and Akemi closed her eyes" 

    n"Akemi heard that someone is calling her and as she slowly opens her eyes, she saw this mysterious woman." 
    stop music fadeout 0.5
    play music "4.mp3" fadein 1.0 fadeout 1.0
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
    show akemi 3 at speaking
    show princess at notspeaking
    pra"May I ask your name, Hero?" 
    show akemi 3 at speaking
    show princess at notspeaking
    a"Hi, my name is Akemi.... Where am I?" 
    show akemi at notspeaking
    show princess 2 at speaking
    pra"Hero Akemi then... you are in the ruins forest; this place is used to summon a hero from another world" 
    show akemi 3 at speaking
    show princess at notspeaking
    a"Huh? I am not a hero; I am just a regular student." 
    show akemi at notspeaking
    show princess 2 at speaking
    n"As Akemi seems confused, Princess Aoi tries to explain everything as she gradually understands the situation and Akemi asks another question." 
    show akemi 3 at speaking
    show princess at notspeaking
    a"I see, so that's what happened.... then why did you summon me here?" 
    show akemi at notspeaking
    show princess 2 at speaking
    pra"Please help me on my quest to defeat an evil magician that has been terrorizing my kingdom and my father..." 

    pra"Please help me..." 
    hide princess
    show akemi at center, speaking
    n"Akemi has been too honest and always helping someone who needs her help even if she puts herself in danger." 

    a"...Okay, I'll help you Princess Aoi" 
    show akemi at left, speaking
    with move
    show akemi 3
    show princess at right, notspeaking
    pra"Really? Thank you so much, hero Akemi." 
    show akemi 3 at speaking
    show princess at notspeaking
    a"It's fine.... and please stop calling me Hero Akemi. It's kind of embarrassing." 
    
    a"Just call me Akemi... " 
    show akemi at notspeaking
    show princess 3 at speaking
    pra"Okay.... Then you can call me Aoi, it’s so nice to meet you!" 
    show akemi 3 at speaking
    show princess at notspeaking
    a"Yeah, nice to meet you too." 
    hide akemi
    hide princess
    with dissolve
    stop music fadeout 0.5
label branch_2:
    play music"5.mp3" fadein 0.5 fadeout 0.5
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

    n "As they entered the elf village, Akemi was amazed at the scenery of the elf village, especially with the giant tree in the center."

    a "Wow! Look at that tree, it looks bigger than the biggest building in my hometown."

    pra"Really? It was said that the tree has been here for thousands of years, and my father told me that it became the guardian of this forest."

    a "Amazing!"

    n "As they enter inside the giant tree, they are greeted by the elder of the elf village."

    elder "Greetings! Princess Aoi, you have grown much."

    pra"It's nice to see you again!"

    elder "Hmm... Princess Aoi, are you doing okay? I heard what happened to your father and your kingdom."

    elder "You know that we have a great friendship with your ancestor and your father. I’m sorry to hear it."

    pra"Thank you for your concern. Please allow me to introduce you to Akemi, the hero I brought to this world to defeat Himiko."

    a "Hello, it's so nice to meet you."

    elder "Hmmm... I guess that you are here to ask us the location of the Blade of Ethereal Fang."

    pra"Yes, we would like to use it on defeating Himiko."

    elder "I will tell you the location, but it's very dangerous in the forest, and up until now many monsters have been wandering there."

    elder "Do you know how to fight them?"

    pra"Yes"

    elder "And how about you, are you prepared to fight such a monster?"

    n "They both looked at Akemi waiting for her response."

    a "Yes, because I made a promise to Princess Aoi to help her."

    elder "Very well then, the location of the sword is located at the center of Whispering Woods..."

    elder "It is west from here, but recently there's a giant snake wandering, and we tried everything we could, but the monster can heal itself easily."

    elder "Princess Aoi, please be careful and look for each other and one more thing always go the center part of the forest because the monster won't go near that location of the sword." 

    a "Yes."

    pra"Okay, thank you so much! Yes, we will be more careful." 

    n "As they started their quest on getting the sword, Akemi asked Princess Aoi..."

    a "Aoi, why did Himiko attack and want to claim your kingdom?"

    pra"Himiko is also a magic caster like me but instead of helping others, she used it for her personal gain, and became obsessed with gaining more power then, later fell into the darkness and wanted to control others through fear and power."

    a "So, she really is obsessed with gaining more power huh."

    n "As Akemi and Princess Aoi got closer to their destination, suddenly an angry giant snake attacked them..." 

    s "(sssSSsss)"

    a "Ahh!"

    pra"Ahh!"

    a "Are you okay, Aoi?!"

    pra"Yes, I am fine."

    s "(sssSSHAAaa)"

    n "As they dodged from the attack of the giant snake, Akemi suddenly stumbled by a tree."

    a "Ahh!"

    n "Then the snake suddenly releases a purple smoke and let it out to Akemi"

    s "(sssSSsss)"

    n "Akemi suddenly felt dizzy and weak with the smoke and the giant snake saw Akemi lie down on the ground"

    n "The giant snake tries to attack again as Akemi looked weak"

    s "(sssSSHAAaa)"

    pra"Akemi, Look out!!"

    n "As Princess Aoi saw Akemi can move, she used her magic and attack the snake with fire"

    pra"Fireball!"

    n "As the giant snake got fired, it got distracted and Princess Aoi used the chance to see and help Akemi"

    s "(sssSSsss)"

    pra"Are you alright, Akemi?"

    a "Yeah, I am fine... I just feel a little dizzy."

    pra"Let's retreat for now."

    a "Yeah, you're right."

    n "As they retreat far away from the monster for now, they rest for a bit."

    pra"Are you okay, Akemi?"

    n "As Princess Aoi asked Akemi if she is okay, she didn't get a respond."

    pra"Akemi, Akemi hey are you okay?"

    n "Princess Aoi shake Akemi and noticed something is strange on Akemi…"

    pra"Huh!? Poison?"

    pra"That is the content of the purple smoke that the snake released earlier."

    pra"I must do something."

    n "As soon as Princess Aoi knows that it is a poison, she began to sight an incantation for magic."

    pra"Heal!"

    pra"Yes, it works, are you okay now Akemi?"

    n "Suddenly Akemi began to open her eyes and see Princess Aoi was about to cry."

    a "Aoi, what happened?"

    pra"Thank goodness you're okay... are you still injured?"

    a "No, I think I am fine... What happened anyway?"

    pra"You got poisoned!"

    a "Oh, I see! Thank you for helping me."

    pra"It’s okay, don't mention it."

    n "As they rested for a bit, Akemi heard something rustling in the forest, and the giant snake appeared again."

    s "(sssSSHAAaa)"

    a "Aoi, look out!"

    pra"Ahh!"

    n "Princess Aoi and Akemi were able to dodge from the snake attack."

    pra"Be careful, Akemi!"

    a "Yeah, we need to run deep in the forest."

    pra"Yeah, you're right! The monster won't go near the location of the sword."

    pra"Akemi, I will cast a support magic on you, but I need some time."

    a "Okay, got it."

    s "(sssSSsss)"

    n "As Akemi tries to distract the giant snake, Princess Aoi is preparing her magic on the side."

    pra"I am ready, Akemi."

    a "Okay!"

    pra"Mega Flare!!"

    s "(sssSSHAAaa)"

    n "As the snake got attacked again by fire, Akemi rushed towards Princess Aoi."

    a "We did it! Let’s go."

    pra"Yeah, but I can’t run that fast because I’ve used all my magic power on that attack."

    a "Okay then, I'll carry you. Let’s go."

    pra"Thank you Akemi."

    a "No worries."

    n "Akemi carries Princess Aoi and ran fast at the center of the forest as much as they could."

    a "AAHHH! We made it!"

    pra"Yeah!"

    n "As they got in the center of the forest, Akemi look at the sword"

    a "So, that is the Blade of Ethereal Fang"

    pra"Yes, go on Akemi, try to pull it."

    a "Yeah okay, let’s do this."

    n "As Akemi approaches to the sword, she can already feel the power and wonders if this is the reason why the monster can’t go near it,"

    n "As Akemi holds the sword, she felt warm feelings all over her body."

    a "Here’s go nothing on trying."

    n "As soon as Akemi tried to pull the sword, she felt it was too light."

    a "Yes! Look Aoi, I did it! I pulled the sword."

    n "Princess Aoi looked at Akemi and smiled."

    pra"Yes, you did it!"

    a "Let's rest here for a while, are you still tired?"

    pra"Yes, thank you for asking."

    n "Akemi and Princess Aoi finally rested for a bit. They are now trying to go back to the elf village once again."

    a "Finally, we got the Blade of Ethereal Fang. We’re close in saving your Kingdom, Aoi."

    pra"Yes."

    s "(sssSSsss)"

    n "Akemi and Princess Aoi chatting, the snake appears again on their way."

    a "Aoi, be careful. Let's defeat this giant snake for real this time."

    pra"Right!"

    n "Akemi proposes a plan on how to fight the giant snake…"

    a "Use your magic and support me as I will draw its attention. Try to use fire magic only."

    pra"Okay"

    s "(sssSSsss)"

    n "Akemi draws the attention of the snake and Princess Aoi used fire magic to make the giant snake more confused."

    n "Because of this, the giant snake tries to use the purple smoke and Princess Aoi used her support magic for Akemi resists to be poised just a short of time"

    pra"Now is your chance, Akemi."

    a "Right, HYAAAA!"

    s "(sssSSHAAaa)"

    n "Akemi jumps high and goes directly to attack the head of the snake. As she swings her sword to the head, it lands on the giant snake's head."

    a "Wow, this sword cut it like paper... we did it Aoi!"

    pra"Yeah... that was amazing Akemi!"

    a "Let's go back to the elf village now."

    pra"Yeah."

    n "Akemi and Princess Aoi got in front of the elf village. The elves were surprised to see that Akemi is holding the Blade of Ethereal Fang"

    elder "I am so glad that you are safe Princess Aoi and Akemi."

    pra"Thank you."

    n "Akemi and Princess Aoi explained what happened, they are relieved and surprised because they were able to slay the giant snake."

    elder "I have been trying to find out for a long time how did that snake appeared out of nowhere and how it releases purple smoke."

    pra"Himiko must be the one behind it. She must be trying to stop someone who will search for the sword."

    elder "It must be.... but the sword can’t be pulled by a normal person, Akemi."

    a "Yes."

    elder "The sword chooses you to be its user. Please use it only for good."

    a "I will."

    elder "I assumed that the two of you will continue your journey, we will all pray for your success and safety, good luck Akemi and Princess Aoi."

    a "Thank you!"

    pra"Thank you!"

    n "Akemi and Princess Aoi say goodbye to the elf village as they take off on their next journey."

with dissolve
#Necklace of Valor
label branch_4:
    scene black
    with dissolve
    n"As Akemi and Princess Aoi set their journey to get the Necklace of Valor from the dwarf kingdom which is from the Ironforge mountain."
    with dissolve
    scene bg fgdwarf
    show princess 2
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
    hide princess at top
    hide akemi at top
    with dissolve
    n"Akemi and Princess Aoi got closer to the entrance of the the dwarf kingdom."
    with dissolve
    scene bg gatedwarf
    show princess 2
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
    show throin at speaking 
    show princess at notspeaking
    k"I fear I must deliver grim tidings."
    
    n"The king tells them with heavy sorrow."
    
    k"The Necklace of Valor was stolen and destroyed from us by one of Himiko’s men in the past few months by General Ragnor, a cunning and ruthless adversary."
    show princess 3 at speaking
    n"Princess Aoi’s heart sank at the news, but before she could despair, King Throin spoke again, his tine resolute."
    show princess 3 at notspeaking
    k"However, there’s another way. We can forge a new necklace, one that is more powerful than its predecessor."
    show princess 2 at speaking
    n"A glimmer of hopes sparked within Princess Aoi’s heart at the King's words, but their joy was short-lived as the ground tremble beneath their feet a harbinger of impending danger."
    hide princess
    hide throin
    show durin
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
    pra"*Swiftly blocking Minion 2's attack and providing a shield* I’ve got your back, Akemi!"
    show princess 4:
        linear 0.2 xalign -0.2 yalign 1.0
    show akemi 5 at left, flip:
        xalign -1.0 yalign 1.0
        linear 0.4 xalign 0.7 yalign 1.0
        linear 0.4 xalign 0.0 yalign 1.0
    pause(0.7)
    hide minion1
    with dissolve
    pause(0.7)
    show ragnor:
        xcenter 0.75
        yalign 1.0
    with Dissolve(2.0)
    n"As they defeated the minions, a menacing figure stepped out from the shadows... General Ragnor himself."
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
    pra"And we fight for a just cause! *Casts a protective spell on Akemi*"

    g"*Deflects Aoi's attack with a powerful swing* Foolish girl!"
    hide princess
    show akemi
    a"(Flanking Ragnor) Over here, brute! (Strikes at Ragnor's side)"

    g"(Roars in anger) You will pay for that! (Swings his massive axe at Akemi)"
    hide akemi
    show princess
    pra"Akemi, look out! (Uses her shield to block the axe)"

    n"The battle intensifies, with Akemi and Aoi coordinating their attacks, wearing Ragnor down"

    g"(Breathing heavily) This... this cannot be!"

    a"It's over, Ragnor. Surrender!"

    g"Never! (Lunges desperately)"

    pra"(Providing a final spell boost to Akemi) Now, Akemi!"
    hide princess
    show akemi
    a"(With a final, powerful strike) For the dwarves! For our people!"
    
    n"With a final, resounding clash, General Ragnor fell to the ground, defeated. The cavern echoed with the silence of their victory."
    n"With the gem safely in their possession, Akemi and Princess Aoi return to the dwarven kingdom, their hearts buoyed by the success of their mission."
    hide akemi
    with dissolve
    play music"7.mp3" fadein 0.5 fadeout 0.5 
    scene bg cc
    show princess 2 at left
    pra"Akemi, look! Over there, deep in the mining cave. It's the Mystic Lunar, shimmering in a radiant sky blue. It's truly breathtaking... Our journey was not in vain, this gem holds the key to our kingdom's salvation."
    hide princess
    show akemi 2 at left 
    a"Princess Aoi, I've never seen anything so beautiful. It's like the heavens themselves have descended into this cave. With this gem, we can forge the Necklace of Valor and bring hope back to your people."
    with dissolve
    scene black
    show bg ctr 
    with fade
    n"As Akemi and Princess Aoi return, King Throin greeted them with gratitude. He thanked both for their bravery."
    k"You have defeated General Ragnor and I congratulate you on your victory. It seems the victory has weakened our enemy's forces."
    with dissolve
    scene bg throne1
    a"Thank you, King Throin. We're honored to have helped. Our encounter with General Ragnor was challenging, but with Princess Aoi's leadership, we prevailed."

    k"Your bravery has brought light to our kingdom in these dark times. With the Mystic Lunar in our possession, we can now forge a necklace stronger than ever before. Guards, prepare the forge and summon our most skilled smith. The Necklace of Valor shall rise again!"
    hide akemi
    show princess
    pra"Akemi, our journey together has been filled with danger and uncertainty, but seeing the Mystic Lunar fills me with hope. We've faced adversity and triumphed, and now our kingdom can rebuild."
    hide princess
    show akemi 
    a"Princess Aoi, it's been an honor to fight by your side. Your courage and determination inspire me. Together, we've overcome every obstacle, and I have no doubt that we'll continue to do so."
    hide akemi
    show princess
    pra"Thank you, Akemi. Your strength and loyalty have been invaluable to our cause. Let us go forth and ensure that the Necklace of Valor is forged with the same determination that brought us here! But for now we must rest up I am tired!"
    n"After all was said and done everyone rested up for a few days waiting for the smith to finish forging the Necklace of Valor"
    n"While resting, Akemi notice something is worrying Princess Aoi."
    a"Aoi are you okay? I can see the worry in your eyes."

    pra"Thank you Akemi, I am just worry about my father and the people of Azurevale"
    hide princess
    show akemi at left
    a"I see... But for now, let us focus on the task at hand. We have the gem, and soon we will have the necklace. With its power, we will be better equipped to face whatever challenges lie ahead."
    hide akemi
    show princess 2 at left
    pra"You're right, Akemi. We must stay focused on our mission. But I cannot shake the worry for my father and my people. They need us now more than ever."

    a"We'll do everything we can to protect them, Princess. But for now, let's trust in the dwarven craftsmanship and the magic of the necklace."

    pra"Yes, you're right, Akemi. Thank you for your support. Let's assist wherever we can in the dwarven kingdom while we await the completion of the necklace."
    with dissolve
    scene black
    n"As they awaited the necklace's completion, Akemi and Princess Aoi spent their days in the dwarven kingdom, assisting those in need. Though outwardly brave, the weight of their responsibilities grew heavier, intensifying their sense of urgency."

    n"On the day of completion, King Throin presented the finished necklace to Akemi and Princess Aoi."
    stop music fadeout 0.5
    with fade
    scene bg throne1
    k"This necklace is a testament to your bravery and determination. May it serve you well in your quest to bring peace to your kingdom."

    pra"Thank you King Throin"
    hide princess
    show akemi
    a"Thank you"

    n"As they set their next journey, the grand halls of the royal palace, they were greeted with cheers and applause from the dwarven citizens, who hailed them as heroes."

    if menu_flag == False:
        jump branch_3
    elif menu_flag == True:
        jump branch_5

label branch_5:
    scene black
    n"Akemi and Princess Aoi continue and prepare their journey and Princess Aoi turned to Akemi with a determined look in her eyes."
    with fade
    scene bg deepforest
    show princess
    pra"Akemi, there is one final item we need to retrieve toeat Himiko once and for all."
    n"she explained, her voice filled with resolve"
    pra"The Crimson Radiance Ring, said to protect its wearer from even the most powerful of attacks. However, it is in the realm of one of the Heavenly Dragons, guarded for millennia, awaiting the true and worthy hero to retrieve it."
    hide princess
    show akemi 2
    n"Akemi nodded, understanding the gravity of their task." 
    a "Then we must journey to the realm of the Heavenly Dragon and prove ourselves worthy of the Crimson Radiance Ring."
    n"She replied, her voice steady with determination"
    a"Together, we will face whatever challenges lie ahead and emerge victorious."
    hide akemi
   
    n"With their hearts set on their next quest, Akemi and Princess Aoi, their minds filled with thoughts of the trials and tribulations that awaited them."
    with dissolve
    scene black 
    #black screen
    n"As one of the minions of General Ragnor escaped from the kingdom of the dwarves,"
    n"he wasted no time in delivering his message to Himiko. Rage consumed her as she learned of Princess Aoi and Akemi's involvement."
    with fade
    scene bg throne2
    show himiko 
    min1"Your Majesty General Ragnor was defeated by a Princess Aoi and a girl named Akemi."
    hide Himiko
    show himiko 3 at left
    h"What...theyeated Ragnor what Ragnor is supposed to be strong, and he was defeated."
    min1"What should we do you Majesty."
    h"Bring me King Charles (king of Azurevale) from his cell now!"
    min2"Yes, your Majesty."
    n"The Minion brings King Charles to Himiko and asks him the location of the Crimson Radiance Ring."
    hide himiko 3
    show himiko 1
    h"Hmmm...I want you to tell me something and don't think of lying to me! "
    c"Hmmm... "
    h"Tell me the location of the Crimson  of Radiance Ring."
    c"Hmmm...I won't tell you even if you threat to kill me"
    h"hmm....If you don't tell me the location of the Crimson radiance ring i will kill ever person in this castle HAHAHHAHAH!"
    h"And that's not all I will also kill your beloved daughter"
    c"You monster don't you dare to hurt her...or-"
    hide himiko 1
    show himiko 2
    h"AHAHAHAH!...Or what haha what can you possible do in your current state...I make you a deal, I will order my Servant to only capture Princess Aoi and return her to you safe and sound if you tell me the location of the ring."
    c"Hmmm....I want you to give me your word that you won't hurt my daughter and my people."
    h"Hehe, Fine i give you my word"
    c"The location of the Crimson Radiance Ring is in the Heavenly Dragon Mountain."
    hide himiko 2
    show himiko 1
    h"Was that hard to say, take him back to his cell. "
    n"With King Charles returning to back to his cell his heart heavy with guilt and despair, he hoped to protect his people and Princess Aoi from her wrath."
    n"But as soon as the information was in her grasp, Himiko's true intentions were revealed. With a wicked grin, she ordered her minion to return the king to his cell, his fate sealed for daring toy her."
    h"Heavenly Dragons Mountain huh....Let's see if this time they will survive HAHAHAAHAH!."
    n"Himiko concocted a sinister plan to ensure Akemi and Princess Aoi's demise. Harnessing her dark powers, she formed a purple orb infused with her malevolent energy."
    h"Come my servant i want to give you a special quest right now you are my general I need you to deliver this in the heavenly dragons Mountain now, "
    min1" I am honored your majesty."
    n"The orb contains some of Himiko power and it will realease  a purple smoke that will make any living creature to go berserk and becomes Himikos pawn,meanwhile Akemi and Princess Aoi continue their journey. "
    hide himiko
    with dissolve
    scene black
    h"HAHAHAHAHAHAHHA!"
    with fade
    #Next Scene for akemi and aio  ot heavenly dragon mountain
    scene bg mountain
    show akemi 
    a"So thats the heavenly Mountain Dragon."
    hide akemi
    show princess
    pra"Yes..theirs also a dragon living there"
    hide princess
    show akemi
    a"Really thats amazing, wait if there is a dragon living there then we will get attacked by it"
    hide akemi
    show princess
    pra"No its okey the dragon thats been living there is actually a kind dragon he never go attack human as long as it doesnt bother him."
    hide princess
    show akemi
    a"Really then were safe..as long as we dont bother him okey seems easy."
    hide akemi
    show princess
    pra"Yes"
    dragon"(Roar)RAWWWWWWW!!!!"
    n"As Akemi and Princess Aoi continue their walk a violent wind suddenly whipped around them."
    hide princess
    show akemi
    a"Aoi, AAHHHH!"
    hide akemi
    show princess
    pra"Akemi, AAHHHH!"
    hide princess
    show akemi
    a"It's the Dragon...Be careful Aoi.!!"
    n"As the dragon poised itself for another strike, Akemi leaped high into the air, carrying Princess Aoi to safety."
    a"Are you okey Aoi. "
    hide akemi
    show princess
    pra"Yes, i am fine, Thank you."
    hide princess
    show akemi
    a"Stay here i deal with the dragon."
    n"Akemi drew her sword, ready to face the formidable foe. With a swift and precise strike, she lunged at the dragon, but to her astonishment, her blade had no effect. "
    a"What...It didn’t work, what's going on?"
    n"Princess Aoi uses her magic to strike the dragons wing and to Akemi is surprised that magic is working. She also try to use it."
    a"So magic works huh..then let's see you try to take this."
    n"The sword lights fire and Akemi try to slash the dragon but as soon as Akemi is about to attack Princess Aoi stops her."
    hide akemi
    show princess
    pra"Wait Akemi!!"
    hide princess
    show akemi 
    a"Huh,why whats wrong."
    n"As soon as Akemi got stopped by princess Aoi the dragon raise up and started to fire a multipe fireball."
    a"Whooo!, Thats was close."
    hide akemi
    show princess
    pra"Akemi lets hide for now, trust me. "
    hide princess
    show akemi 
    a"Really, Okey if you say so."
    with fade
    scene bg deepforest
    n"Akemi and princess Ai ran deep to the forest were the stumble a lake and Princess Aoi explained to Akemi what she noticed."
    show akemi 3
    a"What happen why did you stop me. "
    hide akemi
    show princess
    pra"That dragon seems in pain and under an influence of something like there is something controlling it against its will."
    hide princess
    show akemi 
    a"Then what should we do."
    hide akemi
    show princess
    pra"I know that i am asking too much, but can we save it. "
    hide princess
    show akemi
    a"Okey if that's what you want so how we will help it."
    hide akemi
    show princess
    pra"Hmmmmm...how about we investigate his lair maybe we can find somethig there or."
    pra"We can try to make it unconscious and see what is going on to him Whats your choice?"
menu:
        "Investiagte the cause":
            $ menu_flag = True
            jump invest_dragon

        "Fight the dragon":
            $ menu_flag = False
            jump fight_dragon

label invest_dragon:
    hide princess
    show akemi 
    a"We should investigate it then" 
    hide akemi
    show princess
    pra"Okey then "
    with dissolve
    n"As they try to hide from the trees to go look for the dragon lair Princess Aoi saw something."
    scene bg cave1 
    pra"Hmm,whats that, Akemi come over here"
    hide princess
    show akemi
    a"What did you saw."
    hide akemi
    show princess
    pra"There's seemed to be a cave over theirs seem to be a purple fog inside it."
    hide princess
    show akemi 
    a"We Should go and see it."
    hide akemi
    show princess
    pra"Okey, but first i will cast a spell to prevent us from that purple smoke."
    with dissolve
    scene bg cavepurple
    n"Akemi and Princess Aoi enter the cave the saw a purple orb that is releasing purple smoke. "
    hide princess
    show akemi
    a"What is that should we go and see it."
    hide akemi
    show princess
    pra"Okey, but lest be carefull"
    n"Akemi and Aoi got closer to the purple orb Princess Aoi looks it and realize that this is Himiko’s doing."
    pra"I see now Himiko must have used this purple orb to control the dragon. "
    hide princess
    show akemi 3 
    a"Should we destroy it then?"
    hide akemi
    show princess
    pra"Wait if we just destroy it the smoke will get more powerful  "
    hide princess
    show akemi
    a"So What should we do"
    hide akemi
    show princess
    pra"We need to purify it by chaneling light magic maybe it will stop the smoke but my magic it not enough to purify it but I think you can do it  Akemi you Blade of Ethereal Fang to cast the light magic and necklace of valor to boost your magic."
    hide princess
    show akemi at left
    a"Okey, i will try"
    n"Akemi try to focus with the help of the elder of the elf Akemi is able to cast magic into the sword and as the sword lights all the smoke slowly vanishes, and the purple orb suddenly turns gray. "
    a"HMMMMMM!MMMMMM!!! "
    hide akemi
    scene bg cavepurple
    with fade

 
    scene bg gcave

    n"Princess Aoi notice that the purple smoke gradually fading and the orb is turning into a gray orb"
    show princess
    pra"Yes thats it Akemi you did it now we should see what the condition of the dragon is outside"
    n"Akemi saw the dragon fall sleep nearby when the purple smoke is gone."
    with fade
    jump outcome



label fight_dragon:
    hide princess
    scene bg deepforest
    show akemi 
    a"We should fight it if we dont try to stop in now the dragon might attack an innocent"
    hide akemi
    show princess
    pra"Okey, I understand."
    pra"First we need plan, magic is the only thing to hurt him and we have to knock him down so i will be able to observe what is wrong with him, "
    hide princess
    show akemi
    a"I Have an idea Aoi."
    hide akemi
    show princess
    pra"Okey lets hear it."
    hide princess
    show akemi 
    a"First I will draw its attention and you try to attack him with magic and once he is down i will try to use a bind magic so he mont be able to move"
    hide akemi
    show princess
    pra"Okey I,got it."
    n" As Akemi try to shout loudly to lure the dragon."
    hide princess
    show akemi 
    a"HYYAAAAAAAAAAA!!"
    n" A violent wind dash through Akemi as see observe where will it attack Akemi."
    a"Hmmm,Over there, aoi get ready."
    hide akemi
    show princess
    pra"On it."
    n"Narator As akemi draw the attention of the dragon princess Aoi used this chance to fire at the dragon."
    pra"FireBall"
    n"As the dragon got hit Akemi used a binding magic to seal the movement of the dragon while Princess Aoi notice the purple aura raleasing n the body of the dragon"
    pra"Akemi I got it we need to use light magic to remove the purple aura but my magic is not enough."
    hide princess
    show akemi 
    a"I will do it i will used the Blade of Ethereal Fang to cast the light magic and necklace of valor to boost your magic"
    n"As Akemi concentrate in casting light magic the sword light and the necklace glow and the purple aura is slowly fading and making the dragon fall sleep"
    jump outcome

#Same ending for branch 6
label outcome:
    scene bg deepforest
    n"Exhausted from the Akemi and Princess Aoi shared a triumphant smile, knowing they had succeeded in freeing the dragon from Himiko's control, As minutes passed, the dragon stirred awake, its eyes filled with remorse for its actions. "
    show akemi 
    a"Hi are you okey?"
    hide akemi
    show princess
    pra"How are you feeling?"
    hide princess
    dragon"Yes and thank you for saving me."
    pra"My name is Aoi and this is my companion Akemi."
    show akemi
    a"Hi whats your name."
    dragon"Akemi and Aoi it's a pleasure to meet you...My name is Draythorn" 
    n"As they rest for bit, Draythorn asks what are they doing here in heavenly mountain?"
    hide akemi
    show princess
    pra" We are looking for the Crimson of Radiance Ring."
    dra"So you are also looking for it too?" 
    hide princess
    show akemi 
    a"What do you mean by that "
    dra"When i was under the influence of that purple smoke a keep hearing a female voice to destroy someone and bring her the ring."
    hide akemi
    show princess
    pra"Its Himiko again."
    hide princess
    show akemi
    a"Yeah and she is probably trying to get the ring for herself."
    dra" So that's her name huh, it's true that i have the ring but it won't work if I don't give my magic to power to it, I will give you the ring as a reward for helping me and promise me this Akemi and Princess Aoi toeat Himiko."
    a" I Promise"
    hide akemi
    show princess
    pra" I Promise"

    n"Draythorn gave Crimson Radiance Ring. Akemi donned the ring, feeling its power course through her veins, and to their surprise, Draythorn blessed the ring, imbuing it with even greater strength. "
    n"With their mission accomplished, Draythorn offers Princes Aoi and Akemi a ride. As they soared towards the edge of the forest"
    n"they bid farewell to Draythorn, expressing their gratitude for his aid and the swift ride, With the Crimson Radiance Ring in their possession"
    n"and Draythorn's blessing, Akemi and Princess Aoi continued their quest with renewed determination"

label branch_6:
    scene bg forest1
    show princess
    pra"Now that we have gathered everything, we finally have all the necessary items needed to defeat Himiko!"
    hide princess
    show akemi 2 at left
    a"Lead the way princess towards the Kingdom of Azurevale."
    hide akemi
    show princess 2
    pra"Draythorn dropped us off at the outskirts of the Kingdom, it will only take us half a day on foot to reach Azurevale, if we follow this path, we should be fine."
    show akemi 2 at left
    a"Then, let’s get going then…"
    hide akemi
    n"Akemi and Aoi set off to the kingdom of Azurevale."

    n"As they follow the path towards the kingdom their surroundings are filled with destruction and despair as they see villages nearby abandoned, natural resources destroyed, and dead bodies scattered in the area."

    n"Fear soon filled the air as the duo witnessed the results of their evil thinking how bad it is at the center of it all."
    show princess 3 at left
    pra"This is one of the villages that are outside of the Azurevale. I know Himiko is evil, but it is worse than I thought."

    pra"All villagers that met their untimely demise, the houses are in ruins, even the farms and surrounding forest are reduced to ashes."

    pra"Can we really win this fight against Himiko? "

    pra"Was calling you from the other world was a big mistake?"

    pra"If this is what happened to the outskirts of the kingdom then how bad is it at the castle?"

    pra"I am afraid we are too late to take action?"

    pra"What do you think we should do?"
    menu:
        "Akemi comforted Aoi ":
            jump option_1

        "Akemi made Aoi stay":
            jump option_2
    

    
label option_1:
    hide princess
    show akemi 2 at left, flip
    a"Aoi you are the Princess of Azurevale, the one who helped me through this journey to get the necessary equipment to defeat Himiko, and the one who will free your people from Himeko."
    a"We may not be able to save everyone but there are still people who are waiting to be save and if we don’t stop her then she will continue destroying everything"
    hide akemi
    show princess 3 at right
    pra"You are right, defeat is never an option. We must continue."
    pra"I will support you with all I got Akemi and together we will defeat Himiko!"
    hide princess
    n"The duo continued its way towards the kingdom but as they get closer and closer to their destination the sound of demons screaming and the undead growling can be heard getting louder and louder"
    hide akemi
    hide princess
    n"Then they saw it, outside of the kingdom a massive horde of demons and undead scattered outside ravaging everything from houses to the land scape itself"
    n"The once beautiful kingdom was turn into a desolate place by the army"
    n"As both of them are shocked at what they saw Akemi filled with self-doubt asked Princess Aoi"
    show akemi 3 at left , flip
    a"With all these demons and undead are we able to fight this head on?"
    hide akemi_def
    show princess at right
    pra"Although the legendary equipments are powerful, they only protect you and an ambush from Himiko herself can easily be the death of both of us."
    pra"Our best bet is to avoid conflict against the whole army and sneak our way in!"
    show himiko 2
    h"That’s a brilliant idea princess! *Binds the princess*"
    hide princess
    h"You may have the legendary equipment (looks at Akemi) but the princess doesn’t have anything!"
    n"Akemi surprised of what happened angerly tried to attack Himiko but was swiftly blocked by Himiko’s demons."
    h"What will you do now that you lost your partner? Are you really going to fight me and my army all on your own?"
    show akemi 3 at left, flip
    a"What should I do? Why is she here? Can I even defeat her with her army?"
    show princess at right
    pra"Stop doubting yourself!"
    pra"We have come this far just to give up! We got everything we needed. You can do it, Akemi!"
    pra"You have all you need to defeat her!"
    hide princess
    show akemi 2 at left, flip
    a"You are right princess!"

    a"Himiko! If you are really that powerful, then you can defeat me all by yourself! Stop hiding behind your minions like a coward and fight me in a duel! Just you and me!"
    show himiko 2 at right
    h"And what makes you think I would accept that? You are the one who is surrounded here, and I can easily command my army to attack you all at once."

    h"What gave you the authority to challenge me in a duel?"

    a"If you truly are as powerful as you say then there’s nothing to fear about the duel. At the very least if I fail to defeat you, I can have an honorable departure."

    h"You amuse me. Your name is Akemi, correct?"

    a"Yes, I am Akemi the Outworlder that will defeat you once and for all!"

    h"You amuse me Akemi, I will accept your duel so that you will have a much more humiliating defeat! I want to see you beg as you wish you fought my army instead of me!"

    h"Take the princess to the dungeon with the rest of the people and do not interfere with our fight!"

    n"Himiko started chanting as she prepares to transport both herself and Akemi to the throne room."

    jump himiko_fight

    

label option_2: 
    hide princess
    show akemi 2 at left, flip
    a"I am afraid that something bad may happen to you princess, so I must fight her alone."

    pra"What are you saying? That’s suicide!"

    a"I know it may be suicide but what will happen when we fail to defeat Himiko, and you didn’t survive?"

    a"What would happen if we won but at the cost of your life? Who will lead your people? Who will look for help from other kingdoms when things don’t go our way?"

    a"I will continue to take this path alone. Please go back or stay at a safe place."

    a"I will be back when everything is done and if I don’t come back ask the other kingdom for help."
    hide princess
    n"As Princess Aoi thought of everything Akemi has said. Akemi heads towards the Azurevale."

    n"As Akemi gets closer and closer to her destination the sound of demons screaming and the undead growling can be heard getting louder and louder"

    n"Then she saw it, outside of the kingdom a massive horde of demons and undead scattered outside ravaging everything from houses to the landscape itself"

    n"The once beautiful kingdom was turn into a desolate place"

    n"With determination in her heart, she continued her path and was met someone unfamiliar"
    show himiko 2 at right
    h"Are you the hero they keep on talking about? Where is the princess? Did she run away like the coward she is? Hahahahaha"

    a"So, you must be Himiko, the reason why the kingdom is in ruins."

    h"The one and only!"

    a"If you are really that powerful then you can defeat me all by yourself! I challenge you in a duel! Just you and me!"

    h"And what makes you think I would accept that? You are the one who is outnumbered here, and I can easily command my army to attack you all at once."

    h"What gave you the authority to challenge me in a duel?"

    a"If you truly are as powerful as you say then there’s nothing to fear about the duel. At the very least if I fail to defeat you, I can have an honorable departure."

    h"You amuse me, what is your name?"

    a"I am Akemi the Outworlder that will defeat you once and for all!"

    h"You amuse me Akemi, I will accept your duel so that you will have a much more humiliating defeat! I want to see you beg as you wish you fought my army instead of me!"

    n"Himeko started chanting as she prepared to transport both herself and Akemi to the throne room."

    h"Will this be a suitable place for the duel? And for our audience we have the King himself!"

    jump himiko_fight

label himiko_fight:
    show akemi 3 at left, flip
    a"What just happened? Where are we?"
    show himiko 2 at right
    h"We are in the Throne Room of the castle where you will rest as the King watches you suffer."

    a"(Looks towards the throne and saw the king) What have you done to the king?"

    h"Nothing really, He was very reluctant to give me his Kingdom, so I made sure he wouldn’t change his mind."

    a"By chaining him to the throne? This is torture!"

    h"That’s what he wanted its not like I killed him or something he is still alive"

    n"As the king holds on to his life, so does the castle where the pillars and walls that became the foundation of the castle where now damaged and barely able to support the ceiling."

    n"This will be Akemi’s final battle!"

    h"Shall we commence this duel once and for all?"

    a "Im ready!"

    n"As Akemi was preparing and taking a stance. Himiko immediately launched an attack towards Akemi hitting her on her left side while a cloud of dust covered."

    h"Is it already over? And here I thought I would be able to torture her some…"

    n"As the dust settled, Himiko saw Akemi still standing."

    h"So, you were able to be survive..."

    n"Himiko paused as she noticed that Akemi only received a scratch."

    h"That attack only scratched you? Just how powerful are these items!"

    a"That didn’t really hurt too much! So, this must be the power of the ring and with this I have a chance to defeat you!"

    h"How powerful can these legendary items be? To think that attack will only leave a scratch!"

    n"Akemi with her newfound confidence charged at Himiko preparing an attack."

    h"That attack is nothing (waves hand to try deflecting the attack) A magician defense must not be… (spell slowly breaks and forced Himeko to retreat) These items’ power holds is impressive if I don’t get serious, I may lose this battle."

    h"How are you able to get all 3 Legendary Items especially the necklace since it was broken?"

    n"Akemi didn’t respond as she is too focused on the fight as one wrong step may lead to her demise"

    h"So, you are going to be quiet about everything then so be it! (launches a volley of attacks with different elements)"

    n"Akemi although amazed at how powerful Himiko is, however she was unable to say anything as she is to focus on dodging while inching closer and closer towards Himeko waiting for the right opportunity to strike!"

    a"I finally got close enough to you (lunges at her preparing for an attack)"

    h"A magician doesn’t only specialize in long range *As she says that a power spell that was prepared for the opportune moment was launched at Akemi hitting her directly*"

    n"The hit was so powerful it launched Akemi towards the wall!"

    n"Akemi visible hurt from the blast and impact was bleeding but still able to stand and fight."

    h"Still not giving up? Then you will suffer some more!"

    n"A barrage of spells continued to target Akemi as she tries to dodge and inch forward."

    a"What should I do? Getting closer to her is no problem but I am not fast enough to dodge the attack up close!"

    n"Akemi thinks of a way and wished she had a shield to block the spell to create an opening"

    n"An idea popped up in her head and gathered all her courage because she knew if she fails, she will meet death."

    h"You may be strong because of the items but in terms of experience you are no match for me! A simple girl with no sword training is nothing compared to me!"

    n"Himiko knows Akemi’s defense so strong, she prepared a spell with all her power and focusing it on one point, strong enough to piece anything. As she did that, she continued her volley of attack not letting Akemi gain any room to rest."

    h"With this spell, no matter how strong her defense is this spell will pierce through it!"

    n"As Akemi is a meter away from Himiko, Himiko unleashed the magic circle where a huge spike burst through with a lot of speed"

    n"This was the opportunity Akemi was waiting for as she clashed with the spell head on with the spell. Both attacks clashed to see which one is more powerful!"

    h"Give it up Akemi! If you apologize and grovel now, I will let you live and be a part of my army or maybe even bring you back home."

    a"I don’t need your pity for I will be the victor here!"

    n"With all their might, the clashed continued until the spell broke surprising Himeko as the slash was able to connect to Himiko"

    n"Himiko collapsed as Akemi points her sword towards her."

    a"You lose Himiko, surrender and get rid of all demons and undead in the kingdom!"

    h"So, this is the power of the legendary items? With this power even if my army ambushed you, you will be able to wipe them out."

    h"I was supposed to let my demons ambush you, but it is too late now. I will honor our duel and let my army retreat. For I was defeated with honor."

    n"As she used her last bit of energy to order her army to retreat, Himiko has met her end."

    n"The battle was done, and Akemi was the Victor!"

    n"Akemi released the king and, with his help, freed all prisoners."

    n"Aoi then reunites with Akemi."

    pra"You did it, you won! You saved us all from Himiko! Our kingdom is once again free!"

with dissolve
return

