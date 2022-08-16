import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
     path: '/',
     component: () => import('pages/WelcomePage.vue'),
  },

  {
    path: '/home',
    component: () => import('pages/HomePage.vue')
  },

  {
     path: '/questions',
     component: () => import('pages/BrowseQuestions.vue'),
  },
  {
    path: '/questions/add',
    component: () => import('pages/BrowseQuestions.vue'),
  },
  {
    path: '/set',
    component: () => import('pages/ViewSetPage.vue'),
  }
];

export default routes;
