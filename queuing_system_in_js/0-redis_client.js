'use strict';
import redis from 'redis';
const redisClient = redis.createClient();

redisClient.on("error", (error) => {
  if (error) console.log(`Redis client not connected to the server: ${error}`)
}).on('ready', () => {
  console.log('Redis client connected to the server');
});
