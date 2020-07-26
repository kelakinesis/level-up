class Employee:
    def __init__(self, first_name, last_name, start_date, department, title, is_currently_employeed):
        self.first_name = first_name
        self.last_name = last_name
        self.start_date = start_date
        self.department = department
        self.title = title
        self.is_currently_employeed = is_currently_employeed
    
    def is_captain(self):
        if self.title == "Captain":
            return True
        else:
            return False