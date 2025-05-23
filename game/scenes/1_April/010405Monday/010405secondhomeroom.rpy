label secondhomeroom010405:

$ timeOfDay = "Evening"

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

scene homeroom with Dissolve(2.0)

show oakbg with dis

$ renpy.transition(dissolve)
show screen currentdate
$ renpy.pause(1.5, hard=True)

narrator "[day_010405secondhomeroom_scene_text[0]]"
redmind uniform "[day_010405secondhomeroom_scene_text[1]]"
narrator "[day_010405secondhomeroom_scene_text[2]]"
redmind @thonk "[day_010405secondhomeroom_scene_text[3]]"
redmind @thinking "[day_010405secondhomeroom_scene_text[4]]"

hide blank2

oak @talkingmouth "[day_010405secondhomeroom_scene_text[5]]"
oak @talkingmouth "[day_010405secondhomeroom_scene_text[6]]"
oak @talkingmouth "[day_010405secondhomeroom_scene_text[7]]"

show pokeballs_full:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 1.0 alpha 1.0

$ renpy.pause(2.0, hard=True)

redmind @surprisedbrow frownmouth "[day_010405secondhomeroom_scene_text[8]]"

oak @talkingmouth "[day_010405secondhomeroom_scene_text[9]]"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

oak @talkingmouth "[day_010405secondhomeroom_scene_text[10]]"

show pokeballs_full:
    alpha 1.0
    ease 0.5 alpha 0.0

show blue uniform with dis

blue @talkingmouth "[day_010405secondhomeroom_scene_text[11]]"

oak @talkingmouth "[day_010405secondhomeroom_scene_text[12]]"
oak @talkingmouth "[day_010405secondhomeroom_scene_text[13]]"

blue @angry "[day_010405secondhomeroom_scene_text[14]]"
show blue surprisedbrow frownmouth with dis

oak @talkingmouth "[day_010405secondhomeroom_scene_text[15]][blue_name][day_010405secondhomeroom_scene_text[16]]"

hide blue with dis

redmind "[day_010405secondhomeroom_scene_text[17]]"

oak @talkingmouth "[day_010405secondhomeroom_scene_text[18]]"

red @talkingmouth "[day_010405secondhomeroom_scene_text[19]][pika_name][day_010405secondhomeroom_scene_text[20]]"

$ renpy.music.play("Audio/pokemon/cries/37.mp3", channel="altcry", loop=None)

Character("[day_010405secondhomeroom_scene_text[21]]") "[day_010405secondhomeroom_scene_text[22]]"

redmind "[day_010405secondhomeroom_scene_text[23]]"

oak @talkingmouth "[day_010405secondhomeroom_scene_text[24]][first_name][day_010405secondhomeroom_scene_text[25]]"

$ renpy.music.set_volume(0.0, delay=1.0, channel="music")

redmind "[day_010405secondhomeroom_scene_text[26]]"
redmind @sweat closedbrow frownmouth "[day_010405secondhomeroom_scene_text[27]]"

show pokeballs_emptyA:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 1.0 alpha 1.0

redmind @sadbrow sweat "[day_010405secondhomeroom_scene_text[28]]"
redmind @closedbrow frownmouth "[day_010405secondhomeroom_scene_text[29]]"
redmind @thinking "[day_010405secondhomeroom_scene_text[30]][ellipses][day_010405secondhomeroom_scene_text[31]]"
redmind "[day_010405secondhomeroom_scene_text[32]]"

pause 1.0

redmind "[day_010405secondhomeroom_scene_text[33]]"

menu:
    "[day_010405secondhomeroom_scene_text[34]]":
        $ starter_id = renpy.call("PickPokemon", "all")

    "[day_010405secondhomeroom_scene_text[35]]":
        $ starter_id = renpy.call("PickPokemon", "electives")

    "[day_010405secondhomeroom_scene_text[36]]":
        call PickType() from _call_PickType
        $ starter_id = renpy.call("PickPokemon", _return)

    "[day_010405secondhomeroom_scene_text[37]]":
        $ starter_id = renpy.call("PickPokemon", "every")

$ starter_id = _return
$ starter_name = pokedexlookup(starter_id, DexMacros.Name)

show blank with dis:
    alpha 1.0

pause 0.5

$ PlaySound("Pokemon/Ball sound.ogg")

oak @talkingmouth "[day_010405secondhomeroom_scene_text[38]]"

hide pokeballs_emptyA

pause 1.5

$ startercry = "Audio/pokemon/cries/{}.mp3".format(starter_id)
$ renpy.music.play(startercry, channel="altcry", loop=None)

show pokeballs_emptyB behind blank:
    xalign 0.5 yalign 1.0

show blank:
    alpha 1.0
    ease 1.0 alpha 0.0

pause 1.0

$ renpy.music.play("Audio/Get.ogg", channel="XYgame", loop=None, fadeout=0.5)

show starterportraitfull at pokeball:
    align (0.5, 0.5)
    zoom max(1, (ReadHeight(starter_id) / 40.0))

$ starterobj = Pokemon(starter_id, shinylock=False)
$ playerparty.append(starterobj)
$ starter_species_name = playerparty[0].GetNickname()
$ starter_preposition = ("a" if starter_species_name[0] not in ["A", "E", "I", "O", "U"] else "an")
oak @happy "[day_010405secondhomeroom_scene_text[39]][starter_preposition][day_010405secondhomeroom_scene_text[40]][starter_name][day_010405secondhomeroom_scene_text[41]]"
oak @talkingmouth "[day_010405secondhomeroom_scene_text[42]]"

if (ReadHeight(starter_id) > 48):
    oak @angry "[day_010405secondhomeroom_scene_text[43]]"
    red @surprised "[day_010405secondhomeroom_scene_text[44]]"

