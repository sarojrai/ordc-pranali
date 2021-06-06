import { Component, ViewEncapsulation } from "@angular/core";
import { FormControl, FormGroup } from "@angular/forms";
import { debounceTime, filter, startWith, switchMap } from 'rxjs/operators';
import * as moment from 'moment';
import { formatDate } from '../../shared/helper';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Order } from "../models/order.model";
import { OrdersDataService } from "../services/ordersDataService";

import { MAT_DATE_FORMATS } from '@angular/material/core';
import { ORDER_RANGE_FORMATS, compareDates, convertRemainingDays } from 'src/app/modules/material/lib/helper';
import { Router } from "@angular/router";
@Component({
    selector: 'order-list',
    templateUrl: './list-orders.component.html',
    styleUrls: ['./list-orders.component.scss'],
    encapsulation: ViewEncapsulation.None,
    providers: [
      { provide: MAT_DATE_FORMATS, useValue: ORDER_RANGE_FORMATS },
  ]
})
export class ListOrdersComponent {
    displayedColumns: string[] = ['select', '#', 'order_number', 'source', 'payment_type', 'gross_amount', 'status', 'is_blacklisted', 'created_at', 'updated_at', 'updated_by'];
    ordersList: any[] = []
    formGroup!: FormGroup;

    constructor(private ordersDataService: OrdersDataService,
      private router: Router,
      private _snackBar: MatSnackBar,) {

        this.formGroup = new FormGroup({
          code: new FormControl(''),
          cost_min_value: new FormControl(0),
          cost_max_value: new FormControl(0),
          status: new FormControl('DRAFT'),
          start_date: new FormControl(''),
          end_date: new FormControl('')
      });

    }

    ngOnInit(): void {
      this.formGroup.valueChanges
          .pipe(
              startWith(''),
              debounceTime(400),
              switchMap(values => this.getOrderDetails(values))
          )
          .subscribe(orders => {});

      this.ordersDataService.getOrderList({}).subscribe((data:any[]) => {
        if (data.length > 0) {
          this.displayedColumns = ['select', '#'].concat(Object.keys(data[0].metadata));
        }
        this.ordersList = data;
      }, (err) => {
        console.log('err', err);
      });
  }


  compareWithToday(to: string) {
      return !compareDates(new Date(), new Date(to));
  }

  remainingDates(to: string) {
      return convertRemainingDays(new Date(), new Date(to));
  }

  routeToOrderDetails(orderDetails: any) {
      // this.dataService.setSelectedOrderDetails(orderDetails);
      // this.router.navigate(['/home/orders/order-details']);
  }

  getOrderDetails(formValues: any) {
      let filters: any = {};

      for (let key in formValues) {
          if (formValues[key] !== '' && formValues[key] !== 0 && formValues[key] !== "") {
              filters[key] = formValues[key];
          }
      }

      this.convertToNativeDate(filters, 'start_date');
      this.convertToNativeDate(filters, 'end_date');
      return this.ordersDataService.getOrderList(filters);
  }

  convertToNativeDate(formValues: any, dateKey: string) {
      if (formValues.hasOwnProperty(dateKey)) {
          formValues[dateKey] = formatDate(moment(formValues[dateKey]).toDate());
      }
  }

  processOrderResults(orders: any[]) {
      let currentDate = new Date();
      orders.forEach(order => {
          order.isSelected = false;
          if (order.general_info.closing_at != null && currentDate > new Date(order.general_info.closing_at)) {
              order.general_info.countDown = 'Expired';
          }
          else if (order.general_info.opening_at != null && new Date()) {
              order.general_info.countDown = convertRemainingDays(currentDate, new Date(order.general_info.opening_at))
          }
      });
      this.ordersList = orders;
  }

  reset() {
      this.formGroup.reset({
          status: 'DRAFT',
          code: '',
          cost_min_value: 0,
          cost_max_value: 0,
          start_date: '',
          end_date: ''
      });
  }

  inviteBidders(order: any) {
      this.router.navigate(['/home/bidders/invite-bidders/', order.general_info.code]);
  }

  checkBids(order: any) {
      this.router.navigate(['/home/bidders/order-bids']);
  }

  changeSingleOrderStatus(order: any, action: string) {
      let code = order?.general_info?.code;
      order.isSelected = true;
      // TODO remove hardcoded action_by, Auth need to be implemented
      if (typeof code === 'string') {
          this.changeOrderStatus([code], action, 2);
      }
  }

  changeBulkOrderStatus(action: string) {
      // TODO remove hardcoded action_by, Auth need to be implemented
      console.log("Action " + action);
      if (action != "") {
          let codes = this.ordersList
              .filter(order => order.isSelected)
              .map(order => (order.general_info.code || '').toString())

          this.changeOrderStatus(codes, action, 2);
      }
  }

  changeOrderStatus(code: Array<string>, action: string, action_by: number) {
  }

}
