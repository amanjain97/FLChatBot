// server.js


var express = require('express');
var app		= express();
var bodyParser = require('body-parser');	

var bear = require('./app/models/bear');


var mongoose   = require('mongoose');
mongoose.connect('mongodb://127.0.0.1:27017');


app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var port = process.env.PORT || 8080;        // set our port


var router = express.Router();
router.use(function(req, res, next){
	console.log("something good is happening");
	next();

});


router.get('/', function(req, res) {
    res.json({ message: 'hooray! welcome to our api!' });   
});

router.route('/bears')
		.post(function(req, res) {

        var bear = new Bear();      // create a new instance of the Bear model
        bear.name = req.body.name;  // set the bears name (comes from the request)

        // save the bear and check for errors
        bear.save(function(err) {
            if (err)
                res.send(err);

            res.json({ message: 'Bear created!' });
        });


        .get(function(req, res) {
        	Bear.find(function (err, bears) {
        		// body...
        		if(err){
        			res.send(err);
        		}
        		res.json(bears);
        	});
        	// body...
        })
    });


router.route('/bears/:bear_id')

    // get the bear with that id (accessed at GET http://localhost:8080/api/bears/:bear_id)
    .get(function(req, res) {
        Bear.findById(req.params.bear_id, function(err, bear) {
            if (err)
                res.send(err);
            res.json(bear);
        });
    });


app.use('/api', router);

app.listen(port);
console.log('Magic happens on port ' + port);