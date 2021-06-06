import { Component, EventEmitter, Input, Output, ViewEncapsulation } from '@angular/core';
import { CdkStep, CdkStepper } from '@angular/cdk/stepper';

@Component({
    selector: 'order-stepper',
    templateUrl: './order-stepper.component.html',
    styleUrls: ['./order-stepper.component.scss'],
    encapsulation: ViewEncapsulation.None,
    providers: [
        { provide: CdkStepper, useExisting: OrderStepper }
    ],
})
export class OrderStepper extends CdkStepper {
    activeClass = 'active';

    completeClass = 'completed';

    @Output() submit: EventEmitter<any> = new EventEmitter();
    @Output() nextEvent: EventEmitter<any> = new EventEmitter();

    @Input() cancelButtonText!: string;
    onSubmit() {
        this.submit.emit(true);
        this.nextEvent.emit(true);
    }

    getCompletedStateIcon(state: string) {
        return state + '_active';
    }

    nextClicked() {
        this.nextEvent.emit(true);
    }
}