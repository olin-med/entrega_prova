import rclpy
from rclpy.node import Node
import inquirer
from inquirer.themes import GreenPassion


def cli(q):
    q = [
        inquirer.Text("Comando", message="Envie um comando de movimentação no formato (vx vy vtheta tempo_em_ms):", default="0.0 0.0 0.0 1000"),
    ]

    inquirer.prompt(q, theme=GreenPassion())



def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('movement_publisher')
    client = node.create_client(cli, 'publisher')

    req = cli.Request()
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('service not available, waiting again...')

    future = client.call_async(req)
    rclpy.spin_until_future_complete(node, future)

    result = future.result()
    node.get_logger().info(
        'Input: %s' %
        (req))

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()