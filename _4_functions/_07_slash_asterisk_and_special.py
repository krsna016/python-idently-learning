def example_func(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    # pos1 and pos2 are positional-only parameters
    # pos_or_kwd can be passed either by position or keyword
    # kwd1 and kwd2 are keyword-only parameters
    pass  # / is used to indicate positional-only parameters

# * is used to indicate keyword-only parameters
# ** is used to collect keyword arguments into a dictionary
