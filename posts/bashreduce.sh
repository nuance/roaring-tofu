#!/bin/bash

MAPPER=$1
REDUCER=$2
shift
shift

echo "Map-Reduce in bash: $MAPPER => sort => $REDUCER"

echo $(cat $* | $MAPPER | sort | $REDUCER)
