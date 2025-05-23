label lunch010405:

$ timeOfDay = "Afternoon"

$ renpy.transition(dissolve)
show screen currentdate

queue music "Audio/Music/Road to Viridian City.ogg"
    
hide blank2 with splitfade

$ renpy.pause(0.5, hard=True)

show bianca uniform with dis

bianca @happy "[day_010405lunch_scene_text[0]]"

red uniform @talkingmouth "[day_010405lunch_scene_text[1]]"

bianca @talkingmouth "[day_010405lunch_scene_text[2]]"

red @confused "[day_010405lunch_scene_text[3]]"

bianca @happy "[day_010405lunch_scene_text[4]]"

red @happy "[day_010405lunch_scene_text[5]]"
red @talkingmouth "[day_010405lunch_scene_text[6]]"

show blank2 with splitfade

hide bianca

narrator "[day_010405lunch_scene_text[7]]"
narrator "[day_010405lunch_scene_text[8]]"
narrator "[day_010405lunch_scene_text[9]]"

cheren uniform @talkingmouth "[day_010405lunch_scene_text[10]]"

hide blank2 with splitfade

show cafeB_CG:
    subpixel True
    alpha 0.0 xalign 0.5 yalign 1.0 zoom 1.25
    parallel:
        ease 1.5 alpha 1.0
    parallel:
        ease 5.0 zoom 1.0

redmind "[day_010405lunch_scene_text[11]]"

serena uniform @talkingmouth "[day_010405lunch_scene_text[12]]"

cheren @talking2mouth "[day_010405lunch_scene_text[13]]"

hide calem
hide hilda

cheren @talking2mouth "[day_010405lunch_scene_text[14]]"

calem uniform @talkingmouth "[day_010405lunch_scene_text[15]]"

hilda uniform @smirkmouth "[day_010405lunch_scene_text[16]]"

$ BecomeNamed("Hilda")
cheren @happy "[day_010405lunch_scene_text[17]]"
cheren @talkingmouth "[day_010405lunch_scene_text[18]]"
cheren @closedbrow talking2mouth "[day_010405lunch_scene_text[19]]"

hilbert uniform @sadbrow talkingmouth "[day_010405lunch_scene_text[20]]"

hilda @angry "[day_010405lunch_scene_text[21]]"

cheren @surprised "[day_010405lunch_scene_text[22]]"

hilbert @talkingmouth "[day_010405lunch_scene_text[23]]"

cheren @angrybrow "[ellipses]"

cheren @sad "[day_010405lunch_scene_text[24]]"
cheren @happy "[day_010405lunch_scene_text[25]]"

hilbert @sadbrow talkingmouth "[day_010405lunch_scene_text[26]][ellipses][day_010405lunch_scene_text[27]]" 
extend @talkingmouth "[day_010405lunch_scene_text[28]]"

pause 1.0

red uniform @confused "[day_010405lunch_scene_text[29]]"

cheren @happy "[day_010405lunch_scene_text[30]][first_name][day_010405lunch_scene_text[31]]" 
cheren @talkingmouth "[day_010405lunch_scene_text[32]]"

red @confused "[day_010405lunch_scene_text[33]]"

cheren @happy "[day_010405lunch_scene_text[34]]"
cheren @closedbrow talking2mouth "[day_010405lunch_scene_text[35]]"
cheren @talkingmouth "[day_010405lunch_scene_text[36]][first_name][day_010405lunch_scene_text[37]]"

if (council_campaigning):
    red @happy "[day_010405lunch_scene_text[38]]"

else:
    menu:
        "[day_010405lunch_scene_text[39]]":
            $ council_campaigning = True

        "[day_010405lunch_scene_text[40]]":
            pass

if (council_campaigning):
    cheren @happy "[day_010405lunch_scene_text[41]]"
    cheren @talking2mouth "[day_010405lunch_scene_text[42]]"
    cheren @talking2mouth "[day_010405lunch_scene_text[43]][first_name][day_010405lunch_scene_text[44]]"

else:
    cheren @sad "[day_010405lunch_scene_text[45]]"
    cheren @talking2mouth "[day_010405lunch_scene_text[46]]"
    cheren @talking2mouth "[day_010405lunch_scene_text[47]]"

cheren @sad "[day_010405lunch_scene_text[48]]"
cheren @talking2mouth "[day_010405lunch_scene_text[49]]"

