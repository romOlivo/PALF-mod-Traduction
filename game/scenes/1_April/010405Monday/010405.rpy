label day010405:
call calendar(3) from _call_calendar
$ calDate = calDate.replace(day=5, month=4, year=2004)

$ timeOfDay = "Morning"

queue music "Audio/Music/Road to Viridian City.ogg"

scene dorm_A with Dissolve(2.0)
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.0, hard=True)

hide blank2

$ renpy.music.set_volume(1.0, delay=0.0, channel="ctc")

redmind uniform closedbrow frownmouth "[day_010405_scene_text[0]]"
redmind happy "[day_010405_scene_text[1]]"

show calem uniform:
    xpos 0.25
show ethan uniform:
    xpos 0.5 
show brendan uniform:
    xpos 0.75
with dis
    
$ renpy.pause(0.5, hard=True)
    
calem @talkingmouth "[day_010405_scene_text[2]]"
brendan @happy "[day_010405_scene_text[3]]"
ethan @closedbrow talking2mouth "[day_010405_scene_text[4]]"
red @happy "[day_010405_scene_text[5]]"
calem @talking2mouth "[day_010405_scene_text[6]]"

show calem surprisedbrow with dis

$ renpy.music.play("Audio/Pokemon/pikachu_pikapika1.ogg", channel="altcry", loop=None)

pikachu neutral_2b "Pikapika!"

red @talkingmouth "[day_010405_scene_text[7]][pika_name][day_010405_scene_text[8]]"

calem -surprisedbrow @sadbrow talkingmouth "[day_010405_scene_text[9]]"

brendan @talking2mouth "[day_010405_scene_text[10]]"

ethan @sadbrow talkingmouth "[day_010405_scene_text[11]]"

show calem surprisedbrow
show brendan surprisedbrow frownmouth
with dis

$ renpy.music.play("Audio/Pokemon/pikachu_excite1.ogg", channel="altcry", loop=None)

pikachu angry_3 "Pi-{i}ka!{/i}"

show brendan -surprisedbrow -frownmouth with dis

calem -surprisedbrow @closedbrow talkingmouth "[day_010405_scene_text[12]]"

ethan @happy "[day_010405_scene_text[13]]"
ethan @sad "[day_010405_scene_text[14]]"

brendan @happy "[day_010405_scene_text[15]]"

calem @talkingmouth "[day_010405_scene_text[16]]"

red @confused "[day_010405_scene_text[17]]"

brendan @surprised "[day_010405_scene_text[18]]"

calem @happy "[day_010405_scene_text[19]]"

red @sadeyes sadeyebrows talkingmouth "[day_010405_scene_text[20]][pika_name][day_010405_scene_text[21]]"
red @confused "[day_010405_scene_text[22]]"

$ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)

pikachu angry_2 "Pi-ka!"
    
red @happy "[day_010405_scene_text[23]]"
red @angrybrow talking2mouth "[day_010405_scene_text[24]]"

$ renpy.music.play("Audio/Pokemon/pikachu_happy2.ogg", channel="altcry", loop=None)

pikachu happy_3 "Piiiikaaaa.~"

pause 2.0

show calem:
    xpos 0.25
    ease 1.0 xpos 0.4

show ethan:
    xpos 0.5
    ease 1.0 xpos 0.6

show brendan:
    xpos 0.75
    ease 1.0 xpos 0.8

show hilbert uniform:
    xpos -0.5 xzoom -1
    ease 1.0 xpos 0.2

pause 2.0

red @confused "[day_010405_scene_text[25]]"

hilbert @closedbrow talkingmouth "[day_010405_scene_text[26]]"

ethan @playfulbrow talking2mouth "[day_010405_scene_text[27]]"

hilbert @sadbrow talkingmouth "[day_010405_scene_text[28]]"

calem @closedbrow talkingmouth "[day_010405_scene_text[29]]"

hilbert @talkingmouth "[day_010405_scene_text[30]]"

brendan @happy "[day_010405_scene_text[31]]"

hilbert @angrybrow talkingmouth "[day_010405_scene_text[32]]"

pause 1.0

ethan @happy "[day_010405_scene_text[33]]"

show hilbert:
    xpos 0.2
    ease 1.0 xpos 1.5

pause 1.0

$ PlaySound("Door_Close1.ogg")

red @closedeyes sadeyebrows talkingmouth "[day_010405_scene_text[34]]"

ethan surprisedbrow frownmouth @surprised "[day_010405_scene_text[35]]"

pause 0.75

window hide

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_2

show blank2 with dis:
    alpha 1.0
    
$ renpy.pause(2.0, hard=True)

hide ethan
hide brendan
hide hilbert
hide calem

show relichall_A behind brendan with dis
    
pause 1.0

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with dis

show may uniform with dis
    
$ renpy.pause(1.0, hard=True)

red @talkingmouth "[day_010405_scene_text[36]]"

show may:
    xpos 0.5
    ease 0.5 xpos 0.33

show brendan uniform with dis:
    xpos 0.66
    
hide blank2

may @happy "[day_010405_scene_text[37]]"

red @happy "[day_010405_scene_text[38]]"

may @sadbrow talkingmouth "[day_010405_scene_text[39]]"

red @talkingmouth "[day_010405_scene_text[40]]"

may @happy "[day_010405_scene_text[41]][first_name][day_010405_scene_text[42]]"

brendan @surprised "[day_010405_scene_text[43]][first_name][day_010405_scene_text[44]]"

show brendan happy with dis

$ BecomeContacted("Brendan")

brendan -happy @talking2mouth "[day_010405_scene_text[45]][first_name][day_010405_scene_text[46]]"

may @surprised "[day_010405_scene_text[47]]"

red @talkingmouth "[day_010405_scene_text[48]]"

show may happy 
with dis

$ BecomeContacted("May")

show may -happy with dis

ethan uniform @happy "[day_010405_scene_text[49]]"

scene cafe with Dissolve(1.5)
$ renpy.pause(1.5, hard=True)

hide blank2

red uniform @surprisedbrow talking2mouth "[day_010405_scene_text[50]]"

show calem uniform with dis:
    xpos 0.166

calem @talkingmouth "[day_010405_scene_text[51]]"

red @wince talking2mouth"[day_010405_scene_text[52]]"

show ethan uniform with dis:
    xpos 0.333

ethan @talkingmouth "[day_010405_scene_text[53]]"

calem @surprised "[day_010405_scene_text[54]]"

show calem:
    xpos 0.166
    ease 5.0 xpos 0.07

show brendan uniform with dis:
    xpos 0.499

