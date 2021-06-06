import { NgModule } from '@angular/core';

import { OrderSharedModule } from 'src/app/modules/shared/shared.module';
import { OrderMaterialModule } from 'src/app/modules/material/material.module';
import { AuthRoutingModule } from 'src/app/modules/auth/auth.routing.module';

import { LoginComponent } from 'src/app/modules/auth/login/login.component';




@NgModule({
  declarations: [
    LoginComponent
  ],
  imports: [
    OrderSharedModule,
    OrderMaterialModule,
    AuthRoutingModule
  ],
  providers: []
})
export class AuthModule { }