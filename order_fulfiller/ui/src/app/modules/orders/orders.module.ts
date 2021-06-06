import { CommonModule } from "@angular/common";
import { NgModule } from "@angular/core";
import { TitlePipe } from "src/app/pipes/title.pipe";
import { OrderMaterialModule } from "../material/material.module";
import { OrderSharedModule } from "../shared/shared.module";
import { ListOrdersComponent } from "./list-orders/list-orders.component";
import { OrdersRoutingModule } from "./orders.routing.module";

@NgModule({
    declarations: [
        ListOrdersComponent,
        TitlePipe
    ],
    imports: [
        CommonModule,
        OrderSharedModule,
        OrderMaterialModule,
        OrdersRoutingModule,
    ],
    providers: [
    ]
})
export class OrdersModule { }
