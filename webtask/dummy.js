var util = require('util');

module.exports = function (ctx, done) {

  done(null, util.inspect(ctx, {showHidden: false, depth: null}));
}
