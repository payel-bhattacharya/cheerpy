import random

class CheerPy:
    def __init__(self):
        self.success_messages = [
            "Great job! 🎉 Keep it up!",
            "Success! You're on fire! 🔥",
            "Well done! You've nailed it! 🚀",
            "Pipeline passed! High-five! 🙌",
            "You’re a coding rockstar! 🌟"
        ]
        
        self.failure_messages = [
            "Don't worry, failure is part of the journey! 💪",
            "Oops! Let's fix this and get back on track! 🔧",
            "Keep going, success is just around the corner! 🚀",
            "Take a break, you’ve got this! ☕",
            "Remember, even the best fall down sometimes! 🌱"
        ]
    
    def random_success_message(self):
        return random.choice(self.success_messages)

    def random_failure_message(self):
        return random.choice(self.failure_messages)
    
    def add_custom_success_message(self, message):
        self.success_messages.append(message)
    
    def add_custom_failure_message(self, message):
        self.failure_messages.append(message)
    
    def cheer(self, status="success"):
        if status == "success":
            return self.random_success_message()
        elif status == "fail":
            return self.random_failure_message()
        else:
            return "Unknown status. Please use 'success' or 'fail'."