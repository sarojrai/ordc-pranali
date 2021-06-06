import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { OrderRoutingModule } from './order-routing.module';
import { OrderListComponent } from './order-list/order-list.component';
import { MatTableModule } from '@angular/material/table';


@NgModule({
  declarations: [
    OrderListComponent
  ],
  imports: [
    CommonModule,
    OrderRoutingModule,
    MatTableModule
  ]
})
export class OrderModule { }
