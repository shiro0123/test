module.exports = {
  module: {
    rules: [
      {
        test: /\.m?js$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-env"],
          },
        },
      },
    ],
  },
  entry: "./app/frontend.js",
  output: {
    filename: "bundle.js",
    path: __dirname + "/app/public",
  },
};
