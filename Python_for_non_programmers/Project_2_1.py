from webbrowser import get


text = """
I'm going through changes
I'm going through changes
Lately I really, feel like I'm rolling Delph for like Philly
I feel like I'm losing control of myself, I sincerely
Apologize if all that I sound like, is I'm complaining
But life keeps on complicating and I'm debating
On leaving this world, this evening, even my girls
Can see I'm grievin', I try and hide it
But I can't, why do I act like I'm all high and mighty
When inside, I'm dying, I am finally realizing I need help
I can't do it by myself
Too weak, 2 weeks I've been having ups and downs
Going through peaks and valleys, dilly dallying
Around with the idea of ending the shit right here
I'm hatin' my reflection, I walk around the house tryin' to fight mirrors
I can't stand what I look like, yeah, I look fat, but what do I care?
I give a fuck, only thing I fear is Hailie
I'm afraid if I close my eyes I might see her, shit
I'm going through changes
I'm going through changes
I lock myself in the bedroom, bathroom, nappin' at noon
Yeah, dad's in a bad mood, he's always snappin' at you
Marshall, what happened at you? Can't stop with these pills
And you've fallen off with your skills
And your own fans are laughin' at you
It become a problem you're too pussy to tackle, get up
Be a man, stand, a real man woulda had this shit handled
Know you just had your heart ripped out and crushed
They say Proof just flipped out, homie just swift out and bust
Nah, it ain't like Doody to do that
He wouldn't fuckin' shoot at, nobody, he fights first
But dwellin' on it only makes the night worse
Now I'm poppin Vic's, perks and Methadone pills
Yeah 'em, tight verse, you killed it
Fuckin' drug dealers hang around me like yes man
And they gon' do whatever I says when, I says it
It's in their best interest to protect their investment
And I just lost my fuckin' best friend, so fuck it, I guess then
I'm going through changes
(Don't know what I'm going through)
(But I just keep on going through changes)
My friends just can't understand this new me
That's understandable man but just think how bananas
You'd be, you'd be an animal too, if you were trapped
In this fame and caged in it like a zoo
And everybody's lookin' at you, what you want me to do?
I'm startin' to live like a recluse and the truth is
Fame startin' to give me an excuse, to be at a all time low
I sit alone in my home theater, watchin' the same damn DVD
Of the first tour, the last tour, he was still alive
And it hurt sore, fast forward, sleepin' pills'll make me feel alright
And if I'm still awake in the middle of the night
I just take a couple more, yeah, you're motherfuckin' right
I ain't slowin' down for no one, I am almost homeward bound
Almost in a coma, yeah, homie, come on, don't look now
Daddy, don't you die on me, daddy, better hold your ground
Fuck, don't I know the sound of that voice
Yeah, baby, hold me down
I'm going through changes
(Don't know what I'm going through)
Wake up in the hospital
Full of tubes, plus somehow I'm pullin' through
Swear when I come back I'ma be bulletproof
I'ma do it just for Proof, I think I should state a few
Facts 'cause I may not get a chance again to say the truth
Shit it just hit me that what if I would notta made it through?
I think about the things I would never got to say to you
I'd never get to make it right, so here's what I came to do
Hailie this one is for you, Whitney and Alaina too
I still love your mother, that'll never change
Think about her every day, we just could never get it together
Hey, wish there was a better way, for me to say it
But I swear on everything, I'd do anything for her on any day
There are just too many things to explain, when it rains
Guess it pours, yes it does, wish there wasn't any pain
But I can't pretend there ain't, I ain't placin' any blame
I ain't pointin' fingers, heaven knows there never been a saint
I know it just feels like we just pissed away our history
And just today, I looked at your picture, almost hate to say
I miss you self consciously, wish it didn't end this way
But I just had to get away, don't know why
I don't know what else to say, I guess I'm
I'm going through changes
(Don't know what I'm going through)
(But I just keep on going through changes)
"""

# print(len(text.split()))

word_count = {}

for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

max_value = max(word_count.values())  # maximum value
max_keys = [k for k, v in word_count.items() if v == max_value] # getting all keys containing the `maximum`

print(max_value, max_keys)