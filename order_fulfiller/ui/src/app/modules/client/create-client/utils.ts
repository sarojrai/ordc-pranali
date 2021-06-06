import { FormBuilder, Validators } from "@angular/forms";

export function generateBankDetailFG(_formBuilder: FormBuilder) {
    return _formBuilder.group({
        bankName: _formBuilder.control('', [Validators.required]),
        ifscCode: _formBuilder.control('', [Validators.required]),
        accountNo: _formBuilder.control('', [Validators.required, Validators.pattern("^[0-9]*$"),])
    })
}

export function generateContactDetailFG(_formBuilder: FormBuilder) {
    return _formBuilder.group({
        name: _formBuilder.control('', [Validators.required]),
        contactNo: _formBuilder.control('', [Validators.required, Validators.pattern("^[0-9]*$")]),
        email: _formBuilder.control('', [Validators.required, Validators.email])
    })
}