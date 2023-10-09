from file_management import File_management_system


def get_available_structure_versions(
    list_of_available_files: list,
) -> tuple:
    """Gets the available structure versions from the list of available files.

    Args:
        list_of_available_files (list): The list of available files.

    Returns:
        tuple: A tuple containing the output text and the list of available files.
    """
    output_text = ""
    for index, file in enumerate(list_of_available_files):
        output_text += f"{index}. {file}\n"
    return output_text, list_of_available_files
