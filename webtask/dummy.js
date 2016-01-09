var redis = require('redis');
var util = require('util');

module.exports = function (ctx, done) {
  console.log(util.inspect(ctx, {showHidden: false, depth: null}))

  r = redis.createClient(9950, 'ray.redistogo.com', {no_ready_check: true});
  r.auth('ctx.data.secrets.REDIS_PASS');


  r.hset('h-watchlist', ctx.data.title, ctx.data.time);
  r.quit()

  done(null, 1);

};
