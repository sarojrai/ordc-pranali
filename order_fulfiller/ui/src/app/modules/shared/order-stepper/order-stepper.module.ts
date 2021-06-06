import { NgModule, } from '@angular/core';

import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';

import { OrderMaterialModule } from 'src/app/modules/material/material.module'

import { ErrorStateMatcher, ShowOnDirtyErrorStateMatcher } from '@angular/material/core';

import { OrderStepper } from 'src/app/modules/shared/order-stepper/order-stepper.component';

@NgModule({
    declarations: [
        OrderStepper
    ],
    imports: [
        CommonModule,
        OrderMaterialModule
    ],
    exports: [
        CommonModule,
        FormsModule,
        ReactiveFormsModule,
        HttpClientModule,
        OrderStepper,
    ],
    providers: [
        { provide: ErrorStateMatcher, useClass: ShowOnDirtyErrorStateMatcher }
    ]
})
export class OrderStepperModule { }