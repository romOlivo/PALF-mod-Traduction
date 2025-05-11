
label prologue:
    stop music

    scene blank2
    $ RealignTextbox()

    TempCharacter("[prologue_scene_text[0]]") "[prologue_scene_text[1]]" 
    TempCharacter("[prologue_scene_text[2]]") "[prologue_scene_text[3]]" 
    TempCharacter("[prologue_scene_text[4]]") "[prologue_scene_text[5]]"

    menu: 
        "[prologue_scene_text[6]]":
            narrator "[prologue_scene_text[7]]"

        "[prologue_scene_text[8]]":
            narrator "[prologue_scene_text[9]]"

            $ MainMenu(confirm=False)()

    play music "audio/music/Dreams and Adventures.ogg"
    
    show pallet with dis:
        alpha 0.75
        
    show blank with dis:
        alpha 0.85
    
    pause 2.0

    show oak with dis

    oak @talkingmouth "[prologue_scene_text[10]]"
    oak @happy "[prologue_scene_text[11]]"
    oak @talkingmouth "[prologue_scene_text[12]]"
    oak @closedbrow talkingmouth "[prologue_scene_text[13]]"
    oak @happy "[prologue_scene_text[14]]"
    red "[ellipses]"

    oak @confusedbrow talkingmouth "[prologue_scene_text[15]]"

    label firstname:
        $ first_name = renpy.input("[prologue_scene_text[16]]", length=12, exclude="{}[[]%<>",)
        $ first_name = first_name.strip()

        if first_name == "":
            $ first_name = "Red"

        oak @talkingmouth "[prologue_scene_text[17]][first_name][prologue_scene_text[18]]"

        menu:
            "[prologue_scene_text[19]]":
                red @happy "[prologue_scene_text[20]]"
                pass

            "[prologue_scene_text[21]]":
                red @sadeyes sadeyebrows talkingmouth "[prologue_scene_text[22]]"
                oak @surprised "[prologue_scene_text[23]]"
                jump firstname

    oak @talkingmouth "[prologue_scene_text[24]]"

    label lastname:
        $ last_name = renpy.input("[prologue_scene_text[25]]", length=20, exclude="{}[[]%<>",)
        $ last_name = last_name.strip()

        if last_name == "":
            $ last_name = "Sugimori"

        oak @happy "[prologue_scene_text[26]][last_name][prologue_scene_text[27]]"

        menu:
            "[prologue_scene_text[28]]":
                red @happy "[prologue_scene_text[29]]"
                pass

            "[prologue_scene_text[30]]":
                red @sadeyes sadeyebrows talkingmouth "[prologue_scene_text[31]]"
                oak @surprised "[prologue_scene_text[32]]"
                jump lastname

    oak @happy "[prologue_scene_text[33]][first_name][prologue_scene_text[34]][last_name][prologue_scene_text[35]]"
    oak @surprised sweat "[prologue_scene_text[36]]" 
    extend @happy sweat "[prologue_scene_text[37]]"

    $ renpy.music.play("Audio/Pokemon/pikachu_norm1.ogg", channel="altcry")

    pikachu neutral_2 "Pi-KA-chu!"

    oak @happy "[prologue_scene_text[38]]"
    oak @sadeyes sadeyebrows talkingmouth "[prologue_scene_text[39]]"

    label pikaname:
        $ pika_name = renpy.input("[prologue_scene_text[40]]", length=12, exclude="{}[[]%<>",)
        $ pika_name = pika_name.strip()
        
        if pika_name == "" or pika_name == "pikachu":
            $ pika_name = "Pikachu"

        oak @talkingmouth "[prologue_scene_text[41]][pika_name][prologue_scene_text[42]]"

        menu:
            "[prologue_scene_text[43]]":
                red @happybrow talkingmouth "[prologue_scene_text[44]]"
                pass

            "[prologue_scene_text[45]]":
                red @angrybrow talking2mouth "[prologue_scene_text[46]]"
                oak @surprised "[prologue_scene_text[47]]"
                jump pikaname

    oak @happy "[prologue_scene_text[48]][pika_name][prologue_scene_text[49]]"

    oak @talkingmouth "[prologue_scene_text[50]]"
    oak @sadbrow talkingmouth sweat "[prologue_scene_text[51]]"
    oak @closedbrow talkingmouth "[prologue_scene_text[52]]"

    oak @talkingmouth "[prologue_scene_text[53]]"

    menu:
        "[prologue_scene_text[54]]":
            $ profanity = True
            red @angry "[prologue_scene_text[55]]"

        "[prologue_scene_text[56]]":
            red @sadbrow happymouth "[prologue_scene_text[57]]"

    oak @happy "[prologue_scene_text[58]]"
    
    oak @talkingmouth "[prologue_scene_text[59]][first_name][prologue_scene_text[60]]"

    oak @angrybrow talkingmouth "[prologue_scene_text[61]]"
    oak happy "[prologue_scene_text[62]]"

    hide oak with dis

    stop music fadeout 2.5
        
    show blank:
        alpha 0.85
        ease 2.0 alpha 1.0
        
    oak "[prologue_scene_text[63]]"
    
    show pallet:
        alpha 0.75
        pause 2.5
        ease 2.5 alpha 1.0
    
    $ renpy.pause(2.5, hard=True)

    hide blank    
    show pallet with vpunch:
        alpha 1.0
    $ PlaySound("Body Roll.ogg")
    
    red casual hatless @surprised "[prologue_scene_text[64]]"

    $ renpy.music.queue("Audio/Music/Pallet Town A.ogg", channel='music', loop=True, fadein=1.0, tight=None)
    $ renpy.pause(1.25, hard=True)

    hide oak
    hide blank2
    hide blank
    
    red sadeyebrows closedeyes talking2mouth "[prologue_scene_text[65]]"

    red angrybrow happymouth "[prologue_scene_text[66]]"

    pause 1.5
    
    $ renpy.music.play("Audio/Pokemon/pikachu_question.ogg", channel="altcry", loop=None)
    pikachu neutral_4 "Pi-ka?"

    red -sadeyebrows -closedeyes -talking2mouth "[prologue_scene_text[67]][pika_name][prologue_scene_text[68]]"

    $ renpy.music.play("Audio/Pokemon/pikachu_norm2.ogg", channel="altcry", loop=None)
    pikachu neutral_2b "Piiii-ka!"

    red -angrybrow -happymouth @happy "[prologue_scene_text[69]]"

    $ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)
    pikachu bashful "Piiii{w=0.5}{nw}"
    extend bashful_2 "[prologue_scene_text[70]]"

    red talkingmouth "[prologue_scene_text[71]]"

    red talking2mouth angrybrow "[prologue_scene_text[72]]"
    red -angrybrow happy "[prologue_scene_text[73]]"

    $ renpy.music.play("Audio/Pokemon/pikachu_excite4.ogg", channel="altcry", loop=None)
    pikachu neutral_2b "Piii-kaaaa!"

    show mom:
        xpos 1.5

    mom "[prologue_scene_text[74]]"

    show mom at moveinleft

    pause 1.0

    red frownmouth angryeyes confusedeyebrows @talking2mouth "[prologue_scene_text[75]]"

    mom @angry "[prologue_scene_text[76]]"

    red closedeyes -confusedeyebrows happymouth "[prologue_scene_text[77]]"

    mom @happymouth "[prologue_scene_text[78]]"

    red surprised "[prologue_scene_text[79]]"

    mom @happy "[prologue_scene_text[80]]"

    red -surprisedbrow -frownmouth -surprised @happy sweat "[prologue_scene_text[81]]"

    mom sadeyebrows sadeyes @talkingmouth "[prologue_scene_text[82]][pika_name][prologue_scene_text[83]]"

    pause 1.0

    $ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)

    pikachu yawn "{cps=*0.1}Pikaaaaaa..."

    pause 1.0

    red @closedeyes talking2mouth "[prologue_scene_text[84]][pika_name][prologue_scene_text[85]]"
    red @angrybrow happymouth "[prologue_scene_text[86]][pika_name][prologue_scene_text[87]]"

    mom @surprised "[prologue_scene_text[88]]"

    red -angrybrow -happymouth @talkingmouth "[prologue_scene_text[89]]"

    mom sadeyes sadeyebrows @talkingmouth "[prologue_scene_text[90]]"

    menu:
        "[prologue_scene_text[91]]":
            show mom -sadeyes -sadeyebrows with dis

            red happy "[prologue_scene_text[92]]"

            mom @sadeyes sadeyebrows happymouth "[prologue_scene_text[93]]"

            red -happy @talkingmouth "[prologue_scene_text[94]]"
            
            red @closedeyes sadeyebrows talking2mouth "[prologue_scene_text[95]]"
            
            mom @talkingmouth "[prologue_scene_text[96]]"
            
            mom @happy "[prologue_scene_text[97]]"
           
            red @confused "[prologue_scene_text[98]]"

            show mom happy:
                zoom 1.0 ypos 1.0
                ease 0.75 zoom 1.25 ypos 1.25
            
            pause 0.75
            
            mom "[prologue_scene_text[99]]"

            red @closedeyes lightblush talking2mouth "[prologue_scene_text[100]]"

            show mom -happy sadeyes sadeyebrows:
                zoom 1.25 ypos 1.25
                ease 0.75 zoom 1.0 ypos 1.0
            
            mom @sadbrow talkingmouth "[prologue_scene_text[101]]"
            
            mom @happy "[prologue_scene_text[102]]"
            
        "[prologue_scene_text[103]]":
            show mom surprisedbrow frownmouth with dis

            red @playfulbrow sweat talkingmouth "[prologue_scene_text[104]]"

            mom angrybrow frownmouth -surprisedbrow -frownmouth -surprised @surprised "[prologue_scene_text[105]][first_name][prologue_scene_text[106]]"
            
            red -angrybrow happymouth "[prologue_scene_text[107]]"
            
            mom @angry "[prologue_scene_text[108]]"
                      
            mom -angrybrow -frownmouth @happy "[prologue_scene_text[109]]"
        
        "[prologue_scene_text[110]]":
            show mom -sadeyes -sadeyebrows with dis

            red @sadeyebrows closedeyes talkingmouth sweat "[prologue_scene_text[111]]"
            
            mom @happy "[prologue_scene_text[112]]"

            show mom happy:
                zoom 1.0 ypos 1.0
                ease 0.75 zoom 1.25 ypos 1.25
            
            pause 0.75
            
            mom "[prologue_scene_text[113]]"

            red @closedeyes lightblush talking2mouth "[prologue_scene_text[114]]"

            show mom -happy sadeyes sadeyebrows:
                zoom 1.25 ypos 1.25
                ease 0.75 zoom 1.0 ypos 1.0
            
            mom @sadbrow talkingmouth "[prologue_scene_text[115]]"
            
            mom @happy "[prologue_scene_text[116]]"

    stop music fadeout 2.0    

    pause 2.0

    red angrybrow sadmouth "[prologue_scene_text[117]]"

    $ renpy.music.queue("Audio/Music/Littleroot_Start.ogg", channel='music', loop=False, fadein=1.0, tight=None)
    $ renpy.music.queue("Audio/Music/Littleroot_Loop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

    mom sadeyebrows frownmouth @surprised "[prologue_scene_text[118]]"

    red -angrybrow closedeyes sadeyebrows "[prologue_scene_text[119]]"

    red sadeyes "[prologue_scene_text[120]]"

    red @talkingmouth "[prologue_scene_text[121]]"

    mom @angry "[prologue_scene_text[122]]"

    red sad "[prologue_scene_text[123]]"

    red sadeyebrows closedeyes happymouth "[prologue_scene_text[124]]"

    mom @sad "[prologue_scene_text[125]]"

    red happy "[prologue_scene_text[126]]"

    pause 1.0

    stop music fadeout 1.0

    red confused "[prologue_scene_text[127]]"

    $ renpy.music.queue("Audio/Music/Pallet Town A.ogg", channel='music', loop=True, fadein=1.0, tight=None)

    mom happy "[prologue_scene_text[128]]"

    red -confused closedeyes talking2mouth "[prologue_scene_text[129]]"
    red neutraleyes talking2mouth "[prologue_scene_text[130]]"

    mom -happy @talkingmouth "[prologue_scene_text[131]]"

    show letter at itemhover

    show mom:
        xcenter 0.5
        ease 1.0 xcenter 0.75
    
    $ PlaySound("item_get.ogg")

    red @confused "[prologue_scene_text[132]]"
    red @sad2eyes angryeyebrows talking2mouth "[prologue_scene_text[133]]"

    mom sadeyes sadeyebrows @talkingmouth "[prologue_scene_text[134]]"

    red happy "[prologue_scene_text[135]]"

    mom @angry "[prologue_scene_text[136]]"

    red closedeyes @talkingmouth "[prologue_scene_text[137]][last_name][prologue_scene_text[138]]"

    show letter at itemhide
    show mom:
        ease 1.0 xcenter 0.5

    red -happy -closedeyes @talkingmouth "[prologue_scene_text[139]]"

    red @thinking "[ellipses]"

    show mom -sadeyebrows -sadeyes with dis

    show red:
        xpos -0.5

    show image "CG/Acceptance Letter.webp" with Dissolve(2.0)

    red @surprisedeyes frownmouth "[ellipses]"


    show mom happyeyes happyeyebrows with dis

    red @surprisedeyes frownmouth "[ellipses]"


    show mom happy with dis

    red @surprised "[ellipses]"


    pause 1.0

    red @surprised "[prologue_scene_text[140]]"

    mom @talkingmouth "[prologue_scene_text[141]]"

    mom @playfulbrow talkingmouth blush "[prologue_scene_text[142]]"

    red @surprisedeyes confusedeyebrows talking2mouth "[prologue_scene_text[143]]"

    mom @closedbrow talking2mouth "[prologue_scene_text[144]]"

    red @surprised "[ellipses]"


    $ renpy.music.play("Audio/Pokemon/pikachu_confused.ogg", channel="altcry", loop=None)
    pikachu neutral_4 "Piiika?"

    red @surprised "[prologue_scene_text[145]][pika_name][prologue_scene_text[146]]"

    show mom happybrow neutralmouth
    hide image "CG/Acceptance Letter.webp"
    hide red
    with Dissolve(1.0)

    pause 1.0

    red hatless casual @happy "[prologue_scene_text[147]]"

    mom sadeyes sadeyebrows @talkingmouth "[prologue_scene_text[148]]"

    stop music fadeout 2.0
    show blank2 with splitfade
    
    $ renpy.pause(2.0, hard=True)
    
    hide pallet
    hide mom
    
    $ renpy.music.queue("Audio/Music/ViridianB_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
    $ renpy.music.queue("Audio/Music/ViridianB_Loop.ogg", channel='music', loop=True, tight=None)
    
    $ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=0.5)
    
    scene airport behind blank2:
        xalign 1.0 yalign 1.0
    hide blank2 with splitfade
    
    pause 1.0

    redmind angrybrow frownmouth "[prologue_scene_text[149]]"
    red -angrybrow closedeyes @talkingmouth sweat"[prologue_scene_text[150]]"
    red -closedeyes @confused "[prologue_scene_text[151]]"
    
    show mom with dis

    mom @talkingmouth "[prologue_scene_text[152]]"

    red @closedbrow talking2mouth "[prologue_scene_text[153]]"
    extend @closedbrow sweat talkingmouth "[prologue_scene_text[154]]"
    
    mom @angry "[prologue_scene_text[155]]"
    extend @happy "[prologue_scene_text[156]]"

    red @thinking "[ellipses]"

    red @sadeyes sadeyebrows talkingmouth "[prologue_scene_text[157]]"
    red @happy "[prologue_scene_text[158]]"
    mom @angryeyes angryeyebrows happymouth blush "[prologue_scene_text[159]]"
    
    pause 2.0

    mom @sadeyebrows sadeyes talkingmouth "[prologue_scene_text[160]][first_name][prologue_scene_text[161]]"
    
    red @talkingmouth "[prologue_scene_text[162]]"
    
    mom @happy "[prologue_scene_text[163]]"
    mom @sadbrow talkingmouth "[prologue_scene_text[164]]"
    
    red @sad2eyes sadeyebrows lightblush talkingmouth "[prologue_scene_text[165]]"

    show mom happyeyes sadeyebrows -happymouth blush:
        zoom 1.0 ypos 1.0
        ease 0.75 zoom 1.25 ypos 1.25
    
    pause 2.5

    show mom -happy -blush:
        zoom 1.25 ypos 1.25
        ease 0.75 zoom 1.0 ypos 1.0
    
    red @talkingmouth sadbrow "[prologue_scene_text[166]]"
    mom tears sadbrow @talkingmouth "[prologue_scene_text[167]]"
    
    $ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)
    pikachu sad_2 "Piiiikaaaa."

    mom sadeyes sadeyebrows @talkingmouth "[prologue_scene_text[168]][pika_name][prologue_scene_text[169]]"
    
    red @happy "[prologue_scene_text[170]]"
    red @talkingmouth "[prologue_scene_text[171]][first_name][prologue_scene_text[172]]"
    
    $ renpy.music.play("Audio/Pokemon/pikachu_sad2.ogg", channel="altcry", loop=None)
    pikachu @sad "Pika... piiiikaaaa."
    
    show mom -sadeyebrows -sad -talkingmouth with dis

    red @talkingmouth "[prologue_scene_text[173]]"
    
    mom @talkingmouth "[prologue_scene_text[174]]"

    show mom surprised:
        xpos 0.5
        ease 7.0 xpos 1.2
        
    show airport:
        xalign 1.0 yalign 1.0
        ease 8.0 xalign 0.0
        
    mom "[prologue_scene_text[175]]"

    pause 1.0

    redmind sadeyes sadeyebrows "[prologue_scene_text[176]]"

    pause 1.0

    redmind sad "[prologue_scene_text[177]][pika_name][prologue_scene_text[178]]"

    stop music fadeout 2.0
    pause 2.5
    
    show airport:
        xalign 0.0 yalign 1.0
        ease 4.0 xalign 1.0

    show mom -surprisedbrow -frownmouth -surprised:
        xpos 1.2
        ease 4.0 xpos 0.5
    
    $ renpy.pause(4.5, hard=True)
    
    show airport:
        xalign 1.0
    
    $ renpy.music.play("Audio/Pokemon/pikachu_sad2.ogg", channel="altcry", loop=None)
    pikachu sad_2 "Pika... piiiikaaaa."
        
    mom -tears @talkingmouth "[prologue_scene_text[179]][pika_name][prologue_scene_text[180]]"
    extend angryeyes angryeyebrows @talkingmouth "[prologue_scene_text[181]]"
    
    $ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)
    pikachu sad "Piiiikaaaa."

    mom -angryeyes -angryeyebrows -talkingmouth @happy "[prologue_scene_text[182]]"
    mom happyeyes talkingmouth -tears @talkingmouth "[prologue_scene_text[183]]"
    mom -happyeyes @talkingmouth "[prologue_scene_text[184]]"

    hide mom with dis
    
    $ PlaySound("plane_chime.ogg")
    
    TempCharacter("[prologue_scene_text[185]]") "[prologue_scene_text[186]]"
    TempCharacter("[prologue_scene_text[187]]") "[prologue_scene_text[188]]"
    
    pikachu neutral_3 "[ellipses]"
    
    $ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
    pikachu angry_2 "Pi-ka!"
    $ renpy.music.stop(channel='crowd', fadeout=1.0)
    
    $ renpy.music.queue("Audio/Music/SoaringDreams_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
    $ renpy.music.queue("Audio/Music/SoaringDreams_Loop.ogg", channel='music', loop=True, tight=None)
    
    hide mom
    
    show sky:
        alpha 0.0 yalign 1.0 xalign 0.2 zoom 1.25
        parallel:
            ease 1.0 alpha 1.0
        parallel:
            ease 30.0 xalign 1.0
    
    show clouds1 as base1:
        xpos -200 ypos 100 alpha 0.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 12.0 xpos 2000
            parallel:
                pause 11.0
                linear 1.0 alpha 0.0
    show clouds2 as base2:
        xpos -800 ypos 400 alpha 0.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 8.0 xpos 1000
            parallel:
                pause 7.0
                linear 1.0 alpha 0.0
    show clouds3 as base3:
        xpos -400 ypos 0 alpha 0.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 10.0 xpos 2200
            parallel:
                pause 9.0
                linear 1.0 alpha 0.0
    
    show clouds1 as set1:
        xpos -1800 ypos 100 alpha 0.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 15.0 xpos 1800
            parallel:
                pause 14.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1500
            repeat
    show clouds2 as set2:
        xpos -1700 ypos 100 alpha 0.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 12.0 xpos 2200
            parallel:
                pause 11.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1400
            repeat
    show clouds3 as set3:
        xpos -2100 ypos 0 alpha 0.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 17.0 xpos 2200
            parallel:
                pause 16.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1800
            repeat
    show clouds1 as set4:
        xpos -1700 ypos -100 alpha 0.0
        pause 5.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 6.0 xpos 1800
            parallel:
                pause 5.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1400
            repeat
    show clouds2 as set5:
        xpos -1900 ypos 500 alpha 0.0
        pause 6.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 8.0 xpos 2200
            parallel:
                pause 7.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1700
            repeat
    show clouds3 as set6:
        xpos -2100 ypos -50 alpha 0.0
        pause 5.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 20.0 xpos 2200
            parallel:
                pause 19.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1900
            repeat
    show clouds2 as set7:
        xpos -1900 ypos 200 alpha 0.0
        pause 4.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 10.0 xpos 2200
            parallel:
                pause 9.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1700
            repeat
    
    $ renpy.pause(1.5, hard=True)
    
    hide airport
    
    redmind -sadeyebrows closedeyes frownmouth "[prologue_scene_text[189]]"
    redmind "[prologue_scene_text[190]]"
    redmind happymouth "[prologue_scene_text[191]]"
    redmind -happymouth -closedeyes -frownmouth "[prologue_scene_text[192]]"
    redmind confusedeyebrows frownmouth "[prologue_scene_text[193]]"
    redmind closedeyes frownmouth "[prologue_scene_text[194]]" 
    redmind surprised "[prologue_scene_text[195]]"

    $ PlaySound("plane_chime.ogg")

    "[prologue_scene_text[196]]" "{color=#e70000}Good afternoon, passengers. We are expecting to land in the Kobukan region in approximately twenty minutes. The weather in Inspira City is clear and sunny.{/color}" 
    "[prologue_scene_text[197]]" "{color=#e70000}As we start our descent, please make sure your seat belt is securely fastened, your tray table is in the locked and upright position, and all electronic devices are turned off. Thank you.{/color}"
    
    red happy "[prologue_scene_text[198]]"
    
    show blank2 with Dissolve(1.0)
        
    $ PlaySound("Airplane.ogg")
    
    $ renpy.pause(2.0, hard=True)
    
    hide clouds1 as base1
    hide clouds2 as base2
    hide clouds3 as base3
    hide clouds1 as set1
    hide clouds2 as set2
    hide clouds3 as set3
    hide clouds1 as set4
    hide clouds2 as set5
    hide clouds3 as set6
    hide clouds2 as set7    
    
    stop music fadeout 2.0
    $ renpy.pause(2.5, hard=True)
    
    $ renpy.music.play("Audio/cityambience.ogg", channel='crowd', loop=True, fadein=1.5)
    
    $ renpy.pause(1.5, hard=True)
    
    scene city_A with Dissolve(2.0)
        
    $ renpy.pause(1.5, hard=True)
    
    hide sky
    hide blank2
    
    redmind closedeyes frownmouth "[prologue_scene_text[199]]"
    redmind happymouth "[prologue_scene_text[200]]"
    redmind angrybrow frownmouth "[prologue_scene_text[201]]"
    red -angrybrow happy "[prologue_scene_text[202]]"

    show pallet at sepia
    show flashback
    with dis

    $ renpy.pause(1.0, hard=True)
    
    show mom angry at sepia, dissolvein behind flashback

    mom "[prologue_scene_text[203]]"

    show blank with splitfade

    hide mom
    hide pallet
    hide flashback
    hide blank with dis

    red @talkingmouth "[prologue_scene_text[204]]"

    pause 1.5

    red talkingmouth "[prologue_scene_text[205]]"
    
    "[prologue_scene_text[206]]" "#!#Huh?#!#"

    show blue surprisedbrow frownmouth sweat with dis

    red surprised "[prologue_scene_text[207]]"

    show blue -surprisedbrow -frownmouth -surprised closedbrow frownmouth with dis
    
    pause 1.0
    
    blue "[ellipses]"

    
    play music "Audio/Music/RivalTune.ogg" noloop
    blue -sweat -frownmouth @happymouth "[prologue_scene_text[208]]"

    red -surprisedbrow -frownmouth -surprised angrybrow talking2mouth "[prologue_scene_text[209]]"
    
    queue music "audio/music/Inspira_start.ogg" noloop
    queue music "audio/music/Inspira_loop.ogg"

    blue -happymouth -closedbrow @surprised "[prologue_scene_text[210]]"
    
    red @closedbrow talking2mouth "[prologue_scene_text[211]]"
    
    blue @happy "[prologue_scene_text[212]]"
    
    red -angrybrow @confused "[prologue_scene_text[213]]"
    
    show blue surprisedbrow frownmouth with dis

    pause 1.5

    blue -surprisedbrow -frownmouth -surprised @happy "[prologue_scene_text[214]]"
    
    red -surprisedeyes -surprisedeyebrows -frownmouth @playfulbrow talkingmouth "[prologue_scene_text[215]]"
    
    blue -happy @surprised sweat "[prologue_scene_text[216]]"
    
    red @happy "[prologue_scene_text[217]]"
    
    blue -surprisedbrow -frownmouth -surprised -sweat @angry "[prologue_scene_text[218]]"
    blue -angry @closedbrow talkingmouth "[prologue_scene_text[219]]"

    red -happy @frownmouth "[prologue_scene_text[220]]"

    red @talkingmouth "[prologue_scene_text[221]]"

    blue frownmouth @angrybrow talkingmouth "[prologue_scene_text[222]]"

    red @talking2mouth "[prologue_scene_text[223]]"

    blue -frownmouth angry "[prologue_scene_text[224]]"

    red -talking2mouth @happy "[prologue_scene_text[225]]"

    label bluename:
        $ blue_name = renpy.input("[prologue_scene_text[226]]", length=12, exclude="{}[[]%<>",)
        $ blue_name = blue_name.strip()

        if blue_name == "" or blue_name == "blue" or blue_name == "Blue":
            $ blue_name = "Blueberry"

        red @happy "[prologue_scene_text[227]][blue_name][prologue_scene_text[228]]"

        menu:
            "[prologue_scene_text[229]]":
                red happyeyes talkingmouth "[prologue_scene_text[230]]"
                pass

            "[prologue_scene_text[231]]":
                red happyeyes talkingmouth "[prologue_scene_text[232]]"
                jump bluename

    blue @angry "[prologue_scene_text[233]]"

    red -happyeyes -happyeyebrows -talkingmouth @talkingmouth "[prologue_scene_text[234]][blue_name][prologue_scene_text[235]]"

    blue @closedbrow happymouth "[prologue_scene_text[236]]"
    blue @angry "[prologue_scene_text[237]]"
    blue -angry @surprisedbrow happymouth "[prologue_scene_text[238]]"

    show blue:
        parallel:
            ease 0.5 alpha 0.0
        parallel:
            ease 0.75 xpos 1.3

    pause 1.5

    redmind @thonk "[prologue_scene_text[239]]"
    
    show city_A:
        zoom 1.0 xalign 0.5 yalign 1.0
        block:
            ease 0.5 zoom 1.1 yalign 1.0 xalign 1.0
            pause 0.5
            ease 0.5 xalign 0.0
            pause 0.5
            ease 0.4 xalign 0.5
            
    redmind -surprisedbrow -frownmouth -surprised "[prologue_scene_text[240]]"
    redmind closedeyes frownmouth "[prologue_scene_text[241]]"
    
    show city_A:
        zoom 1.1 xalign 0.5 yalign 1.0
        ease 0.5 zoom 1.0
    
    pause 0.5
    
    show silver neutral with dis:
        xpos 1.3
        ease 1.0 xpos 0.5
    
    pause 2.0
    
    hide blue
    
    redmind @playfulbrow unamusedmouth "[prologue_scene_text[242]]"
    redmind happy "[prologue_scene_text[243]]"

    silver @talkingmouth "[prologue_scene_text[244]]"

    red surprised "[prologue_scene_text[245]]"

    silver angrybrow @talking2mouth "[prologue_scene_text[246]]"
    
    redmind @winkeyes sadeyebrows sweat frownmouth "[prologue_scene_text[247]]" 
    redmind @thinking "[prologue_scene_text[248]]"

    red @sad2eyes talking2mouth "[prologue_scene_text[249]]"
    
    silver sad "[prologue_scene_text[250]]"

    pause 1.5

    silver closedbrow "[prologue_scene_text[251]]"

    redmind @confusedeyebrows frownmouth "[prologue_scene_text[252]]"

    red @happy "[prologue_scene_text[253]]"

    pause 1.5

    silver -closedbrow @sad "[prologue_scene_text[254]]"

    red @talking2mouth angrybrow "[prologue_scene_text[255]]"

    silver @closedbrow talkingmouth "[prologue_scene_text[256]]"

    red @happy "[prologue_scene_text[257]]"

    silver @sadbrow happymouth "[prologue_scene_text[258]]"
    silver @talkingmouth "[prologue_scene_text[259]]"

    red @talkingmouth "[prologue_scene_text[260]]"

    silver @closedbrow talkingmouth "[prologue_scene_text[261]]"
    extend @surprisedbrow talkingmouth "[prologue_scene_text[262]]"

    pause 1.5

    red @talking2mouth "[prologue_scene_text[263]]"

    silver @closedbrow talkingmouth "[prologue_scene_text[264]]"

    red happy "[prologue_scene_text[265]]"

    silver @surprisedbrow talkingmouth "[prologue_scene_text[266]]"

    red @happy "[prologue_scene_text[267]]"

    show silver:
        xpos 0.5
        ease 3.0 xpos 0.0
        
    show city_A:
        ease 3.0 zoom 2.0

    pause 3.0

    silver @surprised "[prologue_scene_text[268]]"

    show city_A:
        linear 1.0 zoom 1.0

    show silver:
        linear 1.0 xpos 0.5

    red @talkingmouth "[prologue_scene_text[269]]"

    silver @closedbrow talkingmouth "[prologue_scene_text[270]]"
        
    red @confused "[prologue_scene_text[271]]"

    silver @surprisedbrow talkingmouth "[prologue_scene_text[272]]"
    
    red @happy "[prologue_scene_text[273]]"
    
    silver @closedbrow talkingmouth "[prologue_scene_text[274]]"
    extend @happy "[prologue_scene_text[275]]"
    silver @happymouth "[prologue_scene_text[276]]"
    
    show ragecandy at itemhover

    show silver:
        xcenter 0.5
        ease 1.0 xcenter 0.75
    
    $ renpy.music.set_volume(0.25, delay=0.0, channel="music")
    $ PlaySound("item_get.ogg")
    $ renpy.music.set_volume(1.0, delay=2.0, channel="music")
    
    pause 2.0

    red surprised "[prologue_scene_text[277]]"
        
    silver sadbrow @talkingmouth "[prologue_scene_text[278]]"
    
    red @talkingmouth "[prologue_scene_text[279]]"

    show ragecandy at itemhide

    show silver:
        xcenter 0.75
        ease 1.0 xcenter 0.5

    pause 1.0

    red happy "[prologue_scene_text[280]][first_name][prologue_scene_text[281]]"

    $ BecomeNamed("Silver")

    silver @talkingmouth "[prologue_scene_text[282]]"

    red -happy @talkingmouth "[prologue_scene_text[283]]"

    show silver closedbrow with dis:
        xpos 0.5
        ease 3.0 xpos 0.0
        
    show city_A:
        ease 3.0 zoom 2.0

    pause 3.0

    $ renpy.music.queue("Audio/Bus arrive1.ogg", channel='misc', loop=None, tight=None)
    $ renpy.music.queue("Audio/Bus arrive2.ogg", channel='misc', loop=True, tight=None)
    
    pause 2.0
    
    silver neutralbrow @talkingmouth "[prologue_scene_text[284]]"

    show city_A:
        linear 0.5 zoom 1.0

    show silver:
        linear 0.5 xpos 0.5

    red angryeyebrows angryeyes frownmouth @talkingmouth "[prologue_scene_text[285]]" 
    red happy "[prologue_scene_text[286]]"
    
    silver surprisedbrow @talkingmouth "[prologue_scene_text[287]]"
    
    red @talkingmouth "[prologue_scene_text[288]]"

    $ renpy.music.set_volume(0.25, delay=0.5, channel="music")
    $ renpy.music.stop(channel='misc', fadeout=1.5)
    
    show blank2 with splitfade
    $ renpy.music.play("Audio/Bus_stop.ogg", channel='misc', loop=None, fadein=0.0)
    
    $ renpy.pause(2.0, hard=True)
    
    show text "{color=#ffffff}.{/color}" as text1:
        alpha 1.0
        pause 0.5
        linear 0.0 alpha 0.0
    show text "{color=#ffffff}..{/color}" as text2:
        alpha 0.0
        pause 0.5
        block:
            linear 0.0 alpha 1.0
            pause 0.5
            linear 0.0 alpha 0.0
    show text "{color=#ffffff}...{/color}" as text3:
        alpha 0.0
        pause 1.0
        block:
            linear 0.0 alpha 1.0
            pause 1.5
            linear 1.0 alpha 0.0
    $ renpy.pause(4.0, hard=True)
    
    hide city_A
    show city_B behind blank2
    
    hide text
    hide text1
    hide text2
    hide text3
    
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")
    $ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd2', loop=True, fadein=0.5)
    
    hide blank2 with splitfade
    
    $ renpy.pause(1.5, hard=True)
    
    red @surprised "[prologue_scene_text[289]]"

    redmind @thinking "[prologue_scene_text[290]]"
    redmind @upeyes sweat frownmouth "[prologue_scene_text[291]]"

    red happy "[prologue_scene_text[292]]"

    show city_B with hpunch
    
    Character("[prologue_scene_text[293]]") "[prologue_scene_text[294]]"

    red @surprised "[prologue_scene_text[295]]"

    redmind @closedeyes frownmouth "[prologue_scene_text[296]]"

    show brawly uniform:
        xcenter 1.5
        ease 0.5 xcenter 0.5

    brawly happy @angrybrow happymouth "[prologue_scene_text[297]]"
    brawly @closedbrow talking2mouth -happy "[prologue_scene_text[298]]"
 
    red surprised "[prologue_scene_text[299]]"
    red -surprisedbrow -frownmouth -surprised @talking2mouth "[prologue_scene_text[300]]"

    $ BecomeNamed("Brawly")

    brawly -happy @happy "[prologue_scene_text[301]]"

    redmind closedeyes frownmouth "[prologue_scene_text[302]]"
    red surprised "[prologue_scene_text[303]]"
    brawly @surprised "[prologue_scene_text[304]]"
    red -surprisedbrow -frownmouth -surprised @talkingmouth "[prologue_scene_text[305]][first_name][prologue_scene_text[306]]"
    brawly @talkingmouth "[prologue_scene_text[307]][first_name][prologue_scene_text[308]]"
    red surprised "[prologue_scene_text[309]]"
    red happy "[prologue_scene_text[310]]"

    show blank2:
        alpha 0.0
        ease 2.0 alpha 1.0
    
    $ renpy.music.stop(channel='crowd', fadeout=1.5)
    $ renpy.music.stop(channel='crowd2', fadeout=1.5)
    
    $ renpy.pause(4.0, hard=True)
    
    show relichall_A:
        alpha 0.0
        ease 2.0 alpha 1.0
    
    $ renpy.pause(2.5, hard=True)

    hide brawly
    
    hide blank2

    show brawly uniform:
        xcenter 1.5 xzoom -1
        ease 0.5 xcenter 0.5

    brawly @surprisedbrow happymouth "[prologue_scene_text[311]]"
    red closedeyes @talking2mouth "[prologue_scene_text[312]]"
    brawly @happy "[prologue_scene_text[313]]"
    
    hide city_B
    
    show relichall_A:
        subpixel True
        zoom 1.0 xpos 0.0 ypos 0.0 alpha 1.0
        ease 6.0 zoom 1.14 xpos -0.14 ypos -0.04
    
    red surprised "[prologue_scene_text[314]]"
     
    red closedeyes happymouth happyeyebrows "[prologue_scene_text[315]]" 
    red -closedeyes -happymouth -happyeyebrows @talkingmouth "[prologue_scene_text[316]]"
    brawly @happy "[prologue_scene_text[317]]"

    show relichall_A with vpunch

    roxanne uniform @angry "[prologue_scene_text[318]]"
    brawly @closedbrow talking2mouth "[prologue_scene_text[319]]"
    
    show roxanne uniform:
        xcenter -0.5 xzoom -1
        ease 1.0 xcenter 0.33

    show brawly:
        xcenter 0.5
        ease 1.0 xcenter 0.66

    roxanne @angrybrow talking2mouth "[prologue_scene_text[320]]"
    brawly @sadbrow happymouth "[prologue_scene_text[321]]"
    roxanne @happybrow talkingmouth "[prologue_scene_text[322]]"
    brawly @sadbrow happymouth "[prologue_scene_text[323]]"
    
    show roxanne:
        xcenter 0.33
        ease 0.75 zoom 1.25 xcenter 0.33 ypos 1.1

    roxanne @talkingmouth "[prologue_scene_text[324]]"
    red @talkingmouth "[prologue_scene_text[325]][first_name][prologue_scene_text[326]]"

    menu: 
        "[prologue_scene_text[327]]":
            show brawly happy with dis
            red @talkingmouth "[prologue_scene_text[328]]"
            $ AddEvent("Brawly", "Covered")

            show roxanne:
                zoom 1.25 xcenter 0.33 ypos 1.1
                ease 0.5 xzoom -1 xcenter 0.33 ypos 1.1 

            roxanne @happy "[prologue_scene_text[329]]"

            show roxanne:
                xzoom -1 xcenter 0.33 ypos 1.1 
                ease 0.75 xzoom 1 xcenter 0.33 ypos 1.1

            roxanne @talkingmouth "[prologue_scene_text[330]]"

        "[prologue_scene_text[331]]":
            red @talkingmouth "[prologue_scene_text[332]]"
            roxanne @talkingmouth "[prologue_scene_text[333]]"

    $ BecomeNamed("Roxanne")
    roxanne @closedbrow talkingmouth "[prologue_scene_text[334]]"
    roxanne @happybrow sweat talking2mouth "[prologue_scene_text[335]]"

    red surprised "[prologue_scene_text[336]]"

    brawly @happy "[prologue_scene_text[337]][first_name][prologue_scene_text[338]]"

    show brawly:
        ease 1.0 xcenter -0.5

    show roxanne:
        zoom 1.25 ypos 1.1
        ease 1.0 xcenter -0.5

    red -surprisedbrow -frownmouth -surprised @talkingmouth "[prologue_scene_text[339]]"

    show relichall_A:
        ease 3.0 zoom 1.3

    pause 3.0

    show mace:
        alpha 0.0 xpos 0
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            ease 1.75 xpos 0.66

    show face:
        alpha 0.0 xpos 0
        pause 0.25
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            ease 1.5 xpos 0.33    
    
    mace @talkingmouth "[prologue_scene_text[340]]"
    
    show relichall_A:
        zoom 1.3
        ease 1.0 zoom 1.14 xpos -0.1 ypos -0.1
    
    red @talkingmouth "[prologue_scene_text[341]]"

    show face smile2mouth happyeyebrows with dis

    mace smilemouth happybrow @happy "[prologue_scene_text[342]]"
    
    face @happy "[prologue_scene_text[343]]"

    show face surprisedbrow frownmouth
    show mace surprisedbrow frownmouth
    with dis

    red @happy "[prologue_scene_text[344]]"
    
    show face surprisedbrow with dis
    
    mace surprisedbrow @surprisedbrow talkingmouth "[prologue_scene_text[345]]"
    
    red -happy @sweat talkingmouth "[prologue_scene_text[346]]"

    face -surprisedbrow -frownmouth -surprised smile2mouth sadbrow @happy "[prologue_scene_text[347]]"
    
    mace @closedbrow talkingmouth "[prologue_scene_text[348]]"
    
    show face sad
    show mace sad
    with dis
    
    red @happy "[prologue_scene_text[349]]"
    
    mace @sweat sadbrow sadmouth "[prologue_scene_text[350]]"
    
    red -happy @talkingmouth "[prologue_scene_text[351]]"
    
    face @angry "[prologue_scene_text[352]]"
    
    red @closedeyes sadmouth "[prologue_scene_text[353]]"
    red @happy sweat "[prologue_scene_text[354]]"
    
    mace angry -sweat "[ellipses]"

    
    face @closedbrow frownmouth "[ellipses]"

    
    show face sad with dis
    
    mace @sad "[prologue_scene_text[355]]"

    show mace sad:
        alpha 1.0 xpos 0.66
        parallel:
            pause 0.25
            ease 0.5 alpha 0.0
        parallel:
            ease 1.0 xpos 1.0

    show face sad:
        alpha 1.0 xpos 0.33
        parallel:
            pause 0.5
            ease 0.5 alpha 0.0
        parallel:
            ease 1.0 xpos 1.0
    
    pause 2.0

    stop music fadeout 3.5
    
    redmind sad "[prologue_scene_text[356]]"
    red @thinking "[ellipses]"

    redmind angrybrow frownmouth "[prologue_scene_text[357]]"

    queue music "Audio/Music/Show Me Around.ogg"
    
    show relichall_A:
        subpixel True
        zoom 1.14 xpos -0.1 ypos -0.1
        ease 3.0 zoom 1.25 ypos -200 xpos -320
    
    $ renpy.pause(1.8, hard=True)
    
    $ PlaySound("ExitBuilding.ogg")
    scene blank with dip_white

    jump day010402
