import { CommonModule } from "@angular/common";
import { NgModule } from "@angular/core";
import { OrderMaterialModule } from "../material/material.module";
import { OrderSharedModule } from "../shared/shared.module";
import { OrderClientRoutingModule } from "./client.routing.module";
import { BasicClientComponent } from "./create-client/basic-detail/basic-detail.component";
import { ClientCommunicationComponent } from "./create-client/client-communication/client-communication.component";
import { ClientIntegrationComponent } from "./create-client/client-integration/client-integration.component";
import { CreateClientComponent } from "./create-client/create-client.component";
import { ListClientComponent } from "./list-client/list-client.component";

@NgModule({
    declarations: [
        CreateClientComponent,
        BasicClientComponent,
        ClientIntegrationComponent,
        ClientCommunicationComponent,
        ListClientComponent
    ],
    imports: [
        CommonModule,
        OrderSharedModule,
        OrderMaterialModule,
        OrderClientRoutingModule
    ],
    providers: [
    ]
})
export class OrderClientModule { }