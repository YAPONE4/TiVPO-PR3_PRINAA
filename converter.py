def convert(value, from_unit, to_unit):
    conversions = {
        ('inches', 'cm'): 2.54,
        ('miles', 'km'): 1.60934,
        ('arshins', 'meters'): 0.7112
    }
    return value * conversions[(from_unit, to_unit)]