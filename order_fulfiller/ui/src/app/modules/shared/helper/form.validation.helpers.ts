import { AbstractControl, Form, FormArray, FormControl, FormGroup, ValidationErrors, ValidatorFn } from "@angular/forms";
import * as moment from "moment";

export function dateShouldBeLessThan(to: string, label: string): ValidatorFn {
    return (control: AbstractControl): ValidationErrors | null => {
        const fromCtrl = control;
        const toCtrl = control.parent?.get(to);
        return (fromCtrl?.value && toCtrl?.value && moment(fromCtrl?.value).isAfter(moment(toCtrl?.value))) ? { message: 'Date Should be less than' + label } : null;
    }
}

export function dateShouldBeGreaterThan(from: string, label: string): ValidatorFn {
    return (control: AbstractControl): ValidationErrors | null => {
        const fromCtrl = control.parent?.get(from);
        const toCtrl = control;
        return (fromCtrl?.value && toCtrl?.value && moment(fromCtrl?.value).isAfter(moment(toCtrl?.value))) ? { message: 'Date Should be greater than Closing Date' + label } : null;
    }
}


/**
  * Marks all controls in a form group as touched
  * @param group - The form group to touch
  */
export function markFormGroupTouched(group: FormGroup | FormArray) {
    if (group?.controls) {
        if (Array.isArray(group.controls)) {
            let formArray = group as FormArray;
            formArray.markAsDirty();
            formArray.controls.forEach(control => {
                control.markAsDirty();
                if ('controls' in control) {
                    markFormGroupTouched(control as FormArray | FormGroup);
                }
            });
        } else {
            let formGroup = group as FormGroup;
            Object.keys(group.controls)
                .forEach(controlName => {
                    let control: FormControl | FormGroup = (formGroup.controls[controlName]) as FormControl | FormGroup;
                    control.markAsDirty();
                    if ('controls' in control) {
                        markFormGroupTouched(control as FormArray | FormGroup);
                    }
                });
        }
    }
}