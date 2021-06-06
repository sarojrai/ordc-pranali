import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { LoginComponent } from 'src/app/modules/auth/login/login.component';

const routes: Routes = [
    {
        path: 'login',
        component: LoginComponent,
        data: {
            breadcrumb: 'Login'
        }
    },
    {
        path: '', redirectTo: '/login', pathMatch: 'full'
    },
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class AuthRoutingModule { }