serena @talkingmouth "[day_010405lunch_scene_text[50]]"
serena @blush heartbrow talkingmouth "[day_010405lunch_scene_text[51]]"

calem @surprised "[day_010405lunch_scene_text[52]]"

serena @happy "[day_010405lunch_scene_text[53]]"

cheren @happy "[day_010405lunch_scene_text[54]]"

if (council_campaigning):
    cheren @talkingmouth "[day_010405lunch_scene_text[55]][first_name][day_010405lunch_scene_text[56]]"

    red @talking2mouth "[day_010405lunch_scene_text[57]]"

    cheren @closedbrow talkingmouth "[day_010405lunch_scene_text[58]]"

hilda @talkingmouth "[day_010405lunch_scene_text[59]]"

hilbert @closedbrow talkingmouth "[day_010405lunch_scene_text[60]]"

hide bianca

cheren @closedbrow talkingmouth "[day_010405lunch_scene_text[61]]"
cheren @talkingmouth "[day_010405lunch_scene_text[62]]"

bianca uniform @happy "[day_010405lunch_scene_text[63]]"

pause 1.0
    
bianca @happy sweat "[day_010405lunch_scene_text[64]]"

redmind @closedbrow talkingmouth "[day_010405lunch_scene_text[65]]"

serena @talkingmouth "[day_010405lunch_scene_text[66]]"
serena @happy "[day_010405lunch_scene_text[67]]"

hilda @happy "[day_010405lunch_scene_text[68]]"

hilbert @surprised "[day_010405lunch_scene_text[69]]"

serena @talkingmouth "[day_010405lunch_scene_text[70]]"

hilbert @talkingmouth "[day_010405lunch_scene_text[71]]"

hilda @closedbrow talking2mouth veins "[day_010405lunch_scene_text[72]]"

hilbert @sadbrow talkingmouth "[day_010405lunch_scene_text[73]]"
hilbert @angry "[day_010405lunch_scene_text[74]]"

hilda @angrybrow smirkmouth "[day_010405lunch_scene_text[75]]"

hilbert @frownmouth "[ellipses]"

hilbert @talkingmouth "[day_010405lunch_scene_text[76]]"

calem @talkingmouth "[day_010405lunch_scene_text[77]]"

serena @talkingmouth "[day_010405lunch_scene_text[78]]"

calem @talkingmouth "[day_010405lunch_scene_text[79]]"

serena @talkingmouth "[day_010405lunch_scene_text[80]]"

cheren @talking2mouth "[day_010405lunch_scene_text[81]]"

bianca @happy "[day_010405lunch_scene_text[82]]"

serena @happy "[day_010405lunch_scene_text[83]]"
serena @talkingmouth "[day_010405lunch_scene_text[84]][first_name][day_010405lunch_scene_text[85]]"

redmind @thinking "[day_010405lunch_scene_text[86]]"

menu:
    "[day_010405lunch_scene_text[87]]":
        $ ValueChange("Calem", 1, (448/1920, 641/1080), False)
        $ ValueChange("Hilbert", 1, (1579/1920, 281/1080))
        
        hilbert @closedbrow talkingmouth "[day_010405lunch_scene_text[88]]"
        hilbert @talkingmouth "[day_010405lunch_scene_text[89]]"
        
        hilda @sad "[day_010405lunch_scene_text[90]]"
        
        serena @poutmouth "[day_010405lunch_scene_text[91]]"
        
        calem @closedbrow talking2mouth "[day_010405lunch_scene_text[92]]"
        
        serena @angrybrow talkingmouth "[day_010405lunch_scene_text[93]]"
    
    "[day_010405lunch_scene_text[94]]":
        $ ValueChange("Serena", 1, (112/1920, 426/1080), False)
        $ ValueChange("Hilda", 1, (1455/1920, 650/1080))

        serena @happy "[day_010405lunch_scene_text[95]]"

        calem @sadmouth "[day_010405lunch_scene_text[96]]"
        
        hilda @smirkmouth "[day_010405lunch_scene_text[97]]"
        hilda @closedbrow talkingmouth "[day_010405lunch_scene_text[98]]"
        
        hilbert @angrybrow talkingmouth "[day_010405lunch_scene_text[99]]"
        hilbert @closedbrow talkingmouth "[day_010405lunch_scene_text[100]]"

        hilda @sadbrow talking2mouth "[day_010405lunch_scene_text[101]]"
        
        calem @closedbrow talkingmouth "[day_010405lunch_scene_text[102]]"
    
    "[day_010405lunch_scene_text[103]]":
        red @talkingmouth "[day_010405lunch_scene_text[104]]"
        red @happy "[day_010405lunch_scene_text[105]]"
        
        $ ValueChange("Cheren", 1, (914/1920, 197/1080), False)
        $ ValueChange("Bianca", 1, (1326/1920, 285/1080))
        
        cheren @closedbrow talkingmouth "[day_010405lunch_scene_text[106]]"
        
        bianca @happy "[day_010405lunch_scene_text[107]]"
        
        serena @sadbrow talkingmouth "[day_010405lunch_scene_text[108]]"
        
        hilbert @angry "[day_010405lunch_scene_text[109]]"
    
