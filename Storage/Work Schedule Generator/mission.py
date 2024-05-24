def schedule_generator(staff: dict, business_needs: list) -> list[list[str]]:
    # your code here
    return [[], []]


print("Example:")
print(
    schedule_generator(
        {
            "Charlie": {
                "pref_shifts": ["first", "second"],
                "days_off": ["Wednesday"],
                "skills": ["customer service", "inventory", "cleaning", "sales"],
            },
            "Alice": {
                "pref_shifts": ["second"],
                "days_off": ["Saturday", "Sunday"],
                "skills": ["customer service", "sales"],
            },
            "Bob": {
                "pref_shifts": ["first"],
                "days_off": ["Monday", "Tuesday"],
                "skills": ["customer service", "inventory"],
            },
        },
        ["Monday", 1, ["customer service", "sales"]],
    )
)

# These "asserts" are used for self-checking
assert schedule_generator(
    {
        "Charlie": {
            "pref_shifts": ["first", "second"],
            "days_off": ["Wednesday"],
            "skills": ["customer service", "inventory", "cleaning", "sales"],
        },
        "Alice": {
            "pref_shifts": ["second"],
            "days_off": ["Saturday", "Sunday"],
            "skills": ["customer service", "sales"],
        },
        "Bob": {
            "pref_shifts": ["first"],
            "days_off": ["Monday", "Tuesday"],
            "skills": ["customer service", "inventory"],
        },
    },
    ["Monday", 1, ["customer service", "sales"]],
) == [[], ["Alice"]]
assert schedule_generator(
    {
        "Charlie": {
            "pref_shifts": ["first", "second"],
            "days_off": ["Wednesday"],
            "skills": ["customer service", "inventory", "cleaning", "sales"],
        },
        "Alice": {
            "pref_shifts": ["second"],
            "days_off": ["Saturday", "Sunday"],
            "skills": ["customer service", "sales"],
        },
        "Bob": {
            "pref_shifts": ["first"],
            "days_off": ["Monday", "Tuesday"],
            "skills": ["customer service", "inventory"],
        },
    },
    ["Monday", 2, ["customer service", "sales"]],
) == [["Charlie"], ["Alice"]]
assert schedule_generator(
    {
        "Charlie": {
            "pref_shifts": ["first", "second"],
            "days_off": ["Wednesday"],
            "skills": ["customer service", "inventory", "cleaning", "sales"],
        },
        "Alice": {
            "pref_shifts": ["second"],
            "days_off": ["Saturday", "Sunday"],
            "skills": ["customer service", "sales"],
        },
        "Bob": {
            "pref_shifts": ["first"],
            "days_off": ["Monday", "Tuesday"],
            "skills": ["customer service", "inventory"],
        },
    },
    ["Wednesday", 1, ["customer service", "sales", "inventory"]],
) == [[], []]

print("The mission is done! Click 'Check Solution' to earn rewards!")
