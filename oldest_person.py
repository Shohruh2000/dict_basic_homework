def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    kat = 0
    s = ""
    ls = len(people)
    for k,v in people.items():
        if v>kat:
            ket = v
            s = k
    return s
print(oldest({"Shohruh":22,"Suhrob":24,"Jaloliddin":25}))
    