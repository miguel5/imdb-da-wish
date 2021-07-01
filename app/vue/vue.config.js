module.exports = {
    devServer: {
     proxy: {
       '/api': {
         target: 'http://localhost:7001',
         secure: true,
         changeOrigin: true,
         pathRewrite: {
           '^/api': ''
         }
       },
     }
   } 
   };