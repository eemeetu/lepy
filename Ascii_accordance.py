with open("input.txt", 'r') as file:
    data = file.readlines()

# Использование функции зависит от понимания задания, некоторые переменные вводятся для потенциала масштабирования
def analytica(dataset):
    stripped = []
    for line in data:
        stripped.append(line.rstrip('\n'))

    info1 = stripped[0].split()
    x1 = int(info1[0])
    y1 = int(info1[1])
    info2 = stripped[x1+1].split()
    x2 = int(info2[0])
    y2 = int(info2[1])

    image1 = []
    image2 = []
    for i in range(x1):
        image1.append(list(stripped[i+1]))
    for i in range(x1+1, x1+x2+1):
        image2.append(list(stripped[i+1]))

    image1right = []
    for l in range(y1):
        newline = []
        for p in range(x1-1, -1, -1):
            newline.append(image1[p][l])
        image1right.append(newline)
    img1r = []
    for line in image1right:
        img1r.append(''.join(line))
    img1r = '\n'.join(img1r)

    image1left = []
    for l in range(y1):
        newline = []
        for p in range(x1):
            newline.append(image1[p][l])
        image1left.append(newline)
    img1l = []
    for line in image1left:
        img1l.append(''.join(line))
    img1l = '\n'.join(img1l)

    image1ud = []
    for l in range(x1-1, -1, -1):
        newline = []
        for p in range(y1-1, -1, -1):
            newline.append(image1[l][p])
        image1ud.append(newline)
    img1ud = []
    for line in image1ud:
        img1ud.append(''.join(line))
    img1ud = '\n'.join(img1ud)

    if image1left == image2 or image1right == image2 or image1ud == image2:
        result = 'Yes'
    else:
        result = 'No'

    print (result)
    return result

analytica(data)