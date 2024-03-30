import pandas
import turtle

screen = turtle.Screen()
screen.title("state guess game")
image = "/Users/nishantkumarchauhan/python/panda_project/stt.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("/Users/nishantkumarchauhan/python/panda_project/usstates.csv")
all_states = data.state.to_list()
guess_state = []
while len(guess_state) < 50:
  answer = screen.textinput(title=f" { len(guess_state)}/50 states correct ",prompt="choose your state").title() 
  print(answer)
  if answer == "Exit":
    missing_states = [state for state in all_states if state not in guess_state]
    # for state in all_states:
    #   if state not in guess_state:
    #     missing_states.append(state)
    data_frame = pandas.DataFrame(missing_states)
    data_frame.to_csv("miss.csv")
    break  
  if answer in all_states:
    guess_state.append(answer)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer]
    t.goto(int(state_data.x),int(state_data.y)) 
    t.write(state_data.state.item())
screen.exitonclick()