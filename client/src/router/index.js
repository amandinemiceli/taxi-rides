import Vue from 'vue'
import VueRouter from 'vue-router'
import RideList from '../components/RideList.vue'

Vue.use(VueRouter)

const routes = [
    {
      path: '/rides',
      name: 'RideList',
      component: RideList,
    }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
