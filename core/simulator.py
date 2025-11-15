import math
import matplotlib.pyplot as plt
from matplotlib import animation
from .topic import TopicManager
from .messages import Twist
from IPython.display import HTML

class MiniRosSimulator:
    def __init__(self, dt=0.05):
        self.dt = dt
        self.time = 0.0
        self.nodes = []
        self.robots = []
        self.topics = TopicManager()

        self.xlim = (-5, 5)
        self.ylim = (-5, 5)

    def add_node(self, node):
        node._attach_sim(self)
        self.nodes.append(node)

    def add_robot(self, robot):
        self.robots.append(robot)

    def step(self):
        # 1. Node computations
        for node in self.nodes:
            node.step(self.dt)

        # 2. Apply commands
        for robot in self.robots:
            cmd = self.topics.read(robot.cmd_topic)
            if cmd is None: 
                cmd = Twist(0, 0)
            robot.update(self.dt, cmd)

        self.time += self.dt

    def run(self, duration):
        steps = int(duration / self.dt)
        for _ in range(steps):
            self.step()

    def animate(self, interval_ms=50, tail_length=200):
        if not self.robots:
            raise RuntimeError("No robots to animate.")

        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.set_xlim(self.xlim)
        ax.set_ylim(self.ylim)
        ax.set_xlabel("x [m]")
        ax.set_ylabel("y [m]")

        patches_robot = []
        patches_traj = []

        for r in self.robots:
            body, = ax.plot([], [], 'o', markersize=r.radius * 50)
            traj, = ax.plot([], [], '-')
            patches_robot.append(body)
            patches_traj.append(traj)

        def init():
            for b, t in zip(patches_robot, patches_traj):
                b.set_data([], [])
                t.set_data([], [])
            return patches_robot + patches_traj

        def update(frame):
            self.step()

            for i, r in enumerate(self.robots):
                patches_robot[i].set_data([r.pose.x], [r.pose.y])
                x_data = list(r.traj_x[-tail_length:])
                y_data = list(r.traj_y[-tail_length:])

                patches_traj[i].set_data(x_data, y_data)

            return patches_robot + patches_traj

        ani = animation.FuncAnimation(
            fig, update, init_func=init,
            interval=interval_ms, blit=True,
            cache_frame_data=False
        )

        plt.close(fig)   # Important so Colab doesn't show an empty static figure
        ani.save("animation.gif", writer="pillow", fps=20)
        return HTML(ani.to_jshtml())
