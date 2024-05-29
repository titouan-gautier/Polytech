#!/bin/bash

# Vérifie si un nombre d'arguments correct est fourni
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <nombre_de_machines>"
    exit 1
fi

# Nombre de machines à lancer
NUM_MACHINES=$1

# Chemin de l'exécutable
EXECUTABLE="./ring_network"

# Vérifie si l'exécutable existe
if [ ! -f "$EXECUTABLE" ]; then
  echo "L'exécutable $EXECUTABLE n'existe pas. Assurez-vous de l'avoir compilé."
  exit 1
fi

# Port de base
BASE_PORT=5000

# Lancement des instances dans des terminaux séparés
for (( i=1; i<NUM_MACHINES; i++ ))
do
  PORT=$((BASE_PORT + i))
  NEXT_PORT=$((BASE_PORT + (i + 1) % NUM_MACHINES))
  gnome-terminal -- bash -c "$EXECUTABLE $i $PORT $NEXT_PORT $NUM_MACHINES; exec bash"
done

gnome-terminal -- bash -c "$EXECUTABLE 0 5000 5001 £NUM_MACHINES; exec bash"

echo "Instances lancées dans des terminaux séparés."

