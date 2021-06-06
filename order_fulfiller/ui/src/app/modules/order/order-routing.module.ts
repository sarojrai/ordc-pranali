import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { OrderListComponent } from './order-list/order-list.component';

const routes: Routes = [
  {
      path: '',
      component: OrderListComponent,
      data: {
          breadcrumb: 'Order List'
      }
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class OrderRoutingModule { }
