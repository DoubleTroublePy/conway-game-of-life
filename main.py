from ConwayClass import ConwayClass

if __name__ == '__main__':

    cc = ConwayClass(9)
    cc.draw_grid()

    while True:
        cc.evolve()
        print('evolving')
        cc.update()