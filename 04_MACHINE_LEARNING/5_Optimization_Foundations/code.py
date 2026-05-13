"""Chapter 4.5: Small optimization foundations demos for machine learning.

This chapter demonstrates gradient descent, which is fundamental to
training neural networks in the next section.

We establish the optimization patterns that will be reused in
neural network training.
"""


def objective(theta):
    return (theta - 3) ** 2


def gradient(theta):
    return 2 * (theta - 3)


def gradient_descent(start, learning_rate, steps):
    theta = start
    history = []
    for step in range(steps):
        loss = objective(theta)
        history.append((step, theta, loss))
        theta = theta - learning_rate * gradient(theta)
    history.append((steps, theta, objective(theta)))
    return history


def run_demo():
    print("Optimization foundations demo\n")

    for learning_rate in [0.05, 0.2, 1.1]:
        print(f"learning rate = {learning_rate}")
        history = gradient_descent(start=0.0, learning_rate=learning_rate, steps=6)
        for step, theta, loss in history:
            print(
                "step",
                step,
                "theta=",
                round(theta, 4),
                "loss=",
                round(loss, 4),
            )
        print()


if __name__ == "__main__":
    run_demo()
