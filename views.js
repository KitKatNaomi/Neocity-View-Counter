var NeoCities = require('neocities')
var api = new NeoCities('YOURUSERNAME', 'YOURPASSWORD')
api.info(function(resp) {
  console.log(resp.info.views)
})