from file_management import File_management_system as fms
from tum_structure import Tum_structure
import tools as ts
import logging

# Configure the logging system
logging.basicConfig(filename="app.log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


class Tum_system:
    """A class representing the TUM student management system."""

    def __init__(self):
        """Initializes a new instance of the Tum_system class."""
        self.tum_structures = []
        self.current_structure = None
        self.available_memory_files = []
        self.running_state = True
        print("Welcome to the TUM student management system, process initialization started")
        logging.info("Initialized TUM system")

    def initialize_tum_system_structure(self):
        """Initializes the TUM system structure."""
        while self.running_state:
            logging.info("Start intialization step")
            print("Select and type in the number of the option from below: ")
            print("    0. Use previous structure")
            print("    1. Create a new structure")
            print("    2. Exit")
            initialization_option = input()

            if initialization_option == "0":
                logging.info("Option 0. Use previous structure was selected")
                output_text, self.available_memory_files = ts.get_available_structure_versions(
                    fms.get_available_files()
                )
                if not output_text:
                    logging.info("Missing files to select from")
                    print("There are no available files, please create a new structure")
                else:
                    print("Below are provided the available systems.")
                    logging.info(f"File propsed for selection {output_text}")
                    print(output_text)
                    print("Please type in the number of the system from the list that you would like to continue with")
                    selected_version = input()
                    logging.info(f"The selected option was {selected_version}")
                    self.current_structure = Tum_structure(
                        selected_file=self.available_memory_files[int(selected_version)],
                    )
                    self.start_tum_system_interaction()

            elif initialization_option == "1":
                logging.info("Option 1. Create a new structure was selected")
                self.current_structure = Tum_structure()
                self.start_tum_system_interaction()

            elif initialization_option == "2":
                logging.info("Option 2. Exit was selected")
                self.stop_tum_system_interaction()

            else:
                logging.info("Invalid option was selected")
                print("Invalid option, please try again and use one of the provided options in the description")

    def check_system_validations(self):
        """Checks if the system is valid."""
        if not self.current_structure:
            logging.info("No structure was initialized")
            print("No structure is initialized, return to initialization process")
            return False
        else:
            logging.info("Structure was initialized, continuing the process further")
            return True

    def start_tum_system_interaction(self):
        """Starts the interaction with the TUM system.
        This function displays a menu of actions that the user can perform and handles the selected action.
        """
        start_tum_system_interaction_state = True
        while start_tum_system_interaction_state:
            if self.check_system_validations():
                logging.info("General menu option provided")
                print("Select the type of action you would like to perform:")
                print("    0. Student actions")
                print("    1. Faculty actions")
                print("    2. University actions")
                print("    3. Save current structure")
                print("    4. Back")
                print("    5. Exit")
                print("    6. Batch actions")
                action_type = input()
                if action_type == "0":
                    logging.info("Option 0. Student actions was selected")
                    self.student_actions()
                elif action_type == "1":
                    logging.info("Option 1. Faculty actions was selected")
                    self.faculty_actions()
                elif action_type == "2":
                    logging.info("Option 2. University actions was selected")
                    self.university_actions()
                elif action_type == "3":
                    logging.info("Option 3. Save current structure was selected")
                    self.save_current_structure()
                elif action_type == "4":
                    logging.info("Option 4. Back was selected")
                    start_tum_system_interaction_state = False
                elif action_type == "5":
                    logging.info("Option 5. Exit was selected")
                    self.stop_tum_system_interaction()
                    start_tum_system_interaction_state = False
                    self.running_state = False
                elif action_type == "6":
                    logging.info("Option 6. Batch actions was selected")
                    self.batch_actions()
                else:
                    logging.info("Invalid option was selected")
                    print("Invalid option, please try again and use one of the provided options in the description")

    def stop_tum_system_interaction(self):
        """Stops the interaction with the TUM system.
        This function asks the user if they want to save the current structure and terminates the process accordingly.
        """
        logging.info("Initializes tum_system stopping process")
        if self.current_structure:
            print("Do you want to save the current structure?")
            print("    0. Yes")
            print("    1. No")
            save_option = input()
            if save_option == "0":
                logging.info("Option of saving current structure was selected")
                self.save_current_structure()
            else:
                logging.info("Option of not saving the current structure was selected")
                print("The current structure will not be saved")
        print("Thank you for using the TUM student management system, process terminated")

    def faculty_actions(self):
        """Handles faculty-specific actions within the TUM system.
        This function displays a menu of faculty actions that the user can perform and handles the selected action.
        """
        faculty_actions_state = True
        while faculty_actions_state:
            if self.check_system_validations():
                logging.info("General faculty action options menu provided")
                print("Select the type of faculty action you would like to perform:")
                print("    0. Add a student")
                print("    1. Graduate a student")
                print("    2. Display enrolled students")
                print("    3. Display graduated students")
                print("    4. Display all students")
                print("    5. Check student belonging")
                print("    6. Back")
                action_type = input()
                if action_type == "0":
                    logging.info("Option 0. Add a student was selected")
                    self.system_add_student()
                elif action_type == "1":
                    logging.info("Option 1. Graduate a student was selected")
                    self.system_graduate_student()
                elif action_type == "2":
                    logging.info("Option 2. Display enrolled students was selected")
                    self.system_display_enrolled_students()
                elif action_type == "3":
                    logging.info("Option 3. Display graduated students was selected")
                    self.system_display_graduated_students()
                elif action_type == "4":
                    logging.info("Option 4. Display all students was selected")
                    self.system_display_all_students()
                elif action_type == "5":
                    logging.info("Option 5. Check student belonging was selected")
                    self.system_check_student_information()
                elif action_type == "6":
                    logging.info("Option 6. Back was selected")
                    faculty_actions_state = False
                else:
                    logging.info("Invalid option was selected")
                    print("Invalid option, please try again and use one of the provided options in the description")

    def university_actions(self):
        """Handles university-specific actions within the TUM system.
        This function displays a menu of university actions that the user can perform and handles the selected action.
        """
        university_actions_state = True
        while university_actions_state:
            if self.check_system_validations():
                logging.info("General university action options menu provided")
                print("Select the type of university action you would like to perform:")
                print("    0. Add a faculty")
                print("    1. Display all faculties")
                print("    2. Display faculties by field")
                print("    3. Search for a faculty by student")
                print("    4. Update faculty information")
                print("    5. Back")
                action_type = input()
                if action_type == "0":
                    logging.info("Option 0. Add a faculty was selected")
                    self.system_add_faculty()
                elif action_type == "1":
                    logging.info("Option 1. Display all faculties was selected")
                    self.system_display_all_faculties()
                elif action_type == "2":
                    logging.info("Option 2. Display faculties by field was selected")
                    self.system_display_faculties_by_field()
                elif action_type == "3":
                    logging.info("Option 3. Search for a faculty by student was selected")
                    self.system_search_faculty_by_student()
                elif action_type == "4":
                    logging.info("Option 4. Update faculty information was selected")
                    self.system_update_faculty_information()
                elif action_type == "5":
                    logging.info("Option 5. Back was selected")
                    university_actions_state = False
                else:
                    logging.info("Invalid option was selected")
                    print("Invalid option, please try again and use one of the provided options in the description")

    def student_actions(self):
        """Handles student-specific actions within the TUM system.
        This function displays a menu of student actions that the user can perform and handles the selected action.
        """
        student_actions_state = True
        while student_actions_state:
            if self.check_system_validations():
                logging.info("General student action options menu provided")
                print("Select the type of student action you would like to perform:")
                print("    0. Update student information")
                print("    1. Back")
                action_type = input()
                if action_type == "0":
                    logging.info("Option 0. Update student information was selected")
                    self.system_update_student_information()
                elif action_type == "1":
                    logging.info("Option 1. Back was selected")
                    student_actions_state = False
                else:
                    logging.info("Invalid option was selected")
                    print("Invalid option, please try again and use one of the provided options in the description")

    def batch_actions(self):
        """Handles batch-specific actins within the TUM system"""
        batch_actions_state = True
        while batch_actions_state:
            if self.check_system_validations():
                logging.info("General batch action options menu provided")
                print("Select the type of batch action you would like to perform:")
                print("    0. Graduate student")
                print("    1. Enroll students")
                print("    2. Back")
                batch_action = input()
                if batch_action == "0":
                    logging.info("Option 0. Graduate student was selected")
                    self.system_graduate_student_txt()
                elif batch_action == "1":
                    logging.info("Option 1. Enroll students")
                    self.system_enroll_student_txt()
                elif batch_action == "2":
                    logging.info("Option 2. Back")
                    batch_actions_state = False
                else:
                    logging.info("Invalid option was selected")
                    print("Invalid option, please try again and use one of the provided options in the description")

    def system_graduate_student_txt(self):
        """Graduates a student from the current structure."""
        print("Provide the file name from which to read the information")
        graduation_file_txt = input()
        self.current_structure.graduate_from_txt(graduation_file_txt)

    def system_enroll_student_txt(self):
        """Enrolls a student to the current structure."""
        print("Provide the file name from which to read the information")
        enrollment_file_txt = input()
        self.current_structure.enroll_from_txt(enrollment_file_txt)

    def save_current_structure(self):
        """Saves the current structure to a file.
        If there is no current structure initialized, it prompts the user to initialize a structure first.
        """
        if self.current_structure:
            logging.info(f"Current structure state was saved to {self.current_structure.selected_file}")
            fms.save_structure_file(
                self.current_structure.selected_file,
                self.current_structure.university.to_dict(),
            )
        else:
            print("No structure is initialized, please initialize a structure first")

    def system_add_student(self):
        """Adds a student to the current structure."""
        if self.check_system_validations():
            logging.info("Student addition process initialized")
            print("Please type in the student information in the following format:")
            print(
                "    <faculty_id>, ",
                "<student_first_name>, ",
                "<student_last_name>, ",
                "<student_email>, ",
                "<student_enrollment_date>, ",
                "<student_graduation_status>, ",
                "<student_birth_date>",
            )
            student_information = input()
            logging.info(f"Student data provided {student_information}")
            self.current_structure.add_student(student_information)

    def system_graduate_student(self):
        """Graduates a student from the current structure."""
        logging.info("Start graduation process")
        if self.check_system_validations():
            print("Please type in the student id of the student you would like to graduate")
            student_id = input()
            logging.info(f"Student id selected for graduation {student_id}")
            self.current_structure.graduate_student(student_id)

    def system_display_enrolled_students(self):
        """Displays the enrolled students from the current structure."""
        logging.info("Start enrolled students display process")
        if self.check_system_validations():
            print("Below are provided the enrolled students:")
            self.current_structure.display_enrolled_students()

    def system_display_graduated_students(self):
        """Displays the graduated students from the current structure."""
        logging.info("Started graduated students display process")
        if self.check_system_validations():
            print("Below are provided the graduated students:")
            self.current_structure.display_graduated_students()

    def system_check_student_information(self):
        """Checks the student information from the current structure."""
        logging.info("Started student information check process")
        if self.check_system_validations():
            print("Please type in the student id of the student you would like to check")
            student_id = input()
            logging.info(f"Student id selected of information check {student_id}")
            print(self.current_structure.check_student_information(student_id))

    def system_display_all_students(self):
        """Displays all the students from the current structure."""
        logging.info("Started all students display process")
        if self.check_system_validations():
            print("Below are provided all the students:")
            self.current_structure.display_all_students()

    def system_add_faculty(self):
        """Adds a faculty to the current structure."""
        logging.info("Started faculty addition process")
        if self.check_system_validations():
            print("Please type in the faculty information in the following format:")
            print(
                "    <faculty_name>, ",
                "<faculty_abbreviation>, ",
                "<faculty_field>",
            )
            faculty_information = input()
            logging.info(f"Faculty information provided {faculty_information}")
            self.current_structure.add_faculty(faculty_information)

    def system_display_all_faculties(self):
        """Displays all the faculties from the current structure."""
        logging.info("Started all faculties display process")
        if self.check_system_validations():
            print("Below are provided all the faculties:")
            self.current_structure.display_all_faculties()

    def system_display_faculties_by_field(self):
        """Displays the faculties by field from the current structure."""
        logging.info("Started faculties by field display process")
        if self.check_system_validations():
            print("Please type in the field of the faculties you would like to display")
            field = input()
            logging.info(f"Field provided for faculties by field display {field}")
            self.current_structure.display_faculties_by_field(field)

    def system_search_faculty_by_student(self):
        """Searches a faculty by student from the current structure."""
        logging.info("Started faculty search by student process")
        if self.check_system_validations():
            print("Please type in the student id of the student you would like to search for")
            student_id = input()
            logging.info(f"Student id provided for faculty search by student {student_id}")
            self.current_structure.search_faculty_by_student(student_id)

    def system_update_faculty_information(self):
        """Updates the faculty information from the current structure."""
        logging.info("Started faculty information update process")
        system_update_faculty_information_state = True
        while system_update_faculty_information_state:
            if self.check_system_validations():
                logging.info("Provided available faculties to modify")
                print("Please type in the faculty name of the faculty you would like to update")
                print("Available faculties are:")
                self.current_structure.display_all_faculties()
                faculty_id = input()
                logging.info(f"Faculty with id {faculty_id} was selected")
                print(self.current_structure.check_faculty_information(faculty_id))
                print("Select the information you would like to update:")
                print("    0. Faculty name")
                print("    1. Faculty abbreviation")
                print("    2. Faculty field")
                print("    3. Back")
                logging.info("Possible faculty information updates menu provided")
                information_type = input()
                if information_type == "0":
                    logging.info("Option 0. Faculty name was selected")
                    print("Please type in the new faculty name")
                    faculty_name = input()
                    self.current_structure.update_faculty_name(faculty_id, faculty_name)
                elif information_type == "1":
                    logging.info("Option 1. Faculty abbreviation was selected")
                    print("Please type in the new faculty abbreviation")
                    faculty_abbreviation = input()
                    self.current_structure.update_faculty_abbreviation(faculty_id, faculty_abbreviation)
                elif information_type == "2":
                    logging.info("Option 2. Faculty field was selected")
                    print("Please type in the new faculty field")
                    faculty_field = input()
                    self.current_structure.update_faculty_field(faculty_id, faculty_field)
                elif information_type == "3":
                    logging.info("Option 3. Back was selected")
                    system_update_faculty_information_state = False
                else:
                    logging.info("Invalid option selected")
                    print("Invalid option, please try again and use one of the provided options in the description")

    def system_update_student_information(self):
        """Updates the student information from the current structure."""
        logging.info("Started student information update process")
        system_update_student_information_state = False
        while system_update_student_information_state:
            if self.check_system_validations():
                logging.info("Provided available students to modify")
                print("Please type in the student id of the student you would like to update")
                student_id = input()
                logging.info(f"Student id provided for update {student_id}")
                print(self.current_structure.check_student_information(student_id))
                print("Select the information you would like to update:")
                print("    0. Student first name")
                print("    1. Student last name")
                print("    2. Student email")
                print("    3. Student enrollment date")
                print("    4. Student graduation status")
                print("    5. Student birth date")
                print("    6. Back")
                logging.info("Possible student information updates menu provided")
                information_type = input()
                logging.info(f"Option selected {information_type}")
                if information_type == "0":
                    logging.info("Option 0. Student first name was selected")
                    print("Please type in the new student first name")
                    student_first_name = input()
                    logging.info(f"Student first name provided {student_first_name}")
                    self.current_structure.update_student_first_name(student_id, student_first_name)
                elif information_type == "1":
                    logging.info("Option 1. Student last name was selected")
                    print("Please type in the new student last name")
                    student_last_name = input()
                    logging.info(f"Student last name provided {student_last_name}")
                    self.current_structure.update_student_last_name(student_id, student_last_name)
                elif information_type == "2":
                    logging.info("Option 2. Student email was selected")
                    print("Please type in the new student email")
                    student_email = input()
                    logging.info(f"Student email provided {student_email}")
                    self.current_structure.update_student_email(student_id, student_email)
                elif information_type == "3":
                    logging.info("Option 3. Student enrollment date was selected")
                    print("Please type in the new student enrollment date")
                    student_enrollment_date = input()
                    logging.info(f"Student enrollment date provided {student_enrollment_date}")
                    self.current_structure.update_student_enrollment_date(student_id, student_enrollment_date)
                elif information_type == "4":
                    logging.info("Option 4. Student graduation status was selected")
                    print("Please type in the new student graduation status")
                    student_graduation_status = input()
                    logging.info(f"Student graduation status provided {student_graduation_status}")
                    self.current_structure.update_student_graduation_status(student_id, student_graduation_status)
                elif information_type == "5":
                    logging.info("Option 5. Student birth date was selected")
                    print("Please type in the new student birth date")
                    student_birth_date = input()
                    logging.info(f"Student birth date provided {student_birth_date}")
                    self.current_structure.update_student_birth_date(student_id, student_birth_date)
                elif information_type == "6":
                    logging.info("Option 6. Back was selected")
                    system_update_student_information_state = False
                else:
                    logging.info("Invalid option was selected")
                    print("Invalid option, please try again and use one of the provided options in the description")
