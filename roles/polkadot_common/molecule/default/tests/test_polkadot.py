def test_polkadot_user(host):
    user = host.user('polkadot')
    assert user.exists

    group = host.group('polkadot')
    assert group.exists

    assert user.gid == group.gid


def test_polkadot_binary(host):
    binary = host.file('/usr/local/bin/polkadot')
    assert binary.exists
    assert binary.user == 'polkadot'
    assert binary.group == 'polkadot'
    assert binary.mode == 0o700
