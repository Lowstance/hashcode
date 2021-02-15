
file_name = 'hashcode2018/a_example'


class car:
    def __init__(self):
        self.routes = []
        self.x = 0
        self.y = 0
        self.t = 0

def parser():
    file1 = open(file_name+'.in', 'r')
    data = file1.readlines()
    first_line = data[0][:-1].split(" ")
    other_lines = [i[:-1].split(" ") for i in data[1:]]
    coordinates = [[[int(i[0]), int(i[1])],[int(i[2]), int(i[3])],int(i[4]), int(i[5])] for i in other_lines]
    #print(coordinates)
    file1.close()
    return coordinates, int(first_line[2])

def calc_distance(start, end):
    return abs(end[0]-start[0])+abs(end[1]-start[1])


def move(current_car, route): 
    current_car.t += calc_distance([current_car.x, current_car.y], route[0])
    current_car.x = route[0][0]
    current_car.y = route[0][1]

    if current_car.t < route[2]:
        current_car.t = route[2]

    #calculate from start to finish    
    current_car.t += calc_distance(route[0], route[1])
    current_car.x = route[1][0]
    current_car.y = route[1][1]


def findRoute(cars, route):
    min_distance = calc_distance([cars[0].x, cars[0].y], route[0])
    best_car = []
    for current_car in cars:
        distance_start = calc_distance([current_car.x, current_car.y], route[0])
        distance_end = calc_distance(route[0], route[1])
        if distance_start+distance_end+current_car.t > route[3]:
            continue
        if calc_distance([current_car.x, current_car.y], route[0])<=min_distance:
            best_car = current_car
            min_distance = calc_distance([current_car.x, current_car.y], route[0])

    return best_car


def dothejob(cars, routes, indexes):
    for i in range(len(routes)):
        car1 = findRoute(cars, routes[i])
        if not car1:
            continue
        move(car1, routes[i])
        car1.routes.append(indexes[i])
   
def sort_routes(mixed_routes):
    routes = []
    for element in enumerate(mixed_routes):
        routes.append(list(element))

    routes.sort(key=lambda x: x[:][1][2])
    print(routes)
    return routes

if __name__ == '__main__':
    mixed_routes, num_cars = parser()
    routes = sort_routes(mixed_routes)
    car_list = []
    for i in range(num_cars):
        car_list.append(car())

    dothejob(car_list,[i[1] for i in routes], [i[0] for i in routes])
    for i in car_list:
        print(f"x={i.x}, y={i.y}, in time {i.t}")
        print(i.routes)

