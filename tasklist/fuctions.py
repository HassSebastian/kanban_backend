from django.contrib.auth.models import User
from django.http import JsonResponse


def get_all_members(request):
    """
    Retrieves information about all members and returns it in a JSON response.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing serialized information about all members.
    """
    members = User.objects.all()
    serialized_members = [
        {
            "user_id": member.id,
            "username": member.username,
            "email": member.email,
            "first_name": member.first_name,
            "last_name": member.last_name,
            "checked": False,
            "color": get_member_color(member),
            "initials": get_member_initials(member),
        }
        for member in members
    ]
    return JsonResponse(serialized_members, safe=False)


def get_member_color(member):
    """
    This function determines the color for a given member based on available information.

    Parameters:
    - member (dict): A dictionary representing a member with information such as first name, last name, and username.

    Returns:
    - str: A string representing the calculated color for the member, or an empty string if no color is determined.
    """
    if exist_first_and_last_name(member):
        return calculate_color_for_first_and_last_name(member)
    elif exist_username(member):
        return calculate_color_for_username(member)
    else:
        return ""


def calculate_color_for_first_and_last_name(member):
    """This function determines the color for a given member based on available information.

    Parameters:
    - member (dict): A dictionary representing a member with information such as first name, last name, and username.

    Returns:
    - str: A string representing the calculated color for the member, or an empty string if no color is determined.
    """
    ascii_first_letter = ord(member.first_name[0])
    ascii_second_letter = ord(member.last_name[0])
    sum = ascii_first_letter + ascii_second_letter
    color_index = sum % 7
    return color_index


def calculate_color_for_username(member):
    """
    This function determines the color for a given member based on available information.

    Parameters:
    - member (dict): A dictionary representing a member with information such as first name, last name, and username.

    Returns:
    - str: A string representing the calculated color for the member, or an empty string if no color is determined.
    """
    ascii_username_first_letter = ord(member.username[0])
    ascii_username_second_letter = ord(member.username[1])
    sum = ascii_username_first_letter + ascii_username_second_letter
    color_index = sum % 7
    return color_index


def get_member_initials(member):
    """
    Retrieves the initials of a member based on their first and last name or username.

    Args:
        member (object): The member object for which initials are to be retrieved.

    Returns:
        str: A string containing the initials. Returns an empty string if no initials are available.
    """
    if exist_first_and_last_name(member):
        return member.first_name[0] + member.last_name[0].upper()
    elif exist_username(member):
        return member.username[:2].upper()
    else:
        return ""


def exist_first_and_last_name(member):
    """
    Checks if a first_name and last_name exists for a given member.

    Args:
        member (object): The member object for which the first_name and last_name is to be checked.

    Returns:
        bool: True if a first_name and last_name exists, False otherwise.
    """
    return bool(member.first_name and member.last_name)


def exist_username(member):
    """
    Checks if a username exists for a given member.

    Args:
        member (object): The member object for which the username is to be checked.

    Returns:
        bool: True if a username exists, False otherwise.
    """
    return bool(member.username)
