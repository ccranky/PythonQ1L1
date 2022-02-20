from time import sleep

class TrafficLight:
    color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 5}
    def __init__(self, in_state = 1):
        if in_state in TrafficLight.color:
            self.state = in_state
            self.time = TrafficLight.color[in_state]
        else:
            self.state = 'Красный'
            self.time = TrafficLight.color[self.state]
    def next_state(self):
        if self.state == 'Красный':
            self.state = 'Желтый'
        elif self.state == 'Желтый':
            self.state = 'Зеленый'
        else:
            self.state = 'Красный'
    def running(self):
        while True:
            print(self.state)
            sleep(TrafficLight.color[self.state])
            self.next_state()

a = TrafficLight('Красный')
a.running()


