#!/bin/bash
java -jar selenium-server-4.9.1.jar hub &
java -jar selenium-server-4.9.1.jar node --detect-drivers false --log-level "fine" --port 5555   --override-max-sessions true --max-threads 55 --driver-configuration display-name="$(hostname)" max-sessions=3 stereotype='{"browserName":"chrome"}' &
java -jar selenium-server-4.9.1.jar node --detect-drivers false --log-level "fine" --port 5556   --override-max-sessions true --max-threads 55 --driver-configuration display-name="$(hostname)" max-sessions=3 stereotype='{"browserName":"firefox"}' &
java -jar selenium-server-4.9.1.jar node --detect-drivers false --log-level "fine" --port 5557   --override-max-sessions true --max-threads 55 --driver-configuration display-name="$(hostname)" max-sessions=3 stereotype='{"browserName":"safari"}'