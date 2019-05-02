def limit_color(color):
    for index, c in enumerate(color):
        c = max(min(c,255),0)
        color[index] = c
    return color

print(limit_color([500,-1,200]))
