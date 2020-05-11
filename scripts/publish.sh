#!/bin/sh

collection_path="$(ansible-galaxy collection build --force ./w3f/polkadot_validator |  awk '{print $6}')"
ansible-galaxy collection publish --api-key $ANSIBLE_GALAXY_TOKEN  ${collection_path}