$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

red @surprised "[day_010405secondhomeroom_scene_text[45]]"
red @happy sweat"[day_010405secondhomeroom_scene_text[46]]"

oak @talkingmouth "[day_010405secondhomeroom_scene_text[47]]"

red @happy "[day_010405secondhomeroom_scene_text[48]]"
$ starter_preposition = ("a" if starter_species_name[0] not in ["A", "E", "I", "O", "U"] else "an").title()
redmind @closedeyes frownmouth "[day_010405secondhomeroom_scene_text[49]][starter_preposition][day_010405secondhomeroom_scene_text[50]][starter_name][day_010405secondhomeroom_scene_text[51]]"
redmind @closedeyes frownmouth "[day_010405secondhomeroom_scene_text[52]]"
redmind happy "[day_010405secondhomeroom_scene_text[53]]"

hide pokeballs_emptyB
hide starterportraitfull
hide blank2 
with dis

$ PlaySound("BellChime.ogg")

show leaf uniform at leftside with dis:
    xzoom -1

leaf @happy "[day_010405secondhomeroom_scene_text[54]][first_name][day_010405secondhomeroom_scene_text[55]]"

red @happy "[day_010405secondhomeroom_scene_text[56]]"

leaf @talkingmouth "[day_010405secondhomeroom_scene_text[57]]"

$ DisplayPokemon("Bulbasaur")

leaf @happy "[day_010405secondhomeroom_scene_text[58]][starter_name][day_010405secondhomeroom_scene_text[59]]"
leaf @flirttalk "[day_010405secondhomeroom_scene_text[60]]"

$ PlaySound("pokemon/ball sound.ogg")
show sideportraitfull at backinpokeball

red @confused "[day_010405secondhomeroom_scene_text[61]]"
show leaf surprisedbrow frownmouth with dis

hide blue
show blue uniform at rightside with dis:
    xzoom -1

$ starter_preposition = ("a" if starter_species_name[0] not in ["A", "E", "I", "O", "U"] else "an")
blue @happy "[day_010405secondhomeroom_scene_text[62]][starter_preposition][day_010405secondhomeroom_scene_text[63]][starter_name][day_010405secondhomeroom_scene_text[64]][first_name][day_010405secondhomeroom_scene_text[65]]"

show leaf flirtbrow with dis

red @sweat talking2mouth "[day_010405secondhomeroom_scene_text[66]]" 
extend @confused "[day_010405secondhomeroom_scene_text[67]][starter_preposition][day_010405secondhomeroom_scene_text[68]][starter_name][day_010405secondhomeroom_scene_text[69]]"

blue @happy "[day_010405secondhomeroom_scene_text[70]]"
show leaf angrybrow frownmouth with dis
blue @angrybrow happymouth "[day_010405secondhomeroom_scene_text[71]]"

red @surprised "[day_010405secondhomeroom_scene_text[72]]"

blue @happy "[day_010405secondhomeroom_scene_text[73]]"
blue @closedbrow talkingmouth "[day_010405secondhomeroom_scene_text[74]]"
blue @happy "[day_010405secondhomeroom_scene_text[75]]"

red @closedbrow talking2mouth "[day_010405secondhomeroom_scene_text[76]]"

blue @angry "[day_010405secondhomeroom_scene_text[77]]"
show blue surprisedbrow frownmouth with dis

oak @talkingmouth "[day_010405secondhomeroom_scene_text[78]]"

blue @sad2eyes talkingmouth "[day_010405secondhomeroom_scene_text[79]]"
show blue surprisedbrow frownmouth with dis
show leaf surprisedbrow frownmouth with dis

show may uniform angrybrow frownmouth with dis

may @angry "[day_010405secondhomeroom_scene_text[80]]"

blue @closedbrow sweat talkingmouth "[day_010405secondhomeroom_scene_text[81]]"

may @angry "[day_010405secondhomeroom_scene_text[82]]"

leaf -surprisedbrow -frownmouth @talkingmouth "[day_010405secondhomeroom_scene_text[83]]"

hide blue with dis

$ renpy.pause(1.0, hard=True)

may -angrybrow -frownmouth @happy "[day_010405secondhomeroom_scene_text[84]]"

leaf @happy "[day_010405secondhomeroom_scene_text[85]]"

may @surprised "[day_010405secondhomeroom_scene_text[86]]" 
may @happy "[day_010405secondhomeroom_scene_text[87]]"

$ showredonly = True

whitney uniform @smile "[day_010405secondhomeroom_scene_text[88]]"

show may:
    xpos 0.5
    ease 0.5 xpos 0.8

show leaf:
    xpos 0.25 xzoom -1
    ease 0.5 xpos 0.6 xzoom 1

show whitney uniform:
    xpos -0.5
    ease 0.4 xpos 0.4

show flannery uniform:
    xpos -0.5
    ease 1.0 xpos 0.2

pause 1.0

$ showredonly = False

red @talkingmouth "[day_010405secondhomeroom_scene_text[89]]"

whitney @happy "[day_010405secondhomeroom_scene_text[90]]"
whitney @winkbrow talkingmouth "[day_010405secondhomeroom_scene_text[91]]"

flannery @happybrow talkingmouth "[day_010405secondhomeroom_scene_text[92]]"
flannery @closedbrow talkingmouth "[day_010405secondhomeroom_scene_text[93]]"

whitney @talking2mouth "[day_010405secondhomeroom_scene_text[94]]"
whitney @surprised "[day_010405secondhomeroom_scene_text[95]]"

flannery @happy "[day_010405secondhomeroom_scene_text[96]]"

redmind @thinking "[day_010405secondhomeroom_scene_text[97]]"

