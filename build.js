const fs = require('fs');
const {join} = require('path');

const addIndex = path => {
	fs.readdir(path, (err, files) => {
		if(err && err.code === 'ENOTDIR') return;
		if(!files){
			console.error('undefined files in ' + path, err);
			return;
		}
		fs.writeFile(join(path, '.index'), files.filter(file => file !== '.index').join('\n'), () => {
			for(const file of files){
				addIndex(join(path, file));
			}
		});
	});
};

addIndex('./data');