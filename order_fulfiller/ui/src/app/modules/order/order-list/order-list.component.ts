import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-order-list',
  templateUrl: './order-list.component.html',
  styleUrls: ['./order-list.component.scss']
})
export class OrderListComponent implements OnInit {

  orderList: Array<any> = [];
  displayedColumns: string[] = ['order_number','source_type', 'source', 'payment_type', 'currency', 'gross_amount', 'source_status', 'is_blacklisted', 'created_at', 'updated_at'];

  constructor() { }

  ngOnInit(): void {
    this.processOrderResults([
      {
          "id": 2,
          "customer": {
              "id": 10,
              "unique_id": "d6a1076b-37e6-45c9-97a9-8c48f1b8e3aa",
              "email": "ankit.sojitra@emamigroup.com",
              "first_name": "ass",
              "last_name": "ase",
              "orders_count": 6,
              "state": "disabled",
              "total_spent": "4144.05",
              "last_order_id": 3768820138179,
              "verified_email": true,
              "tax_exempt": false,
              "phone": null,
              "currency": "INR",
              "created_at": "2021-04-21T06:40:29Z",
              "updated_at": "2021-04-30T05:27:53Z",
              "is_blacklisted": false
          },
          "billing_address": {
              "id": 6349241188558,
              "address_type": "BILLING",
              "unique_id": "19f1d228-5068-4bc0-8584-7ae5f43f6f35",
              "first_name": "Ankit",
              "last_name": "Sojitra",
              "address1": "403/A G Bawdi Road Railway Colony Byculla",
              "address2": "new villa",
              "city": "Mumbai",
              "province": "Maharashtra",
              "country": "India",
              "zipcode": "400010",
              "phone": "88988 10400",
              "name": "Ankit Sojitra",
              "province_code": "MH",
              "country_code": "IN",
              "country_name": "",
              "default": false,
              "company": null,
              "latitude": 18.968376,
              "longitude": 72.8434765,
              "customer": 10
          },
          "shipping_address": {
              "id": 6349241188559,
              "address_type": "SHIPPING",
              "unique_id": "170c8482-d68e-47e6-aaa0-d108d44fdc4f",
              "first_name": "Ankit",
              "last_name": "Sojitra",
              "address1": "403/A G Bawdi Road Railway Colony Byculla",
              "address2": "new villa",
              "city": "Mumbai",
              "province": "Maharashtra",
              "country": "India",
              "zipcode": "400010",
              "phone": "88988 10400",
              "name": "Ankit Sojitra",
              "province_code": "MH",
              "country_code": "IN",
              "country_name": "",
              "default": false,
              "company": null,
              "latitude": 18.968376,
              "longitude": 72.8434765,
              "customer": 10
          },
          "unique_id": "66fd1114-fbae-434e-8b8d-8296b600ccf5",
          "order_number": "1118",
          "payment_type": "Cash on Delivery (COD)",
          "is_blacklisted": false,
          "status": "order_placed",
          "gross_amount": "544.00",
          "currency": "INR",
          "discount": "0.00",
          "tax": "0.00",
          "requested_payload": {},
          "source_type": "brand",
          "source": "shopify",
          "source_website": "https://www.shopify.in",
          "client_id": "TEST",
          "source_status": "pending",
          "created_at": "2021-04-22T12:47:28Z",
          "updated_at": "2021-04-22T12:47:30Z",
          "created_by": "",
          "updated_by": ""
      },
      {
          "id": 3,
          "customer": {
              "id": 11,
              "unique_id": "8eefa624-9e1e-424e-8917-d9ba6c9291b9",
              "email": "Akshay.Saini@emamigroup.com",
              "first_name": "ass",
              "last_name": "ase",
              "orders_count": 6,
              "state": "disabled",
              "total_spent": "4144.05",
              "last_order_id": 3768820138179,
              "verified_email": true,
              "tax_exempt": false,
              "phone": null,
              "currency": "INR",
              "created_at": "2021-04-21T06:40:29Z",
              "updated_at": "2021-04-30T05:27:53Z",
              "is_blacklisted": false
          },
          "billing_address": {
              "id": 6349241188560,
              "address_type": "BILLING",
              "unique_id": "32164798-ef4d-4df1-a208-c746597d7c5f",
              "first_name": "Akshay",
              "last_name": "Saini",
              "address1": "403/A G Bawdi Road Railway Colony Byculla",
              "address2": "new villa",
              "city": "Mumbai",
              "province": "Maharashtra",
              "country": "India",
              "zipcode": "400010",
              "phone": "88988 10400",
              "name": "Akshay Saini",
              "province_code": "MH",
              "country_code": "IN",
              "country_name": "",
              "default": false,
              "company": null,
              "latitude": 18.968376,
              "longitude": 72.8434765,
              "customer": 11
          },
          "shipping_address": {
              "id": 6349241188561,
              "address_type": "SHIPPING",
              "unique_id": "47629d25-d4f8-412a-84a3-b8dbc121cd1b",
              "first_name": "Akshay",
              "last_name": "Saini",
              "address1": "403/A G Bawdi Road Railway Colony Byculla",
              "address2": "new villa",
              "city": "Mumbai",
              "province": "Maharashtra",
              "country": "India",
              "zipcode": "400010",
              "phone": "88988 10400",
              "name": "Akshay Saini",
              "province_code": "MH",
              "country_code": "IN",
              "country_name": "",
              "default": false,
              "company": null,
              "latitude": 18.968376,
              "longitude": 72.8434765,
              "customer": 11
          },
          "unique_id": "2600441a-e6d8-4ae0-9dc9-ca26b57822c7",
          "order_number": "1119",
          "payment_type": "Cash on Delivery (COD)",
          "is_blacklisted": false,
          "status": "order_placed",
          "gross_amount": "544.00",
          "currency": "INR",
          "discount": "0.00",
          "tax": "0.00",
          "requested_payload": {},
          "source_type": "brand",
          "source": "shopify",
          "source_website": "https://www.shopify.in",
          "client_id": "TEST",
          "source_status": "pending",
          "created_at": "2021-04-22T12:47:28Z",
          "updated_at": "2021-04-22T12:47:30Z",
          "created_by": "",
          "updated_by": ""
      }
  ])
  }

  processOrderResults(orders: any[]) {
    // let currentDate = new Date();
    // orders.forEach(order => {
    // });
    this.orderList = orders;
  }
}
