import { Component, OnDestroy, OnInit, ViewEncapsulation } from '@angular/core';
import { MAT_DATE_FORMATS } from '@angular/material/core';
// import { client, clientStatus } from 'src/app/modules/models/client';
// import { clientCrudService } from 'src/app/modules/clients/services/clientCrudService';
import { ORDER_RANGE_FORMATS, compareDates, convertRemainingDays } from 'src/app/modules/material/lib/helper';
// import { clientDataService } from '../services/clientDataService';
import { Router } from '@angular/router';
import { FormControl, FormGroup } from '@angular/forms';
import { debounceTime, filter, startWith, switchMap } from 'rxjs/operators';
import * as moment from 'moment';
import { formatDate } from '../../shared/helper';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Subscription } from 'rxjs';
import { ClientDataService } from '../services/ClientDataService';
import { Client } from '../../models';

@Component({
    selector: 'order-list-client',
    templateUrl: './list-client.component.html',
    styleUrls: ['./list-client.component.scss'],
    encapsulation: ViewEncapsulation.None,
    providers: [
        { provide: MAT_DATE_FORMATS, useValue: ORDER_RANGE_FORMATS },
    ]
})
export class ListClientComponent implements OnInit, OnDestroy {
    clientList!: Array<Client>;
    // clientStatusList!: Array<clientStatus>;
    // displayedColumns: string[] = ['select', 'sno', 'id', 'name', 'duration', 'bidders', 'price', 'created', 'countdown', 'status', 'more'];
    displayedColumns: string[] = ['select', 'sno', 'id', 'name', 'client_type', 'status'];

    formGroup!: FormGroup;

    formGroupSubscription!: Subscription;
    clientStatusSubscription!: Subscription;

    constructor(
        private router: Router,
        private _snackBar: MatSnackBar,
        private dataService: ClientDataService,
    ) {
        this.formGroup = new FormGroup({
            code: new FormControl(''),
            cost_min_value: new FormControl(0),
            cost_max_value: new FormControl(0),
            status: new FormControl(''),
            start_date: new FormControl(''),
            end_date: new FormControl('')
        });
    }

    ngOnInit(): void {
        this.formGroupSubscription = this.formGroup.valueChanges
            .pipe(
                startWith(''),
                debounceTime(400),
                switchMap(values => this.getclientDetails(values))
            )
            .subscribe(clients => this.processClientResults(clients));

        this.clientStatusSubscription = this.dataService.getClients()
            .subscribe(clients => this.clientList = clients);
    }

    ngOnDestroy(): void {
        this.formGroupSubscription.unsubscribe();
        this.clientStatusSubscription.unsubscribe();
    }

    compareWithToday(to: string) {
        return !compareDates(new Date(), new Date(to));
    }

    remainingDates(to: string) {
        return convertRemainingDays(new Date(), new Date(to));
    }

    // routeToclientDetails(clientDetails: client) {
    //     this.dataService.setSelectedclientDetails(clientDetails);
    //     this.router.navigate(['/home/clients/client-details']);
    // }

    getclientDetails(formValues: any) {
        console.log("FormValues");
        console.log(formValues);
        let filters: any = {};

        for (let key in formValues) {
            if (formValues[key] !== '' && formValues[key] !== "" && ((key === 'status' && formValues[key] === 0) || formValues[key] !== 0)) {
                filters[key] = formValues[key];
            }
        }

        this.convertToNativeDate(filters, 'start_date');
        this.convertToNativeDate(filters, 'end_date');
        return this.dataService.getClients();
    }

    convertToNativeDate(formValues: any, dateKey: string) {
        if (formValues.hasOwnProperty(dateKey)) {
            formValues[dateKey] = formatDate(moment(formValues[dateKey]).toDate());
        }
    }

    processClientResults(clients: Client[]) {
        let currentDate = new Date();
        clients.forEach(client => {
            client.isSelected = false;
        });
        this.clientList = clients;
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

    // inviteBidders(client: client) {
    //     this.router.navigate(['/home/bidders/invite-bidders/', client.general_info.code]);
    // }

    // checkBids(client: client) {
    //     this.router.navigate(['/home/bidders/client-bids/', client.general_info.code]);
    // }

    // changeSingleclientStatus(client: client, action: string) {
    //     let code = client?.general_info?.code;
    //     client.isSelected = true;
    //     // TODO remove hardcoded action_by, Auth need to be implemented
    //     if (typeof code === 'string') {
    //         this.changeclientStatus([code], action, 2);
    //     }
    // }

    changeBulkClientStatus(action: string) {
        // TODO remove hardcoded action_by, Auth need to be implemented
        console.log("Action " + action);
        if (action != "") {
            let codes = this.clientList
                .filter(client => client.isSelected)
                .map(client => (client.id || '').toString())

            // this.changeclientStatus(codes, action, 2);
        }
    }

    // changeclientStatus(code: Array<string>, action: string, action_by: number) {
    //     this.clientService
    //         .changeclientStatus(code, action, action_by)
    //         .subscribe(result => {
    //             if (!result['is_error']) {
    //                 this._snackBar.open('client Status Changed Successfully', 'Ok', {
    //                     duration: 2000,
    //                     panelClass: ['success-snackbar']
    //                 });
    //                 this.clientList.filter(client => client.isSelected).forEach(client => {
    //                     client.isSelected = false;
    //                     client.general_info.status = action;
    //                 });

    //             } else {
    //                 this._snackBar.open('client Status Changed  Failed', 'Ok', {
    //                     duration: 2000,
    //                     panelClass: ['error-snackbar']
    //                 });
    //             }
    //         }, err => {
    //             this._snackBar.open('client Creation Changed  Failed', 'Ok', {
    //                 duration: 2000,
    //                 panelClass: ['error-snackbar']
    //             });
    //         })
    // }

    // editCreateclient(clientDetails: client) {
    //     this.dataService.setSelectedclientDetails(clientDetails);
    //     this.router.navigate(['/home/clients/create-client'], { queryParams: { edit: true } });
    // }
}