show hilbert uniform sad behind leaf with dis:
    xpos 0.5 zoom 0.8

pause 2.0 

redmind @thonk "[day_010405secondhomeroom_scene_text[98]]"

pause 1.0

show hilbert surprisedbrow with dis
red @happy "[day_010405secondhomeroom_scene_text[99]]"

hilbert @surprised "[day_010405secondhomeroom_scene_text[100]]"

show hilbert uniform sad behind whitney:
    xpos 0.5 zoom 0.8
    ease 0.5 zoom 1.0

show may:
    xpos 0.8
    ease 0.5 xpos 0.9

show leaf:
    xpos 0.6
    ease 0.5 xpos 0.7

show whitney uniform:
    xpos 0.4
    ease 0.5 xpos 0.3

show flannery uniform:
    xpos 0.2
    ease 0.5 xpos 0.1

hilbert @sadbrow talkingmouth "[day_010405secondhomeroom_scene_text[101]]"

red @confused "[day_010405secondhomeroom_scene_text[102]]"

whitney @happy "[day_010405secondhomeroom_scene_text[103]]"
whitney @talking2mouth sadbrow "[day_010405secondhomeroom_scene_text[104]]"

whitney @sadbrow talking2mouth "[day_010405secondhomeroom_scene_text[105]]"

hilbert @angrybrow talkingmouth "[day_010405secondhomeroom_scene_text[106]]"

whitney @sad "[day_010405secondhomeroom_scene_text[107]]"

hide hilbert with dis

show may:
    xpos 0.9
    ease 0.5 xpos 0.8

show leaf:
    xpos 0.7
    ease 0.5 xpos 0.6

show whitney uniform:
    xpos 0.3
    ease 0.5 xpos 0.4

show flannery uniform:
    xpos 0.1
    ease 0.5 xpos 0.2


$ renpy.pause(0.6, hard=True)

may @happy "[day_010405secondhomeroom_scene_text[108]]"

flannery @surprised "[day_010405secondhomeroom_scene_text[109]]"

leaf @talking2mouth "[day_010405secondhomeroom_scene_text[110]]"
leaf @talkingmouth "[day_010405secondhomeroom_scene_text[111]]"

leaf @closedbrow talking2mouth "[day_010405secondhomeroom_scene_text[112]]"

whitney @angrybrow talking2mouth "[day_010405secondhomeroom_scene_text[113]]"

may @talkingmouth "[day_010405secondhomeroom_scene_text[114]]"

show leaf surprisedbrow frownmouth with dis
show may surprisedbrow frownmouth with dis
show whitney surprisedbrow frownmouth with dis
show flannery surprisedbrow frownmouth sweat with dis
oak @talkingmouth "[day_010405secondhomeroom_scene_text[115]]"

show leaf:
    alpha 1.0 xpos 0.6
    ease 0.5 alpha 0.0

show flannery:
    alpha 1.0 xpos 0.2
    ease 0.5 alpha 0.0

show whitney:
    alpha 1.0 xpos 0.4
    ease 0.5 alpha 0.0

show may:
    alpha 1.0 xpos 0.8
    ease 0.5 alpha 0.0

$ renpy.music.stop(channel='crowd', fadeout=0.5)
$ renpy.pause(0.5, hard=True)

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_10

window hide

stop music fadeout 2.5

scene blank2 with spinfade
$ renpy.pause(1.0, hard=True)

$ renpy.music.play("Audio/hall_crowd.ogg", channel='crowd', loop=True, fadein=1.75)
$ renpy.pause(2.0, hard=True)

scene academyhall with spinfade
$ renpy.pause(1.5, hard=True)

$ renpy.transition(dissolve)
show screen currentdate

show leaf uniform with dis

show may uniform at leftside with dis

leaf @happy "[day_010405secondhomeroom_scene_text[116]]"
    
may @sadbrow happymouth "[day_010405secondhomeroom_scene_text[117]]"

leaf @surprised "[day_010405secondhomeroom_scene_text[118]]"

leaf @flirttalk "[day_010405secondhomeroom_scene_text[119]]"

may @sadbrow happymouth "[day_010405secondhomeroom_scene_text[120]]"

leaf @talkingmouth "[day_010405secondhomeroom_scene_text[121]]"
extend @flirttalk "[day_010405secondhomeroom_scene_text[122]][first_name][day_010405secondhomeroom_scene_text[123]]"

red uniform @confused "[day_010405secondhomeroom_scene_text[124]]"
red @happy "[day_010405secondhomeroom_scene_text[125]]"

leaf @angrybrow talking2mouth "[day_010405secondhomeroom_scene_text[126]]"

red @closedeyes happymouth "[day_010405secondhomeroom_scene_text[127]]"

show brendan uniform happybrow at rightside with dis

brendan @happymouth "[day_010405secondhomeroom_scene_text[128]]"

may @happy "[day_010405secondhomeroom_scene_text[129]]"

show may:
    xpos 0.25
    ease 0.5 xpos 0.4

may @flirtbrow talkingmouth "[day_010405secondhomeroom_scene_text[130]]"

leaf @flirttalk "[day_010405secondhomeroom_scene_text[131]]"

hide may
hide brendan
with dis

leaf @happy "[day_010405secondhomeroom_scene_text[132]]"

$ renpy.pause(1.5, hard=True)

leaf happybrow @happy "[day_010405secondhomeroom_scene_text[133]]"

red @happy "[day_010405secondhomeroom_scene_text[134]]"

leaf @happy "[day_010405secondhomeroom_scene_text[135]]"
leaf @closedbrow talking2mouth "[day_010405secondhomeroom_scene_text[136]]"
extend -happybrow @talking2mouth "[day_010405secondhomeroom_scene_text[137]]"

