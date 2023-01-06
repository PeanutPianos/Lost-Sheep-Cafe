# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define k = Character("Kai")
define h = Character("Holle")
define j = Character("Jack")
define a = Character("Amelia")

transform centerfood:
    xalign 0.43 yalign 0.73

transform centerdrink:
    xalign 0.49 yalign 0.73

transform trueleft:
    xalign 0.3 yalign 1.0

transform trueright:
    xalign 0.6 yalign 1.0

label start:
$ drinkchoc = False
$ drinktea = False
$ soupchoice = False


play music winter_music loop

"?" "Winter time is often referred to as a time to be with family and celebrate; However, for some that is not what the holidays entail."
"?" "Let us begin our story like many others before it. Once upon a time two stray sheep lost their way on a winter's day."
"?"  "The wind was frightfully cold that day and the snow was falling heavy and fast. As the snow piled up the two of them realized they each had nowhere to go."
"?" "Then as if fate had taken pity on them they suddenly could see the warm hearth of our cafe. An inviting place where they could warm their cold hands, and cheeks."
"?" "The two who found their way to us on that day were a young man and a young woman about twenty years of age. This is the tale of how we all met each other on that snowy winter's day."  
scene bedroom
with fade

show holle-simple at trueleft 
with dissolve 

h "Jack….Jack! Foolish boy, where are you?"
show jack-simple at right 
with dissolve
j "I’m right here Miss Holle. I was just putting the kettle on to make us some tea."
show holle-smile at center
hide holle-simple
h "Oh how thoughtful of you. Now are you prepared for our guests?"
show jack-tisk at right
j "Guests miss? But it’s a clear night. Unless you are suggesting?"
show holle-simple at center
h "Oh yes I am. I can sense some lost sheep coming our way. Start the ovens and I’ll prepare the beds for them."
    
scene black 
with fade 

h "As we went about our preparations. I knew what I had to do."
h "I took the blankets on the bed, took a deep breath and threw them up into the air. As they softly fell I could feel the temperature dropping."
h "I knew my lost sheep were out there and I would let no sheep go cold this season."

scene outside
with dissolve

show kai-nor at left
k "S-snow right now are you kidding me?"
k "First I have to leave and now it just has to start snowing."
'As I trudged through the snow I could feel the cold nipping at my ankles. I needed to find somewhere to go before I froze.'
show kai-nor at trueleft
k "Come on Kai you can do this."
show kai-nor at center 
k "Just need to k-keep moving."
show kai-sad at center
hide kai-sad    
k "What i-is that?"
"I’d passed this building many times on night walks. It’s abandoned. Nothing has been here for years. So how is there suddenly a cafe?"

scene cafe 
with dissolve
stop music fadeout 2.0
play music cafe_music_looped fadein 1.0 loop

show kai-nor at trueleft
with dissolve
k "W-what?" 
"I couldn’t believe my eyes. It was a full cafe. I swear I have never seen this place here before."
show jack-simple at trueright
with dissolve
j "Oh! Hello there, welcome to the Lost Sheep Cafe."
show jack-talk at trueright
hide jack-simple
j "My name is Jack and I’ll be your server today."
k "The Lost Sheep? When did this place open? I’ve never seen it here before."
j "We’ve been open a long time you could say."
k "What does-"
hide jack-talk 
show jack-talk2 at center 
j "Now can I interest you in a drink? We have Tea, Hot Chocolate, and Coffee right now. If you are feeling hungry we also have homemade potato soup or a chicken soup"
menu:
    "Which soup?"
    "Potato soup": 
        $ soupchoice = True
        show jack-smile at center
        j "Potato soup. Good choice"
    "Chicken soup": 
        show jack-smile at center
        j "Chicken soup. Good choice"
    
menu:
    "Now for yout drink?"
    "Hot Chocolate": 
        $ drinkchoc = True
        hide jack-talk2
        show jack-smile at center
        j "Oh you picked my favorite! One hot chocolate coming up"
    "Coffee": 
        hide jack-talk2
        show jack-smile at center
        j "One cup of coffee coming up!"
    "Tea": 
        $ drinktea = True
        hide jack-talk2
        show jack-smile at center
        j "Good choice we have a nice peppermint tea brewing at the moment."
j "Alright i'll be back shortly!"
hide jack-smile
k "This is strange. First I got caught in a snowstorm and now apparently a cafe has been inside an abandoned building this whole time?"
k "This feels off….but I don’t have anywhere I can go so I guess it will do."
show kai-sad at trueleft
"Thinking back on it now Did I really ever truly have a place I could go…"
hide kai-sad
"I look back and see jack Returning with a bowl and cup in hand"
show jack-simple at trueright

