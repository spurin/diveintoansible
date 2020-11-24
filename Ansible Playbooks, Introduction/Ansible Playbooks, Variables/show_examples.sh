for i in 01 02 03 04 05; do clear;
  cd $i
  pwd
  more variables_playbook.yaml
  read
  echo ansible-playbook variables_playbook.yaml
  ansible-playbook variables_playbook.yaml
  read
  cd ..
done

for i in 06; do clear;
  cd $i
  pwd
  echo
  echo external_vars.yaml file contents -
  more external_vars.yaml
  read
  clear
  echo variables_playbook.yaml file contents -
  more variables_playbook.yaml
  read
  echo ansible-playbook variables_playbook.yaml
  ansible-playbook variables_playbook.yaml
  read
  cd ..
done

for i in 07 08 09 10 11 12 13 14 15; do clear;
  cd $i
  pwd
  more variables_playbook.yaml
  read
  echo ansible-playbook variables_playbook.yaml
  ansible-playbook variables_playbook.yaml
  read
  cd ..
done

for i in 16; do clear;
  cd $i
  pwd
  echo
  echo using extra vars in ini format
  echo
  read
  echo ansible-playbook variables_playbook.yaml -e 'extra_vars_key="extra vars value"'
  ansible-playbook variables_playbook.yaml -e 'extra_vars_key="extra vars value"'
  read
  clear

  pwd
  echo
  echo using extra vars in json format
  echo
  read
  echo ansible-playbook variables_playbook.yaml -e '{"extra_vars_key": "extra vars value"}'
  ansible-playbook variables_playbook.yaml -e '{"extra_vars_key": "extra vars value"}'
  read
  clear

  pwd
  echo
  echo using extra vars in yaml format
  echo
  read
  echo ansible-playbook variables_playbook.yaml -e '{extra_vars_key: extra vars value}'
  ansible-playbook variables_playbook.yaml -e '{extra_vars_key: extra vars value}'
  read
  clear

  cd ..

for i in 17; do clear;
  cd $i
  pwd
  echo
  echo passing variables as a yaml file
  echo
  read
  echo ansible-playbook variables_playbook.yaml -e @extra_vars_file.yaml
  ansible-playbook variables_playbook.yaml -e @extra_vars_file.yaml
  read
  clear

  pwd
  echo
  echo using extra vars as a json file
  echo
  read
  echo ansible-playbook variables_playbook.yaml -e @extra_vars_file.json
  ansible-playbook variables_playbook.yaml -e @extra_vars_file.json
  read
  clear
done
done
