import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable, of } from "rxjs";
import { catchError, map, retry } from "rxjs/operators";
import { environment } from "src/environments/environment";
import { Client } from "../../models";
import { handleError } from "../../shared/helper";

@Injectable({
    providedIn: 'root',
})
export class ClientDataService {

    constructor(private _http: HttpClient) { }

    createClient(clientInfo: any) {
        return this._http.post(environment.authUrl + 'api/clients/create', clientInfo)
            .pipe(
                retry(3),
                map((response: any) => {
                    return response.data
                }),
                catchError(handleError))
    }

    getState() {
        // this._http.get()
    }

    getClients(): Observable<Array<Client>> {
        return this._http.get(environment.authUrl + 'api/clients')
        .pipe(
            retry(3),
            map((response: any) => {
                return response.data
            }),
            catchError(handleError))
        // return of([
        //     {
        //         "id": 1,
        //         "name": "Emami",
        //         "code": "EMAMI",
        //         "website": null,
        //         "email": null,
        //         "referred_by": null,
        //         "client_type": "BRND",
        //         "contact_person": null,
        //         "contract_from": "2021-05-22",
        //         "contract_to": "2021-05-22",
        //         "created_by_id": null,
        //         "updated_by_id": null,
        //         "added_on": "2021-05-22T19:00:47.039696",
        //         "updated_on": "2021-05-22T19:03:53.549555",
        //         "status": 0.0,
        //         "activation_status": true,
        //         "activation_date": null,
        //         "activated_by_id": null,
        //         "deactivation_date": "2021-05-22",
        //         "billing_schedule": 7,
        //         "day_of_billing": 7,
        //         "remittance_cycle": 7,
        //         "credit_limit": 10000,
        //         "credit_period": 10,
        //         "bill_delivery_email": true,
        //         "bill_delivery_hand": true,
        //         "latest_invoice_date": null,
        //         "next_bill_date": null,
        //         "approved_id": null,
        //         "authorized_id": null
        //     },
        //     {
        //         "id": 2,
        //         "name": "Amazon",
        //         "code": "AMZ",
        //         "website": null,
        //         "email": null,
        //         "referred_by": null,
        //         "client_type": "MRKT",
        //         "contact_person": null,
        //         "contract_from": "2021-05-22",
        //         "contract_to": "2021-05-22",
        //         "created_by_id": null,
        //         "updated_by_id": null,
        //         "added_on": "2021-05-22T19:03:23.443394",
        //         "updated_on": "2021-05-22T19:03:23.443426",
        //         "status": 0.0,
        //         "activation_status": true,
        //         "activation_date": "2021-05-22",
        //         "activated_by_id": null,
        //         "deactivation_date": "2021-05-22",
        //         "billing_schedule": 7,
        //         "day_of_billing": 7,
        //         "remittance_cycle": 7,
        //         "credit_limit": 10000,
        //         "credit_period": 10,
        //         "bill_delivery_email": true,
        //         "bill_delivery_hand": true,
        //         "latest_invoice_date": null,
        //         "next_bill_date": null,
        //         "approved_id": null,
        //         "authorized_id": null
        //     },
        //     {
        //         "id": 3,
        //         "name": "Emami_Test",
        //         "code": "BRND87EBFB0",
        //         "website": null,
        //         "email": null,
        //         "referred_by": null,
        //         "client_type": "BRND",
        //         "contact_person": null,
        //         "contract_from": "2021-05-22",
        //         "contract_to": "2021-05-22",
        //         "created_by_id": null,
        //         "updated_by_id": null,
        //         "added_on": "2021-05-22T19:24:36.486967",
        //         "updated_on": "2021-05-22T19:24:36.487016",
        //         "status": 0.0,
        //         "activation_status": true,
        //         "activation_date": null,
        //         "activated_by_id": null,
        //         "deactivation_date": "2021-05-22",
        //         "billing_schedule": 7,
        //         "day_of_billing": 7,
        //         "remittance_cycle": 7,
        //         "credit_limit": 10000,
        //         "credit_period": 10,
        //         "bill_delivery_email": true,
        //         "bill_delivery_hand": true,
        //         "latest_invoice_date": null,
        //         "next_bill_date": null,
        //         "approved_id": null,
        //         "authorized_id": null
        //     },
        //     {
        //         "id": 4,
        //         "name": "Emami_Test1",
        //         "code": "BRND46782A0",
        //         "website": null,
        //         "email": null,
        //         "referred_by": null,
        //         "client_type": "BRND",
        //         "contact_person": null,
        //         "contract_from": "2021-05-22",
        //         "contract_to": "2021-05-22",
        //         "created_by_id": null,
        //         "updated_by_id": null,
        //         "added_on": "2021-05-22T19:27:40.295569",
        //         "updated_on": "2021-05-22T19:27:40.295599",
        //         "status": 0.0,
        //         "activation_status": true,
        //         "activation_date": null,
        //         "activated_by_id": null,
        //         "deactivation_date": "2021-05-22",
        //         "billing_schedule": 7,
        //         "day_of_billing": 7,
        //         "remittance_cycle": 7,
        //         "credit_limit": 10000,
        //         "credit_period": 10,
        //         "bill_delivery_email": true,
        //         "bill_delivery_hand": true,
        //         "latest_invoice_date": null,
        //         "next_bill_date": null,
        //         "approved_id": null,
        //         "authorized_id": null
        //     },
        //     {
        //         "id": 5,
        //         "name": "Emami_Test2",
        //         "code": "MRKTD2B6CD0",
        //         "website": null,
        //         "email": null,
        //         "referred_by": null,
        //         "client_type": "MRKT",
        //         "contact_person": null,
        //         "contract_from": "2021-05-22",
        //         "contract_to": "2021-05-22",
        //         "created_by_id": null,
        //         "updated_by_id": null,
        //         "added_on": "2021-05-22T19:32:35.671106",
        //         "updated_on": "2021-05-22T19:32:35.671149",
        //         "status": 0.0,
        //         "activation_status": true,
        //         "activation_date": null,
        //         "activated_by_id": null,
        //         "deactivation_date": "2021-05-22",
        //         "billing_schedule": 7,
        //         "day_of_billing": 7,
        //         "remittance_cycle": 7,
        //         "credit_limit": 10000,
        //         "credit_period": 10,
        //         "bill_delivery_email": true,
        //         "bill_delivery_hand": true,
        //         "latest_invoice_date": null,
        //         "next_bill_date": null,
        //         "approved_id": null,
        //         "authorized_id": null
        //     },
        //     {
        //         "id": 6,
        //         "name": "Emami_Test3",
        //         "code": "MRKTC084110",
        //         "website": null,
        //         "email": null,
        //         "referred_by": null,
        //         "client_type": "MRKT",
        //         "contact_person": null,
        //         "contract_from": "2021-05-22",
        //         "contract_to": "2021-05-22",
        //         "created_by_id": null,
        //         "updated_by_id": null,
        //         "added_on": "2021-05-23T08:06:59.520617",
        //         "updated_on": "2021-05-23T08:06:59.520639",
        //         "status": 0.0,
        //         "activation_status": true,
        //         "activation_date": null,
        //         "activated_by_id": null,
        //         "deactivation_date": "2021-05-22",
        //         "billing_schedule": 7,
        //         "day_of_billing": 7,
        //         "remittance_cycle": 7,
        //         "credit_limit": 10000,
        //         "credit_period": 10,
        //         "bill_delivery_email": true,
        //         "bill_delivery_hand": true,
        //         "latest_invoice_date": null,
        //         "next_bill_date": null,
        //         "approved_id": null,
        //         "authorized_id": null
        //     }
        // ])
    }
}