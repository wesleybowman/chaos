import numpy as np
import matplotlib.pyplot as plt

def f(x, r):
    """Discrete logistic equation with parameter r"""
    return r*x*(1-x)

if __name__ == '__main__':
    # initial condition for x
    ys = []
    rs = np.linspace(0, 4, 400)
    #rs = [1+ 2*np.sqrt(2)]

    # Loop through `rs`. `r` is assigned the values in `rs` one at a time.
    for r in rs:
        x = 0.1
        # Repeat this loop 500 times.
        # i is just a dummy variable since it is not used inside the for-loop.
        for i in range(500):
            # Evaluate f at (x, r). The return value is assigned to x.
            # x is then fed back into f(x, r).
            # This makes x jump around 500 times according to the logistic equation.
            # r remains fixed.
            x = f(x, r)

        # Do this 50 times
        for i in range(50):
            # Again make the x jump around according to the logistic equation
            x = f(x, r)
            # Save the point (r, x) in the list ys
            ys.append([r, x])

    # ys is a list of lists.
    # You can also think of ys as a list of [r, x] point.
    # This converts the list of lists into a 2D numpy array.
    ys = np.array(ys)

    # ys[:,0] is a 1D array of r values
    # ys[:, 1] is a 1D array of x values
    # This draws a scatter plot of (r, x) points.
    plt.plot(ys[:,0], ys[:,1], '.')
    plt.show()


    dataF = np.abs(np.fft.fftshift(np.fft.fft(ys[:,1])))
    #dataF = np.abs((np.fft.fft(ys[:,1])))

    plt.semilogy(ys[:,0],dataF)
    plt.show()