brendan @happy "[day_010405_scene_text[55]]"

show may uniform with dis:
    xpos 0.666

may @sadbrow talkingmouth "[day_010405_scene_text[56]]"

brendan @happybrow angrymouth "[day_010405_scene_text[57]]"

show hilbert uniform with dis:
    xpos 0.833

hilbert @sadbrow angrymouth "[day_010405_scene_text[58]]"

redmind @thonk "[day_010405_scene_text[59]]"

show hilbert with dis

show calem:
    xpos 0.07 xzoom 1.0
    ease 0.5 xzoom -1.0

pause 1.5
    
calem @talkingmouth "[day_010405_scene_text[60]]"

show calem:
    xpos 0.07 xzoom -1
    ease 0.5 xpos (2.0/7.0)

show ethan:
    xpos 0.333
    ease 0.5 xpos (3.0/7.0)

show brendan:
    xpos 0.499
    ease 0.5 xpos (4.0/7.0)

show may:
    xpos 0.666
    ease 0.5 xpos (5.0/7.0)

show hilbert:
    xpos 0.833
    ease 0.5 xpos (6.0/7.0)

show serena uniform:
    xpos -0.5
    ease 1.0 xpos (1.0/7.0)

pause 1.5

ethan @happy "[day_010405_scene_text[61]]"
calem @sadbrow talkingmouth "[day_010405_scene_text[62]]"

redmind @thonk "[day_010405_scene_text[63]]"
redmind @thonk "[day_010405_scene_text[64]]"

red @talkingmouth "[day_010405_scene_text[65]]"

serena @talkingmouth "[day_010405_scene_text[66]][first_name][day_010405_scene_text[67]]"

calem @surprised "[day_010405_scene_text[68]]"
calem @closedbrow happymouth "[day_010405_scene_text[69]]"

serena @sadbrow talkingmouth "[day_010405_scene_text[70]]"

calem @angrybrow talking2mouth "[day_010405_scene_text[71]]"

pause 2.0

redmind @confusedeyebrows frownmouth "[day_010405_scene_text[72]]"

hilbert @talkingmouth "[day_010405_scene_text[73]]"

serena @surprised "[day_010405_scene_text[74]]"

ethan @surprised "[day_010405_scene_text[75]]"

brendan @surprisedbrow talking2mouth "[day_010405_scene_text[76]]"

ethan @sweat closedbrow talkingmouth "[day_010405_scene_text[77]]"

hilbert @angry "[day_010405_scene_text[78]]"

ethan @happy "[day_010405_scene_text[79]]"

hilbert @sadbrow "[day_010405_scene_text[80]]"

hilbert @closedbrow talkingmouth "[day_010405_scene_text[81]]"

show hilbert:
    xpos (6.0/7.0)
    ease 1.0 xpos 1.5

ethan happy "[day_010405_scene_text[82]]"

show ethan:
    xpos (3.0/7.0)
    ease 1.0 xpos 1.5

show may happy with dis

brendan happy "[day_010405_scene_text[83]]"

show brendan:
    xpos (4.0/7.0)
    ease 1.0 xpos -0.5

show may:
    xpos (5.0/7.0)
    ease 1.0 xpos -0.5

pause 2.0

serena @talkingmouth "[day_010405_scene_text[84]]"

show calem: 
    xpos (2.0/7.0)
    ease 0.2 xpos 0.75

show serena sadbrow with dis:
    xpos (1.0/7.0)
    ease 1.0 xpos 0.25

calem @talking2mouth "[day_010405_scene_text[85]]"

redmind @thinking "[day_010405_scene_text[86]]"

redmind @surprisedbrow frownmouth "[day_010405_scene_text[87]]"

serena sadbrow @talkingmouth "[day_010405_scene_text[88]]"

show calem thinking with dis

serena sadbrow frownmouth "[ellipses]"


serena -sadbrow -frownmouth @sadbrow talkingmouth "[day_010405_scene_text[89]]"

calem -thinking @surprised "[day_010405_scene_text[90]]"

stop music fadeout 1.5
queue music "Audio/Music/Waltz of the Sea_start.ogg" noloop
queue music "Audio/Music/Waltz of the Sea_loop.ogg"

serena @talkingmouth "[day_010405_scene_text[91]]"

calem @closedbrow talking2mouth "[day_010405_scene_text[92]]"

serena @closedbrow talkingmouth "[day_010405_scene_text[93]]" 
serena @happy "[day_010405_scene_text[94]]"
serena @talkingmouth "[day_010405_scene_text[95]]"

calem smilemouth @happy "[day_010405_scene_text[96]]"

serena @closedbrow talkingmouth "[day_010405_scene_text[97]]"

calem @closedbrow talking2mouth "[day_010405_scene_text[98]]"

serena @sadbrow talkingmouth "[day_010405_scene_text[99]]"

calem @sadbrow talkingmouth "[day_010405_scene_text[100]]"

serena @happy "[day_010405_scene_text[101]]"

calem @closedbrow talking2mouth "[day_010405_scene_text[102]]"

serena @thinking "[ellipses]"


calem @thinking "[ellipses]"


serena @pout "[ellipses]"


serena @sadbrow talkingmouth "[day_010405_scene_text[103]]"

calem @sad "[day_010405_scene_text[104]]"

serena @pout "[ellipses]"

serena @happy "[day_010405_scene_text[105]]"

calem @closedbrow talkingmouth "[day_010405_scene_text[106]]"

serena @happy "[day_010405_scene_text[107]][first_name][day_010405_scene_text[108]]"

menu:
    "[day_010405_scene_text[109]]":
        redmind @thinking "[day_010405_scene_text[110]]"
       
    "[day_010405_scene_text[111]]":
        $ council_campaigning = True

        show calem surprisedbrow -smilemouth
        show serena surprisedbrow frownmouth
        with dis

        red @happy "[day_010405_scene_text[112]]"
        
        $ ValueChange("Serena", 1, 0.25, False)
        $ ValueChange("Calem", 1, 0.75)

        pause 1.5
        
        calem -surprisedbrow @sadbrow talkingmouth "[day_010405_scene_text[113]]"
        
        show serena -surprisedbrow -frownmouth with dis

        red @sweat happy "[day_010405_scene_text[114]]"
        
        red @talkingmouth "[day_010405_scene_text[115]]"
        
        serena @sadbrow happymouth "[day_010405_scene_text[116]]"
        
        calem @closedbrow talkingmouth "[day_010405_scene_text[117]]"
        
        red @happy "[day_010405_scene_text[118]]"
        
        calem @closedbrow talking2mouth "[day_010405_scene_text[119]]"
        
        serena @closedbrow talkingmouth "[day_010405_scene_text[120]]"
        
        calem @closedbrow talkingmouth "[day_010405_scene_text[121]]"
        
        red @confused "[day_010405_scene_text[122]]"
        
        calem @sad "[day_010405_scene_text[123]]"
        
        serena @happy "[day_010405_scene_text[124]]"
        
        calem @happy "[day_010405_scene_text[125]][first_name][day_010405_scene_text[126]]"
        calem @closedbrow talking2mouth "[day_010405_scene_text[127]]"
        
        serena @sad "[ellipses]"

        serena @talkingmouth "[day_010405_scene_text[128]]"
        
        redmind @thonk "[day_010405_scene_text[129]]"

        $ BecomeContacted("Serena")
        
        serena @happy "[day_010405_scene_text[130]][first_name][day_010405_scene_text[131]]"