bianca @talkingmouth "[day_010405lunch_scene_text[110]]"
bianca @happy "[day_010405lunch_scene_text[111]]"

cheren @confused "[day_010405lunch_scene_text[112]]"

bianca @talkingmouth "[day_010405lunch_scene_text[113]]"

cheren @happy "[day_010405lunch_scene_text[114]]"

bianca @happy "[day_010405lunch_scene_text[115]]"

cheren @closedbrow talkingmouth "[day_010405lunch_scene_text[116]]"
cheren @happy "[day_010405lunch_scene_text[117]]"

bianca @happy "[day_010405lunch_scene_text[118]]"

cheren @sadbrow talkingmouth "[day_010405lunch_scene_text[119]]"

serena @talkingmouth "[day_010405lunch_scene_text[120]]"

calem @closedbrow talkingmouth "[day_010405lunch_scene_text[121]]"

serena @sadbrow happymouth "[day_010405lunch_scene_text[122]]"

cheren @closedbrow talkingmouth "[day_010405lunch_scene_text[123]]"
cheren @happy "[day_010405lunch_scene_text[124]]"
cheren @talkingmouth "[day_010405lunch_scene_text[125]]"

bianca @surprised "[day_010405lunch_scene_text[126]]" 
extend talkingmouth "[day_010405lunch_scene_text[127]]"
bianca @happy "[day_010405lunch_scene_text[128]]"

cheren @talking2mouth "[day_010405lunch_scene_text[129]]"

bianca @surprised "[day_010405lunch_scene_text[130]]"

calem @sad "[day_010405lunch_scene_text[131]]"

serena @talkingmouth "[day_010405lunch_scene_text[132]]"
serena @happy "[day_010405lunch_scene_text[133]]"

calem @talkingmouth "[day_010405lunch_scene_text[134]]"

serena @happy "[day_010405lunch_scene_text[135]]"

hilda @sadbrow smirkmouth "[day_010405lunch_scene_text[136]]"
hilda @happy "[day_010405lunch_scene_text[137]]"

serena @surprised "[day_010405lunch_scene_text[138]]"

hilda @sadbrow smirkmouth "[day_010405lunch_scene_text[139]]"

pause 1.0

hilda @smirkmouth "[day_010405lunch_scene_text[140]]"

hilbert @closedbrow talkingmouth"[day_010405lunch_scene_text[141]]"

hilda @talkingmouth "[day_010405lunch_scene_text[142]]"

hilbert @talkingmouth "[day_010405lunch_scene_text[143]]"
hilbert @talkingmouth "[day_010405lunch_scene_text[144]]"

calem @closedbrow talkingmouth "[day_010405lunch_scene_text[145]][first_name][day_010405lunch_scene_text[146]]"

if council_campaigning:
    calem @talkingmouth "[day_010405lunch_scene_text[147]]"

red @closedbrow talking2mouth "[day_010405lunch_scene_text[148]]"

