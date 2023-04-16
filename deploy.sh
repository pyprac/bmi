#!/bin/bash

if [[ $CREATE_SUPERUSER ]];
then
  python demo-crm/manage.py createsuperuser --no-input
fi