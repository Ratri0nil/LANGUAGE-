#!/bin/bash

read -p " enter server address : " server_adrs
#ping server till count of 4 or wait 5 seconds if not found
ping -c4 -w5 $server_adrs