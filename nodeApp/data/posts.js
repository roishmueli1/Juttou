var mongoose = require('mongoose');
var Post = require('./schema/postSchema');
//var random = require('mongoose-random')

exports.getPosts = (req, res) => {
    console.log('getPosts');
	var q = Post.findOne({number: "2"});

	q.exec(function(err, posts)  {
		if (err) {
			console.log(`err: ${err}`);
			res.status(200).json(`{ err : ${err} }`);
		}
		console.log(posts);
		res.status(200).json(posts);
	});
};
