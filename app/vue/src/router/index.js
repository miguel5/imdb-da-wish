import Vue from 'vue'
import VueRouter from 'vue-router'
import Atores from '../views/Atores.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/atores',
    name: 'Atores',
    component: Atores,
  },
  {
    path: '/atores/:idAtor',
    name: 'Ator',
    component: () => import('../views/Ator.vue')
  },
  {
    path: '/filmes',
    name: 'Filmes',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Filmes.vue')
  },
  {
    path: '/filmes/:idFilme',
    name: 'Filme',
    component: () => import('../views/Filme.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
