import redis from 'redis';
const redisClient = redis.createClient();

redisClient.on("error", (error) => {
  if (error) console.log(`Redis client not connected to the server: ${error}`)
}).on('ready', () => {
  console.log('Redis client connected to the server');
});

redisClient.subscribe("holberton school channel");

redisClient.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    redisClient.unsubscribe(channel);
    process.exit(0);
  }
});
