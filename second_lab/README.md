# University Management System (UMS) - Laboratory Work 2

This repository contains the source code and documentation for a University Management System (UMS) created as part of the Object-Oriented Programming (OOP) course at the Technical University of Moldova, under the guidance of Professor Dominic Flocea.

## Table of Contents

1. [Introduction](#introduction)
2. [Files and Directory Structure](#files-and-directory-structure)
3. [Contributors](#contributors)

## Introduction

The University Management System (UMS) is a Python-based application that provides a framework for managing faculties, students, and study fields within a university. It facilitates the storage and manipulation of data related to the university's administrative and academic activities.

## Files and Directory Structure

- `faculty.py`: Contains the `Faculty` class, which defines the attributes and methods for managing faculty information, including name, abbreviation, and study field.

- `file_management.py`: Provides utility functions for uploading and downloading information within the system.

- `main.py`: The main entry point of the application. It orchestrates the interactions with the `tum_system` module.

- `student.py`: Contains the `Student` class, which represents student data, including first name, last name, email, enrollment date, graduation date, and birth date.

- `study_field.py`: Lists the possible available study fields at the university.

- `tools.py`: Includes various utility functions that can be helpful throughout the application.

- `tum_structure.py`: Defines the necessary functions for making changes to university, faculty, and student objects.

- `tum_system.py`: Manages communication through multiple functions and structures, serving as the core of the University Management System.

- `university.py`: Contains the `University` class, which represents the overall university object.

- `memory/`: A folder that stores JSON files with different versions of university and faculty data.

- `bash_scripts/`: Includes Bash scripts for running and using the entire application.

## Contributors

 - Eduard Balamatiuc
 - Dominic Flocea (Course Instructor)