show serena at dissolveaway:
    xpos 0.25

show calem:
    xpos 0.75
    ease 1.0 xpos 0.5

pause 2.0

menu:
    "[day_010405_scene_text[132]]":
        red @angrybrow talking2mouth "[day_010405_scene_text[133]]"
        
        calem angrybrow frownmouth @talking2mouth "[day_010405_scene_text[134]]"
        
        red @talking2mouth "[day_010405_scene_text[135]]"
        red @talking2mouth "[day_010405_scene_text[136]]"

        $ ValueChange("Calem", -1, 0.5)

        calem @angry "[day_010405_scene_text[137]]"

        red @closedbrow talking2mouth "[day_010405_scene_text[138]]"
        
        calem @angrybrow talking2mouth "[day_010405_scene_text[139]]"
        calem -sad @closedbrow talking2mouth "[day_010405_scene_text[140]]"
       
    "[day_010405_scene_text[141]]":
        red @happy "[day_010405_scene_text[142]]"
        
        calem sad "[day_010405_scene_text[143]]"
        calem "[ellipses]"

        calem -sad @closedbrow talking2mouth "[day_010405_scene_text[144]]"

    "[day_010405_scene_text[145]]":
        red @sadeyebrows sadeyes talkingmouth "[day_010405_scene_text[146]]"
        
        calem @sad "[day_010405_scene_text[147]]"
        calem @angrybrow talking2mouth "[day_010405_scene_text[148]]"
        
        red @confused "[day_010405_scene_text[149]]"
        
        calem @happy "[day_010405_scene_text[150]]"
        
        $ ValueChange("Calem", 1, 0.5)
        
        calem @sadbrow talkingmouth "[day_010405_scene_text[151]]"
        calem @talkingmouth "[day_010405_scene_text[152]]"

red @talkingmouth "[day_010405_scene_text[153]]"

if council_campaigning:
    redmind @thinking "[day_010405_scene_text[154]]"

scene cafe with Dissolve(1.5)

show bianca uniform with dis

bianca @thinking "[ellipses]"

redmind uniform "[ellipses]"


show bianca happyeyes with dis:
    ypos 1.0 zoom 1.0
    ease 0.2 ypos 1.05 zoom 1.1

redmind @confusedeyebrows frownmouth "[day_010405_scene_text[155]]"

show bianca happyeyes with dis:
    ypos 1.05 zoom 1.1
    ease 0.2 ypos 1.1 zoom 1.2

calem uniform @talkingmouth "[day_010405_scene_text[156]]"
red @closedeyes talking2mouth "[day_010405_scene_text[157]]"

show bianca excitedeyes:
    ypos 1.1 zoom 1.2
    ease 0.2 ypos 1.15 zoom 1.3

redmind @surprised "[day_010405_scene_text[158]]"

show bianca excitedeyes:
    ypos 1.15 zoom 1.3
    ease 0.2 ypos 1.2 zoom 1.4

red talking2mouth "[day_010405_scene_text[159]]"

$ BecomeNamed("Bianca")

bianca @happy "[day_010405_scene_text[160]]"

red @surprised "[day_010405_scene_text[161]]"

bianca @happymouth "[day_010405_scene_text[162]]"
bianca -excitedeyes @happy "[day_010405_scene_text[163]]"

show calem uniform surprisedbrow at dissolvein:
    xpos 0.25

calem @sadbrow talkingmouth "[day_010405_scene_text[164]]"

show bianca:
    ypos 1.2 zoom 1.4 xpos 0.5
    ease 1.0 ypos 1.0 zoom 1.0 xpos 0.75

bianca @happy "[day_010405_scene_text[165]]"

show calem deadbrow surprisedmouth at monochrome with vpunch:
    ypos 1.0 xpos 0.25
    ease 1.0 ypos 1.1 rotate 5.0    

calem @talkingmouth "[day_010405_scene_text[166]]"

show calem at monochrome:
    ypos 1.1 rotate 5.0 xpos 0.25
    ease 0.5 ypos 2.0 rotate 30.0

show bianca:
    ypos 1.0 zoom 1.0 xpos 0.75
    ease 1.0 ypos 1.2 zoom 1.4 xpos 0.5

bianca @talkingmouth "[day_010405_scene_text[167]][first_name][day_010405_scene_text[168]]"

red @surprised "[day_010405_scene_text[169]]"

bianca @happy "[day_010405_scene_text[170]]"

red @confused "[day_010405_scene_text[171]]"
red @closedbrow sweat talking2mouth "[day_010405_scene_text[172]]"

bianca @talkingmouth "[day_010405_scene_text[173]][ellipses][day_010405_scene_text[174]][first_name][day_010405_scene_text[175]]"

red @happy "[day_010405_scene_text[176]]"

bianca @talkingmouth "[day_010405_scene_text[177]]"

redmind @thinking "[day_010405_scene_text[178]][first_name][day_010405_scene_text[179]]"

bianca @unamusedbrow trianglemouth "[day_010405_scene_text[180]]"

red @confused "[day_010405_scene_text[181]][ellipses][day_010405_scene_text[182]]"

bianca @talkingmouth "[day_010405_scene_text[183]]"

red @happy "[day_010405_scene_text[184]]"

bianca happy "[day_010405_scene_text[185]]"

show bianca:
    xpos 0.5 ypos 1.2 zoom 1.4
    ease 2.0 xpos 1.5 ypos 1.0 zoom 1.0

redmind @thonk "[day_010405_scene_text[186]][ellipses][day_010405_scene_text[187]]"
redmind @thinking "[day_010405_scene_text[188]]"

show blank2 with dis

pause 2.0

