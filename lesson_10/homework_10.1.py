class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, department, name, salary):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, programming_language, name, salary):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, team_size, programming_language, department, name, salary):
        Manager.__init__(self, department, name, salary)
        Developer.__init__(self, programming_language, name, salary)
        self.team_size = team_size


team_lead = TeamLead(
    name="Dara",
    salary=100500,
    department="IT",
    programming_language="Python",
    team_size=1,
)
print(
    team_lead.name,
    team_lead.salary,
    team_lead.department,
    team_lead.programming_language,
    team_lead.team_size,
)
