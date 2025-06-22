import turtle

def draw_tree(t, branch_len, rec_level):
    if rec_level == 0:
        return
    
    if rec_level > 0:
        t.forward(branch_len)
        t.left(45)
        draw_tree(t, 0.7 * branch_len, rec_level - 1)
        t.right(90)
        draw_tree(t, 0.7 * branch_len, rec_level - 1)
        t.left(45)
        t.backward(branch_len)

def main(rec_level):
    screen = turtle.Screen()
    
    t = turtle.Turtle()
    t.speed(0)

    t.left(90)
    t.penup()
    t.goto(0, -screen.window_height() // 2 + 20)
    t.pendown()

    draw_tree(t, 100, rec_level)

    screen.mainloop()

if __name__ == "__main__":
    try: 
        level = int(input('Enter recursion level: '))
        if level <=0:
            print('Recursion level should be greater than 0.')
        else:
            main(level)
    except ValueError:
        print('Invalid input. Please, enter the number for the recursion level of thr tree.')