import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ListOrdersComponent } from './list-orders/list-orders.component';

const routes: Routes = [
    {
        path: 'list',
        component: ListOrdersComponent,
        data: {
            breadcrumb: 'List'
        }
    },
    {
        path: '', redirectTo: '/list', pathMatch: 'full'
    },
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class OrdersRoutingModule { }
