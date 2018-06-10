const fs = require('fs');
const {join} = require('path');

const addIndex = path => {
	fs.readdir(path, (err, files) => {
		if(err && err.errno ===	 -4052) return;
		fs.writeFile(join(path, 'index.txt'), files.join('\n'), () => {
			for(const file of files){
				addIndex(join(path, file));
			}
		});
	});
};

addIndex('./data');