red @happy "[day_010405_scene_text[189]]"

ethan uniform @talkingmouth"[day_010405_scene_text[190]]"

red @talkingmouth "[day_010405_scene_text[191]]"

ethan @surprised "[day_010405_scene_text[192]]"

red @talking2mouth "[day_010405_scene_text[193]]"

pause 1.0

brendan uniform angrymouth closedbrow "[day_010405_scene_text[194]]"

may uniform surprised "[day_010405_scene_text[195]]"

ethan @sweat lightblush sadbrow talkingmouth "[day_010405_scene_text[196]]"

may frownmouth sadbrow @talking2mouth "[day_010405_scene_text[197]]"

ethan sadbrow happymouth "[day_010405_scene_text[198]]"

brendan @angrybrow frownmouth "[day_010405_scene_text[199]]"

brendan @talkingmouth sweat closedbrow "[day_010405_scene_text[200]]"

pause 1.0

hide calem

red @sadbrow talkingmouth "[day_010405_scene_text[201]]"
calem uniform sad "[day_010405_scene_text[202]]"

red @confused "[day_010405_scene_text[203]]"

calem surprisedbrow frownmouth @surprised "[day_010405_scene_text[204]]" 
calem sad "[day_010405_scene_text[205]]"

pause 1.0

red @happy "[day_010405_scene_text[206]]"

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_3
scene blank2 with dissolve

$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5
$ renpy.pause(1.5, hard=True)
play music "Audio/Music/Beyond.ogg" loop fadein 3.0

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.5)
$ renpy.pause(3.0, hard=True)

$ renpy.transition(dissolve)
show screen currentdate

scene academyold with Dissolve(2.0)

$ renpy.pause(2.0, hard=True)

hide blank2
hide cafe

show academy:
    xpos 0 ypos 0 zoom 0.625
    ease 3.0 zoom 1.0 xpos -700 ypos -575

$ renpy.pause(3.0, hard=True)

red uniform @surprised "[day_010405_scene_text[207]]"

show academy:
    zoom 1.0 xpos -700 ypos -575
    ease 1.0 zoom 1.1 xpos -730 ypos -300
$ renpy.pause(1.2, hard=True)

red @talkingmouth "[day_010405_scene_text[208]]"
red @angrybrow talkingmouth "[day_010405_scene_text[209]]"
red @happy "[day_010405_scene_text[210]]"

show academy:
    zoom 1.1 xpos -730 ypos -300
    ease 1.0 zoom 1.05 xpos -730 ypos -300
$ renpy.pause(1.0, hard=True)

red @talkingmouth "[day_010405_scene_text[211]]"

show academy:
    zoom 1.05 xpos -730 ypos -300
    ease 1.5 zoom 1.0 xpos -700 ypos -575
$ renpy.pause(2.0, hard=True)

red @happy "[day_010405_scene_text[212]]"

pause 1.0
show academy:
    zoom 1.0 xpos -700 ypos -575
    ease 0.5 zoom 0.9 xpos -800 ypos -450
pause 1.0
show academy:
    zoom 0.9 xpos -800 ypos -450
    ease 0.75 zoom 0.85 xpos -100 ypos -350
pause 2.0
show academy:
    zoom 0.85 xpos -100 ypos -350
    ease 1.0 zoom 1.0 xpos -700 ypos -525
$ renpy.pause(2.0, hard=True)

redmind @thinking "[day_010405_scene_text[213]]"
redmind @happy "[day_010405_scene_text[214]]"

show academy:
    zoom 1.0 xpos -700 ypos -525
    ease 4.0 zoom 1.4 xpos -600 ypos -600
$ renpy.pause(1.0, hard=True)

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_4

scene blank with Dissolve(1.0)
$ PlaySound("ExitBuilding.ogg")

stop music fadeout 2.25
$ renpy.music.stop(channel='crowd', fadeout=1.5)
$ renpy.pause(3.0, hard=True)

$ renpy.music.play("Audio/hall_crowd.ogg", channel='crowd', loop=True, fadein=1.5)
scene academyhall with Dissolve(1.5)

$ renpy.transition(dissolve)
show screen currentdate
$ renpy.pause(1.5, hard=True)

hide blank
hide academy
hide academyold

redmind uniform "[day_010405_scene_text[215]]"

window hide
show academyhall_blur with dis:
    alpha 1.0

show class_assign:
    alpha 0.0 xalign 0.5 ypos -50
    ease 1.0 alpha 1.0

python:
    fontsize = 15
    if (len(last_name) > 12):
        fontsize = 10

show text "{font=fonts/consola_0.ttf}{color=#000000}{size=[fontsize]}{b}[last_name], [first_name[0]].{/b}{/size}{/color}{/font}":
    alpha 0.0 xanchor 188 ypos 634
    ease 1.0 alpha 0.7

$ renpy.pause(2.0, hard=True)

redmind surprisedbrow frownmouth @surprised "[day_010405_scene_text[216]]"
redmind "[day_010405_scene_text[217]]"
redmind "[day_010405_scene_text[218]][blue_name][day_010405_scene_text[219]]"
redmind "[day_010405_scene_text[220]]"
redmind angrybrow frownmouth "[day_010405_scene_text[221]]"
redmind angrybrow "[day_010405_scene_text[222]]"

blue uniform "[day_010405_scene_text[223]]"

show academyhall_blur:
    alpha 1.0
    ease 0.5 alpha 0.0
show class_assign:
    alpha 1.0
    ease 0.5 alpha 0.0
show text "{font=fonts/consola_0.ttf}{color=#000000}{size=[fontsize]}{b}[last_name], [first_name[0]].{/b}{/size}{/color}{/font}":
    alpha 1.0 xanchor 188 ypos 634
    ease 0.5 alpha 0.0

red @frownmouth "[ellipses]"


show blue with dis:
    xpos 1600
    ease 0.75 xpos 700

play music "Audio/Music/RivalTune.ogg" noloop
$ renpy.music.queue("Audio/Music/Road to Viridian City.ogg", channel='music', loop=True, fadein=4.0, tight=None)

$ renpy.pause(0.75, hard=True)

hide class_assign
hide academyhall_blur
hide text
    
