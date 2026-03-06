from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name: str = name
        self.description: str = description
        self.weeks: int = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days + 6) // 7

    @classmethod
    def from_dict(
        cls, course_dict: dict[str, int | str]
    ) -> OnlineCourse:
        name: str = course_dict["name"]  # type: ignore[assignment]
        description: str = (
            course_dict["description"]  # type: ignore[assignment]
        )
        days: int = course_dict["days"]  # type: ignore[assignment]
        weeks: int = cls.days_to_weeks(days)  # type: ignore[arg-type]sadsadas

        return cls(name=name, description=description, weeks=weeks)