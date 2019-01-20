var path = require('path');

module.exports = {
    entry: {
        app: ['./client/main/index.js'],
    },
    output: {
        path: path.join(__dirname, 'server/static/'),
        filename: '[name]-bundle.js'
    },
    module: {
        loaders: [
            {
                test: /\.js$/,
                include: path.join(__dirname, 'client/main'),
                loader: 'babel-loader',
                query: {
                    presets: ['es2015', 'react', 'stage-2']
                }
            }
        ]
    }
};