blue @angry "[day_010405_scene_text[224]]"
red @upeyes talking2mouth "[day_010405_scene_text[225]]"
blue @angrybrow happymouth "[day_010405_scene_text[226]]"
blue @happy "[day_010405_scene_text[227]]"
redmind -angrybrow @confusedeyebrows frownmouth "[day_010405_scene_text[228]]"
blue @closedbrow talking2mouth "[day_010405_scene_text[229]]"
show blue surprisedbrow frownmouth with dis
red @talking2mouth "[day_010405_scene_text[230]]"
blue @talkingmouth "[day_010405_scene_text[231]]"
blue sad "[day_010405_scene_text[232]]"
$ renpy.pause(1.0, hard=True)
blue angry "[day_010405_scene_text[233]]" 
blue closedbrow -angrymouth @talkingmouth "[day_010405_scene_text[234]]"

$ showredonly = True

leaf uniform "[day_010405_scene_text[235]]"

redmind surprisedbrow frownmouth @surprised "[day_010405_scene_text[236]]"

$ showredonly = False

show blue surprisedbrow frownmouth with dis:
    xpos 700
    ease 0.5 xpos 450

show leaf uniform:
    alpha 0.0 xpos 1800 
    ease 0.75 xpos 970 alpha 1.0
    
$ renpy.pause(0.75, hard=True)

show blue surprisedbrow frownmouth with dis:
    xpos 450

show leaf:
    xpos 970 alpha 1.0

red @talkingmouth "[day_010405_scene_text[237]]"
leaf @happy "[day_010405_scene_text[238]]"
leaf @flirtbrow talkingmouth "[day_010405_scene_text[239]]"

show blue angry with dis

red @pity "[day_010405_scene_text[240]]"

leaf @flirtbrow talkingmouth blush "[day_010405_scene_text[241]]"

show leaf angrybrow frownmouth with dis

blue frownmouth -angry @sad2eyes talkingmouth"[day_010405_scene_text[242]]"

leaf @angrybrow talking2mouth "[day_010405_scene_text[243]]"

show leaf surprisedbrow frownmouth with dis

blue @closedbrow talkingmouth "[day_010405_scene_text[244]]"

pause 1.0

leaf embarrassed @embarrassedbrow talking2mouth "[day_010405_scene_text[245]]"

window hide
pause 1.5

leaf @frownmouth "[ellipses]"


show leaf at getcloser:
    xpos 970
    ease 0.9 xpos 840
    
$ renpy.pause(0.9, hard=True)

redmind @thinking lightblush"[day_010405_scene_text[246]]"

leaf flirtbrow blush @talking2mouth "[day_010405_scene_text[247]]"

red @sad2eyes talkingmouth lightblush "[day_010405_scene_text[248]][first_name][day_010405_scene_text[249]][last_name][day_010405_scene_text[250]]"
red @closedbrow talkingmouth "[day_010405_scene_text[251]]"

show leaf at getfurther:
    xpos 840
    ease 0.9 xpos 970

leaf -flirtbrow @happy "[day_010405_scene_text[252]][first_name][day_010405_scene_text[253]]"

blue @closedbrow angrymouth "[day_010405_scene_text[254]]"

leaf @surprised "[day_010405_scene_text[255]][first_name][day_010405_scene_text[256]]"
leaf @happybrow talkingmouth "[day_010405_scene_text[257]][first_name][day_010405_scene_text[258]][first_name][day_010405_scene_text[259]]"

red @talkingmouth "[day_010405_scene_text[260]]"

leaf @winkbrow talkingmouth "[day_010405_scene_text[261]]"

redmind @thinking "[day_010405_scene_text[262]]"

red @talkingmouth "[day_010405_scene_text[263]]"

$ BecomeNamed("Leaf")

leaf @happy "[day_010405_scene_text[264]]"

blue @surprisedbrow angrymouth "[day_010405_scene_text[265]]"

red @closedbrow sweat talking2mouth "[day_010405_scene_text[266]][blue_name][day_010405_scene_text[267]]"
red @talkingmouth "[day_010405_scene_text[268]]"

show leaf surprisedbrow frownmouth with dis

blue @closedbrow angrymouth "[day_010405_scene_text[269]]"

pause 0.7

blue @angrybrow talkingmouth "[day_010405_scene_text[270]]"
blue angrybrow happymouth "[day_010405_scene_text[271]]"

show blue:
    alpha 1.0 xpos 450
    parallel:
        ease 0.65 xpos 1000
    parallel:
        ease 0.5 alpha 0.0

$ renpy.pause(2, hard=True)
    
leaf @talking2mouth "[day_010405_scene_text[272]]"

hide blue

red @closedbrow sweat talking2mouth "[day_010405_scene_text[273]][blue_name][day_010405_scene_text[274]]"
red @closedeyes talking2mouth "[day_010405_scene_text[275]]"

leaf flirtbrow -frownmouth @talkingmouth "[day_010405_scene_text[276]]"

red @closedbrow sweat talking2mouth "[day_010405_scene_text[277]]"

leaf happy "[day_010405_scene_text[278]][first_name][day_010405_scene_text[279]]"

window hide

show leaf happy:
    alpha 1.0 xpos 970
    parallel:
        ease 0.5 xpos 1120
    parallel:
        ease 0.5 alpha 0.0
        
$ renpy.pause(1.5, hard=True)

redmind @thinking "[day_010405_scene_text[280]][blue_name][day_010405_scene_text[281]]"

hide leaf

redmind @thinking "[day_010405_scene_text[282]]"
redmind @thinking "[ellipses]"

redmind @happy "[day_010405_scene_text[283]]"

window hide

show academyhall:
    subpixel True
    zoom 1.0 xpos 960 ypos 1080
    ease 3.5 zoom 1.5 xpos 850 ypos 1320
$ renpy.pause(1.0, hard=True)

show blank2 with dis:
    alpha 1.0

$ renpy.pause(1.0, hard=True)
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_5
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5
$ renpy.pause(2.0, hard=True)

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

scene homeroom with Dissolve(2.0)

show oakbg:
    xpos 2500

$ renpy.transition(dissolve)
show screen currentdate
$ renpy.pause(1.5, hard=True)

hide blank2
hide academyhall

show leaf uniform with dis:
    xpos 430
    ease 0.5 xpos 550

show may uniform with dis:
    xpos 1120
    pause 0.5
    ease 0.5 xpos 1000

leaf @happy "[day_010405_scene_text[284]]"

show leaf:
    xpos 550

show may:
    xpos 1000

red uniform @talkingmouth "[day_010405_scene_text[285]]"

may @talkingmouth "[day_010405_scene_text[286]]"
may @happy "[day_010405_scene_text[287]][first_name][day_010405_scene_text[288]]"

leaf @flirtbrow talkingmouth "[day_010405_scene_text[289]]"

show may surprisedbrow frownmouth with dis

leaf @happy "[day_010405_scene_text[290]]"

