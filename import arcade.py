import arcade





class MyGame(arcade.Window):
    """ My window class. """

    def __init__(self, width, height, title):
        """ Constructor. """

        # Call the parent class's init function
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)


    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()


def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()