show leaf surprisedbrow frownmouth with dis

red @sadbrow talkingmouth "[day_010405secondhomeroom_scene_text[138]]"

leaf @surprised "[day_010405secondhomeroom_scene_text[139]]"
leaf @happybrow talkingmouth"[day_010405secondhomeroom_scene_text[140]]"

pause 1.5

leaf -surprisedbrow -frownmouth @sarcastic "[day_010405secondhomeroom_scene_text[141]]"

red @confused "[day_010405secondhomeroom_scene_text[142]]"
extend @closedbrow talking2mouth sweat "[day_010405secondhomeroom_scene_text[143]]"

leaf @happy "[day_010405secondhomeroom_scene_text[144]]"
leaf @flirttalk "[day_010405secondhomeroom_scene_text[145]]"

$ renpy.music.play("Audio/Music/Show Me Around.ogg", channel='music', loop=True, fadein=1.0)

show academyhall_blur 
show mapdemo 
with dis

$ renpy.pause(1.5, hard=True)

leaf @talking2mouth "[day_010405secondhomeroom_scene_text[146]]"
leaf @flirttalk "[day_010405secondhomeroom_scene_text[147]]"

red @unamusedbrow talking2mouth "[day_010405secondhomeroom_scene_text[148]]"

leaf @happy "[day_010405secondhomeroom_scene_text[149]]"

jump map_tutorial

label map_tutorial:

menu:
    extend "[day_010405secondhomeroom_scene_text[150]]"
    "[day_010405secondhomeroom_scene_text[151]]":
        leaf @talkingmouth "[day_010405secondhomeroom_scene_text[152]]"

        red @talkingmouth "[day_010405secondhomeroom_scene_text[153]]"

        leaf @talking2mouth "[day_010405secondhomeroom_scene_text[154]]"
        leaf @talkingmouth "[day_010405secondhomeroom_scene_text[155]]"

        jump map_tutorial

    "[day_010405secondhomeroom_scene_text[156]]":
        red @talkingmouth "[day_010405secondhomeroom_scene_text[157]]"

        leaf @talking2mouth "[day_010405secondhomeroom_scene_text[158]]"

        leaf @talkingmouth "[day_010405secondhomeroom_scene_text[159]]"
        leaf @talking2mouth "[day_010405secondhomeroom_scene_text[160]]"

        leaf @flirttalk "[day_010405secondhomeroom_scene_text[161]]"
        leaf @surprised "[day_010405secondhomeroom_scene_text[162]]"
        leaf @talking2mouth "[day_010405secondhomeroom_scene_text[163]]"
        extend @talking2mouth "[day_010405secondhomeroom_scene_text[164]]"
        
        red @talkingmouth "[day_010405secondhomeroom_scene_text[165]]"

        leaf @talkingmouth "[day_010405secondhomeroom_scene_text[166]]"

        jump map_tutorial

    "[day_010405secondhomeroom_scene_text[167]]":
        red @talkingmouth "[day_010405secondhomeroom_scene_text[168]]"

        leaf @happy "[day_010405secondhomeroom_scene_text[169]]"
        leaf @talking2mouth "[day_010405secondhomeroom_scene_text[170]]"

        leaf @flirttalk "[day_010405secondhomeroom_scene_text[171]]"
        
        red @closedbrow talking2mouth "[day_010405secondhomeroom_scene_text[172]]"

        leaf @talking2mouth "[day_010405secondhomeroom_scene_text[173]]"

        jump map_tutorial

    "[day_010405secondhomeroom_scene_text[174]]":
        red @talkingmouth "[day_010405secondhomeroom_scene_text[175]]"

        leaf @happy "[day_010405secondhomeroom_scene_text[176]]"

hide academyhall_blur
hide mapdemo
with dis

$ renpy.pause(1.5, hard=True)

leaf @talking2mouth "[day_010405secondhomeroom_scene_text[177]]"

red @confused "[day_010405secondhomeroom_scene_text[178]]"

leaf @flirttalk "[day_010405secondhomeroom_scene_text[179]]"  
leaf @happy "[day_010405secondhomeroom_scene_text[180]]"

red @talkingmouth "[day_010405secondhomeroom_scene_text[181]]"

leaf @happy "[day_010405secondhomeroom_scene_text[182]]"
leaf @closedbrow talking2mouth "[day_010405secondhomeroom_scene_text[183]]"
leaf @flirttalk blush "[day_010405secondhomeroom_scene_text[184]]"

red @upeyes angryeyebrows talking2mouth "[day_010405secondhomeroom_scene_text[185]]"

leaf @happy "[day_010405secondhomeroom_scene_text[186]]"

pause 2.0

red @closedbrow talking2mouth sweat "[day_010405secondhomeroom_scene_text[187]]"

leaf @happy "[day_010405secondhomeroom_scene_text[188]]"

red @unamusedbrow talking2mouth "[day_010405secondhomeroom_scene_text[189]]"

pause 1.0

leaf @sad "[day_010405secondhomeroom_scene_text[190]]"

red @sigh "[day_010405secondhomeroom_scene_text[191]]"

leaf happy "[day_010405secondhomeroom_scene_text[192]]"

hide leaf with dis

pause 0.5

window hide

show blank2 with dis

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_11
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5
$ renpy.pause(2.0, hard=True)

############################################################################################################################################################################################################################
#### KORRINA INTRO #########################################################################################################################################################################################################
############################################################################################################################################################################################################################
#### NO IT ISN'T ###########################################################################################################################################################################################################
############################################################################################################################################################################################################################

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

$ renpy.transition(dissolve)
show screen currentdate

scene gym with Dissolve(2.0)