may -surprisedbrow -frownmouth @sadbrow talkingmouth "[day_010405_scene_text[291]][first_name][day_010405_scene_text[292]]"
may @happy "[day_010405_scene_text[293]]"

red @closedeyes talking2mouth "[day_010405_scene_text[294]]"

leaf @blush happybrow talkingmouth "[day_010405_scene_text[295]]" 
leaf @sadbrow cry talking2mouth blush "[day_010405_scene_text[296]]"

show leaf -blush happy
show may happy 
with dis

red @angrybrow talking2mouth "[day_010405_scene_text[297]]"

if leafwindowjump == True:
    red @angrybrow talking2mouth "[day_010405_scene_text[298]]"
else:
    pass

show leaf flirt blush:
    xpos 550 ypos 1080
    ease 0.5 ypos 1120 xpos 530
    pause 1.0
    ease 0.5 ypos 1080 xpos 550

pause 1.0

redmind @thonk "[day_010405_scene_text[299]]"

show leaf -flirt -blush
show may -happy 
with dis

red @talkingmouth "[day_010405_scene_text[300]]"

may @happy "[day_010405_scene_text[301]]"

leaf @talkingmouth "[day_010405_scene_text[302]]"

show leaf surprisedbrow frownmouth
show may surprisedbrow frownmouth 
with dis

oak @talkingmouth "[day_010405_scene_text[303]]"

show oak with dis:
    xpos 150
    ease 1.5 xpos 300

show leaf:
    xpos 550
    ease 0.65 xpos 800

show may:
    xpos 1000
    ease 0.75 xpos 1200

extend @talkingmouth "[day_010405_scene_text[304]]"

show oak:
    xpos 300

show leaf:
    xpos 800

show may:
    xpos 1200

red @happy "[day_010405_scene_text[305]]"

oak @talkingmouth "[day_010405_scene_text[306]]"

red @pity "[day_010405_scene_text[307]]"

oak @angrybrow talkingmouth "[day_010405_scene_text[308]][first_name][day_010405_scene_text[309]]"

redmind @thinking "[day_010405_scene_text[310]]"

oak @closedeyes talkingmouth "[day_010405_scene_text[311]]"

red @surprised "[day_010405_scene_text[312]]"

show leaf -surprisedbrow -frownmouth 
show may -surprisedbrow -frownmouth
with dis

oak @happy "[day_010405_scene_text[313]]"

may @sadbrow talkingmouth "[day_010405_scene_text[314]]"
may @happy "[day_010405_scene_text[315]]"

oak @talkingmouth "[day_010405_scene_text[316]]"

may @happy "[day_010405_scene_text[317]]"

oak @closedbrow talkingmouth "[day_010405_scene_text[318]]"

may @talkingmouth "[day_010405_scene_text[319]]"

leaf @talkingmouth "[day_010405_scene_text[320]]"

oak @happy "[day_010405_scene_text[321]]"

red @happy "[day_010405_scene_text[322]]"

oak angrybrow frownmouth "[day_010405_scene_text[323]]"

redmind @sad "[day_010405_scene_text[324]]"

oak -angrybrow -frownmouth @happyeyes talkingmouth "[day_010405_scene_text[325]]"
oak @happy "[day_010405_scene_text[326]]"

red @surprised "[day_010405_scene_text[327]]"
red @happy "[day_010405_scene_text[328]]"

oak @closedeyes sadeyebrows happymouth "[day_010405_scene_text[329]][first_name][day_010405_scene_text[330]]"

red @closedbrow talkingmouth "[day_010405_scene_text[331]]"

oak @closedbrow talkingmouth "[day_010405_scene_text[332]][bluecolor][day_010405_scene_text[333]]"
oak @talkingmouth "[day_010405_scene_text[334]]"

hide oak with dis

window hide

pause 1.0

show may surprisedbrow frownmouth with dis

show homeroom with vpunch

leaf @angry "[day_010405_scene_text[335]]"

show may -surprisedbrow -frownmouth with dis

red @closedbrow talking2mouth "[day_010405_scene_text[336]]"

leaf @closedbrow talking2mouth "[day_010405_scene_text[337]][ellipses][day_010405_scene_text[338]]" 
leaf @happy "[day_010405_scene_text[339]]"
leaf happy @flirtbrow talkingmouth blush "[day_010405_scene_text[340]][first_name][day_010405_scene_text[341]]"

hide leaf with dis

$ renpy.pause(1.25, hard=True)

show may:
    xpos 1200
    ease 0.65 xpos 880

$ renpy.pause(0.65, hard=True)

may @angrybrow talkingmouth "[day_010405_scene_text[342]][first_name][day_010405_scene_text[343]]"
    
hide leaf

red @pity "[day_010405_scene_text[344]]"
may @happybrow talkingmouth "[day_010405_scene_text[345]]"
may @happy "[day_010405_scene_text[346]]"

hide may

$ renpy.pause(1.0, hard=True)

red @happy "[day_010405_scene_text[347]][blue_name][day_010405_scene_text[348]]"

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_6
show blank2 with splitfade
$ renpy.pause(0.5, hard=True)
$ PlaySound("BellChime.ogg")
show morning at vspaz  
pause 3.5
hide blank2 with splitfade
$ renpy.music.set_volume(1.0, delay=1.00, channel="music")
$ renpy.transition(dissolve)
show screen currentdate
$ renpy.pause(1.0, hard=True)
hide morning

show oak with dis

oak @talkingmouth "[day_010405_scene_text[349]]"
oak @talkingmouth "[day_010405_scene_text[350]]"
oak @talkingmouth "[day_010405_scene_text[351]]"

window hide
pause 1.5

oak @closedbrow sweat talking2mouth "[day_010405_scene_text[352]]"

Character("[day_010405_scene_text[353]]") "[day_010405_scene_text[354]]"
Character("[day_010405_scene_text[355]]") "[day_010405_scene_text[356]]"

redmind "[day_010405_scene_text[357]]"
redmind thinking "[day_010405_scene_text[358]]"
redmind happy "[day_010405_scene_text[359]]"

oak @angrybrow talking2mouth "[day_010405_scene_text[360]]"
oak @closedbrow talking2mouth sweat "[day_010405_scene_text[361]]"

Character("[day_010405_scene_text[362]]") "[day_010405_scene_text[363]]"
Character("[day_010405_scene_text[364]]") "[day_010405_scene_text[365]]"

redmind @closedbrow frownmouth "[day_010405_scene_text[366]]"

