import { Component, Input, ViewEncapsulation, OnInit } from "@angular/core";
import { FormGroup } from "@angular/forms";
import { BrandWebsite, WarehouseManagementSystem } from "src/app/modules/models";
import { CourierPartner } from "src/app/modules/models";
import { Bankdetails, ContactDetails } from '../../../models/clientCreate';
@Component({
    selector: 'order-client-integration',
    templateUrl: './client-integration.component.html',
    styleUrls: ['./client-integration.component.scss'],
    encapsulation: ViewEncapsulation.None,
    // providers: [
    // ],
})


export class ClientIntegrationComponent{
    @Input() formGroup!: FormGroup;
    // @Input() brandWebsites!: Array<BrandWebsite>;
    // @Input() marketPlaceWebsites!: Array<BrandWebsite>;
    // @Input() warehouseMgmts!: Array<WarehouseManagementSystem>;
    // @Input() courierPartners!: Array<CourierPartner>;

    brandwebsite: Array<string> = ['Shopify','Megento','NooCommerce','In-House']
    marketplace: Array<string> = ['Shopify','Flipcart','Myntra']
    wms: Array<string> = ['Uni - commerce','Purpledron','Other']
    courier_partner: Array<string> = ['Picker','BlueDart','EcomExpress']

   
}