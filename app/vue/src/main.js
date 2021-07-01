import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VuePageTitle from 'vue-page-title'

Vue.config.productionTip = false

Vue.use(VuePageTitle)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
