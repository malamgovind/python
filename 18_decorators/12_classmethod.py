class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()

# Global Memory
# ────────────────────────

# Student
#    │
#    ▼
# <class Student>
#       │
#       ├── school = "ABC School"
#       │
#       └── show_school


# Local Memory (show_school)
# ────────────────────────

# cls
#  │
#  ▼
# Student
#  │
#  ▼
# <class Student>
#       │
#       └── school = "ABC School"
