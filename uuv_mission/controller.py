class PDController:
    def __init__(self, kp: float, kd: float):
        self.kp = kp
        self.kd = kd
        self.previous_error = 0.0
    
    def controller_action(self, error: float):
        control_action = self.kp * error + self.kd * (error - self.previous_error)
        self.previous_error = error
        return control_action
        