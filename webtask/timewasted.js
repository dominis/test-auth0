var redis = require('redis');
var util = require('util');

module.exports = function (ctx, done) {
  function add(a, b) {
    return parseInt(a) + parseInt(b);
  }

  console.log(util.inspect(ctx, {showHidden: false, depth: null}))

  r = redis.createClient(9950, 'ray.redistogo.com', {no_ready_check: true});
  r.auth(ctx.data.REDIS_PASS, function (err) { if (err) done(err); });

  r.hvals('h-watchlist',  function (err, res) {
    if (err) done(err);

    console.log(res);

    totals = res.reduce(add, 0);

    console.log(totals)

    totalh = (totals / 3600).toFixed(2)

    done(null, util.format('Total time wasted: %d hours', totalh));
  });

};