hide blank2

$ renpy.pause(1.0, hard=True)

show leaf uniform with dis

leaf @talkingmouth "[day_010405secondhomeroom_scene_text[193]]" 

red uniform @talkingmouth "[day_010405secondhomeroom_scene_text[194]]"

leaf @closedbrow talkingmouth "[day_010405secondhomeroom_scene_text[195]]"
show leaf surprisedbrow frownmouth with dis

pause 1.5

red @confused "[day_010405secondhomeroom_scene_text[196]]"

leaf surprisedbrow frownmouth @surprised "[day_010405secondhomeroom_scene_text[197]]"

$ rosanamed = IsNamed("Rosa")

if (rosanamed):
    if (classstats["Electric"] > 0):
        red @confused "[day_010405secondhomeroom_scene_text[198]]" 
        extend @talkingmouth "[day_010405secondhomeroom_scene_text[199]]"

        leaf @angry "[day_010405secondhomeroom_scene_text[200]]"

    else:
        red @confused "[day_010405secondhomeroom_scene_text[201]]" 
        red @talkingmouth "[day_010405secondhomeroom_scene_text[202]]"

        leaf @angry "[day_010405secondhomeroom_scene_text[203]]"

    red @happy "[day_010405secondhomeroom_scene_text[204]]"

    leaf @angry "[day_010405secondhomeroom_scene_text[205]]"

    red @confused "[day_010405secondhomeroom_scene_text[206]]"

else:
    red @confused "[day_010405secondhomeroom_scene_text[207]]"

leaf @surprised "[day_010405secondhomeroom_scene_text[208]]"

red @talking2mouth "[day_010405secondhomeroom_scene_text[209]]"

leaf -surprisedbrow -frownmouth @happy "[day_010405secondhomeroom_scene_text[210]]"
leaf @happy "[day_010405secondhomeroom_scene_text[211]]"

red @confused "[day_010405secondhomeroom_scene_text[212]]"

leaf @embarrassedbrow talkingmouth "[day_010405secondhomeroom_scene_text[213]]"
leaf @happy "[day_010405secondhomeroom_scene_text[214]]"

red @confused "[day_010405secondhomeroom_scene_text[215]]"

pause 1.0

leaf @talking2mouth angrybrow "[day_010405secondhomeroom_scene_text[216]]"

red @talking2mouth "[day_010405secondhomeroom_scene_text[217]]"

leaf surprisedbrow frownmouth @surprised "[ellipses]"

leaf surprisedbrow @talking2mouth "[day_010405secondhomeroom_scene_text[218]]"

red @confused "[day_010405secondhomeroom_scene_text[219]]"
red @closedbrow talkingmouth "[day_010405secondhomeroom_scene_text[220]]"

leaf "[ellipses]"

leaf -surprisedbrow -frownmouth @closedbrow talking2mouth "[day_010405secondhomeroom_scene_text[221]]"
leaf @happy "[day_010405secondhomeroom_scene_text[222]]"

red @wince talking2mouth "[day_010405secondhomeroom_scene_text[223]]"

leaf @closedbrow talkingmouth "[day_010405secondhomeroom_scene_text[224]]"

pause 2.0

leaf @happy "[day_010405secondhomeroom_scene_text[225]]"

red @happy "[day_010405secondhomeroom_scene_text[226]]"

show rosa with dis:
    xpos 0.66

show leaf:
    xpos 0.5 xzoom 1
    ease 0.5 xpos 0.33 xzoom -1

leaf @happy "[day_010405secondhomeroom_scene_text[227]]"

$ BecomeNamed("Rosa")

show leaf:
    xpos 0.33 xzoom -1

show rosa:
    xpos 0.66

rosa @surprised "[day_010405secondhomeroom_scene_text[228]]"
rosa @talkingmouth "[day_010405secondhomeroom_scene_text[229]]"

leaf @surprised "[day_010405secondhomeroom_scene_text[230]]"

leaf @happy "[day_010405secondhomeroom_scene_text[231]][first_name][day_010405secondhomeroom_scene_text[232]]"

red @happy "[day_010405secondhomeroom_scene_text[233]]"

show rosa happybrow sweat with dis

leaf @embarrassedbrow talkingmouth "[day_010405secondhomeroom_scene_text[234]]"

rosa @talkingmouth "[day_010405secondhomeroom_scene_text[235]]"
rosa @closedbrow sweat talking2mouth "[day_010405secondhomeroom_scene_text[236]]"

leaf @happy "[day_010405secondhomeroom_scene_text[237]]"

if (not rosanamed):
    leaf @happy "[day_010405secondhomeroom_scene_text[238]]"

    rosa @happy "[day_010405secondhomeroom_scene_text[239]]"

    leaf @surprised "[day_010405secondhomeroom_scene_text[240]]"
    
leaf @flirttalk "[day_010405secondhomeroom_scene_text[241]]"

redmind @unamusedbrow unamusedmouth "[day_010405secondhomeroom_scene_text[242]]"

show leaf surprisedbrow frownmouth with dis

red @sadbrow talkingmouth "[day_010405secondhomeroom_scene_text[243]]"
    
leaf @surprised "[day_010405secondhomeroom_scene_text[244]]"

rosa -sweat -happybrow @talkingmouth "[day_010405secondhomeroom_scene_text[245]]"
rosa @happy "[day_010405secondhomeroom_scene_text[246]]"

leaf @sadbrow talkingmouth "[day_010405secondhomeroom_scene_text[247]]" 
leaf -surprisedbrow -frownmouth @happy "[day_010405secondhomeroom_scene_text[248]]"

rosa @happy "[day_010405secondhomeroom_scene_text[249]]"

pause 0.75

