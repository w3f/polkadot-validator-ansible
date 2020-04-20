#!/bin/sh

collection_path="$(ansible-galaxy collection build --force ./w3f/polkadot_validator |  awk '{print $6}')"
ansible-galaxy collection publish ${collection_path}
