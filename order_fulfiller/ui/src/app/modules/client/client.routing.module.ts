import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CreateClientComponent } from './create-client/create-client.component';
import { ListClientComponent } from './list-client/list-client.component';

const routes: Routes = [
    {
        path: 'create',
        component: CreateClientComponent,
        data: {
            breadcrumb: 'Create'
        }
    },
    {
        path: 'list',
        component: ListClientComponent,
        data: {
            breadcrumb: 'List'
        }
    },
    {
        path: '', redirectTo: '/create', pathMatch: 'full'
    },
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class OrderClientRoutingModule { }