if (rosanamed):
    rosa @talkingmouth "[day_010405secondhomeroom_scene_text[250]][first_name][day_010405secondhomeroom_scene_text[251]]"

    red @happy "[day_010405secondhomeroom_scene_text[252]]"

    rosa @sadbrow talkingmouth "[day_010405secondhomeroom_scene_text[253]]"

    red @happy "[day_010405secondhomeroom_scene_text[254]]"
    
rosa @talkingmouth "[day_010405secondhomeroom_scene_text[255]]"

leaf surprisedbrow frownmouth @surprised "[day_010405secondhomeroom_scene_text[256]][first_name][day_010405secondhomeroom_scene_text[257]][first_name][day_010405secondhomeroom_scene_text[258]]"
      
rosa @surprised sweat "[day_010405secondhomeroom_scene_text[259]]"

leaf @happy "[day_010405secondhomeroom_scene_text[260]]"

show leaf surprisedbrow frownmouth with dis

red @closedeyes talkingmouth "[day_010405secondhomeroom_scene_text[261]]" 
extend @noeyes shadow frownmouth "[day_010405secondhomeroom_scene_text[262]]"

show leaf sadbrow -frownmouth with dis

pause 1.5
    
rosa @surprisedbrow talking2mouth sweat "[day_010405secondhomeroom_scene_text[263]]" 
extend @sadbrow talkingmouth "[day_010405secondhomeroom_scene_text[264]]"
rosa @happy "[day_010405secondhomeroom_scene_text[265]]"

show rosa happybrow sweat with dis
    
leaf -sadbrow @happy "[day_010405secondhomeroom_scene_text[266]]"

rosa @talkingmouth "[day_010405secondhomeroom_scene_text[267]]"

hide rosa at rightside with dis

pause 1.0

hide rosa

red @happy "[day_010405secondhomeroom_scene_text[268]]"

leaf -happy @talkingmouth "[day_010405secondhomeroom_scene_text[269]]"
leaf @happy "[day_010405secondhomeroom_scene_text[270]]"

leaf @talkingmouth "[day_010405secondhomeroom_scene_text[271]]"

red @talkingmouth "[day_010405secondhomeroom_scene_text[272]]"

leaf @surprised "[day_010405secondhomeroom_scene_text[273]]"

red @happy "[day_010405secondhomeroom_scene_text[274]]"

leaf thinking @angrybrow talking2mouth "[day_010405secondhomeroom_scene_text[275]]"

pause 2.0

leaf -thinking @sadbrow talkingmouth "[day_010405secondhomeroom_scene_text[276]][ellipses][day_010405secondhomeroom_scene_text[277]]"

red @confused "[day_010405secondhomeroom_scene_text[278]]"

leaf @talking2mouth "[day_010405secondhomeroom_scene_text[279]]"
leaf @talkingmouth "[day_010405secondhomeroom_scene_text[280]]"

hide leaf with dis

window hide

show blank2 with Dissolve(1.5)

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_12
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5
$ renpy.pause(2.5, hard=True)

show night at vspaz

pause 3.5

############################################################################################################################################################################################################################
#### END OF DAY ############################################################################################################################################################################################################
############################################################################################################################################################################################################################

play music "Audio/Music/SoaringIllusions_Intro.ogg" noloop
queue music "Audio/Music/SoaringIllusions.ogg"

$ renpy.transition(dissolve)
show screen currentdate

$ timeOfDay = "Night"

scene relichall_B with Dissolve(2.0)

hide blank2
hide night

show leaf uniform happy at night with dis

narrator "[day_010405secondhomeroom_scene_text[281]]"
narrator "[day_010405secondhomeroom_scene_text[282]]"

leaf frownmouth @surprised "[day_010405secondhomeroom_scene_text[283]]"

red night uniform @sigh "[day_010405secondhomeroom_scene_text[284]]"

leaf -surprisedbrow -frownmouth -surprised @sarcastic "[day_010405secondhomeroom_scene_text[285]]"
leaf @talking2mouth "[day_010405secondhomeroom_scene_text[286]]"
leaf -frownmouth @happy "[day_010405secondhomeroom_scene_text[287]]"

red @talking2mouth "[day_010405secondhomeroom_scene_text[288]]"

leaf @surprised "[day_010405secondhomeroom_scene_text[289]]"
leaf @happy "[day_010405secondhomeroom_scene_text[290]]"

red @sadbrow talkingmouth "[day_010405secondhomeroom_scene_text[291]]"

leaf happy "[day_010405secondhomeroom_scene_text[292]]"

hide leaf at night with dis

pause 2.0

redmind @thinking "[day_010405secondhomeroom_scene_text[293]]"

window hide

show blank2 with dis

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_13

$ renpy.pause(2.0, hard=True)

$ renpy.transition(dissolve)
show screen currentdate

$ PlaySound("Door_Open1.ogg")
scene dorm_B norm with Dissolve(2.0)

hide blank2
hide relichall_B

red uniform @talkingmouth "[day_010405secondhomeroom_scene_text[294]]"

$ PlaySound("Door_Close1.ogg")

red @happy "[day_010405secondhomeroom_scene_text[295]]"
red @happy "[day_010405secondhomeroom_scene_text[296]]"

$ renpy.music.play("Audio/Pokemon/pikachu_norm1.ogg", channel="altcry", loop=None)

pikachu happy_3 "[day_010405secondhomeroom_scene_text[297]]"

red @happy "[day_010405secondhomeroom_scene_text[298]][pika_name][day_010405secondhomeroom_scene_text[299]]"

$ renpy.music.play("Audio/Pokemon/pikachu_norm4.ogg", channel="altcry", loop=None)

