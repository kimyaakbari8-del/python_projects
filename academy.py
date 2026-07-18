class Academy:
    class Teachers:
        report = ""
        name = ""
        rate = 0

        def input_opinion():
            Academy.Teachers.report = input("Enter your report: ")
            Academy.Teachers.name = input("Enter the teacher's name: ")
            Academy.Teachers.rate = int(input("Enter your rate (1-10): "))

        def output_opinion():
            print(
                Academy.Teachers.name,
                Academy.Teachers.rate,
                Academy.Teachers.report
            )

        class Students:
            name = ""
            report = ""

            def input_bio():
                Academy.Teachers.Students.name = input("Enter the student's name: ")
                Academy.Teachers.Students.report = input("Enter the report: ")

            def output_bio():
                print(
                    Academy.Teachers.Students.name,
                    Academy.Teachers.Students.report
                )

            class Courses:
                course = ""

                def input_detail():
                    Academy.Teachers.Students.Courses.course = input(
                        "Enter which subject you are studying: "
                    )

                def output_detail():
                    print(Academy.Teachers.Students.Courses.course)

                class Finance:
                    cost = 0
                    opinion = ""

                    def input_fact():
                        Academy.Teachers.Students.Courses.Finance.cost = int(
                            input("Enter how much you spent for that subject: ")
                        )
                        Academy.Teachers.Students.Courses.Finance.opinion = input(
                            "Any opinion? "
                        )

                        if Academy.Teachers.Students.Courses.Finance.opinion.lower() == "no":
                            print("OK")

                    def output_fact():
                        print(
                            Academy.Teachers.Students.Courses.Finance.cost,
                            Academy.Teachers.Students.Courses.Finance.opinion
                        )

    class Education:
        idea = ""

        def input_idea():
            Academy.Education.idea = input(
                "Enter your idea to improve learning: "
            )

        def output_idea():
            print(Academy.Education.idea)


Academy.Teachers.input_opinion()
Academy.Teachers.output_opinion()

Academy.Teachers.Students.input_bio()
Academy.Teachers.Students.output_bio()

Academy.Teachers.Students.Courses.input_detail()
Academy.Teachers.Students.Courses.output_detail()

Academy.Teachers.Students.Courses.Finance.input_fact()
Academy.Teachers.Students.Courses.Finance.output_fact()

Academy.Education.input_idea()
Academy.Education.output_idea()