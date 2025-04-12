import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import AddMovieFormView from '../views/AddMovieFormView.vue';
import MoviesView from '../views/MoviesView.vue';

const routes = [
  { path: '/', name: 'Home', component: HomeView },
  { path: '/movies/create', name: 'AddMovieFormView', component: AddMovieFormView },
  { path: '/about', name: 'about', component: () => import('../views/AboutView.vue')},
  { path: '/movies', name: 'MoviesView', component: MoviesView}
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes  
});

export default router;

