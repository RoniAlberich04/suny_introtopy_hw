from tkinter import Tk, Canvas
import random

class BouncingBall:
    def __init__(self):
        self.window = Tk() 
        self.window.title("BOUNCING BALL GAME")
        
        self.lives = 5
        self.score = 0
        
        self.canvas = Canvas(self.window, width=600, height=400, bg="grey")
        self.canvas.pack()
        
        self.score_text = self.canvas.create_text(50, 20, text=f"Score: {self.score}", fill="white", font=("Arial", 14))
        self.lives_text = self.canvas.create_text(550, 20, text=f"Lives: {self.lives}", fill="white", font=("Arial", 14))
        
        self.ball = self.canvas.create_oval(50, 50, 100, 100, fill="red", outline="darkred")
        self.dx = 3
        self.dy = 2
        
        self.paddle = self.canvas.create_rectangle(250, 380, 350, 400, fill="blue", outline="darkblue")
        self.paddle_speed = 8
        
        self.paddle_collisions = 0
        
        self.window.bind("<Left>", self.move_left)
        self.window.bind("<Right>", self.move_right)
        self.window.focus_set()  
        
        # Start animation
        self.animate()
        
        self.window.mainloop()
    
    def reset_ball(self):
        
        x1 = random.randint(50, 550)
        y1 = random.randint(50, 150)
        self.canvas.coords(self.ball, x1, y1, x1+50, y1+50)
        
        self.dx = random.choice([-3, 3])
        self.dy = 2
    
    def animate(self):
        pos_ball = self.canvas.coords(self.ball) 
        pos_paddle = self.canvas.coords(self.paddle)
        
        
        if pos_ball[3] >= 400:
            self.lives -= 1
            self.canvas.itemconfig(self.lives_text, text=f"Lives: {self.lives}")
            
            if self.lives <= 0:
                self.game_over()
                return
            else:
                self.reset_ball()
        
        if (pos_ball[2] >= pos_paddle[0] and pos_ball[0] <= pos_paddle[2] and 
            pos_ball[3] >= pos_paddle[1] and pos_ball[3] <= pos_paddle[3]):
            self.dy = -abs(self.dy)  
            self.score += 1
            self.paddle_collisions += 1
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
            
            if self.paddle_collisions % 4 == 0:
                self.dx *= 1.2
                self.dy *= 1.2
        
        if pos_ball[0] <= 0 or pos_ball[2] >= 600:
            self.dx = -self.dx 
        if pos_ball[1] <= 0:
            self.dy = -self.dy 
        
        
        self.canvas.move(self.ball, self.dx, self.dy) 
        
        self.window.after(30, self.animate)
    
    def move_left(self, event):
        position = self.canvas.coords(self.paddle)
        if position[0] > 0:
            self.canvas.move(self.paddle, -self.paddle_speed, 0)
    
    def move_right(self, event):
        position = self.canvas.coords(self.paddle)
        if position[2] < 600:
            self.canvas.move(self.paddle, self.paddle_speed, 0)
    
    def game_over(self):
        self.canvas.create_text(300, 200, text="GAME OVER", fill="red", font=("Arial", 30))
        self.canvas.create_text(300, 250, text=f"Final Score: {self.score}", fill="white", font=("Arial", 20))

if __name__ == "__main__":
    game = BouncingBall()