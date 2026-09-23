def label(colors):
    resistor_colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    ohms = ((resistor_colors.index(colors[0]) * 10) + resistor_colors.index(colors[1])) * (10 ** resistor_colors.index(colors[2]))
    if ohms != 0 and ohms % 1000000000 == 0:
        return f"{ohms // 1000000000} gigaohms"
    if ohms != 0 and ohms % 1000000 == 0:
        return f"{ohms // 1000000} megaohms"
    if ohms != 0 and ohms % 1000 == 0:
        return f"{ohms // 1000} kiloohms"
    return f"{ohms} ohms"