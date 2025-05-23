label gym010405:

$ timeOfDay = "Noon"

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

$ renpy.transition(dissolve)
show screen currentdate

scene gym with Dissolve(2.0)

$ renpy.pause(1.0, hard=True)

ethan uniform @talkingmouth "[day_010405gym_scene_text[0]]"

red uniform @talking2mouth "[day_010405gym_scene_text[1]]"
red @closedbrow talkingmouth "[day_010405gym_scene_text[2]]"

ethan @surprised "[day_010405gym_scene_text[3]]"

red @happy "[day_010405gym_scene_text[4]]"

pause 2.0

red @sad "[day_010405gym_scene_text[5]]"

ethan @talking2mouth "[day_010405gym_scene_text[6]]"

hide blank2

show brendan uniform happy:
    xpos (1/6) xzoom -1
show may uniform happy:
    xpos (2/6)
show leaf uniform flirt behind may:
    xpos (3/6)
show calem uniform happy behind leaf:
    xpos (4/6)
show hilbert uniform sad:
    xpos (5/6)
with Dissolve(0.5)

ethan @happy "[day_010405gym_scene_text[7]]"

pause 1.0

show misty uniform with Dissolve(0.5):
    xpos (4.5/6)

red @talkingmouth "[day_010405gym_scene_text[8]]"

ethan @talkingmouth "[day_010405gym_scene_text[9]]"

red @happy "[day_010405gym_scene_text[10]]"

if (GetElective("Water") > 0 or GetElective("Ice") > 0):
    red @talkingmouth "[day_010405gym_scene_text[11]]"

hide misty
hide calem
hide cheren
hide hilda
hide hilbert
hide brendan
hide leaf
hide may
with dis

show flannery uniform:
    xpos (1/6)
show whitney uniform happy:
    xpos (2/6)
show gardenia uniform cocky:
    xpos (4/6)
show sabrina uniform behind gardenia:
    xpos (5/6)
show skyla uniform:
    xpos 850
    pause 1.0
    parallel:
        ease 0.3 xpos 950
        ease 0.3 xpos 900
        pause 0.3
        ease 0.3 xpos 870
        ease 0.3 xpos 920
with Dissolve(0.5)

$ renpy.pause(1.5, hard=True)

ethan @talkingmouth "[day_010405gym_scene_text[12]]"

hide flannery
hide whitney
hide gardenia
hide sabrina
hide skyla
with dis

show blue uniform with dis

red @talkingmouth "[day_010405gym_scene_text[13]][blue_name][day_010405gym_scene_text[14]]"

ethan @talkingmouth "[day_010405gym_scene_text[15]]"

red @talkingmouth "[day_010405gym_scene_text[16]]"

ethan @confused "[day_010405gym_scene_text[17]]"

red @happy "[day_010405gym_scene_text[18]]"

ethan @happy "[day_010405gym_scene_text[19]]"

pause 1.0

red @angrybrow talking2mouth "[day_010405gym_scene_text[20]]"
ethan @surprised "[day_010405gym_scene_text[21]]"
red @angrybrow talking2mouth "[day_010405gym_scene_text[22]]"
ethan @winkeyes sadeyebrows sweat talking2mouth "[day_010405gym_scene_text[23]]"

hide flannery
hide whitney
hide gardenia
hide sabrina
hide skyla
hide text

hide blue with dis

red @talkingmouth "[day_010405gym_scene_text[24]]"

$ renpy.pause(1.0, hard=True)

hide blue

show bruno with dis:
    xpos 0.33

show alder happy with dis:
    xpos 0.66

alder @happy2 "[day_010405gym_scene_text[25]]"

$ renpy.music.stop(channel='crowd', fadeout=1.5)

red @confused "[day_010405gym_scene_text[26]]"

show bruno think with dis:
    xpos 0.33

ethan @closedbrow talkingmouth "[day_010405gym_scene_text[27]]"

$ BecomeNamed("Alder")
$ BecomeNamed("Bruno")

alder @norm2 "[day_010405gym_scene_text[28]]"
alder @happy2 "[day_010405gym_scene_text[29]]"
alder @norm2 "[day_010405gym_scene_text[30]]"
alder @happy2 "[day_010405gym_scene_text[31]]"
alder norm @norm2 "[day_010405gym_scene_text[32]]"

pause 1.5

alder @norm2 "[day_010405gym_scene_text[33]]"
alder @happy2 "[day_010405gym_scene_text[34]]"

hide alder
hide bruno
with dis

show cheren uniform with dis:
    xpos 0.25

show hilda uniform behind cheren with dis:
    xpos 0.75

show serena uniform behind cheren with dis:
    xpos 0.5

cheren @talking2mouth "[day_010405gym_scene_text[35]]"

serena @talkingmouth "[day_010405gym_scene_text[36]]"

hilda @closedbrow talking2mouth "[day_010405gym_scene_text[37]]"

hide hilda
hide cheren
hide serena
show alder happy:
    xpos 0.66
show bruno:
    xpos 0.33
with dis

alder @winkbrow talkingmouth "[day_010405gym_scene_text[38]]"

hide cheren
hide hilda
hide serena

alder @happy2 "[day_010405gym_scene_text[39]]"
alder @talkingmouth "[day_010405gym_scene_text[40]]"
alder @spunky2 "[day_010405gym_scene_text[41]]"

leaf uniform @surprised "[day_010405gym_scene_text[42]]"

show bruno think with dis

alder norm @happy2 "[day_010405gym_scene_text[43]]"

leaf @sadmouth "[day_010405gym_scene_text[44]]"

alder @happy2 "[day_010405gym_scene_text[45]]"
alder @happy2 "[day_010405gym_scene_text[46]]"

show alder happy with dis

