import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from 'src/app/components/home/home.component';

const routes: Routes = [
  {
    path: 'auth',
    loadChildren: () => import('src/app/modules/auth/auth.module').then(m => m.AuthModule),
    data: {
      breadcrumb: 'Auth'
    }
  },
  {
    path: 'home',
    component: HomeComponent,
    data: {
      breadcrumb: 'My Home'
    },
    children: [
      {
        path: 'client',
        loadChildren: () => import('src/app/modules/client/client.module').then(m => m.OrderClientModule),
        data: {
          breadcrumb: 'Client'
        }
      },
      {
        path: 'orders',
        loadChildren: () => import('src/app/modules/orders/orders.module').then(m => m.OrdersModule),
        data: {
          breadcrumb: 'Orders'
        }
      }
    ]
  },
  {
    path: '**', component: HomeComponent,
    data: {
      breadcrumb: 'My Home'
    }
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { scrollPositionRestoration: 'enabled' })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
