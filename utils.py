def triangle_area(p1, p2, p3):
    """
    Calculate the triangle area given from 3 points
    :param p1:
    :param p2:
    :param p3:
    :return:
    """
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)


def triangle_collide(point, tp_1, tp_2, tp_3):
    """
    Check if a point is inside/collide the triangle(given by 3 points)
    :param point: node's coordinates
    :param tp_1: triangle point 1
    :param tp_2: triangle point 2
    :param tp_3: triangle point 3
    :return:
    """
    # calculate triangles ' area
    area = triangle_area(tp_1, tp_2, tp_3)
    a1 = triangle_area(tp_1, tp_2, point)
    a2 = triangle_area(tp_2, tp_3, point)
    a3 = triangle_area(tp_1, tp_3, point)
    if a1 + a2 + a3 == area:
        return True
    return False
