var NeoCities = require('neocities')
var api = new NeoCities('YOURUSERNAME', 'YOURPASSWORD')
api.upload([{name: '/count.jpg', path: './count.jpg'}], function(resp) {
	console.log(resp.result)
})