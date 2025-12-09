let temperatura = 0
let brillantor = 0
let musica_alegre_sonant = false
let musica_trist_sonant = false
basic.forever(function () {
    temperatura = input.temperature()
    if (temperatura > 22) {
        basic.showString("Calor")
    } else {
        basic.showString("Fred")
    }
})
basic.forever(function () {
    brillantor = input.lightLevel()
    if (brillantor > 200) {
        if (!(musica_alegre_sonant)) {
            music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Birthday), music.PlaybackMode.InBackground)
            musica_alegre_sonant = true
            musica_trist_sonant = false
        }
    } else if (musica_alegre_sonant) {
        music.stopAllSounds()
        musica_alegre_sonant = false
    }
    if (brillantor < 50) {
        if (!(musica_trist_sonant)) {
            music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Funeral), music.PlaybackMode.InBackground)
            musica_trist_sonant = true
            musica_alegre_sonant = false
        }
    } else if (musica_trist_sonant) {
        music.stopAllSounds()
        musica_trist_sonant = false
    }
})
