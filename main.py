def on_forever():
    basic.show_leds("""
        . . . . .
                . # # # .
                # # # # #
                . # # # .
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_icon(IconNames.SAD)
    basic.show_icon(IconNames.ANGRY)
    basic.show_string("DASH!, I'M HUNGRY.")
basic.forever(on_forever)
