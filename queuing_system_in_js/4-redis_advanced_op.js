import redis from 'redis';
const redisClient = redis.createClient();

redisClient.on("error", (error) => {
  if (error) console.log(`Redis client not connected to the server: ${error}`)
}).on('ready', () => {
  console.log('Redis client connected to the server');
});

const name = 'HolbertonSchools';
const values = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2
}

for (const [key, val] of Object.entries(values)) {
  redisClient.hset(name, key, val, (error, reply) =>
    redis.print((`Reply: ${reply}`))
  );
}

redisClient.hgetall(name, (error, object) => console.log(object));