pikachu happy_3 "[day_010405secondhomeroom_scene_text[300]]"

show calem at leftside with dis

calem @talkingmouth "[day_010405secondhomeroom_scene_text[301]]"

show brendan at rightside with dis

brendan @happy "[day_010405secondhomeroom_scene_text[302]]"

calem @closedbrow talkingmouth "[day_010405secondhomeroom_scene_text[303]]"
calem smilemouth @talkingmouth "[day_010405secondhomeroom_scene_text[304]]"

red @happy "[day_010405secondhomeroom_scene_text[305]]"

calem @surprised "[day_010405secondhomeroom_scene_text[306]]" 
calem @happy "[day_010405secondhomeroom_scene_text[307]]"

brendan @happy "[day_010405secondhomeroom_scene_text[308]]"

red @talkingmouth "[day_010405secondhomeroom_scene_text[309]]"

show ethan with dis

ethan @happy "[day_010405secondhomeroom_scene_text[310]]"

show ethan surprisedbrow frownmouth with dis
show calem surprisedbrow with dis
show brendan surprisedbrow frownmouth with dis
$ starter_preposition = ("a" if starter_species_name[0] not in ["A", "E", "I", "O", "U"] else "an")
red @happy "[day_010405secondhomeroom_scene_text[311]][starter_preposition][day_010405secondhomeroom_scene_text[312]][starter_name][day_010405secondhomeroom_scene_text[313]]"
if (starter_name == "Mudkip"):
    red @happy "[day_010405secondhomeroom_scene_text[314]]"

pause 2.0

red @confused "[day_010405secondhomeroom_scene_text[315]]"

show calem happy with dis
show brendan happy with dis
$ starter_preposition = ("a" if starter_species_name[0] not in ["A", "E", "I", "O", "U"] else "an")
ethan happy "[day_010405secondhomeroom_scene_text[316]][starter_preposition][day_010405secondhomeroom_scene_text[317]][starter_name][day_010405secondhomeroom_scene_text[318]]"

show brendan -happy with dis
show calem -happy with dis
red @happy "[day_010405secondhomeroom_scene_text[319]]"
if (starter_name == "Mudkip"):
    red @talkingmouth "[day_010405secondhomeroom_scene_text[320]]"

ethan @talkingmouth "[day_010405secondhomeroom_scene_text[321]]"
ethan @happy "[day_010405secondhomeroom_scene_text[322]]"

calem @closedbrow talkingmouth "[day_010405secondhomeroom_scene_text[323]]"

if (GetStatRank(0) in classdex["Calem"] and GetStatRank(1) in classdex["Calem"]):
    calem @happy "[day_010405secondhomeroom_scene_text[324]][first_name][day_010405secondhomeroom_scene_text[325]]"
elif (GetStatRank(0) in classdex["Brendan"] and GetStatRank(1) in classdex["Brendan"]):
    brendan @surprised "[day_010405secondhomeroom_scene_text[326]][first_name][day_010405secondhomeroom_scene_text[327]]"

    calem @happy "[day_010405secondhomeroom_scene_text[328]]"

red @talkingmouth "[day_010405secondhomeroom_scene_text[329]]"

calem @closedbrow talking2mouth "[day_010405secondhomeroom_scene_text[330]]"
calem @happy "[day_010405secondhomeroom_scene_text[331]]"

brendan @sadbrow talking2mouth "[day_010405secondhomeroom_scene_text[332]]"
brendan @closedbrow sweat talking2mouth "[day_010405secondhomeroom_scene_text[333]]"

calem @sad "[day_010405secondhomeroom_scene_text[334]]"

brendan @sad "[day_010405secondhomeroom_scene_text[335]]"

ethan @confused "[day_010405secondhomeroom_scene_text[336]]"
ethan @happy "[day_010405secondhomeroom_scene_text[337]]"

brendan frownmouth sadbrow @sad "[day_010405secondhomeroom_scene_text[338]]"

narrator "[day_010405secondhomeroom_scene_text[339]]"

show brendan -frownmouth -sadbrow with dis

narrator "[day_010405secondhomeroom_scene_text[340]]"

$ starter_name = pokedexlookup(starter_id, DexMacros.Name)
red @happy "[day_010405secondhomeroom_scene_text[341]][starter_name][day_010405secondhomeroom_scene_text[342]]"

$ PlaySound("Pokemon/Ball sound.ogg")

show starterportraitfull at pokeball, dormdesk
show calem:
    xpos 0.25
    ease 0.5 xpos 0.1

show ethan:
    xpos 0.5
    ease 0.5 xpos 0.25

show brendan:
    xpos 0.75
    ease 0.5 xpos 0.8

$ renpy.pause(0.5, hard=True)
$ renpy.music.play("Audio/pokemon/cries/{}.mp3".format(starter_id), channel="altcry", loop=None)

$ startercrop = starter_name[:3]
starter @talkingmouth "[day_010405secondhomeroom_scene_text[343]][startercrop][day_010405secondhomeroom_scene_text[344]]"

redmind "[day_010405secondhomeroom_scene_text[345]]"

label nicknamestarter:

$ starter_name = renpy.input("[day_010405secondhomeroom_scene_text[346]]", length=12, exclude="{}[[]%<>",)
$ starter_name = starter_name.strip()

if starter_name == "" or starter_name == pokedexlookup(starter_id, DexMacros.Name).lower():
    $ starter_name = pokedexlookup(starter_id, DexMacros.Name)

red @closedbrow talking2mouth "[day_010405secondhomeroom_scene_text[347]][starter_name][day_010405secondhomeroom_scene_text[348]]"

