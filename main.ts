basic.forever(function () {
    basic.showLeds(`
        . . . . .
        . # # # .
        # # # # #
        . # # # .
        . . # . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showIcon(IconNames.Sad)
    basic.showIcon(IconNames.Angry)
    basic.showString("DASH!, I'M HUNGRY.")
})
