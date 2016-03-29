from expyriment import stimuli
class Timer:
    def __init__(self, time):
        #Settings feedback Balken
        self.midpoint = -180  # Mittelpunkt Balken
        self.height = 100  # Hoehe vom Balken
        self.color_max = 255  # Max Wert RGB-Farbe
        self.max_time = time

    def countdown_buttonpress(self, exp, button):

        boarder = stimuli.Rectangle([22, self.height + 2], [self.color_max, self.color_max, self.color_max],
                                    position=[0, self.midpoint])
        pressed_buttons = list()
        time_presentation = list()

        i = 0
        t_begin = exp._clock.time

        while exp._clock.time < t_begin + self.max_time:

            msec_passed = exp._clock.time - t_begin

            percent_max_time = float(msec_passed) / float(self.max_time)

            bar = stimuli.Rectangle([20, self.height - (percent_max_time * self.height)],
                                    colour=[255 * percent_max_time, 255 - (255 *  percent_max_time), 0],
                                    position=[0, self.midpoint - (percent_max_time * (self.height / 2))])

            boarder.present(clear=False, update=False)
            bar.present(clear=False, update=True)

            pressed_buttons.append(exp.keyboard.check())

            time_presentation.append(msec_passed)

            if button in pressed_buttons:
                return button, msec_passed
                break

            i += 1

        return self.max_time , button