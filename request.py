def request_1(title_name):
    request = f"""
    select title,
    country,
    release_year,
    listed_in as genre,
    description
    from netflix 
    where title = '{title_name}' 
    order by release_year, date_added desc
    limit 1
    """
    return request


def request_2(year_1, year_2):
    if year_1 > year_2:
        year_to = year_1
        year_from = year_2
    else:
        year_to = year_2
        year_from = year_1

    request = f"""
    select title,
    release_year
    from netflix
    where release_year between {year_from} and {year_to}
    limit 100
    """
    return request


def request_3(rating_list):
    rating_for_search = f"'{rating_list[0]}'"
    for rating in rating_list[1:]:
        rating_for_search += f", '{rating}'"
    request = f"""
    select title,
    rating,
    description
    from netflix
    where rating in ({rating_for_search})
    """
    return request


def request_4(genre):
    request = f"""
    select title,
    description,
    listed_in
    from netflix
    where listed_in like '%{genre}%'
    order by release_year, date_added desc

    """
    return request


def request_5(actor_1, actor_2):
    request = f"""
    select title,
    `cast`
    from netflix
    where `cast` like '%{actor_1}%'
    and `cast` like '%{actor_2}%'
    """
    return request


def request_6(type_name, genre, year):
    request = f"""
    select title,
    description,
    listed_in
    from netflix
    where type = '{type_name}'
    and listed_in = '{genre}'
    and release_year = {year}
    """
    return request