menu:
    "[day_010405secondhomeroom_scene_text[349]][starter_name][day_010405secondhomeroom_scene_text[350]]":
        pass

    "[day_010405secondhomeroom_scene_text[351]]":
        jump nicknamestarter

$ playerparty[0].Nickname = starter_name

red @talkingmouth "[day_010405secondhomeroom_scene_text[352]][starter_name][day_010405secondhomeroom_scene_text[353]]"
    
$ renpy.music.play("Audio/pokemon/cries/{}.mp3".format(starter_id), channel="altcry", loop=None)

$ species_name = pokedexlookup(starter_id, DexMacros.Name)
starter @talkingmouth "[day_010405secondhomeroom_scene_text[354]][species_name][day_010405secondhomeroom_scene_text[355]]"

$ startergender = "he" 
if (playerparty[0].GetGender() == Genders.Female):
    $ startergender = "she"
elif (playerparty[0].GetGender() == Genders.Unknown):
    $ startergender = "it"

brendan @happy "[day_010405secondhomeroom_scene_text[356]][startergender][day_010405secondhomeroom_scene_text[357]]"
brendan @talking2mouth "[day_010405secondhomeroom_scene_text[358]]"

red @confused "[day_010405secondhomeroom_scene_text[359]][starter_name][day_010405secondhomeroom_scene_text[360]][pika_name][day_010405secondhomeroom_scene_text[361]]"

brendan @surprised "[day_010405secondhomeroom_scene_text[362]]"

calem @closedbrow talkingmouth "[day_010405secondhomeroom_scene_text[363]][starter_name][day_010405secondhomeroom_scene_text[364]][first_name][day_010405secondhomeroom_scene_text[365]]"

$ startergendercap = startergender.capitalize()
red @confused "[day_010405secondhomeroom_scene_text[366]][startergendercap][day_010405secondhomeroom_scene_text[367]][startergendercap][day_010405secondhomeroom_scene_text[368]]"

calem @sad "[day_010405secondhomeroom_scene_text[369]][startergender][day_010405secondhomeroom_scene_text[370]]"

$ startergenderpronoun = "him" 
if (playerparty[0].GetGender() == Genders.Female):
    $ startergenderpronoun = "her"
elif (playerparty[0].GetGender() == Genders.Unknown):
    $ startergenderpronoun = "them"

ethan @confused "[day_010405secondhomeroom_scene_text[371]][first_name][day_010405secondhomeroom_scene_text[372]][startergenderpronoun][day_010405secondhomeroom_scene_text[373]]"

calem @surprised "[day_010405secondhomeroom_scene_text[374]][startergendercap][day_010405secondhomeroom_scene_text[375]][startergendercap][day_010405secondhomeroom_scene_text[376]][startergender][day_010405secondhomeroom_scene_text[377]]"

ethan @happy "[day_010405secondhomeroom_scene_text[378]]"

calem @angrybrow talking2mouth "[day_010405secondhomeroom_scene_text[379]]"

brendan @closedbrow talkingmouth "[day_010405secondhomeroom_scene_text[380]]" 
brendan frownmouth @sad "[day_010405secondhomeroom_scene_text[381]]"

show brendan:
    xpos 0.8
    ease 0.5 xpos 0.7

show hilbert at dissolvein:
    xpos 0.8

hilbert @talkingmouth "[day_010405secondhomeroom_scene_text[382]]"

calem @angry "[day_010405secondhomeroom_scene_text[383]]"

hilbert @talkingmouth "[day_010405secondhomeroom_scene_text[384]]"

hilbert @talkingmouth "[day_010405secondhomeroom_scene_text[385]][first_name][day_010405secondhomeroom_scene_text[386]]" 
hilbert @talkingmouth "[day_010405secondhomeroom_scene_text[387]]"
hilbert @talkingmouth "[day_010405secondhomeroom_scene_text[388]]"

brendan happy "[day_010405secondhomeroom_scene_text[389]]"

pause 1.0

brendan -happy @closedbrow talking2mouth "[day_010405secondhomeroom_scene_text[390]]"

red @confused "[day_010405secondhomeroom_scene_text[391]]"

red @surprised "[day_010405secondhomeroom_scene_text[392]]"

ethan @surprised "[day_010405secondhomeroom_scene_text[393]]"

red @closedbrow talking2mouth "[day_010405secondhomeroom_scene_text[394]]"

ethan @happy "[day_010405secondhomeroom_scene_text[395]]"

red @talkingmouth "[day_010405secondhomeroom_scene_text[396]]"

redmind @thinking "[day_010405secondhomeroom_scene_text[397]]"

ethan @happy "[day_010405secondhomeroom_scene_text[398]]"

hide hilbert
hide brendan
hide calem
hide ethan
with dis

red @talkingmouth "[day_010405secondhomeroom_scene_text[399]]"

$ renpy.music.play("Audio/Pokemon/pikachu_norm3.ogg", channel="altcry", loop=None)

pikachu happy "[day_010405secondhomeroom_scene_text[400]]"

$ renpy.music.play("Audio/pokemon/cries/{}.mp3".format(starter_id), channel="altcry", loop=None)

$ starter_fragment = pokedexlookup(starter_id, DexMacros.Name)[:3]
starter @talkingmouth "[day_010405secondhomeroom_scene_text[401]][starter_fragment][day_010405secondhomeroom_scene_text[402]]"

window hide

$ PlaySound("Pokemon/Ball sound.ogg")

show starterportraitfull at backinpokeball, dormdesk

pause 1.0

show dorm_B lightsout

pause 1.0

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_14

show blank2 with transeye

narrator "[day_010405secondhomeroom_scene_text[403]]"

window hide

stop music fadeout 1.0
$ renpy.pause(1.0, hard=True)

hide dorm_empty_B
hide blank2

jump day010406

