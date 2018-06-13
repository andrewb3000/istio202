# istio202

## grpc-weather server
```
docker run -d -p 9000:9000 \
  -e OPEN_WEATHER_MAP_API_KEY="a998bb724d70364542952d297b951cdf" \
  -e WEATHER_UNDERGROUND_API_KEY="0dd5caf56d01bb7b" \
  --name weather_service caiofilipini/grpc-weather:master
```

