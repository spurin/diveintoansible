#!/usr/bin/python3

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: icmp

short_description: simple module for icmp ping

version_added: "2.10"

description:
    - "simple module for icmp ping"

options:
    target:
        description:
            - The target to ping
        required: true

author:
    - James Spurin (@spurin)
'''

EXAMPLES = '''
# Ping an IP
- name: Ping an IP
  icmp:
    target: 127.0.0.1

# Ping a host
- name: Ping a host
  icmp:
    target: centos1
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    # define the available arguments/parameters that a user can pass to
    # the module
    module_args = dict(
        target=dict(type='str', required=True)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        return result

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    ping_result = module.run_command('ping -c 1 {}'.format(module.params['target']))

    # use whatever logic you need to determine whether or not this module
    # made any modifications to your target
    if module.params['target']:
        result['debug'] = ping_result
        result['rc'] = ping_result[0]
        if result['rc']:
          result['failed'] = True
          module.fail_json(msg='failed to ping', **result)
        else:
          result['changed'] = True
          module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
