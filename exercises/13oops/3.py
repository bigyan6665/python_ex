class Employee:
    def __init__(self, name, dob, age, salary, skill_sets):
        self.name = name
        self.dob = dob
        self.age = age
        self.salary = salary
        self.skill_sets = skill_sets


class Developer(Employee):
    def __init__(
        self, name, dob, age, salary, skill_sets, github_profile, is_fullstack
    ):
        super().__init__(name, dob, age, salary, skill_sets)
        self.github_profile = github_profile
        self.is_fullstack = is_fullstack

    def display_profile(self):
        print(
            f"{self.name} has skills : {",".join(self.skill_sets)}. Git profile: {self.github_profile}"
        )


class HR(Employee):
    def __init__(self, name, dob, age, salary, skill_sets, is_manager, onboard_rate):
        super().__init__(name, dob, age, salary, skill_sets)
        self.is_manager = is_manager
        self.onboard_rate = onboard_rate

    def display_profile(self):
        print(
            f"{self.name} has skills : {",".join(self.skill_sets)}. Onboard rate: {self.onboard_rate}"
        )


ram = Developer(
    name="ram",
    dob="2040/06/29",
    age=34,
    salary=100000,
    skill_sets=["java", "github"],
    github_profile="xyz",
    is_fullstack=True,
)
hari = Developer(
    name="hari",
    dob="2045/08/13",
    age=34,
    salary=150000,
    skill_sets=["python", "github", "js"],
    github_profile="abc",
    is_fullstack=True,
)
shyam = Developer(
    name="shyam",
    dob="2048/12/0830",
    age=34,
    salary=160000,
    skill_sets=["js", "github"],
    github_profile="pqr",
    is_fullstack=False,
)
bigyan = Developer(
    name="bigyan",
    dob="2049/12/29",
    age=34,
    salary=140000,
    skill_sets=["php", "github", "js"],
    github_profile="ABC",
    is_fullstack=True,
)
dinesh = Developer(
    name="dinesh",
    dob="2042/04/25",
    age=34,
    salary=180000,
    skill_sets=["java", "github"],
    github_profile="XYZ",
    is_fullstack=False,
)

prajal = HR(
    name="prajal",
    dob="2050/11/15",
    age=34,
    salary=200000,
    skill_sets=["java", "github"],
    is_manager=True,
    onboard_rate=20,
)
sandesh = HR(
    name="sandesh",
    dob="2034/01/05",
    age=34,
    salary=250000,
    skill_sets=["java", "github"],
    is_manager=False,
    onboard_rate=40,
)


employees = [ram, hari, shyam, bigyan, dinesh, prajal, sandesh]
for emp in employees:
    if "python" in emp.skill_sets and "github" in emp.skill_sets:
        emp.display_profile()
