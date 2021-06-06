import { CdkStep } from "@angular/cdk/stepper";
import { Component, Input } from "@angular/core";

@Component({
    selector: 'order-step',
    providers: [
        { provide: CdkStep, useExisting: OrderStep }
    ],
})
export class OrderStep extends CdkStep {
    @Input() completedIcon!: string
}