import { createRouter, createWebHistory } from 'vue-router';
import Login from '../components/Login.vue';
import Home from '../components/Home.vue';
import Accounts from '../components/Accounts.vue';
import AccountForm from '../components/AccountForm.vue';
import AccountEdit from '../components/AccountEdit.vue';

const routes = [
  { path: '/', name: 'home', component: Home },
  { path: '/login', name: 'login', component: Login },
  { path: '/accounts', name: 'accounts', component: Accounts, meta: { requiresAuth: true } },
  { path: '/accounts/new', name: 'account-create', component: AccountForm, meta: { requiresAuth: true } },
  { path: '/accounts/:id/edit', name: 'account-edit', component: AccountEdit, meta: { requiresAuth: true } },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('authToken');
  if (to.meta.requiresAuth && !token) {
    next({ name: 'login' });
  } else {
    next();
  }
});

export default router;