oak @talking2mouth "[day_010405_scene_text[367]]"
oak @talkingmouth "[day_010405_scene_text[368]]"
oak @happy "[day_010405_scene_text[369]]"
oak @talking2mouth "[day_010405_scene_text[370]]"
oak @talkingmouth "[day_010405_scene_text[371]]"
oak @angrybrow talking2mouth "[day_010405_scene_text[372]]"

Character("[day_010405_scene_text[373]]") "[day_010405_scene_text[374]]"
Character("[day_010405_scene_text[375]]") "[day_010405_scene_text[376]]"

redmind -frownmouth @sadeyes sadeyebrows "[day_010405_scene_text[377]]"

show may surprisedbrow frownmouth uniform with dis:
    xpos 0.25 ypos 1.3 zoom 1.35

show leaf surprisedbrow frownmouth uniform with dis:
    xpos 0.75 ypos 1.3 zoom 1.35

pause 1.0

redmind @sadbrow frownmouth "[day_010405_scene_text[378]]"

hide leaf
hide may
show blue smilemouth uniform:
    xpos 0.75 xzoom -1
with dis

pause 1.0

redmind @angrybrow frownmouth "[day_010405_scene_text[379]][blue_name][day_010405_scene_text[380]]"

hide leaf
hide may
hide blue 
with dis

show hilbert uniform with dis:
    xpos 1200

pause 1.0
    
redmind @surprisedbrow frownmouth "[day_010405_scene_text[381]]"

hide hilbert with dis

oak @closedbrow sweat talking2mouth "[day_010405_scene_text[382]]"
oak @talkingmouth "[day_010405_scene_text[383]]"

redmind @sad2eyes frownmouth "[day_010405_scene_text[384]]"
redmind @surprisedbrow frownmouth "[day_010405_scene_text[385]]" 

oak @angrybrow talking2mouth "[day_010405_scene_text[386]]"

window hide
pause 1.5

oak @closedbrow talkingmouth "[day_010405_scene_text[387]]"

redmind @thinking "[day_010405_scene_text[388]]"

oak @talkingmouth "[day_010405_scene_text[389]]"
oak confusedbrow frownmouth @happy "[day_010405_scene_text[390]]"

window hide
pause 1.0

redmind @thonk "[day_010405_scene_text[391]]"

oak -confusedbrow @confusedbrow talking2mouth "[day_010405_scene_text[392]]"

show blue closedbrow happymouth uniform:
    xpos 0.75 xzoom -1

blue @happy "[day_010405_scene_text[393]]"
blue angrybrow talkingmouth @talkingmouth "[day_010405_scene_text[394]]"

redmind @thinking "[day_010405_scene_text[395]]"
redmind @thinking "[day_010405_scene_text[396]]"

blue @talkingmouth "[day_010405_scene_text[397]]"

oak @closedbrow talkingmouth "[day_010405_scene_text[398]]"
oak sadbrow @confused "[day_010405_scene_text[399]]"

blue wistfulbrow scaredmouth "[day_010405_scene_text[400]]"

oak @closedbrow talking2mouth "[day_010405_scene_text[401]]"

show blue angry with dis

red @happy "[day_010405_scene_text[402]][blue_name][day_010405_scene_text[403]]"

leaf uniform @happy "[day_010405_scene_text[404]][first_name][day_010405_scene_text[405]]"

oak -sadbrow -frownmouth @closedbrow talking2mouth "[day_010405_scene_text[406]]"

blue @angry "[day_010405_scene_text[407]]"

pause 1.0

may uniform @sad "[day_010405_scene_text[408]][blue_name][day_010405_scene_text[409]]"
red @happy "[day_010405_scene_text[410]]"

show blue angrybrow talkingmouth with dis

redmind @playfulbrow smirkmouth "[day_010405_scene_text[411]]"

hide blue with dis

oak @talkingmouth "[day_010405_scene_text[412]]"
oak @closedbrow talking2mouth "[day_010405_scene_text[413]]"
oak @talkingmouth "[day_010405_scene_text[414]]"

show oak surprisedbrow frownmouth with dis

show homeroom with vpunch

$ showredonly = True

whitney uniform @surprised "[day_010405_scene_text[415]]"

window hide
$ PlaySound("ExitBuilding.ogg")

show whitney surprisedbrow sadmouth uniform:
    xpos 2000 ypos 1.1 alpha 0.0 rotate 10
    ease 0.4 xpos 500 alpha 1.0
    ease 0.5 xpos 300
    pause 0.5
    ease 0.5 xpos 500 ypos 1.2 rotate 0
    
$ renpy.pause(2.0, hard=True)

show whitney happy with dis

$ showredonly = False

redmind @thinking "[day_010405_scene_text[416]]"

whitney @talking2mouth "[day_010405_scene_text[417]]"

show whitney:
    xpos 500 zoom 1.0
    ease 0.4 xpos 340 ypos 1.2 zoom 1.3
    pause 0.3
    ease 0.15 ypos 1.3

narrator "[day_010405_scene_text[418]]"

show whitney -happy with dis:
    xpos 340 ypos 1.3 zoom 1.3

pause 1.5
    
whitney @talking2mouth "[day_010405_scene_text[419]]"

oak -surprisedbrow -frownmouth @closedbrow talking2mouth "[day_010405_scene_text[420]]"
oak @talking2mouth "[day_010405_scene_text[421]]"
oak @angrybrow talking2mouth "[day_010405_scene_text[422]]"
oak @talkingmouth sad2eyes "[day_010405_scene_text[423]]"

whitney @happy sweat "[day_010405_scene_text[424]]"

pause 1.0

whitney @surprised "[day_010405_scene_text[425]]"
whitney @sadeyebrows talking2mouth "[day_010405_scene_text[426]]"

oak @closedbrow talking2mouth "[day_010405_scene_text[427]]"

$ showredonly = True

flannery tired uniform "[day_010405_scene_text[428]]"

show flannery -tired tiredbrow frownmouth uniform behind whitney with dis:
    xpos 0 ypos 1.9 zoom 1.2
    ease 0.75 xpos 0.2 ypos 1.3 zoom 1.1
    ease 1.25 xpos 0.35 ypos 1.1 zoom 1.0
        
$ renpy.pause(2.0, hard=True)

$ showredonly = False

whitney @sweat happy "[day_010405_scene_text[429]]"

flannery @closedbrow frazzled talking2mouth "[day_010405_scene_text[430]]"

oak @talking2mouth "[day_010405_scene_text[431]]"

flannery @talking2mouth "[day_010405_scene_text[432]]"

