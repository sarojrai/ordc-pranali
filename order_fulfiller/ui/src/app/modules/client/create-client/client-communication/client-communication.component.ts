import { Component, Input, ViewEncapsulation } from "@angular/core";
import { FormArray, FormBuilder, FormGroup } from "@angular/forms";
import { COMMA, ENTER } from '@angular/cdk/keycodes';

import { ModeOfNotification, NotificationMethod, OrderType } from "src/app/modules/models";
import { displayModeOfNotification } from "src/app/modules/utils"

@Component({
    selector: 'order-client-communication',
    templateUrl: './client-communication.component.html',
    styleUrls: ['./client-communication.component.scss'],
    encapsulation: ViewEncapsulation.None,
    providers: [
    ],
})
export class ClientCommunicationComponent {
    @Input() formGroup!: FormGroup;
    @Input() notificationMethods!: Array<NotificationMethod>;
    @Input() orderTypes!: Array<OrderType>;
    @Input() modeOfNotifications!: Array<ModeOfNotification>;

    displayedColumns!: Array<string>;
    separatorKeysCodes: number[] = [ENTER, COMMA];
    notificationModePriority!: Array<ModeOfNotification>;
    sequenceNdrShipmentOrders!: Array<ModeOfNotification>;

    constructor(private _formBuilder: FormBuilder) {
        this.displayedColumns = ['modeOfNotifications', 'noOfTimes', 'duration', 'priority'];
        this.notificationModePriority = [];
        this.sequenceNdrShipmentOrders = [];
    }

    displayModeOfNotification = displayModeOfNotification

    notificationPriorityControl(formGroup: FormGroup): FormArray {
        return formGroup.controls.notificationModePriority as FormArray;
    }

    ndrShipmentControl(formGroup: FormGroup): FormArray {
        return formGroup.controls.sequenceNdrShipmentOrders as FormArray;
    }

    addPriorityMode(index: number) {
        let code: string = this.modeOfNotifications[index].value;
        if (!this.checkPriorityModeExist(code)) {
            let formControl = this._formBuilder.control(this.modeOfNotifications[index].value);
            this.notificationPriorityControl(this.formGroup).push(formControl);
            this.notificationModePriority = [...this.notificationModePriority, { ...this.modeOfNotifications[index] }];
        }
    }

    checkPriorityModeExist(code: string) {
        return (this.notificationModePriority.findIndex(pri => pri.value === code) !== -1) ? true : false;
    }


    removePriorityMode(index: number) {
        this.notificationMethods.splice(index, 1);
        this.notificationPriorityControl(this.formGroup).removeAt(index);
    }

    addNdrShipment(index: number) {
        let code: string = this.modeOfNotifications[index].value;
        if (!this.checkNdrShipmentExist(code)) {
            let formControl = this._formBuilder.control(code);
            this.ndrShipmentControl(this.formGroup).push(formControl);
            this.sequenceNdrShipmentOrders = [...this.sequenceNdrShipmentOrders, { ...this.modeOfNotifications[index] }];
        }
    }

    checkNdrShipmentExist(code: string) {
        return (this.sequenceNdrShipmentOrders.findIndex(ndr => ndr.value === code) !== -1) ? true : false;
    }

    removeNdrShipment(index: number) {
        this.sequenceNdrShipmentOrders.splice(index, 1);
        this.ndrShipmentControl(this.formGroup).removeAt(index);
    }
}