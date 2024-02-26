from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import ipaddress

app = Flask(__name__)
CORS(app)

class InventoryApp:
    def __init__(self):
        pass

    def generate_inventory(self, master_ips, worker_ips):
        inventory_content = "[masters]\n"
        inventory_content += "\n".join([f"master-{i} ansible_host={ip} rke2_type=server" for i, ip in enumerate(master_ips, 1)])

        if worker_ips:
            inventory_content += "\n\n[workers]\n"
            inventory_content += "\n".join([f"worker-{i} ansible_host={ip} rke2_type=agent" for i, ip in enumerate(worker_ips, 1)])

        inventory_content += "\n\n[k8s_cluster:children]\n"
        inventory_content += "masters\nworkers"

        return inventory_content

    def create_dynamic_inventory(self, master_ips, worker_ips):
        try:
            inventory_content = self.generate_inventory(master_ips, worker_ips)
            with open('/tmp/dynamic_inventory.ini', 'w') as inventory_file:
                inventory_file.write(inventory_content)
        except Exception as e:
            abort(500, jsonify({'status': 'error', 'message': f'Error creating dynamic inventory: {str(e)}'}))

    def validate_ip_addresses(self, ips):
        if not ips:
            return []
        try:
            return [str(ipaddress.ip_address(ip)) for ip in ips]
        except ValueError as e:
            abort(400, jsonify({'status': 'error', 'message': f'Invalid IP address Format: {str(e)}'}))

inventory_app = InventoryApp()

@app.route('/api/dynamic-inventory/create', methods=['POST'])
def create_dynamic_inventory_api():
    master_ips = request.json.get('master_ips', None)
    worker_ips = request.json.get('worker_ips', [])

    if not master_ips:
        return jsonify({'status': 'error', 'message': 'Master IPs are required'}), 400

    try:
        master_ips = inventory_app.validate_ip_addresses(master_ips)
        worker_ips = inventory_app.validate_ip_addresses(worker_ips)
    except ValueError as e:
        return jsonify({'status': 'error', 'message': f'Invalid IP address Format: {str(e)}'}), 400

    inventory_app.create_dynamic_inventory(master_ips, worker_ips)

    return jsonify({'status': 'success', 'message': 'Dynamic inventory created successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', use_reloader=False)
