brillantor = 0
musica_alegre_sonant = False
musica_trist_sonant = False
temperatura = 0

def on_forever():
    global brillantor, musica_alegre_sonant, musica_trist_sonant
    brillantor = input.light_level()
    if brillantor > 200:
        if not (musica_alegre_sonant):
            music._play_default_background(music.built_in_playable_melody(Melodies.BIRTHDAY),
                music.PlaybackMode.IN_BACKGROUND)
            musica_alegre_sonant = True
            musica_trist_sonant = False
    elif musica_alegre_sonant:
        music.stop_all_sounds()
        musica_alegre_sonant = False
    if brillantor < 50:
        if not (musica_trist_sonant):
            music._play_default_background(music.built_in_playable_melody(Melodies.FUNERAL),
                music.PlaybackMode.IN_BACKGROUND)
            musica_trist_sonant = True
            musica_alegre_sonant = False
    elif musica_trist_sonant:
        music.stop_all_sounds()
        musica_trist_sonant = False
basic.forever(on_forever)

def on_forever2():
    global temperatura
    temperatura = input.temperature()
    if temperatura > 22:
        basic.show_string("Calor")
    else:
        basic.show_string("Fred")
basic.forever(on_forever2)
