def bold_text(func):
    def wrapper(report):
        return "**" + func(report) + "**"
    return wrapper

class Report:

    templates = {}

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def add_template(cls, name, template):
        cls.templates[name] = template

    @classmethod
    def get_template(cls, name):
        return cls.templates[name]

    def __call__(self, name):
        return Report.get_template(name)(self)

    def __str__(self):
        return self.title + "\n" + self.content


def simple_template(report):
    return report.title + "\n" + report.content


@bold_text
def fancy_template(report):
    return report.title + "\n" + report.content


def main():

    Report.add_template("simple", simple_template)
    Report.add_template("fancy", fancy_template)

    report = Report("Monthly Report", "Sales increased by 20%.")
    
    with open("ReportOutput.txt", "w") as file:
        file.write("Simple Report:\n")
        file.write(report("simple"))
        file.write("\n\n")

        file.write("Fancy Report:\n")
        file.write(report("fancy"))
        file.write("\n\n")

        file.write("Default Report:\n")
        file.write(str(report))

    print("Report saved successfully in ReportOutput.txt")


if __name__ == "__main__":
    main()