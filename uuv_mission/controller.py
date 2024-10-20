class PDController:
    def __init__(self, kp: float, kd: float): #initialize the controller with kp and kd
        self.kp = kp
        self.kd = kd
        self.previous_error = 0.0 #initialize previous error to 0
    
    def controller_action(self, error: float): #calculate the control action
        control_action = self.kp * error + self.kd * (error - self.previous_error)
        self.previous_error = error
        return control_action
        