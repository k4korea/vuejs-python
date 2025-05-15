module.exports = {
  transpileDependencies: [],
  devServer: {
    host: '0.0.0.0',
    port: 8080,
    allowedHosts: ['localhost', '127.0.0.1', '192.168.0.10']
  },
  configureWebpack: {
    resolve: {
      extensions: ['.js', '.vue', '.json']
    },
    optimization: {
      removeAvailableModules: false,
      removeEmptyChunks: false,
      splitChunks: false,
    },
    output: {
      filename: '[name].js',
      chunkFilename: '[name].js'
    }
  },
  chainWebpack: config => {
    config.optimization.minimize(false)
  }
} 