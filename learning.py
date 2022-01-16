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
    

class My_window(arcade.Window):
    
    def __init__(self, screen_width, screen_hight, title):
       super().__init__(screen_width, screen_hight, title)
       arcade.set_background_color(arcade.color.ASH_GREY)

       self.button= Button(350,350, 100, 50, arcade.color.WHITE)

    
    def on_draw(self):
        arcade.start_render()
        self.button.draw()

    def update(self, delta_time):
        pass



def main():
    window = My_window(700, 700, "Recall")

    arcade.run()


main()