menu:
    "[day_010405lunch_scene_text[149]]":
        red @talkingmouth "[day_010405lunch_scene_text[150]]"
        
        $ ValueChange("Calem", 1, (448/1920, 641/1080))
        
        calem @happy "[day_010405lunch_scene_text[151]][first_name][day_010405lunch_scene_text[152]]"
        calem @closedbrow talkingmouth "[day_010405lunch_scene_text[153]]"
        
        serena @happy "[day_010405lunch_scene_text[154]]"
        
        calem @sadbrow talkingmouth "[day_010405lunch_scene_text[155]]"
    
    "[day_010405lunch_scene_text[156]]":
        red @talkingmouth "[day_010405lunch_scene_text[157]]"
        
        $ ValueChange("Bianca", 1, (1326/1920, 285/1080))       
        
        bianca @happy "[day_010405lunch_scene_text[158]]"
        
        hilda @happy "[day_010405lunch_scene_text[159]]"
        
        bianca @puppyeyes happymouth "[day_010405lunch_scene_text[160]]"
    
    "[day_010405lunch_scene_text[161]]":     
        red @talkingmouth "[day_010405lunch_scene_text[162]]"
        red @happy "[day_010405lunch_scene_text[163]]"

        $ ValueChange("Serena", 1, (112/1920, 426/1080)) 
        
        serena @happy "[day_010405lunch_scene_text[164]]"
        serena @talkingmouth "[day_010405lunch_scene_text[165]]"

        red @confused "[day_010405lunch_scene_text[166]]"
        
        serena @sadbrow happymouth "[day_010405lunch_scene_text[167]]"

        red @closedbrow talking2mouth "[day_010405lunch_scene_text[168]]"

        pause 1.0

        serena @talkingmouth "[day_010405lunch_scene_text[169]]"
    
    "[day_010405lunch_scene_text[170]]":
        red @talkingmouth "[day_010405lunch_scene_text[171]]"

        $ ValueChange("Hilda", 1, 1290/1920)

        hilda @happy "[day_010405lunch_scene_text[172]]"
        
        red @talkingmouth "[day_010405lunch_scene_text[173]]"
        
        hilda @smirkmouth "[day_010405lunch_scene_text[174]]"
        
        red @confused "[day_010405lunch_scene_text[175]]"
        
        hilda @happy "[day_010405lunch_scene_text[176]]"

        serena @sad "[ellipses]"

        calem @sad "[ellipses]"


        redmind @thinking "[day_010405lunch_scene_text[177]]"

        hilda @smirkmouth "[day_010405lunch_scene_text[178]]" 
        hilda @sadbrow smirkmouth "[day_010405lunch_scene_text[179]]"
    "[day_010405lunch_scene_text[180]]":
        red @talkingmouth "[day_010405lunch_scene_text[181]]"
        red @talkingmouth "[day_010405lunch_scene_text[182]]"

        $ ValueChange("Hilbert", -1, 1690/1920)
        
        hilbert @closedbrow talkingmouth "[day_010405lunch_scene_text[183]]"
        
        red @talkingmouth "[day_010405lunch_scene_text[184]]"

        hilbert @talkingmouth "[day_010405lunch_scene_text[185]]"
    
        red @closedbrow talking2mouth "[day_010405lunch_scene_text[186]]"

        hilbert @sadbrow talkingmouth "[day_010405lunch_scene_text[187]]"

        red @angrybrow  talkingmouth "[day_010405lunch_scene_text[188]]"

calem @surprised "[day_010405lunch_scene_text[189]]"

hilbert @closedbrow talkingmouth "[day_010405lunch_scene_text[190]]"

bianca @happy "[day_010405lunch_scene_text[191]]"

cheren @closedbrow talkingmouth "[day_010405lunch_scene_text[192]]"

hilda @smirkmouth "[day_010405lunch_scene_text[193]]"

bianca @happy "[day_010405lunch_scene_text[194]]"

cheren @happy "[day_010405lunch_scene_text[195]]"

bianca @surprisedbrow talking2mouth "[day_010405lunch_scene_text[196]]"
bianca @happy "[day_010405lunch_scene_text[197]]"
bianca @talkingmouth "[day_010405lunch_scene_text[198]]"

calem @happy "[day_010405lunch_scene_text[199]]"

hilda @smirkmouth "[day_010405lunch_scene_text[200]]"

cheren @talkingmouth "[day_010405lunch_scene_text[201]]"

serena @sadmouth closedbrow "[day_010405lunch_scene_text[202]]"
serena @sadbrow happymouth "[day_010405lunch_scene_text[203]]"

hilda @talkingmouth "[day_010405lunch_scene_text[204]]"

bianca @happy "[day_010405lunch_scene_text[205]]"

narrator "[day_010405lunch_scene_text[206]]"

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")

show blank2 with dis

$ PlaySound("BellChime.ogg")
$ renpy.music.set_volume(1.0, delay=4.0, channel="music")

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_9

$ renpy.pause(1.0, hard=True)

narrator "[day_010405lunch_scene_text[207]]"

window hide
scene blank2
$ renpy.music.stop(channel='crowd', fadeout=1.0)

jump PickElective
