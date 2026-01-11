class OnlineCourse:
    pass
    def __init__(self, name, description, weeks):
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days):
        weeks = (days + 6) // 7
        return weeks

    @classmethod
    def from_dict(cls, course_dict):
        w = OnlineCourse()