j "Sorry for the wait, here's your order!"
if soupchoice == True:
    show potato at centerfood
else:
    show chicken at centerfood

if drinktea == True:
    show peppermint at centerdrink
elif drinkchoc == True:
    show hotchocolate at centerdrink
else:
    show cupcoffee at centerdrink
    
k "Thank you."
" I take a slow sip of my drink and am surprised"
k "It’s perfect!"
hide jack-simple
show jack-smile at trueright
j "Why thank you. I pride myself on my drink making skills. Now try the soup! It’s Miss Holle’s specialty"
k "Miss Holle?"
hide jack-smile
show jack-talk at trueright
j "Oh yes she's the owner of the cafe and the head chef too. She’s been running the Lost Sheep Cafe for years."
k "I see."
j "So what brought you in here tonight? Other than the snow of course."
k "What do you mean? I only came in because of the snow."
hide jack-talk
show jack-talk2 at trueright
j "No no I mean what brought you here"
k "I really do-"
h "Now Jack, leave the poor boy alone; he's just arrived."
"I quickly look to where the voice is coming from and I see her"
show holle-simple at right
with dissolve  
h "Well now what have we here? A new lost sheep came to my cafe? Well welcome Kai, how is your soup?"
k "The soup is good, but how did you know my-"
hide holle-simple
hide jack-talk2
show jack-simple at right
show holle-smile at trueright
h "Oh dear me I forgot to introduce myself! How foolish Hahaha. Nice to meet you dear, my name is Miss Holle! I’m the head chef and owner here."
hide holle-smile
show holle-simple at trueright
h "Now I know what you are thinking, ‘but I’ve never seen this cafe before,’ and you’d be right!"
k "What do you mean?"
h "Oh Kai I’m not done yet. Ahh to be young again like you. You know when I was your age I was learning how to knit, but that’s besides the point."
hide holle-simple 
show holle-sad at trueright
h "You are here because you need something. Am I right in assuming you feel lost?”"
k "..."
hide holle-sad 
show holle-simple
h "It’s fine to say you are! That’s what I opened this cafe for."
k "..."
h "It’s ok if you can’t talk right now. Feel free to stay here as long as you like, we also have a place to sleep since the snow outside is getting stronger. Practically nothing can survive in the cold."
k "Um- Thank you, thank you miss Holle."
hide holle-simple
show holle-smile at trueright
h "If you want more soup or another drink, feel free to ask me or Jack here. I need to go check on the beds."
"She turns her head to Jack, standing next to her with his hands behind his back."
h "Jack dear boy, tend to Kai if he needs anything. And also, there may be another lost sheep coming to the cafe."
hide holle-smile
hide jack-simple
show jack-talk at right
j "Wow another one!? I’ll get right on it Miss Holle!"
"And without another word she leaves going into what I assume is the bedroom"
"I looked around at the place, it felt strangely like home, but warm and peaceful. Jack takes my empty bowl and cup grabbing something from below the counter."
"Machines to packets and even bottles stood on the shelves, ready to be used. Jack looked back up after a few seconds, and gave me a smile."
hide jack-talk
show jack-smile at center 
j "Did you enjoy the meal?"
k "Yeah! It’s very delicious!"
hide jack-smile
show jack-talk at center
j "Miss Holle would be delighted to hear that her customers love her soup, it’s almost out of this world with how it tastes!"
j "She always adds a special touch to each one. It’s almost as if your own grandma made it."
hide jack-talk
show jack-simple at center 
j "Just say if you want more. We have a whole lot"
hide jack-simple
show jack-tisk at left 
k "Looking for something?"
hide jack-tisk
show jack-talk2 at center
j "Oh it was nothing"
hide jack-talk2
show jack-smile
j "Now since you wolfed it down quickly you must be pretty hungry, want more?"
k "Yes please, I never had a meal like this before... Mostly just a sandwich and the rare takeout."
j "Alrighty then, another order of soup and a drink coming right-"
"Before Jack can finnish his sentence the door opens and the cold air comes in."
"Standing in the door, with the blowing winds and frosty cold rushing inside was a young lady."
show amelia-pre at left
with dissolve
hide jack-smile
hide kai-nor
show jack-smile at trueleft
show kai-nor at center
j "Another lost sheep hmm?"
a "Sheep?"
j "Well, ignore that. My name is Jack. Now please sit down while I fetch you some warm soup and tea. The snow must have taken a great toll on you outside."
"Jack quickly walked to the other side of the counter, disappearing through a door and coming back out with great haste, rushing to the shivering woman with a hot bowl of soup and cup of tea in hand as he prepared the meal for her."
hide amalia-pre
with dissolve
hide kai-nor   
hide jack-smile
with dissolve
show kai-nor at trueleft
"As jack came back with more soup I figured it couldn't hurt to ask"
show jack-simple at center
with dissolve
k "Hmm, who is she?"
hide jack-simple
show jack-talk at center
j "Another lost sheep, like you. I’ll just head to the kitchen to wash a few dishes and come back.."
hide jack-talk 
with dissolve
k "Another lost sheep…"
hide kai-nor
show kai-nor at trueright
"I glanced at the woman"
hide amelia-pre
show amelia-pre at trueleft
with dissolve
"Her hands were shivering while covered in layers of cloth, shivering while wolfing down her own food."
"I started eating again finding the food only seemed to be getting better."
k "This really is good."
show jack-smile at center
with dissolve
j "It is right?"
k "Do i need to pay for this?"
j "Of course not, Just eat as much as you like, this cafe is to help lost sheep in the winter, from food to warmth to rest."
k "Rest?"
hide jack-smile
show jack-talk at center
j "Indeed, rest. Nothing can survive in the snow outside, not to mention the frost out there. The beds are almost ready with soft pillows, and specially hand knitted blankets!"
k "So much hospitality. Back at home the blanket would normally be taken, and the cold would just blow inside…"
a "May I have more please"
j "Right away! Glad you also enjoy Miss Holle’s soup and tea!"
hide jack-talk 
with dissolve
show holle-smile at right
with dissolve
h "Ah! We now have two lost sheep in the cafe."
h "Kai my boy, are you full yet? Or still want more?"
k "Umm, I'm full Miss Holle. Th-Thank you for the hospitality."
h "It is the least I could do for the lost sheep. Oh, the beds are almost ready if you wish to rest."
hide holle-smile
show holle-simple at right
h "What about you Amelia? Do you want more soup? Rest? Or sit here for awhile in the warmth"
a "I’m alright, Miss? Wait how do you know my na-"
hide holle-simple  
show holle-smile at right  
h "Oh foolish me, i forgot once more to introduce myself again, i am Miss Holle. Owner of this warm cafe."
h "And I suppose you also met Jack, my helper in the cafe, along with Kai. Another lost sheep."
a "Well, i’m pretty full for now, i suppose i can rest."
h "Splendid! What about you Kai?"
k "Well I do need rest as well."
h "Excellent! Once the two of you are done, I can bring you to your rooms."
"Just as she finished, Jack came out with a filled cup and bowl. Serving it to Amelia."
hide amelia-pre
show amelia at trueleft
show jack-simple at left
with dissolve
h "Jack, could you kindly lead Kai to his room please? I may tend to Amelia for now."
j "Of course Miss Holle!"
hide holle-smile
with dissolve
hide amalia
with dissolve
hide jack-simple
with dissolve
hide kai-nor 
with dissolve
scene black with fade
"I got up and Jack led me behind the counter. As we passed through a curtain I saw a stairwell leading up"
"At the top of the stairwell the hall was lit up by warm lamps hanging on hooks in the walls. Jack opened the nearest door to us and entered inside."
scene bedroom with fade 
show kai-nor at trueright with dissolve
show jack-simple at trueleft with dissolve
j "Here we are! Your quaint cozy room. Warm and prepared for you."
k "This room is…Wonderful! It's unlike where I slept in before."
hide jack-simple
show jack-smile at trueleft
j "Glad you enjoy it."
"I jumped onto the bed, bringing the blanket up until my body was under it."
j "Is it warm and soft to your liking?"
k "Yes! Very!"
hide jack-smile
show jack-talk at trueleft
j "Glad it is. Well you can rest as long as you wish here. If you need anything you can just go downstairs, I gotta get going now."
j "I think Miss Holle is helping Amelia to her bed as well. Poor soul was broken up with and left to the cold."
hide jack-talk
show jack-simple at trueleft
j "Hopefully you enjoy your stay. We would have to leave when winter is over after all."
k "Wait, leave?"
j "Well. yeah. I gotta get going now. Have a good rest Kai!"
hide jack-simple
with dissolve
k "Leave? Weird, wonder what he meant by that. Right now though, its better for me to rest. I haven’t felt such comfort like this before."
scene black with fade

"As the warmth and comfort embraced me, my mind slowly drifted off to sleep.. The sound of snow hitting the windows slowly went away. Feeling a slumber i may never forget."

"END OF DEMO"
"Thank you for playing our demo! this was made for the 2022 Winter Visual Novel Jam"
"Thank you to our amazing team!" 
"Writers - Asclepius, PeanutPiano, MoonlighttheHobkin"
"Music - Pinefall"
"Character Artist - Candycornskull"
"Background art - Dalishous"
"Programming - PeanutPiano"
"Once again thank you so much for playing!"
return