show blue uniform angry behind alder with dis:
    xpos 0.95 xzoom -1 zoom 0.9

redmind @thinking "[day_010405gym_scene_text[47]][blue_name][day_010405gym_scene_text[48]]"
redmind @sad "[day_010405gym_scene_text[49]]"

hide blue with dis

alder @surprised2 "[day_010405gym_scene_text[50]]"
alder @happy2 "[day_010405gym_scene_text[51]]"

bruno @think2 "[day_010405gym_scene_text[52]]"
bruno @norm2 "[day_010405gym_scene_text[53]]"
bruno @think2 "[day_010405gym_scene_text[54]]"
bruno @talkingmouth "[day_010405gym_scene_text[55]]"
bruno @sadbrow talkingmouth "[day_010405gym_scene_text[56]]"
bruno @talkingmouth "[day_010405gym_scene_text[57]]"
bruno @think2 "[day_010405gym_scene_text[58]]"

blue uniform @talkingmouth "[day_010405gym_scene_text[59]]"

bruno @closedbrow talkingmouth "[day_010405gym_scene_text[60]]"
bruno @closedbrow happymouth "[day_010405gym_scene_text[61]]"
bruno @angrybrow talkingmouth "[day_010405gym_scene_text[62]]"

blue @angrybrow talking2mouth "[day_010405gym_scene_text[63]]"

bruno @think2 "[day_010405gym_scene_text[64]]"

blue @happy "[day_010405gym_scene_text[65]]"

bruno @closedbrow talking2mouth "[day_010405gym_scene_text[66]]"
bruno -think @closedbrow smilemouth "[day_010405gym_scene_text[67]]"

blue @happy "[day_010405gym_scene_text[68]]"

alder -happy @sadbrow talkingmouth "[day_010405gym_scene_text[69]]"

blue @happy "[day_010405gym_scene_text[70]]"

$ showredonly = True

lance @talking2mouth "[day_010405gym_scene_text[71]]"

show bruno:
    xpos 0.33
    ease 0.5 xpos 0.25

show alder:
    xpos 0.66
    ease 0.5 xpos 0.75

show lance with dis:
    xpos 0.9 zoom 1.15
    ease 0.75 xpos 0.5 zoom 1.0

pause 1.5

$ showredonly = False

calem uniform @surprised "[day_010405gym_scene_text[72]]"

red @confused "[day_010405gym_scene_text[73]]"

$ BecomeNamed("Lance")

ethan @surprised "[day_010405gym_scene_text[74]]"

red @happy "[day_010405gym_scene_text[75]][blue_name][day_010405gym_scene_text[76]]"

lance @talking2mouth "[day_010405gym_scene_text[77]]"

bruno @norm2 "[day_010405gym_scene_text[78]]"

lance @talking2mouth "[day_010405gym_scene_text[79]]"

alder @happy2 "[day_010405gym_scene_text[80]]"

alder @happy2 "[day_010405gym_scene_text[81]]"

lance @talking2mouth "[day_010405gym_scene_text[82]]"
lance @closedbrow talking2mouth "[day_010405gym_scene_text[83]]"
lance angrybrow @talking2mouth "[day_010405gym_scene_text[84]]"

blue cocky "[day_010405gym_scene_text[85]]"

lance @angrybrow talking2mouth "[day_010405gym_scene_text[86]]"

lance @closedbrow talking2mouth "[day_010405gym_scene_text[87]]"

blue angry "[day_010405gym_scene_text[88]]"

redmind @upeyes frownmouth angryeyebrows "[day_010405gym_scene_text[89]]"

blue @angry "[day_010405gym_scene_text[90]]"

lance @closedbrow talking2mouth "[day_010405gym_scene_text[91]]"

lance @talking2mouth "[day_010405gym_scene_text[92]]"

alder @happy2 "[day_010405gym_scene_text[93]]"
alder @sadbrow happymouth "[day_010405gym_scene_text[94]]"

lance @talking2mouth "[day_010405gym_scene_text[95]]"

hide lance with dis

pause 0.5

show bruno:
    xpos 0.25
    ease 0.5 xpos 0.33

show alder:
    xpos 0.75
    ease 0.5 xpos 0.66

blue angrybrow frownmouth "[ellipses]"

blue angry "[day_010405gym_scene_text[96]]"

alder @happy2 "[day_010405gym_scene_text[97]]"
alder @talkingmouth "[day_010405gym_scene_text[98]]"

alder @happy "[day_010405gym_scene_text[99]]"
alder @closedbrow talking2mouth "[day_010405gym_scene_text[100]]"

show bruno think with dis

alder @happy2 "[day_010405gym_scene_text[101]]"

pause 1.5

alder @happy2 "[day_010405gym_scene_text[102]]"

show blank2 with dis

narrator "[day_010405gym_scene_text[103]]"

hide blank2 with dis

window hide
$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
$ PlaySound("BellChime.ogg")

$ renpy.music.stop(channel='misc', fadeout=1.0)

$ renpy.pause(2.0, hard=True)
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

alder norm @happy2 "[day_010405gym_scene_text[104]]"

show bruno think with dis

alder @talkingmouth "[day_010405gym_scene_text[105]]"

show bruno with dis

bruno @think2 "[day_010405gym_scene_text[106]]"

alder @happy2 "[day_010405gym_scene_text[107]]"

call clearscreens from _call_clearscreens_237
hide alder
hide bruno
show blank2
with dis

ethan uniform @talkingmouth "[day_010405gym_scene_text[108]]"

red @talkingmouth "[day_010405gym_scene_text[109]]"

hide bruno
hide alder
hide bianca
hide cheren

window hide
stop music fadeout 1.0
$ renpy.pause(1.0, hard=True)

show cafe behind blank2
show afternoon at vspaz

pause 3.5

jump lunch010405
