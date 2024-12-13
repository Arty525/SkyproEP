def filter_by_state(list_of_dict: list = [], state: str = "EXECUTED") -> list:
    """
    :param list_of_dict: входной список словарей;
    :param state: параметр, по которому фильтруется список;
    :return: Возвращается отфильтрованный по параметру state и отсортированный по дате по убыванию список словарей;
    """
    filtered_list_of_dict = []  # отфильтрованный список
    for dictionary in list_of_dict:  # фильтрация списка по параметру state
        if dictionary["state"] == state:
            filtered_list_of_dict.append(dictionary)
    return sorted(filtered_list_of_dict, key=lambda _dict: _dict["date"], reverse=True)
