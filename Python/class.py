class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = []
    length_b = 0
    while length_b != length:
        for i in range(len(tickets)):
            # if source is none, that is where you start, destination becomes the beginning
            for j in range(len(route)):
                if tickets[i].source == 'NONE':
                    # we push the destination into our created array, and then loop to find when destination
                    route.append(tickets[i].destination)
                    length_b += 1

                elif tickets[i].source == route[j]:
                    route.append(tickets[i].destination)
                    i += 1
                    j += 1
                    length += 1
                elif tickets[i].destination == 'NONE' and length_b == length:
                    route.append(tickets[i].destination)
                    return route
                else:
                    i += 1

    return route
