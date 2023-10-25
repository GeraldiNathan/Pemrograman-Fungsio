data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

def curried_converter(weeks):
    def inner_curried(days):
        def inner_inner_curried(hours):
            def final_curried(minutes):
                return [weeks, days, hours, minutes]
            return final_curried
        return inner_inner_curried
    return inner_curried

int_values = []
for item in data:
    parts = item.split()
    weeks = int(parts[0])
    days = int(parts[2])
    hours = int(parts[4])
    minutes = int(parts[6])
    # For check detail of weeks, day etc.
    # print(weeks)
    # print(days)

    converted_value = curried_converter(weeks)(days)(hours)(minutes)
    int_values.append(converted_value)

# Data integer with filter dan currying
def is_integer_list(lst):
    return all(isinstance(item, int) for item in lst)

filtered_int_values = list(filter(is_integer_list, int_values))

print(filtered_int_values)
