import { FormGroup } from "@angular/forms";

export function errorHandling(formGroup: FormGroup, control: string, error: string) {
    return formGroup.controls[control].hasError(error);
}