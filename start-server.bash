#!/bin/bash

if [[ -z "${HOST}" ]]; then
  HOST="0.0.0.0"
fi

if [[ -z "${PORT}" ]]; then
  PORT="8000"
fi

uvicorn --host "${HOST}" main:app --port "${PORT}"