"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    return convert_coordinate(get_coordinate(azara_record)) == get_coordinate(rui_record)


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """

    if compare_records(azara_record, rui_record):
        return azara_record + rui_record

    return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """

    # combined_record_group = list(combined_record_group)

    final = ""

    # fail
    """
    for access in range(0, len(combined_record_group)):
        final = final + (
                str(combined_record_group[access][0]) + "', " +
                str(combined_record_group[access][2]) + "', " +
                str(combined_record_group[access][3]) + "', " +
                str(combined_record_group[access][4]) + "'\n"
        )
        
    """
    # fail

    combined_record_group = [list(x) for x in combined_record_group]

    for goin in range(len(combined_record_group)):
        del combined_record_group[goin][1]
        #combined_record_group[goin].append("\n")

    #fail
    """
    # combined_record_group = [str(x) for x in combined_record_group]

    for access in range(len(combined_record_group)):
        final = final + "('"
        for scribe in combined_record_group[access]:
            final = final + f"{scribe}, "
            #if not(combined_record_group[access][0]):
            #    final = final + ", "
        final = final + "')\n"
    """
    #fail

    return final


