import { Component, Input, OnDestroy, OnInit, ViewEncapsulation } from '@angular/core';
import { FormArray, FormBuilder, FormGroup } from '@angular/forms';
import { Bankdetails, ContactDetails } from '../../../models/clientCreate';
import { generateBankDetailFG, generateContactDetailFG } from '../utils';



@Component({
    selector: 'order-client-basic-details',
    templateUrl: './basic-detail.component.html',
    styleUrls: ['./basic-detail.component.scss'],
    encapsulation: ViewEncapsulation.None,

})
export class BasicClientComponent implements OnInit {
    @Input() formGroup!: FormGroup;
    Bankdetails: Array<string> = []
    dynamicArray: Array<Bankdetails> = [];
    newDynamic: any = {};
    index: number = 1;
    index1: number = 1;

    dynamicArrayContact: Array<ContactDetails> = [];
    newDynamicContact: any = {};

    constructor(private _formBuilder: FormBuilder) { }

    ngOnInit(): void {
        this.newDynamic = { bank_name: "", ifsc_code: "", account_no: "" };
        this.dynamicArray.push(this.newDynamic);

        this.newDynamicContact = { name: "", contact_no: "", email: "" };
        this.dynamicArrayContact.push(this.newDynamicContact);
    }

    get bankDetails() {
        return this.formGroup.get('bankDetails') as FormArray
    }

    get contactDetails() {
        return this.formGroup.get('contactDetails') as FormArray
    }

    // addRow(index: number) {
    //     this.newDynamic = { bank_name: "", ifsc_code: "", account_no: "" };
    //     this.dynamicArray.push(this.newDynamic);
    //     console.log(this.dynamicArray);
    //     return true;
    // }

    addBankDetail() {
        this.bankDetails.push(generateBankDetailFG(this._formBuilder));
    }

    deleteBankDetail(index: number) {
        this.bankDetails.removeAt(index);
    }

    addContactDetail() {
        this.contactDetails.push(generateContactDetailFG(this._formBuilder));
    }

    deleteContactDetail(index: number) {
        this.contactDetails.removeAt(index);
    }

    // deleteRow(index: number) {
    //     if (this.dynamicArray.length == 1) {

    //         return false;
    //     } else {
    //         this.dynamicArray.splice(index, 1);

    //         return true;
    //     }
    // }

    // addRowContact(index1: number) {
    //     this.newDynamicContact = { name: "", contact_no: "", email: "" };
    //     this.dynamicArrayContact.push(this.newDynamicContact);
    //     console.log(this.dynamicArrayContact);
    //     return true;
    // }

    // deleteRowContact(index1: number) {
    //     if (this.dynamicArrayContact.length == 1) {

    //         return false;
    //     } else {
    //         this.dynamicArrayContact.splice(index1, 1);

    //         return true;
    //     }
    // }

}


