def value(colors):
    resistor_colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    return (resistor_colors.index(colors[0]) * 10) + resistor_colors.index(colors[1])