show flannery tired:
    xpos 0.35 ypos 1.1 zoom 1.0
    ease 1.5 xpos 0.75 ypos 1.1 zoom 1.35 xzoom -1
    pause 0.5
    ease 0.4 ypos 1.2
    
$ renpy.pause(2.5, hard=True)

redmind @thonk "[day_010405_scene_text[433]]"

pause 1.0

hide flannery 
hide whitney
with dis

redmind @thinking "[day_010405_scene_text[434]]"

hide oak 
show dawn uniform 
with dis

pause 1.0

redmind @thonk "[day_010405_scene_text[435]]"
redmind @thinking "[day_010405_scene_text[436]]"

hide dawn
show oakbg
with dis

redmind @happy "[day_010405_scene_text[437]]"

pause 1.0

show flannery tired uniform with dis:
    xpos 1200 xzoom -1 ypos 1.2 zoom 1.25

pause 1.0

narrator "[day_010405_scene_text[438]]"

redmind @thonk "[day_010405_scene_text[439]]"

menu:
    "[day_010405_scene_text[440]]":        
        flannery angrybrow frownmouth eyebags frazzled @angrybrow talking2mouth "[day_010405_scene_text[441]]"

        red @surprisedbrow talking2mouth "[day_010405_scene_text[442]]"
        red @closedbrow talking2mouth "[day_010405_scene_text[443]]"

        show flannery angry frazzled with dis:
            xpos 1200 ypos 1.2
            ease 0.5 xpos 1140
            
        flannery "[day_010405_scene_text[444]]"

    "[day_010405_scene_text[445]]":
        red @talkingmouth "[day_010405_scene_text[446]]"

        flannery angrybrow frownmouth eyebags frazzled @angrybrow talking2mouth "[day_010405_scene_text[447]]"
        
        red @confusedbrow talking2mouth "[day_010405_scene_text[448]]"
        
        flannery angry frazzled "[day_010405_scene_text[449]]"
        
        $ ValueChange("Flannery", -1, 0.66)

        red @wince talking2mouth "[day_010405_scene_text[450]]"
        
        flannery furiousbrow angrymouth frazzled "[day_010405_scene_text[451]]"
        
        show flannery frazzled with dis:
            xpos 1200 ypos 1.2
            ease 0.5 xpos 1140
            
        flannery furious frazzled veins "[day_010405_scene_text[452]]"

    "[day_010405_scene_text[453]]":        
        redmind "[day_010405_scene_text[454]]"
        
        redmind @thonk "[day_010405_scene_text[455]]"
        
        show flannery eyebags angrybrow frazzled frownmouth with dis
        
        redmind @closedeyes confusedeyebrows sweat frownmouth "[day_010405_scene_text[456]]"
        
        flannery @angrymouth "[day_010405_scene_text[457]]"
        
        red @confused "[day_010405_scene_text[458]]"
        
        flannery @furiousbrow angrymouth "[day_010405_scene_text[459]]"
        
        red @surprisedeyes surprisedeyebrows talking2mouth "[day_010405_scene_text[460]]"
        
        flannery frazzled furiousbrow angrymouth "[day_010405_scene_text[461]]"
        
        red @wince "[day_010405_scene_text[462]]"

        show flannery frazzled with dis:
            xpos 1200 ypos 1.2
            ease 0.5 xpos 1140
            
        flannery furious frazzled veins "[day_010405_scene_text[463]]"

hide whitney

show whitney uniform with dis:
    xpos 685 ypos 1.2 zoom 1.25
    ease 0.5

whitney @happy "[day_010405_scene_text[464]]"

show flannery tiredbrow frownmouth -veins with dis

red @closedeyes talking2mouth  "[day_010405_scene_text[465]]"

whitney @talking2mouth "[day_010405_scene_text[466]]"
whitney @sadbrow talking2mouth "[day_010405_scene_text[467]]"

show flannery:
    xpos 1140 ypos 1.2
    ease 0.6 xpos 1200
    
flannery angrybrow @talking2mouth "[day_010405_scene_text[468]]"

hide flannery with dis

pause 1.0

$ BecomeNamed("Flannery")

whitney @talking2mouth "[day_010405_scene_text[469]]"

red uniform @sadbrow talkingmouth "[day_010405_scene_text[470]]"

whitney @angrybrow happymouth "[day_010405_scene_text[471]]"

show flannery uniform tiredbrow tiredmouth with dis:
    xpos 1200 ypos 1.2 xzoom -1 zoom 1.25

$ BecomeNamed("Whitney")

flannery @talking2mouth "[day_010405_scene_text[472]]"

pause 1.5

show flannery surprisedbrow frownmouth with dis

whitney @happy "[day_010405_scene_text[473]]"

flannery @furious veins "[day_010405_scene_text[474]]"
flannery tiredbrow tiredmouth @angrybrow -veins furiousmouth "[day_010405_scene_text[475]]"

red @pity "[day_010405_scene_text[476]]"
red @happy "[day_010405_scene_text[477]][first_name][day_010405_scene_text[478]]"

whitney @happy "[day_010405_scene_text[479]][first_name][day_010405_scene_text[480]]"

if persondex["Flannery"]["Value"] != -1:
    flannery sad2eyes talking2mouth "[day_010405_scene_text[481]]"

    red @wince talking2mouth "[day_010405_scene_text[482]]"

show flannery surprisedbrow frownmouth
show whitney surprisedbrow frownmouth 
with dis


oak @talkingmouth "[day_010405_scene_text[483]]"

hide flannery
hide whitney 
with dis

stop music fadeout 1.5

redmind @closedbrow sweat frownmouth "[day_010405_scene_text[484]]"

$ renpy.music.queue("Audio/Music/ViridianCity_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/ViridianCity_Loop.ogg", channel='music', loop=True, tight=None)

$ renpy.pause(0.75, hard=True)

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")

show blank2 with dis

$ PlaySound("BellChime.ogg")
$ renpy.music.play("Audio/hall_crowd.ogg", channel='crowd', loop=True, fadein=1.75)
$ renpy.music.set_volume(1.0, delay=4.0, channel="music")

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_7

pause 2.0

narrator "[day_010405_scene_text[485]]"
narrator "[day_010405_scene_text[486]]"

window hide
scene blank2
$ renpy.music.stop(channel='crowd', fadeout=1.0)

narrator "[day_010405_scene_text[487]][bluecolor][day_010405_scene_text[488]]"

narrator "[day_010405_scene_text[489]][bluecolor][day_010405_scene_text[490]]"

narrator "[day_010405_scene_text[491]][bluecolor][day_010405_scene_text[492]]"

jump PickElective
