import json


def test_swarm_active(host):
    # Test if Docker Swarm is active
    cmd = host.run("docker info")
    assert "Swarm: active" in cmd.stdout
    assert "NodeID:" in cmd.stdout
    assert "Is Manager: true" in cmd.stdout


def test_swarm_network_exists_and_is_overlay(host):
    result = host.run("docker network inspect swarm_network --format '{{json .}}'")
    assert result.rc == 0, "Network swarm_network does not exist"

    network = json.loads(result.stdout)
    assert network["Name"] == "swarm_network"
    assert network["Driver"] == "overlay"
