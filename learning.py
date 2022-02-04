import arcade

screen_width=700
screen_hight=700

class Button:
    def __init__(self, point_x, point_y, width, hight, color):
        self.point_x= point_x
        self.point_y= point_y
        self.width= width
        self.hight=hight
        self.color=color

    def draw(self):
        arcade.draw_rectangle_filled(self.point_x, self.point_y, self.width, self.hight, self.color)

class Spin:
    def __init__(self, spin_x, spin_y, width, hight, tilte, tilte_change, color):
        self.spin_x= spin_x
        self.spin_y= spin_y
        self.width= width
        self.hight=hight
        self.color=color
        self.tilte= tilte
        self.tilte_change= tilte_change
    
    def draw(self):
        arcade.draw_rectangle_filled(self.spin_x, self.spin_y, self.width, self.hight, self.color, self.tilte)
        #self.spin_x, self.spin_y, self.width, self.hight, self.tilte, self.color

    def update(self):
        self.tilte += self.tilte_change


class My_window(arcade.Window):
    
    def __init__(self, screen_width, screen_hight, title):
       super().__init__(screen_width, screen_hight, title)
       arcade.set_background_color(arcade.color.ASH_GREY)

       self.button= Button(350,350, 100, 50, arcade.color.WHITE)
       self.spin = Spin(550, 500, 10, 50, 10, 5, arcade.color.AMERICAN_ROSE)
       #550, 500, 10, 50, arcade.color.AMERICAN_ROSE, 5, 50

    
    def on_draw(self):
        arcade.start_render()
        self.button.draw()
        self.spin.draw()

    def update(self, delta_time):
        self.set_update_rate(1 / 20)
        self.spin.update()

    def on_mouse_press(self, x, y, button, modifiers):
    # Called when the user presses a mouse button.

        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse button pressed at", x, y)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right mouse button pressed at", x, y)


def main():
    window = My_window(700, 700, "Recall")

    arcade.run()


main()