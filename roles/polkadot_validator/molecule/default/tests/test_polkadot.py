def test_polkadot_service_file(host):
    if host.ansible.get_variables()['inventory_hostname'] == 'validator':
        svc = host.file('/etc/systemd/system/polkadot.service')
        assert svc.exists
        assert svc.user == 'root'
        assert svc.group == 'root'
        assert svc.mode == 0o600
        assert svc.contains('Restart=always')


def test_polkadot_running_and_enabled(host):
    if host.ansible.get_variables()['inventory_hostname'] == 'validator':
        polkadot = host.service("polkadot.service")
        assert polkadot.is_running
        # assert polkadot.is_enabled
