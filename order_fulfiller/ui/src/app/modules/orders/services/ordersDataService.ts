import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Order } from "../models/order.model";
import { environment } from '../../../../environments/environment';
import { Observable } from "rxjs";
import { retry, map, catchError } from "rxjs/operators";
import { handleError } from "../../shared/helper";
@Injectable({
    providedIn: 'root',
})
export class OrdersDataService {

    orders: Order[] = [];
    BASE_URL = environment.orderBaseUrl;

    constructor(private _http: HttpClient) { }

    getOrders(filters = {}) {
      return this._http.get(`${this.BASE_URL}/order/`);
    }

    getOrderList(filters: any): Observable<Array<any>> {
      return this._http.get<any>(`${this.BASE_URL}/order/?q=${JSON.stringify(filters)}`)
          .pipe(
              retry(3),
              map((response: any) => {
                  return (Array.isArray(response.data) ? response.data : [])
              }),
              catchError(handleError))
  }
}
