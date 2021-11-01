m = open("emotions.txt", "w")
def httperror(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case :
            return "Something's wrong with the internet"