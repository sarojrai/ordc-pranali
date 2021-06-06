import { NgModule, } from '@angular/core';

import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { OrderMaterialModule } from 'src/app/modules/material/material.module'
import { ErrorStateMatcher, ShowOnDirtyErrorStateMatcher } from '@angular/material/core';
import { OrderStepperModule } from 'src/app/modules/shared/order-stepper/order-stepper.module';
import { ConfirmationDialog } from './confirmation-dialog/confirmation.dialog.component';
@NgModule({
    declarations: [
        ConfirmationDialog
    ],
    imports: [
        OrderMaterialModule,
        CommonModule
    ],
    exports: [
        CommonModule,
        FormsModule,
        ReactiveFormsModule,
        HttpClientModule,
        OrderStepperModule,
        ConfirmationDialog
    ],
    providers: [
        { provide: ErrorStateMatcher, useClass: ShowOnDirtyErrorStateMatcher }
    ]
})
export class OrderSharedModule { }