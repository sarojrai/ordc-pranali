import { Directive, ElementRef, forwardRef, HostListener, Input, OnInit } from '@angular/core';
import { MAT_INPUT_VALUE_ACCESSOR } from '@angular/material/input';
import { NG_VALUE_ACCESSOR } from '@angular/forms';
import { numberWithCommas } from 'src/app/modules/material/lib/helper';

@Directive({
    selector: 'input[matInputCommified]',
    providers: [
        { provide: MAT_INPUT_VALUE_ACCESSOR, useExisting: MatInputCommifiedDirective },
        {
            provide: NG_VALUE_ACCESSOR,
            useExisting: forwardRef(() => MatInputCommifiedDirective),
            multi: true,
        }
    ]
})
export class MatInputCommifiedDirective implements OnInit {
    // tslint:disable-next-line:variable-name
    private _value!: string | null;

    @Input() min!: string;
    @Input() max!: string;

    constructor(private elementRef: ElementRef<HTMLInputElement>,
    ) {
    }

    ngOnInit(): void {
        if (this.min && isNaN(Number(this.min))) {
            throw new Error("Min should be number");
        }

        if (this.max && isNaN(Number(this.max))) {
            throw new Error("Max should be number");
        }
    }


    get value(): string | null {
        return this._value;
    }

    @Input('value')
    set value(value: string | null) {
        debugger;
        this._value = value;
        this.formatValue(value);
    }

    private formatValue(value: string | null) {
        if (value !== null && this.valueGreaterThanMin(value, this.min) && this.valueLessThanMax(value, this.max)) {
            this.elementRef.nativeElement.value = numberWithCommas(value);
        } else {
            this.elementRef.nativeElement.value = '';
        }
    }

    private unFormatValue() {
        const value = this.elementRef.nativeElement.value;
        this._value = value.replace(/[^\d.-]/g, '');
        if (value) {
            this.elementRef.nativeElement.value = this._value;
        } else {
            this.elementRef.nativeElement.value = '';
        }
    }

    @HostListener('input', ['$event.target.value'])
    onInput(value: string) {
        this._value = value.replace(/[^\d.-]/g, '');
        this._onChange(this._value);
    }

    @HostListener('blur')
    _onBlur() {
        this.formatValue(this._value);
    }

    @HostListener('focus')
    onFocus() {
        this.unFormatValue();
    }

    _onChange(value: any): void {
    }

    writeValue(value: any) {
        this._value = value;
        this.formatValue(this._value);
        // this._onChange(this._value);
    }

    registerOnChange(fn: (value: any) => void) {
        this._onChange = fn;
    }

    registerOnTouched() {
    }


    valueGreaterThanMin(value: string, min: string) {
        // debugger
        if (!min) {
            return true;
        }
        let minLimit = Number(this.min);
        let valueNumber = Number(this.value);
        // if (!isNaN(minLimit) && !isNaN(valueNumber)) {
        return (!isNaN(minLimit) && !isNaN(valueNumber) && valueNumber >= minLimit);
        // }
        // return true;
    }

    valueLessThanMax(value: string, max: string) {
        if (!max) {
            return true;
        }
        let maxLimit = Number(this.max);
        let valueNumber = Number(this.value);
        // if (!isNaN(maxLimit) && !isNaN(valueNumber)) {
        return (!isNaN(maxLimit) && !isNaN(valueNumber) && valueNumber <= maxLimit);
        // }
        // return true;
    }

}