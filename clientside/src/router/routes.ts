import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
     path: '/',
     component: () => import('pages/HomePage.vue'), //Create welcome page in the future
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
    path: '/set',
    component: () => import('pages/BrowseQuestions.vue'),
  },
  {
    path: '/set/:id',
    component: () => import('pages/BrowseQuestions.vue')
  },
  {
    path: '/set-page/:id',
    component: () => import('pages/SetTriviaPage.vue'),
  }
];

export default routes;
