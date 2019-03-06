var mongoose        = require('mongoose'),
    postSchema      = new mongoose.Schema({
			_id: { $oid: String },
			time: Date,
			content: String,
			number: Number,
		}  , {collection: 'posts'});

module.exports = mongoose.model('Post', postSchema);
