import json

class SimpleRIP:
    def __init__(self):
        self.routing_table = {}

    def update_route(self, destination, next_hop, metric):
        if destination not in self.routing_table or metric < self.routing_table[destination]['metric']:
            self.routing_table[destination] = {'next_hop': next_hop, 'metric': metric}

    def send_update(self):
        return json.dumps(self.routing_table)

    def receive_update(self, update):
        received_routes = json.loads(update)
        for dest, info in received_routes.items():
            self.update_route(dest, info['next_hop'], info['metric'] + 1)

router1 = SimpleRIP()
router2 = SimpleRIP()

router1.update_route('192.168.1.0', '192.168.1.1', 0)
update = router1.send_update()
router2.receive_update(update)

print(router2.routing_table)